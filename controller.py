import actions
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk

path = 'phones.txt'
info=''

info_table = []


def open_file():
    with open(path, 'r', encoding='utf-8') as file:
        global info
        global info_table
        info = file.read()
        info_table =[item.split(':') for item in info.split('\n')]
        print(info_table)

def save_file():
    with open(path, 'w', encoding='utf-8') as file:
        global info_table
        data = [':'.join(item) for item in info_table]
        print(*data, file=file, sep='\n')

def max_id(data: list):
     max_id = int(info_table[-1][0])
     return max_id

res = []

search_contact = ''

def start_search():


    def find_contact():
        global search_contact
        name = name_entry.get()
        search_contact+=name

        for person in info_table:
            for item in person:
                if search_contact and search_contact.lower() in item.lower():
                    res.append(person)
                    continue


        if res:
            messagebox.showinfo('Message', f'Найдено {len(res)} контактов!')
            res_win = tk.Tk()
            res_win.title("Результаты поиска")
            res_win.geometry("250x200")

            res_var = tk.Variable(master=res_win,value=[" | ".join(i) for i in res])

            res_listbox = tk.Listbox(res_win, listvariable=res_var)

            res_listbox.pack(anchor=tk.NW, fill=tk.X, padx=5, pady=5)

            res_win.mainloop()
        else:
            messagebox.showinfo('Message', 'Контактов не найдено!')

    window_search = tk.Tk()
    window_search.title('Поиск контакта')
    window_search.geometry('400x300')
    test1 = tk.StringVar()

    frame = tk.Frame(
        window_search,
        padx=10,
        pady=10
    )
    frame.pack(expand=True)

    name_lb = tk.Label(
        frame,
        text="Введите имя  "
    )
    name_lb.grid(row=3, column=1)



    name_entry = tk.Entry(
        frame,
        textvariable=test1
    )
    name_entry.grid(row=3, column=2, pady=5)



    cal_btn = tk.Button(
        frame,
        text='Поиск',
        command=find_contact
    )
    cal_btn.grid(row=9, column=2)

    window_search.mainloop()


def delete_person():
    window_delete = tk.Tk()
    window_delete.title("Contacts")
    window_delete.geometry("800x400")

    # определяем столбцы

    columns = ["id_user", "name", "phone", "comments"]
    frame_tree = tk.Frame(window_delete)
    frame_tree.pack(anchor=tk.N)
    tree = ttk.Treeview(master=frame_tree, columns=columns, show="headings")
    tree.pack()

    # определяем заголовки
    tree.heading("id_user", text="ID")
    tree.heading("name", text="Имя")
    tree.heading("phone", text="Телефон")
    # tree.heading("comment_person", text="Комментарий")

    # добавляем данные
    for person in info_table:
        tree.insert("", tk.END, values=person)
    user_lb = tk.Label(window_delete, text='Введите ID удаляемого контакта')
    user_lb.pack(anchor="center")
    entry_user = tk.Entry(window_delete)
    entry_user.pack(anchor="center")
    def del_but():

        id_del = int(entry_user.get())
        if id_del in range(1, len(info_table)+1):
            del info_table[id_del - 1]
            messagebox.showinfo('Message', 'Контакт успешно удален!')
        else:
            messagebox.showinfo('Message', 'Контакт невозможно удалить!')
        index=1
        for person in info_table:
            person[0] = str(index)
            index+=1
    del_button = tk.Button(window_delete, text='Удалить', command=del_but)
    del_button.pack(anchor="center")


    close_button = ttk.Button(window_delete, text="Закрыть окно", command=lambda: window_delete.destroy())
    close_button.pack(anchor=tk.S, expand=1)

    window_delete.mainloop()

def change_person():
    window_change = tk.Tk()
    window_change.title("Contacts")
    window_change.geometry("800x400")

    # определяем столбцы

    columns = ["id_user", "name", "phone", "comments"]
    frame_tree = tk.Frame(window_change)
    frame_tree.pack(anchor=tk.N)
    tree = ttk.Treeview(master=frame_tree, columns=columns, show="headings")
    tree.pack()

    # определяем заголовки
    tree.heading("id_user", text="ID")
    tree.heading("name", text="Имя")
    tree.heading("phone", text="Телефон")
    # tree.heading("comment_person", text="Комментарий")

    # добавляем данные
    for person in info_table:
        tree.insert("", tk.END, values=person)
    user_lb = tk.Label(window_change, text='Введите ID изменяемого контакта')
    user_lb.pack(anchor="center")
    entry_user = tk.Entry(window_change)
    entry_user.pack(anchor="center")

    def change_but():

        id_change = int(entry_user.get())
        if id_change in range(1, len(info_table) + 1):
            contact = info_table[id_change-1]
            def  ch_contact():
                global contact
                contact = [str(id_change)]

                name = name_entry.get()
                contact.append(name)

                phone = phone_entry.get()
                contact.append(phone)

                comment = comment_entry.get()
                contact.append(comment)

                info_table[id_change-1] = contact
                messagebox.showinfo('Message', 'Контакт успешно изменен!')

            window_change_contact = tk.Tk()
            window_change_contact.title('Изменение контакта')
            window_change_contact.geometry('400x300')
            test1 = tk.StringVar()
            test2 = tk.StringVar()
            test3 = tk.StringVar()
            frame = tk.Frame(
                window_change_contact,
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
                command=ch_contact
            )
            cal_btn.grid(row=9, column=2)
            close_button = ttk.Button(frame, text="Закрыть окно", command=lambda: window_change_contact.destroy())
            close_button.pack(anchor="center", expand=1)

            window_change_contact.mainloop()


        else:
            messagebox.showinfo('Message', 'Контакт невозможно изменить!')


    change_button = tk.Button(window_change, text='Удалить', command=change_but)
    change_button.pack(anchor="center")


    close_button = ttk.Button(window_change, text="Закрыть окно", command=lambda: window_change.destroy())
    close_button.pack(anchor=tk.S, expand=1)

    window_change.mainloop()
