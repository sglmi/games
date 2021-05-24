import tkinter as tk
from tkinter import ttk

import api


def calc(event):
    answer = api.calculate(num1, num2, '+')
    user_response = int(response.get())
    result = api.compare(answer, user_response)
    if result:
        log_str.set("Correct")
    else:
        log_str.set("Wrong")

root = tk.Tk()
root.title("Fast Calc.")

num1 = api.get_random_number()
num2 = api.get_random_number()
log_str = tk.StringVar()
log_label = ttk.Label(root, text="", textvariable=log_str)

answer = api.calculate(num1, num2, '+')
ttk.Label(root, text=f"{num1} + {num2} = ").pack()
start_time = api.current_time()
response = ttk.Entry(root)
response.pack()
response.focus()
end_time = api.current_time()

log_label.pack()

response.bind("<Return>", calc)


root.mainloop()
