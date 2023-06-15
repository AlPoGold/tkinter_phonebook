import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import controller


def new_window_contact():
    window = tk.Tk()
    window.title("Contacts")
    window.geometry("800x800")

    # определяем столбцы

    columns = ["id_user", "name", "phone", "comments"]
    tree = ttk.Treeview(master=window, columns=columns, show="headings")
    tree.pack()

    #
    # определяем заголовки
    tree.heading("id_user", text="ID")
    tree.heading("name", text="Имя")
    tree.heading("phone", text="Телефон")
    # tree.heading("comment_person", text="Комментарий")

    # добавляем данные
    for person in controller.info_table:
        tree.insert("", tk.END, values=person)


    close_button = ttk.Button(window, text="Закрыть окно", command=lambda: window.destroy())
    close_button.pack(anchor="center", expand=1)

    window.mainloop()


contact = []

def save_new_contact():


    def add_contact():
        global contact

        new_contact.append(str(controller.max_id(controller.info_table) + 1))
        name = name_entry.get()
        new_contact.append(name)

        phone = phone_entry.get()
        new_contact.append(phone)

        comment = comment_entry.get()
        new_contact.append(comment)


        messagebox.showinfo('Message', 'Новый контакт добавлен!')
        controller.info_table.append(new_contact)
        print(new_contact)
        print(controller.info_table)

    window_new_contact = tk.Tk()
    window_new_contact.title('Добавление нового контакта')
    window_new_contact.geometry('400x300')
    test1 = tk.StringVar()
    test2 = tk.StringVar()
    test3 = tk.StringVar()
    frame = tk.Frame(
        window_new_contact,
        padx=10,
        pady=10
    )
    frame.pack(expand=True)

    name_lb = tk.Label(
        frame,
        text="Введите имя  "
    )
    name_lb.grid(row=3, column=1)

    phone_lb = tk.Label(
        frame,
        text="Введите телефон  ",
    )
    phone_lb.grid(row=4, column=1)

    comment_lb = tk.Label(
        frame,
        text="Введите комментарий  ",
    )
    comment_lb.grid(row=5, column=1)

    name_entry = tk.Entry(
        frame,
        textvariable=test1
    )
    name_entry.grid(row=3, column=2, pady=5)

    phone_entry = tk.Entry(
        frame,
        textvariable=test2
    )
    phone_entry.grid(row=4, column=2, pady=5)

    comment_entry = tk.Entry(
        frame,
        textvariable=test3
    )
    comment_entry.grid(row=5, column=2, pady=5)

    cal_btn = tk.Button(
        frame,
        text='Ввести данные',
        command=add_contact
    )
    cal_btn.grid(row=9, column=2)



    close_button = ttk.Button(frame, text="Закрыть окно", command=lambda: window_new_contact.destroy())
    close_button.pack(anchor="center", expand=1)

    window_new_contact.mainloop()



