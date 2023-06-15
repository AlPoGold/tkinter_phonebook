import tkinter as tk
from tkinter import ttk


import text
import controller
import actions
def finish():
    root.destroy()
    print("Закрытие приложения")



root = tk.Tk()
root.title("PHONEBOOK")
root.geometry("600x600")


icon = tk.PhotoImage(file = "icon_tel_book.png")
root.iconphoto(False, icon)





# MAIN MENU
editor = tk.Text()
editor.pack()
editor.insert("1.0", text.main_menu)

#BUTTONS

btn1 = ttk.Button(text="1 Open file", command=controller.open_file)
btn1.pack()


btn2 = ttk.Button(text="2 Save file", command=controller.save_file)
btn2.pack()


#view.console.show_contacts(model.phone_book)
btn3 = ttk.Button(text="3 Show contacts", command=actions.new_window_contact)
btn3.pack()


btn4 = ttk.Button(text="4 Add new contact", command=actions.save_new_contact)
btn4.pack()


btn5 = ttk.Button(text="5 Find contact",command=controller.start_search)
btn5.pack()


btn6 = ttk.Button(text="6 Change contact", command=controller.change_person)
btn6.pack()


btn7 = ttk.Button(text="7 Delete contact ", command=controller.delete_person)
btn7.pack()


btn8 = ttk.Button(text="8 EXIT", command=finish)
btn8.pack()










root.mainloop()