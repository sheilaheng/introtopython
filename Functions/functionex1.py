def calculator(num):
    if num%3==0 and num%5==0:
        return 'FizzBuzz'

    elif num % 3 == 0:
        return 'Fizz'

    elif num % 5==0:
        return 'Buzz'
    else:
        return num

for n in range(1,100):
    print(calculator(n))
