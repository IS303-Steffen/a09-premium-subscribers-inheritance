# PremiumSubscription - set_monthly_fee Method Tests

## PremiumSubscription - set_monthly_fee Method Test 1

### Initial Object Values
````
name: "Music App Premium" - str
extra_services_fee: 50 - int
__monthly_fee: 10 - int
````

### Arguments
````
1: 12 - int
````

### Expected Return Value
````
Does not return anything
````

### Expected Object Update
````
__monthly_fee:
	Initial: 10 - int
	Final: 12 - int
````

