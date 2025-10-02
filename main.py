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

cuenta_2=1
while cuenta_2<=10:
    if cuenta%5==0:
        print("Buzz")
    if cuenta_2%15==0:
        print("FizzBuzz")
    if cuenta_2%3==0:
        print("Fizz")
    else:
        print(cuenta_2)
    cuenta_2+=1

cuenta_3=1
while cuenta_3<=100:
    if cuenta_3%5==0:
        print("Buzz")
    if cuenta_3%3==0:
        print("Fizz")
    if cuenta_3%15==0:
        print("Fizzbuzz")
    else:
        print(cuenta_3)
    cuenta_3+=1