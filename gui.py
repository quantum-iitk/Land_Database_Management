from tkinter import *
from database import Database


root = Tk()
root.title("Land Database Management System")
myContainer = Frame(root)
myContainer.grid()
entries = []
variables = []
array = []
new_var = []
numcol = 0
database = Database()


def view_table():
    value = str((listbox1.get(listbox1.curselection())))

    col_window = Toplevel()
    col_window.title("Name of Columns")
    col_window.focus_set()

    cursor1 = database.get_cursor()

    database1 = "movedb"
    cursor1.execute(
        "SELECT `COLUMN_NAME` FROM `INFORMATION_SCHEMA`.`COLUMNS` WHERE `TABLE_SCHEMA` = %s AND `TABLE_NAME` = %s",
        (database1, value))
    global numcol, i
    numcol = int(cursor1.rowcount)
    for i in range(0, numcol):
        row1 = [x[0] for x in cursor1.fetchmany()]

        array.insert(i, row1)
        label1 = Label(col_window, text=row1[0])
        label1.grid(row=i, column=1, sticky=W)
        va = StringVar()
        entry = Entry(col_window, textvariable=StringVar())
        entry.grid(row=i, column=2, padx=2, pady=2)
        variables.append(va)
        entries.append(entry)

    for k in range(0, numcol):
        vary = (", ".join(array[k]))
        new_var.insert(k, vary)

    button_insert = Button(col_window, text="INSERT",
                           command=lambda: database.insert_data(numcol, entries, new_var, value))
    button_insert.grid(row=i + 1, column=1, sticky=SW)

    button_update = Button(col_window, text="UPDATE",
                           command=lambda: database.update_data(new_var, entries, value, numcol))
    button_update.grid(row=i + 1, column=2, sticky=SW)

    button_delete = Button(col_window, text="Delete", command=lambda: database.delete_data(value, entries, new_var))
    button_delete.grid(row=i + 1, column=3, sticky=SW)


label = Label(root, text="The tables in the database are as follow:")
label.grid(row=0, column=0, sticky=N)
listbox1 = Listbox(root)
listbox1.grid(sticky=NSEW)

click = Button(root, text="Click to view tables", command=view_table)
click.grid(row=2, column=0, sticky=E, padx=2, pady=2)

my_menu = Menu(root)
menu_bar = Menu(root)
file_menu = Menu(menu_bar, tearoff=0)
# all file menu-items will be added here next
menu_bar.add_cascade(label='Help', menu=file_menu)
root.config(menu=menu_bar)
file_menu = Menu(menu_bar, tearoff=0)
# all file menu-items will be added here next
menu_bar.add_cascade(label='About', menu=file_menu)
root.config(menu=menu_bar)

cursor = database.get_cursor()
cursor.execute('SELECT table_name FROM information_schema.tables where table_schema=\'movedb\'')
num_tables = int(cursor.rowcount)
for i in range(0, num_tables):
    row = cursor.fetchone()
    listbox1.insert(END, row[0])

root.mainloop()
database.close_database()
