```.py
# I think it is impossible for a number to take 10 or more steps
# I let this run for a good period of time and the maximum steps I got was 7 (7873917)
def steps(N):
    N = str(N)
    step_count = 0
    while len(N) > 1:
        product = 1
        for digit in N:
            product *= int(digit)
        N = str(product)
        step_count += 1
    return step_count

N = 0
steps = func(N)
while steps < 10:
    N += 1
    steps = func(N)
print(N)
```
