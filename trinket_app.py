import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


import text
import controller
import actions
def finish():
    result = messagebox.askyesno(title="Подтвержение операции", message="Точно хотите выйти?")
    if result:
        root.destroy()
        print("Закрытие приложения")
    else:
        messagebox.showinfo("Результат", "Операция отменена")




root = tk.Tk()
root.title("PHONEBOOK")
root.geometry("600x600")


root.configure(bg="aquamarine1", )

icon = tk.PhotoImage(file = "icon_tel_book.png")
root.iconphoto(False, icon)





# MAIN MENU

photo_main = tk.PhotoImage(file='cat_icon_138789.png')
lb_photo = tk.Label(image=photo_main)
lb_photo.place(x=35, y=60)
editor = tk.Label(text=text.main_menu, font=('Arial', 12))
editor.pack(anchor=tk.N, expand=1,padx=10, pady=10)
frame_main = tk.Frame()
frame_main.pack(anchor="center")
lb_main = tk.Label(frame_main,text="MAIN MENU", font=("Times New Roman", 10))
lb_main.grid(row=0,sticky="n", columnspan=3)

#BUTTONS

btn1 = ttk.Button(frame_main,text="1 Open file", command=controller.open_file)
btn1.grid(row=1,column=1, sticky="ew")


btn2 = tk.Button(frame_main,text="2 Save file", bg="blue", command=controller.save_file)
btn2.grid(row=2, column=1, sticky="ew")


btn3 = ttk.Button(frame_main,text="3 Show contacts", command=actions.new_window_contact)
btn3.grid(row=3, column=1, sticky="ew")


btn4 = tk.Button(frame_main, text="4 Add new contact", bg="blue", command=actions.save_new_contact)
btn4.grid(row=4, column=1, sticky="ew")


btn5 = ttk.Button(frame_main, text="5 Find contact",command=controller.start_search)
btn5.grid(row=1, column=2, sticky="ew")


btn6 = tk.Button(frame_main, text="6 Change contact",bg="blue", command=controller.change_person)
btn6.grid(row=2, column=2, sticky="ew")


btn7 = ttk.Button(frame_main, text="7 Delete contact ", command=controller.delete_person)
btn7.grid(row=3, column=2, sticky="ew")


btn8 = tk.Button(frame_main, text="8 EXIT",bg='brown1', command=finish)
btn8.grid(row=4, column=2, sticky="ew")


root.mainloop()