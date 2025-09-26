
from typing import Any, Optional

# ======================
# METHOD TEST CASE CLASS
# ======================

class MethodTestCase:
    def __init__(self, function_name: str, args: list, expected_return_value: Any,
                 expected_object_update: Optional[dict] = None, set_var_values: Optional[dict] = None, num_calls: int = 1):
        self.function_name = function_name
        self.args = args
        self.expected_return_value = expected_return_value
        self.expected_object_update = expected_object_update
        self.set_var_values = set_var_values
        self.num_calls = num_calls

    def to_dict(self):
        return {
            "function_name": self.function_name,
            "args": self.args,
            "expected_return_value": self.expected_return_value,
            "expected_object_update": self.expected_object_update,
            "set_var_values": self.set_var_values,
            "num_calls": self.num_calls
        }
    
# ======================
# CLASS TEST CASE CLASS
# ======================

class ClassTestCase:
    def __init__(self, class_name, init_args, init_expected_values, expected_function_names, method_test_cases):
        self.class_name = class_name
        self.init_args = init_args
        self.init_expected_values = init_expected_values
        self.expected_function_names = expected_function_names
        self.method_test_cases = [m.to_dict() for m in method_test_cases]

    def to_dict(self):
        return {
            "class_name": self.class_name,
            "init_args": self.init_args,
            "init_expected_values": self.init_expected_values,
            "expected_function_names": self.expected_function_names,
            "method_test_cases": self.method_test_cases
        }

    @classmethod
    def from_dict(cls, data):
        method_test_cases = [MethodTestCase(**m) for m in data["method_test_cases"]]
        return cls(
            class_name=data["class_name"],
            init_args=data["init_args"],
            init_expected_values=data["init_expected_values"],
            expected_function_names=data["expected_function_names"],
            method_test_cases=method_test_cases
        )
    
# ==============================
# CREATE TEST CASE OBJECTS BELOW
# ==============================
'''
MethodTestCase objects should be created first, then placed inside of ClassTestCase
objects in their method_test_cases attribute
'''

# ========================
# METHOD TEST CASE OBJECTS
# ========================

# ---- Subscription method tests ----
subscription_get_monthly_fee = MethodTestCase(
    function_name='get_monthly_fee',
    args=[],
    expected_return_value=10,
    expected_object_update=None
)

subscription_set_monthly_fee_valid = MethodTestCase(
    function_name='set_monthly_fee',
    args=[15],
    expected_return_value=None,
    expected_object_update={
        '__monthly_fee': {
            'initial_value': 10,
            'final_value': 15
        }
    }
)

subscription_set_monthly_fee_negative = MethodTestCase(
    function_name='set_monthly_fee',
    args=[-1],
    expected_return_value=None,
    expected_object_update={
        '__monthly_fee': {
            'initial_value': 10,
            'final_value': 10  # should not change
        }
    }
)

subscription_get_annual_cost = MethodTestCase(
    function_name='get_annual_cost',
    args=[],
    expected_return_value=120,
    expected_object_update=None
)

subscription_get_info = MethodTestCase(
    function_name='get_info',
    args=[],
    expected_return_value="Subscription: Music App - Monthly Fee: $10.00",
    expected_object_update=None
)

# ---- PremiumSubscription method tests ----
premium_get_monthly_fee = MethodTestCase(
    function_name='get_monthly_fee',
    args=[],
    expected_return_value=10,
    expected_object_update=None
)

premium_get_annual_cost = MethodTestCase(
    function_name='get_annual_cost',
    args=[],
    expected_return_value=170,  # (10 * 12) + 50
    expected_object_update=None
)

premium_get_info = MethodTestCase(
    function_name='get_info',
    args=[],
    expected_return_value="Subscription: Music App Premium - Monthly Fee: $10.00 - Extra Services Fee: $50.00",
    expected_object_update=None
)

premium_set_monthly_fee_valid = MethodTestCase(
    function_name='set_monthly_fee',
    args=[12],
    expected_return_value=None,
    expected_object_update={
        '__monthly_fee': {
            'initial_value': 10,
            'final_value': 12
        }
    }
)

premium_get_annual_cost_after_update = MethodTestCase(
    function_name='get_annual_cost',
    args=[],
    expected_return_value=194,  # (12 * 12) + 50
    expected_object_update=None,
    set_var_values={
        '__monthly_fee': 12  # simulate prior setter call
    }
)

# =======================
# CLASS TEST CASE OBJECTS
# =======================

Subscription_class = ClassTestCase(
    class_name='Subscription',
    init_args={
        'name': 'Music App',
        'monthly_fee': 10
    },
    init_expected_values={
        'name': 'Music App',
        '__monthly_fee': 10
    },
    expected_function_names=['get_monthly_fee', 'set_monthly_fee', 'get_annual_cost', 'get_info'],
    method_test_cases=[
        subscription_get_monthly_fee,
        subscription_set_monthly_fee_valid,
        subscription_set_monthly_fee_negative,
        subscription_get_annual_cost,
        subscription_get_info,
    ]
)

PremiumSubscription_class = ClassTestCase(
    class_name='PremiumSubscription',
    init_args={
        'name': 'Music App Premium',
        'monthly_fee': 10,
        'extra_services_fee': 50
    },
    init_expected_values={
        'name': 'Music App Premium',
        'extra_services_fee': 50,
        '__monthly_fee': 10
    },
    expected_function_names=['get_monthly_fee', 'set_monthly_fee', 'get_annual_cost', 'get_info'],
    method_test_cases=[
        premium_get_monthly_fee,
        premium_get_annual_cost,
        premium_get_info,
        premium_set_monthly_fee_valid,
        premium_get_annual_cost_after_update,
    ]
)

# Update the list of test cases
test_cases_classes_list = [Subscription_class, PremiumSubscription_class]

test_cases_classes_list = [class_test_case.to_dict() for class_test_case in test_cases_classes_list]
unique_class_names = {class_name.get('class_name') for class_name in test_cases_classes_list}

test_cases_classes_dict = {}
for class_name in unique_class_names:
    subset_test_cases_classes = [test_case_class for test_case_class in test_cases_classes_list if test_case_class.get('class_name') == class_name]
    test_cases_classes_dict[class_name] = subset_test_cases_classes
