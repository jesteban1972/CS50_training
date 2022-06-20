import sys

def division(dividend, divisor):
    try:
        quotient = dividend / divisor
    except ZeroDivisionError:
        print('wrong parameters: cannot divide by 0')
        sys.exit(1)
    return quotient
    
dividend = float(input('input dividend: '))
divisor = float(input('input divisor: '))
print(f"the quotient is {str(division(dividend, divisor))}")