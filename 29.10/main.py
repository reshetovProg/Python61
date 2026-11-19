from tkinter import ttk

from User import *
from Taxi import *
from tkinter import *
from File import *



def create_order(user: User):
    # depart = input("enter department: ")
    # destination = input("enter destination: ")
    user.create_order("q1", "q2")
    print(user.order)

def fill_table(users):
    tree.delete(*tree.get_children())
    for user in users:
        tree.insert("", END, values = (user.id, user.name, user.count_of_orders))

def click_button(current_user):
    create_order(current_user)
    fill_table(users)

def get_user_by_id(id):
    for user in users:
        if user.id==id:
            return user

def item_selected(event):
    #TODO global current_user нужно сюда передать
    item = tree.item(tree.selection()[0])
    user = item["values"]
    label_user["text"] = f"текущий пользователь: {user[1]}"
    current_user = get_user_by_id(user[0])


if __name__ == '__main__':

    user_db = File("user.csv")
    users_lines = user_db.get_lines()
    for i in range(1, len(users_lines)):
        user = User(users_lines[i].strip('\n'))
        print(user)

    current_user = get_user_by_id(1)
    car1 = Taxi("a678po", "Alex", "red", "Opel")
    car3 = Taxi("a678oo", "Pol", "red", "Opel")
    car4 = Taxi("a678om", "Pol", "red", "Opel")

    root = Tk()
    root.title("Приложение taxi")
    root.geometry("800x600")

    label = Label(text="пользователи")
    label_user = ttk.Label()



    frame = ttk.Frame(borderwidth=1, relief=SOLID, width=200)
    columns = ("id", "name", "count_of_orders")
    tree = ttk.Treeview(frame, columns=columns, show="headings", height=len(users), selectmode="browse")
    tree.heading("id", text="id")
    tree.heading("name", text="имя")
    tree.heading("count_of_orders", text="кол-во заказов")

    fill_table(users)


    tree.bind("<<TreeviewSelect>>", item_selected)
    btn = ttk.Button(text="сделать заказ", command=lambda: click_button(current_user))

    label.pack()
    frame.pack(padx=5, pady=5)
    tree.pack(expand=1)
    label_user.pack()
    btn.pack()

    root.mainloop()
