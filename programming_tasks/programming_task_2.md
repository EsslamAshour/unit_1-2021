```.py
N = input("Input N: ")
step_count = 0
while len(N) > 1:
    product = 1
    for digit in N:
        product *= int(digit)
    N = str(product)
    step_count += 1
print(step_count)
```
