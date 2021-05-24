import api



def menu():
    opr = input("Choice +, -, *, /: ")
    score = 0
    n = 10
    start_range = 1
    end_range = 10
    time_dur = 0

    while n > 0:
        x = api.get_random_number(start_range, end_range)
        y = api.get_random_number(start_range, end_range)
        answer = api.calculate(x, y, opr)
        start_time = api.current_time()
        response = int(input(f"{x} {opr} {y} = "))
        end_time = api.current_time()
        elapsed_time = api.get_time_diff(start_time, end_time)
        time_dur += elapsed_time
        
        if api.compare(answer, response):
            print('Corrent')
            score += 1
        else:
            print('Wrong :-(')
        print(f'Score: {score}')
        print(f'Elapsed time: {elapsed_time:.2f}')
        n -= 1
    print(f'Overall time: {time_dur:.2f}')

if __name__ == "__main__":
    menu()

        
