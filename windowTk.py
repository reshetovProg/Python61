from tkinter import *
from tkinter import ttk
import random

def finish():
    root.destroy()  # ручное закрытие окна и всего приложения
    print("Закрытие приложения")


root = Tk()  # создаем корневой объект - окно
root.title("Приложение на Tkinter")
root.protocol("WM_DELETE_WINDOW", finish)# устанавливаем заголовок окна
# root.geometry("600x800")  # устанавливаем размеры окна
root.iconbitmap(default="favicon.ico")


label = Label(text="Активная кнопка:", background="#B3E5FC")
label.grid(row=0, column=0, pady=4, padx=2, sticky="nsew")
label["background"]="#B3E5FC"
# label.pack()

def on_click(label, text):
    print(text)
    label["text"]=f"Активная кнопка: {text}"
    label["background"]=colors[random.randint(0,len(colors)-1)]

for c in range(3): root.columnconfigure(index=c, weight=1)
for r in range(5): root.rowconfigure(index=r, weight=1)

# style = ttk.Style()
# style.configure("btn_style", background="red")   # фоновый цвет

btns_value=[7,8,9,4,5,6,1,2,3,0]
colors=["red",'green','blue']
for r in range(3):
    for c in range(3):
        val = f"{btns_value[r * 3 + c]}"
        btn = ttk.Button(text=val, command=lambda v=val: on_click(label, v))
        btn.grid(row=r+1, column=c, ipadx=6, ipady=3, padx=2, pady=2, sticky="nsew")
txt = f"{btns_value[len(btns_value)-1]}"
btn = ttk.Button(text=txt, command=lambda: on_click(label, txt))
btn.grid(row=4, column=0, ipadx=6, ipady=3, padx=2, pady=2, columnspan=3, sticky="nsew")


root.mainloop()