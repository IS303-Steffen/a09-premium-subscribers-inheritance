# Subscription - set_monthly_fee Method Tests

## Subscription - set_monthly_fee Method Test 1

### Initial Object Values
````
name: "Music App" - str
__monthly_fee: 10 - int
````

### Arguments
````
1: 15 - int
````

### Expected Return Value
````
Does not return anything
````

### Expected Object Update
````
__monthly_fee:
	Initial: 10 - int
	Final: 15 - int
````

## Subscription - set_monthly_fee Method Test 2

### Initial Object Values
````
name: "Music App" - str
__monthly_fee: 10 - int
````

### Arguments
````
1: -1 - int
````

### Expected Return Value
````
Does not return anything
````

### Expected Object Update
````
__monthly_fee:
	Initial: 10 - int
	Final: 10 - int
````

