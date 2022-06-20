def square(x):
    return x * x

assert square(10) == 100 # should be 100

number = input('number:')    
print('square of ' + number + ' is: ' + str(square(int(number))))