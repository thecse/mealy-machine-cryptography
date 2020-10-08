# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 16:31:54 2020

@author: Rohan
"""
from tkinter import *
from mealyUTIL import mealy
root = Tk()
root.title('Mealy Machine encryption')
#root.geometry("500x350")



def decrypt():
    string = txt.get()
    arr = list(string.split(' '))
    s = int(arr[-1])
    arr.pop()
    n = len(arr)
    arr = [int(arr[i]) for i in range(n)]
    
    state=0
    inp = bin(s)
    inp = inp[2:]
    for i in inp:
        op, state = mealy(i, state)
        op=int(op)
        if i=='0':
            for j in range(0, n, op):
                arr[j]=arr[j]-(2**op)-1
        else:
            for j in range(0, n, op):
                arr[j]=arr[j]-(2**op)+1
    arr = [chr(arr[i]) for i in range(n)]
    out.insert(0,arr)
    
    
lbl = Label(root, text='Enter Encrypted Message: ')
lbl.grid(row=0, column=0, padx=10, pady=10)
txt = Entry(root, width=30)
txt.grid(row=0, column=1, columnspan=3, padx=10, pady=10)
lbl2 = Label(root, text='Orignal Message: ')
lbl2.grid(row=2,column=0, padx=10, pady=10)
out = Entry(root, width=30)
out.grid(row=2, column=1, columnspan=3, padx=10, pady=10)
button = Button(root, text='Encrypt', command=decrypt)
button.grid(row=1, column=1, padx=10, pady=10)
root.mainloop()
