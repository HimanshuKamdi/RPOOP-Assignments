import tkinter as tk
from tkinter import messagebox

def check_answer(answer):
    if answer == 'Correct':
        messagebox.showinfo('Result', 'Correct answer!')
    else:
        messagebox.showinfo('Result', 'Incorrect answer!')

def open_new_window():
    new_window = tk.Toplevel(root)
    new_window.title('New Window')
    new_window.geometry('300x200')  
    new_window_label = tk.Label(new_window, text='This is a new window', font=('Arial', 14))
    new_window_label.pack(fill='both', expand=True, padx=10, pady=10)
    new_window_label.place(relx=0.5, rely=0.5, anchor='center')

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

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label='New Window', command=open_new_window)
file_menu.add_command(label='Open', command=lambda: print("open"))
file_menu.add_command(label='Save', command=lambda: print("Save"))
file_menu.add_command(label='Save As', command=lambda: print("Save As"))
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label='File', menu=file_menu)

root.mainloop()
