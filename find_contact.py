from tkinter import *
from tkinter import messagebox

search_contact = ''
def start_search():


    def find_contact():
        global search_contact

        name = name_entry.get()
        search_contact+=name

    window_search = Tk()
    window_search.title('Поиск контакта')
    window_search.geometry('400x300')
    test1 = StringVar()

    frame = Frame(
        window_search,
        padx=10,
        pady=10
    )
    frame.pack(expand=True)

    name_lb = Label(
        frame,
        text="Введите имя  "
    )
    name_lb.grid(row=3, column=1)



    name_entry = Entry(
        frame,
        textvariable=test1
    )
    name_entry.grid(row=3, column=2, pady=5)



    cal_btn = Button(
        frame,
        text='Поиск',
        command=find_contact
    )
    cal_btn.grid(row=9, column=2)



    window_search.mainloop()
