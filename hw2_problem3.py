# Use Diophantine in python
variables=range(0,10)  # set the coefficient are digitals
test_data=range(50,56)
for total in test_data:
    for a in variables:
        for b in variables:
            for c in variables:
                if total==6*a+9*b+20*c:
                    print a, 'times six', b, 'time nine','and', c ,'times twenty', ', total is', total
