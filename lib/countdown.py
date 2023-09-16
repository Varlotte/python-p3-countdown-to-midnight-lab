import time

def countdown(number):
    number = number
    while number > 0:
        print(f'{number} SECOND(S)!')
        number -=1
    else:
        print("HAPPY NEW YEAR!")


def countdown_with_sleep(number):
    number = number
    while number > 0:
        time.sleep(1)
        print(f'{number} SECOND(S)!')
        number -=1
    else:
        print("HAPPY NEW YEAR!")