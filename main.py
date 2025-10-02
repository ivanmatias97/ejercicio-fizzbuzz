cuenta=1
while cuenta <=1000:
    if cuenta%3==0:
        print("Fizz")
    if cuenta%5==0:
        print("Buzz")
    if cuenta%15==0:
        print("FizzBuzz")
    else:
        print(cuenta)
    cuenta+=1