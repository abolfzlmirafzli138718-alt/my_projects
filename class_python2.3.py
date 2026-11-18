import tkinter as tk
from tkinter import ttk
import json 

list_number_tow = []
list_number_one = []
list_jame = []
list_Subtraction= []
list_mul = []
#####################################################

def number_add(number):
    n = lebel_02.cget("text")
    lebel_02.config(text=n + str(number))

#####################################################

def number_item_Division():
    number = str(lebel_02.cget("text"))
    string_var.set(number +" ÷")
    if number != '' :
        list_number_one.append(int(number))
    lebel_02.config(text="")

def number_add_2():
    number = str(lebel_02.cget("text"))
    if number != '' :
        list_jame.append(int(number))   
    string_var.set(number +" +")
    lebel_02.config(text=" ")

def number_add_3():
    number = str(lebel_02.cget("text"))
    string_var.set(number +" -")
    if number != '' :
        list_Subtraction.append(int(number))
    lebel_02.config(text="")


def number_add_4():
    number = str(lebel_02.cget("text"))
    string_var.set(number +" x")
    if number != '' :
        list_mul.append(int(number))
    lebel_02.config(text="")


def number_add_5():
    lebel_02.config(text=" ")

def number_add_6():
    lebel_02.config(text=" ")
    lebel_01.config(text=" ")
    string_var.set(" ")
#####################################################
def division():
    try:
        num2 = str(lebel_02.cget("text"))
        list_number_tow.append(int(num2))        
        n1 = list_number_one[0]
        n2 = list_number_tow[0]
        result = n1 / n2 
        lebel_02.config(text=" ")
        lebel_02.config(text=str(result))
    except:
        print("Error")

    

def jame():
    try:
        su = 0
        num = str(lebel_02.cget("text"))
        list_jame.append(int(num))
        for i in list_jame:
            su += i 
        lebel_02.config(text=" ")
        lebel_02.config(text=str(su))
    except:
        print("Error")


def Subtraction():
    try:
        num = str(lebel_02.cget("text"))
        list_Subtraction.append(int(num))
        btr = list_Subtraction[0]
        for i in list_Subtraction[1:]:
            btr -= i
        lebel_02.config(text=" ")
        lebel_02.config(text=str(btr))
    except:
        print("Error")



def Multiplication():
    try:
        num = str(lebel_02.cget("text"))
        list_mul.append(int(num))
        mul = list_mul[0]
        for i in list_mul[1:]:
            mul *= i
        lebel_02.config(text=" ")
        lebel_02.config(text=str(mul))
    except:
        print("Error")



################################################
root = tk.Tk()
root.title("ماشین حساب")
root.geometry('900x500')
root.config(bg="#04343B")


string_var = tk.StringVar()

lebel_01 = tk.Label(master=root,text='',width=19,justify=("right"),bd=0,bg="#04343B",fg="white",font=("Roboto",10),textvariable=string_var)
lebel_01.grid(row=2,column=6,pady=15,padx=20,ipady=5)


lebel_02 = tk.Label(master=root,text='',width=19,justify=("right"),bd=0,bg="#096773",fg="white",font=("Roboto",22))
lebel_02.grid(row=1,column=6,pady=15,padx=20,ipady=25)




butten_01 = tk.Button(master=root, width=4,text='7',bg="#096773",fg="white",font=("Roboto",22),command=lambda: number_add(7))
butten_01.grid(row=2,column=1,pady=2,padx=2,ipady=5)

butten_02 = tk.Button(root, width=4,text='8',bg="#096773",fg="white",font=("Roboto",22),command=lambda: number_add(8))
butten_02.grid(row=2,column=2,pady=2,padx=2,ipady=5)

butten_03 = tk.Button(root, width=4,text='9',bg="#096773",fg="white",font=("Roboto",22),command=lambda: number_add(9))
butten_03.grid(row=2,column=3,pady=2,padx=2,ipady=5)

butten_04 = tk.Button(root, width=4,text='6',bg="#096773",fg="white",font=("Roboto",22),command=lambda: number_add(6))
butten_04.grid(row=3,column=1,pady=2,padx=2,ipady=5)

butten_05 = tk.Button(root, width=4,text='5',bg="#096773",fg="white",font=("Roboto",22),command=lambda: number_add(5))
butten_05.grid(row=3,column=2,pady=2,padx=2,ipady=5)

