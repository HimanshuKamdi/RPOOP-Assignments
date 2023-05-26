import tkinter as tk
from tkinter import messagebox

def check_answer(answer):
    if answer == 'Correct':
        messagebox.showinfo('Result', 'Correct answer!')
    else:
        messagebox.showinfo('Result', 'Incorrect answer!')

root = tk.Tk()
root.title('Quiz')
root.geometry('400x300')

frame = tk.Frame(root)
frame.pack(pady=20)

question_label = tk.Label(frame, text='What is the financial capital of India?', font=('Arial', 14))
question_label.grid(row=0, column=0, columnspan=2)

correct_button = tk.Button(frame, text='Mumbai', command=lambda: check_answer('Correct'), bg='cyan', padx=10, pady=5)
correct_button.grid(row=3, column=0, padx=10, pady=50)

incorrect_button = tk.Button(frame, text='Delhi', command=lambda: check_answer('Incorrect'), bg='yellow', padx=10, pady=5)
incorrect_button.grid(row=3, column=1, padx=10, pady=50)

frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)

root.mainloop()
