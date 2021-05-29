import tkinter as tk
from tkinter import ttk

import api

opr = "+"

# when user press Return key:
#  - compare response versus correct answer
#  - create input box
#  - create new equation
#  - set equation to the label


def calc(event):
    equation = equation_var.get().split("=")[0].strip()
    print(equation)
    answer = api.calculate(equation)
    print(answer)
    user_response = int(response.get())
    result = api.compare(answer, user_response)
    if result:
        log_str.set(log_str.get() + "\n✅ Correct")
    else:
        log_str.set(log_str.get() + "\n❌ Wrong")

    response.delete(0, tk.END)  # clear response entry box


root = tk.Tk()
root.title("Fast Calc.")

num1 = api.get_random_number()
num2 = api.get_random_number()

log_str = tk.StringVar()
equation_var = tk.StringVar()
equation_var.set(f"{num1} + {num2} = ?")

log_label = ttk.Label(root, textvariable=log_str)

answer = api.calculate(f"{num1} {opr} {num2}")
equation = ttk.Label(root, textvariable=equation_var)
equation.pack()
start_time = api.current_time()
response = ttk.Entry(root)
response.pack()
response.focus()
end_time = api.current_time()

log_label.pack()

response.bind("<Return>", calc)


root.mainloop()