butten_06 = tk.Button(root, width=4,text='4',bg="#096773",fg="white",font=("Roboto",22),command=lambda: number_add(4))
butten_06.grid(row=3,column=3,pady=2,padx=2,ipady=5)

butten_07 = tk.Button(root, width=4,text='1',bg="#096773",fg="white",font=("Roboto",22),command=lambda: number_add(1))
butten_07.grid(row=4,column=1,pady=2,padx=2,ipady=5)

butten_08 = tk.Button(root, width=4,text='2',bg="#096773",fg="white",font=("Roboto",22),command=lambda: number_add(2))
butten_08.grid(row=4,column=2,pady=2,padx=2,ipady=5)

butten_09 = tk.Button(root, width=4,text='3',bg="#096773",fg="white",font=("Roboto",22),command=lambda: number_add(3))
butten_09.grid(row=4,column=3,pady=2,padx=2,ipady=5)

butten_10 = tk.Button(root, width=4,text='0',bg="#096773",fg="white",font=("Roboto",22),command=lambda: number_add(0))
butten_10.grid(row=5,column=2,pady=2,padx=2,ipady=5)

butten_11 = tk.Button(root, width=4,text='÷',bg="#096773",fg="white",font=("Roboto",22),command=number_item_Division)
butten_11.grid(row=2,column=4,pady=2,padx=2,ipady=5)

butten_12 = tk.Button(root, width=4,text='X',bg="#096773",fg="white",font=("Roboto",22),command=number_add_4)
butten_12.grid(row=3,column=4,pady=2,padx=2,ipady=5)

butten_13 = tk.Button(root, width=4,text='_',bg="#096773",fg="white",font=("Roboto",22),command=number_add_3)
butten_13.grid(row=4,column=4,pady=2,padx=2,ipady=5)

butten_14 = tk.Button(root, width=4,text='+',bg="#096773",fg="white",font=("Roboto",22),command=number_add_2)
butten_14.grid(row=5,column=4,pady=2,padx=2,ipady=5)

butten_15 = tk.Button(master=root, width=4,text=' ',bg="#096773",fg="white",font=("Roboto",22))
butten_15.grid(row=5,column=3,pady=2,padx=2,ipady=5)

butten_15 = tk.Button(master=root, width=4,text='=÷',bg="#1E1E72",fg="white",font=("Roboto",22),command=division)
butten_15.grid(row=6,column=1,pady=2,padx=2,ipady=5)

butten_15 = tk.Button(master=root, width=4,text='=-',bg="#1E1E72",fg="white",font=("Roboto",22),command=Subtraction)
butten_15.grid(row=6,column=2,pady=2,padx=2,ipady=5)

butten_15 = tk.Button(master=root, width=4,text='=x',bg="#1E1E72",fg="white",font=("Roboto",22),command=Multiplication)
butten_15.grid(row=6,column=3,pady=2,padx=2,ipady=5)

butten_15 = tk.Button(master=root, width=4,text='=+',bg="#1E1E72",fg="white",font=("Roboto",22),command=jame)
butten_15.grid(row=6,column=4,pady=2,padx=2,ipady=5)


butten_16 = tk.Button(root, width=4,text=' ',bg="#096773",fg="white",font=("Roboto",22))
butten_16.grid(row=5,column=1,pady=2,padx=2,ipady=5)

butten_16 = tk.Button(root, width=4,text='<=',bg="#096773",fg="white",font=("Roboto",22),command=number_add_5)
butten_16.grid(row=1,column=1,pady=2,padx=2,ipady=5)

butten_16 = tk.Button(root, width=4,text='C',bg="#096773",fg="white",font=("Roboto",22),command=number_add_6)
butten_16.grid(row=1,column=2,pady=2,padx=2,ipady=5)

lebel_03 = tk.Label(master=root,text='نکته : برای  تقسیم کردن بیشتر',width=23,justify=("right"),bd=0,bg="#04343B",fg="black",font=("Roboto",18))
lebel_03.grid(row=3,column=6,pady=14,padx=20,ipady=5)

lebel_04 = tk.Label(master=root,text='دو مقدار وارد نکنید ',width=23,justify=("right"),bd=0,bg="#04343B",fg="black",font=("Roboto",18))
lebel_04.grid(row=4,column=6,pady=14,padx=20,ipady=5)





root.mainloop()