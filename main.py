import tkinter
from tkinter import messagebox

window = tkinter.Tk()

window.title("BMI Calculator")
window.minsize(width=300,height=350)
window.config(padx=90,pady=90)


#reset
def reset_entry():
    my_entry.delete(0,'end')
    my_entry_2.delete(0,'end')


def calculate_bmi():
    try:
        kg = int(my_entry.get())
        m = int(my_entry_2.get())/100
        bmi = kg/(m*m)
        bmi = round(bmi, 1)
        bmi_index(bmi)
    except ValueError:
        messagebox.showerror('bmi-pythonguides',"You entered the information incorrectly!")

#BMI index
def bmi_index(bmi):
    if bmi <= 18.5:
        messagebox.showinfo('bmi-pythonguides', f'BMI = {bmi} is Underweight')
    elif 18.5 < bmi <= 24.9:
        messagebox.showinfo('bmi-pythonguides', f'BMI = {bmi} is Normal')
    elif 24.9 < bmi <= 29.9:
        messagebox.showinfo('bmi-pythonguides', f'BMI = {bmi} is Overweight')
    elif 29.9 < bmi <= 35:
        messagebox.showinfo('bmi-pythonguides', f'BMI = {bmi} is Obese Class 1!')
    elif 35 < bmi <= 40:
        messagebox.showinfo('bmi-pythonguides', f'BMI = {bmi} is Obese Class 2!')
    else:
        messagebox.showinfo('bmi-pythonguides', f'BMI = {bmi} is Obese Class 3!')

#label_1
my_label = tkinter.Label(text= "Enter Your Weight(kg)",font=('Ariel',11,"italic"))
my_label.pack()

#entry_1
my_entry = tkinter.Entry(width=20)
my_entry.pack()

#label_2
my_label_2 = tkinter.Label(text="Enter Your Height(cm)",font=('Ariel',11,"italic"))
my_label_2.pack()

#entry_2
my_entry_2 = tkinter.Entry(width=20)
my_entry_2.pack()

my_button = tkinter.Button(text="Colculate",width=12,command=calculate_bmi  )
my_button.pack()


my_reset_button = tkinter.Button(text="Reset",width=10,command=reset_entry)
my_reset_button.pack()


exit_button = tkinter.Button(text='Exit',width=8,command= lambda:window.destroy())
exit_button.pack()


window.mainloop()
