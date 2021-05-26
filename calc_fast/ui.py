import os
import api

os.system('clear')

def menu():
    operator = input("Choice +, -, *, /: ")
    score = 0
    n = 3
    start_range = 1
    end_range = 10
    total_response_time = 0
    check_mark = "\U0001F603"
    equations = []

    while n > 0:
        # create random numbers
        number1 = api.get_random_number(start_range, end_range)
        number2 = api.get_random_number(start_range, end_range)
        equation = f"{number1} {operator} {number2}"
        
        # get response and set start and end time 
        start_time = api.current_time()
        response = int(input(f"{equation} = "))
        end_time = api.current_time()

        # calculate response and total response time 
        response_time = api.get_time_diff(start_time, end_time)
        total_response_time += response_time
        # get answer of a equation 
        answer = api.calculate(number1, number2, operator)
        if api.compare(answer, response):
            equation = f"{check_mark} {equation} = {answer}" 
            score += 1
        else:
            equation = f"X {equation} = {answer}"
        equations.append(equation)
        
        # clear everything and print each equation that formated
        os.system('clear')
        for equation in equations:
            print(equation)

        n -= 1
    print(f"Total Time {int(total_response_time)}")
if __name__ == "__main__":
    menu()

        
