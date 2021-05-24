import random
import time

# create random number
def get_random_number(start=1, end=100):
    """ Create random number between start and end range."""
    return random.randint(start, end)


# calculate operation
def calculate(x, y, opr):
    """ Calculate the result of x and y based on operator."""
    if opr == "+":
        return x + y
    elif opr == "-":
        return x - y
    elif opr == "*":
        return x * y
    elif opr == "/":
        try:
            return x / y
        except ZeroDivisionError:
            pass

def compare(response, result):
    if response == result:
        return True
    else:
        return False

def add_point(point):
    return point + 1

# calculate current time
def current_time():
    return time.time()

# get time difference
def get_time_diff(start_time, end_time):
    return end_time - start_time



if __name__ == "__main__":
    point = 0
    x = get_random_number()
    y = get_random_number()

    start_time = current_time()
    response = int(input(f"{x} + {y} = "))
    end_time = current_time()

    answer = calculate(x, y, '+')
    result = compare(response, answer)
    time_diff = get_time_diff(start_time, end_time)
    print(f'{time_diff:.2f}')

    if result:
        point += 1
        print('correct')
    else:
        print('not correct')
