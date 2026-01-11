import sys

# calls all functions
def main():
    number = input('Number: ')
    base_number = input('Number is in base: ')
    base = input('To which base conversion: ')
    n, b = to_b10(number, base_number, base)
    digits = base_digits(n, b)
    final_answer = base_conversion(digits)
    print(f'\nValue of {number} in base {base}: {final_answer}\n')

# error checking and conversion to base 10
def to_b10(n, b_n, b):
    try:
        num = int(n, int(b_n))
        base = int(b)
        if num < 0:
            sys.exit('Number needs to be positive\n')
        if (base > 36) or (base <= 1):
            sys.exit('base range is 2 to 36\n')
        return num, base
    except:
        sys.exit('Invalid input given: number and base of number not compatible\n')

# returning a list of digits that are present in the base
def base_digits(n, b):
    number = []
    if n == 0:
        number.append(0)
    else:
        while n > 0:
            n, modulo = divmod(n, b)
            number.insert(0, modulo)
    return number
    
# converting the digits to proper format of the base
def base_conversion(digits):
    map = '0123456789abcdefghijklmnopqrstuvwxyz'
    encoding = ''
    for d in digits:
        encoding += map[d]
    return encoding

if __name__ == '__main__':
    main()

