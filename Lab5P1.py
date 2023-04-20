def request():
    number = input('Enter variable number')
    print(even(number))


def even(number):
    if(int(number)%2==0):
        return 'Even number'
    else:
        return '0dd number'

request()