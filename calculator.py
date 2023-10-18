from tkinter import *

n1 = n2 = operator = None

def create_button(root, text, row, column, command=None):
    button = Button(root, text=text, bg='#00a65c', fg='black', height=2, width=5, command=command)
    button.config(font=('verdana', 14))
    button.grid(row=row, column=column)
    return button

def get_digit(digit):
    current = result_label['text']
    new = current + str(digit)
    if len(new) > 8:
        new = new[:8]  # Limit the display to 8 characters
    result_label.config(text=new)

def clear():
    global n1, operator
    n1 = n2 = operator = None
    result_label.config(text='')

def operation(op):
    global n1, operator
    n1 = int(result_label['text'])
    operator = op
    result_label.config(text='')

def get_result():
    global n1, n2, operator
    try:
        n2 = int(result_label['text'])

        if operator == '+':
            result = n1 + n2
        elif operator == '-':
            result = n1 - n2
        elif operator == 'x':
            result = n1 * n2
        elif operator == '/':
            if n2 == 0:
                result_label.config(text='Math Error')
                return
            result = n1 / n2
            result = format(result, ".2f")  

        result_label.config(text=str(result))
    except ValueError:
        result_label.config(text='Input Error')

# Creating the interface
root = Tk()
root.geometry("280x380")
root.resizable(0, 0)
root.title("Calculator")
root.config(background='black')

# Displaying the number on the screen
result_label = Label(root, text='', bg='black', fg='white')
result_label.config(font=('verdana', 30, 'bold'))
result_label.grid(row=0, column=0, columnspan=5, pady=(50, 25), sticky='w')

# Creating buttons for digits 7-9
create_button(root, text='7', row=1, column=0, command=lambda: get_digit(7))
create_button(root, text='8', row=1, column=1, command=lambda: get_digit(8))
create_button(root, text='9', row=1, column=2, command=lambda: get_digit(9))

# Creating buttons for digits 4-6
create_button(root, text='4', row=2, column=0, command=lambda: get_digit(4))
create_button(root, text='5', row=2, column=1, command=lambda: get_digit(5))
create_button(root, text='6', row=2, column=2, command=lambda: get_digit(6))

# Creating buttons for digits 1-3
create_button(root, text='1', row=3, column=0, command=lambda: get_digit(1))
create_button(root, text='2', row=3, column=1, command=lambda: get_digit(2))
create_button(root, text='3', row=3, column=2, command=lambda: get_digit(3))

# Creating operator buttons
operators = ['+', '-', 'x', '/']
for i, op in enumerate(operators):
    create_button(root, text=op, row=i + 1, column=3, command=lambda op=op: operation(op))

# Creating Clear (C), 0, and Equals (=) buttons
create_button(root, text='C', row=4, column=0, command=lambda: clear())
create_button(root, text='0', row=4, column=1, command=lambda: get_digit(0))
create_button(root, text='=', row=4, column=2, command=lambda: get_result())

root.mainloop()
