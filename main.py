cuenta=1
print("Fizz buzz hasta 1000","\n")
while cuenta <=1000:
    if cuenta%3==0:
        print("Fizz")
    elif cuenta%5==0:
        print("Buzz")
    elif cuenta%15==0:
        print("FizzBuzz")
    else:
        print(cuenta)
    cuenta+=1

cuenta_2=1
print("\n","Fizzbuz hasta 10 ","\n")
while cuenta_2<=10:
    if cuenta%5==0:
        print("Buzz")
    elif cuenta_2%15==0:
        print("FizzBuzz")
    elif cuenta_2%3==0:
        print("Fizz")
    else:
        print(cuenta_2)
    cuenta_2+=1

cuenta_3=1
print("\n","Fizzbuzz hasta 100","\n")
while cuenta_3<=100:
    if cuenta_3%5==0:
        print("Buzz")
    elif cuenta_3%3==0:
        print("Fizz")
    elif cuenta_3%15==0:
        print("Fizzbuzz")
    else:
        print(cuenta_3)
    cuenta_3+=1