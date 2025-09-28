#### Assignment 9
# Premium Subscribers Inheritance

The purpose of this assignment is to be a short introduction to **inheritance** and **private variables** (`__var`) in Python.

You will create two classes: `Subscription` (parent) and `PremiumSubscription` (child). The parent will store a **private** monthly fee that you can access through getter and setter methods. The child will add one extra attribute and **override** some methods to change the behavior.

Put your code in the `a09_premium_subscribers_inheritance.py` file. Don't edit or delete any other files.

## Libraries Required:
- *(none)*

## Classes Required:
You can write the class names, instance variables, and method names in PascalCase, camelCase, or snake_case (though PascalCase is the convention for class names in Python). The automated tests should recognize any of those choices. I write class names in PascalCase, and method/variable names in snake_case as is the convention for Python.

#### Subscription (Parent)
- Instance Variables:
  - `name` (string)
    - the name of the subscription (e.g., “Music App”)
  - `__monthly_fee` (float or int) **(private)**
    - the monthly fee in dollars
- Methods:
  - `__init__(self, name, monthly_fee)`
    - The constructor / initializer!
  - `get_monthly_fee(self)`
    - Returns the current monthly fee.
  - `set_monthly_fee(self, new_fee)`
    - Sets the monthly fee **only if** `new_fee` is `>= 0`. If `new_fee` is negative, print the message: `Monthly fee cannot be negative.` and do not change the value.
  - `get_annual_cost(self)`
    - Returns `12 * monthly_fee`.
  - `get_info(self)`
    - Returns a string with the subscription name and the monthly fee, formatted like:
      - `Subscription: <name> - Monthly Fee: $<fee with 2 decimals>`

#### PremiumSubscription (Child of Subscription)
- Extra Instance Variable:
  - `extra_services_fee` (float or int)
    - a flat fee added to the annual cost to represent extras (e.g., concierge support, add-ons)
- Methods:
  - `__init__(self, name, monthly_fee, extra_services_fee)`
    - Calls the parent constructor for `name` and `monthly_fee`, then sets `extra_services_fee`.
  - **Overridden** `get_annual_cost(self)`
    - Returns `(12 * monthly_fee) + extra_services_fee`.
    - The key principle to learn here is that you can't directly access the monthly_fee from the child class. You need to use the getter method `get_monthly_fee` instead.
  - **Overridden** `get_info(self)`
    - Returns the same string as `Subscription`'s version but with the `extra_services_fee` tacked on, formatted like:
      - `Subscription: <name> - Monthly Fee: $<fee with 2 decimals> - Extra Services Fee: $<extra services fee with 2 decimals>`
      - If you want an extra optional mini challenge, see if you can write this using `super()` and without repeating the same string data as the original `Subscription` version. Doing this won't get you any extra points though.

> Note: The private variable must use **double underscores** (`__monthly_fee`) so it is name-mangled and cannot be directly accessed from outside the class or in the child without using the getter/setter. Do **not** use a single underscore for this assignment.

## Logical Flow:
Note: This program won’t store any user input. You’ll hardcode the values provided in the instructions.

### Part 1: Create the Classes
- Implement the `Subscription` class exactly as described above.
- Implement the `PremiumSubscription` class exactly as described above.

### Part 2: Create and Use Objects
- Create a `Subscription` object:
  - Name: `Music App`
  - Monthly Fee: `10`
- Print the result of `get_info()` for the `Subscription` object.
- Print `Annual cost:` followed by the value returned from `get_annual_cost()`.

- Create a `PremiumSubscription` object:
  - Name: `Music App Premium`
  - Monthly Fee: `10`
  - Extra Services Fee: `50`
- Print the result of `get_info()` for the `PremiumSubscription` object.
- Print `Annual cost:` followed by the value returned from `get_annual_cost()`.
- Update the monthly fee on the `PremiumSubscription` object to 12 bucks a month by calling `set_monthly_fee`.
- Print `Updated Annual cost:` followed by the value returned from `get_annual_cost()` again (you should see the annual cost change).

## Rubric
- See `RUBRIC.md` for details on each of the tests you're scored on.
- To see what score you'll receive, run the tests using the testing tab (it looks like a beaker).
    - In the testing tab, press `Configure Python Tests`, then choose `pytest`, then `tests`, and then press the `Run Tests` button.
        - If you accidentally choose the wrong options for `Configure Python Tests`, to choose again, go to `View` > `Command Palette` and then type `Python: Configure Tests` and hit enter. Then choose the options above again.
- To see your results and any error messages, right click the `TEST_RESULTS_SUMMARY.md` file and choose `Open Preview`.

## Example Output:

```
Subscription: Music App - Monthly Fee: $10.00
Annual cost: 120
Subscription: Music App Premium - Monthly Fee: $10.00 - Extra Services Fee: $50.00
Annual cost: 170
Updated Annual cost: 194
```
