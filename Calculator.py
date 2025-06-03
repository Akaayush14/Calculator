#Manual code to display in terminal:
# def add(a,b):
#     return a+b

# def sub(a,b):
#     return a-b

# def mul(a,b):
#     return a*b

# def div(a,b):
#     return a/b

# print('choose one of the calculations: ')
# print(1,'Addition')
# print(2,'Subtraction')
# print(3,'Multiplication')
# print(4,'Division')

# # This part is not understood by me
# while True:
#     choice = input("Enter choice(1/2/3/4): ")
#     if choice in ('1', '2', '3', '4'):
#         try:
#             x = float(input("Enter first number: "))
#             y = float(input("Enter second number: "))
#         except ValueError:
#             print("Invalid input. Please enter a number.")
#             continue

#         if choice == '1':
#             print(x, "+", y, "=", add(x,y))

#         elif choice == '2':
#             print(x, '-', y, "=", sub(x,y))

#         elif choice == '3':
#             print(x, '*', y, "=", mul(x,y))

#         elif choice == '4':
#             print(x, '/', y, "=", div(x,y))

#         next_calculation = input("Let's do next calculation? (yes/no): ")
#         if next_calculation == "no":
#             break

#         else:
#             print('invalid number')

#Using tikinter

#Tkinter - built in GUI
#tk - is an alias for calling tkinter functions tk.Tk()
#messagebox - to show pop up messages when error is found
from customtkinter import *
import tkinter as tk
from tkinter import messagebox

#creating a button click function.
def click(event):                              #defining 
    current = entry.get()                      #current variable will store/receive/get the entered text from(input field).
    button_text = event.widget["text"]         #to get the text like 7, +, 1, etc (from buttons)

    if button_text == "=":                     #whenever '=' button is clicked, evaluates the output of the expression using eval()
        try:
            result = str(eval(current))        #result variable stores the eval of current(input field expression)
            entry.delete(0, tk.END)            #after getting eval, clears the input field
            entry.insert(tk.END, result)       #displays the final result
        except Exception as e:
            messagebox.showerror("Error", "Invalid Expression") #try exception is used for handling errors.
            entry.delete(0, tk.END)  #If error is found then clears the input field and pop ups error messages.

    elif button_text == "C":         #Clicking this button will clear the input field.
        entry.delete(0, tk.END)
                                     #buttons are clicked then it's representing text field such as 7,+,2 will be shown by this
    else:
        entry.insert(tk.END, button_text)

#creating main application window
root = tk.Tk()

#Setting background
root.configure(bg = "grey")

#setting title
root.title("Calculator")

#adding calculator icon
root.iconbitmap("calculator.ico")

#window size:
root.geometry("360x410")
root.resizable(0,0)

#creating entry text box and managing its structure like giving font, position and all.
#relief --> 3d border effect
#bd=10 --> border thickness
#justify="right" --> aligns text to the right
#columnspan=4 --> stretches textbox to 4 columns.
entry = tk.Entry(root, font="Arial 20", bd=10, relief=tk.FLAT, justify="right") 
entry.grid(row=0, column=0, columnspan=4, pady=10)

#defining the buttons layout
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+']
]

#creating the buttons in a loop
for i in range(4):
    for j in range(4):
        btn = tk.Button(root, text=buttons[i][j], font="Arial 18", width=5, height=2)
        btn.grid(row=i+1, column=j, padx=5, pady=5)
        btn.bind("<Button-1>", click)
#grid places each button in the correct row or column.
#bind connects each button to the click function(for detecting when a button is clicked)

# #manual creation of button and placing buttons value in it:
# # Row 1
# btn_7 = tk.Button(root, text=buttons[0][0], font="Arial 18", width=5, height=2)
# btn_8 = tk.Button(root, text=buttons[0][1], font="Arial 18", width=5, height=2)
# btn_9 = tk.Button(root, text=buttons[0][2], font="Arial 18", width=5, height=2)
# btn_div = tk.Button(root, text=buttons[0][3], font="Arial 18", width=5, height=2)

# btn_7.grid(row=1, column=0, padx=5, pady=5)
# btn_8.grid(row=1, column=1, padx=5, pady=5)
# btn_9.grid(row=1, column=2, padx=5, pady=5)
# btn_div.grid(row=1, column=3, padx=5, pady=5)

# # Row 2
# btn_4 = tk.Button(root, text=buttons[1][0], font="Arial 18", width=5, height=2)
# btn_5 = tk.Button(root, text=buttons[1][1], font="Arial 18", width=5, height=2)
# btn_6 = tk.Button(root, text=buttons[1][2], font="Arial 18", width=5, height=2)
# btn_mul = tk.Button(root, text=buttons[1][3], font="Arial 18", width=5, height=2)

# btn_4.grid(row=2, column=0, padx=5, pady=5)
# btn_5.grid(row=2, column=1, padx=5, pady=5)
# btn_6.grid(row=2, column=2, padx=5, pady=5)
# btn_mul.grid(row=2, column=3, padx=5, pady=5)

# # Row 3
# btn_1 = tk.Button(root, text=buttons[2][0], font="Arial 18", width=5, height=2)
# btn_2 = tk.Button(root, text=buttons[2][1], font="Arial 18", width=5, height=2)
# btn_3 = tk.Button(root, text=buttons[2][2], font="Arial 18", width=5, height=2)
# btn_sub = tk.Button(root, text=buttons[2][3], font="Arial 18", width=5, height=2)

# btn_1.grid(row=3, column=0, padx=5, pady=5)
# btn_2.grid(row=3, column=1, padx=5, pady=5)
# btn_3.grid(row=3, column=2, padx=5, pady=5)
# btn_sub.grid(row=3, column=3, padx=5, pady=5)

# # Row 4
# btn_c = tk.Button(root, text=buttons[3][0], font="Arial 18", width=5, height=2)
# btn_0 = tk.Button(root, text=buttons[3][1], font="Arial 18", width=5, height=2)
# btn_eq = tk.Button(root, text=buttons[3][2], font="Arial 18", width=5, height=2)
# btn_add = tk.Button(root, text=buttons[3][3], font="Arial 18", width=5, height=2)

# btn_c.grid(row=4, column=0, padx=5, pady=5)
# btn_0.grid(row=4, column=1, padx=5, pady=5)
# btn_eq.grid(row=4, column=2, padx=5, pady=5)
# btn_add.grid(row=4, column=3, padx=5, pady=5)

# # Bind all buttons to the click event
# buttons_list = [btn_0, btn_1, btn_2, btn_3, btn_4, btn_5, btn_6, btn_7, btn_8, btn_9,
#                 btn_add, btn_sub, btn_mul, btn_div, btn_eq, btn_c]

# for btn in buttons_list:
#     btn.bind("<Button-1>", click)

#it keeps the app running
root.mainloop()
    