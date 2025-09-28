max_score = 5  # This value is pulled by yml_generator.py to assign a score to this test.

import ast
from conftest import (
    default_module_to_test,
    format_error_message,
    exception_message_for_students,
    pc_get_or_create,
    pc_finalize_and_maybe_fail,
    record_failure
)

BANNED_PREFIXES = ("_Subscription__",
                   "_subscription__",
                   "_PremiumSubscription__",
                   "_premiumSubscription__",
                   "_premium_subscription__")  # direct access to parent privates

def _find_banned_parent_private_references(source: str):
    """
    Scan AST to find any direct parent-private access like:
        obj._Subscription__monthly_fee
        Subscription._Subscription__monthly_fee
        self._Subscription__monthly_fee
    Returns a list of tuples: (lineno, col_offset, snippet_attr)
    """
    tree = ast.parse(source)
    hits = []

    class Visitor(ast.NodeVisitor):
        def visit_Attribute(self, node: ast.Attribute):
            # node.attr is the attribute string
            attr = node.attr
            if any(attr.startswith(pfx) for pfx in BANNED_PREFIXES):
                hits.append((getattr(node, "lineno", None),
                             getattr(node, "col_offset", None),
                             attr))
            self.generic_visit(node)

        def visit_Name(self, node: ast.Name):
            # Extremely rare case: someone binds a name literally equal to a mangled attr.
            # Not typical, but we flag it to be safe.
            if any(node.id.startswith(pfx) for pfx in BANNED_PREFIXES):
                hits.append((getattr(node, "lineno", None),
                             getattr(node, "col_offset", None),
                             node.id))
            self.generic_visit(node)

    Visitor().visit(tree)
    return hits


def test_10_no_referencing_mangled_names(current_test_name):
    rec = pc_get_or_create(current_test_name, max_score)

    try:
        module = default_module_to_test  # e.g., "a09_premium_subscribers_inheritance"
        with open(f"{module}.py", "r", encoding="utf-8") as f:
            source = f.read()

        hits = _find_banned_parent_private_references(source)

        if hits:
            # Build a helpful message with locations
            lines = []
            for lineno, col, attr in hits:
                loc = f"line {lineno}, col {col}" if lineno is not None else "(unknown location)"
                lines.append(f"{loc}: {attr}")
            lines_str = "\n".join(lines)
            custom_msg = format_error_message(
                custom_message=(
                    "This test ensures you **do not** reference the parent class's private variables directly.\n\n"
                    "The test found direct access to `Subscription`'s private attribute(s) (Python name-mangled form):\n"
                    f"```\n{lines_str}\n```\n"
                    "Instead of referencing `Subscription`'s `__private` attributes (e.g., `_Subscription__monthly_fee`),\n"
                    "use the provided **getter/setter methods** (e.g., `get_monthly_fee()` / `set_monthly_fee(...)`)."
                ),
                current_test_name=current_test_name,
                input_test_case=None
            )
            # Record a single binary-style failure
            record_failure(current_test_name, formatted_message=custom_msg, input_test_case=None, reason="binary test fail")
            return

        # Passed: record a passing case so the summary shows 1/1
        rec.pass_case("ok")

    except Exception as e:
        input_test_case = None
        exception_message_for_students(e, input_test_case, current_test_name)
    finally:
        pc_finalize_and_maybe_fail(rec)
