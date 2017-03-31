from tkinter.tix import *
from PIL import ImageTk, Image
#install Pillow using pip

import MySQLdb

root = Tk()
root.title("Land Database Management System")
myContainer = Frame(root)
myContainer.grid()
db = MySQLdb.connect("localhost", port=3306, user="root", db="movedb")
entries = []
variables = []
array = []
new_var = []
numcol = 0


def represents_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def view_table():
    value = str((listbox1.get(listbox1.curselection())))

    col_window = Toplevel()
    col_window.title("Name of Columns")
    col_window.focus_set()

    cursor1 = db.cursor()

    database1 = "movedb"
    cursor1.execute(
        "SELECT `COLUMN_NAME` FROM `INFORMATION_SCHEMA`.`COLUMNS` WHERE `TABLE_SCHEMA` = %s AND `TABLE_NAME` = %s",
        (database1, value))
    db.commit()
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

    #
    # array1=["hey Baby"]
    # print(array1[0])
    # for m in new_var:
    #     print (m)


    def insert_data():
        cursor2 = db.cursor()
        database1 = "movedb"

        # print(entries[j].get())
        p = "("
        q = "("
        for l in range(0, numcol - 1):
            if represents_int(entries[l].get()):
                p = p + entries[l].get() + ","
            else:
                p = p + "'" + entries[l].get() + "'" + ","
            q = q + "`" + new_var[l] + "`" + ","
        if represents_int(entries[numcol - 1].get()):
            p = p + entries[numcol - 1].get() + ")"
        else:
            p = p + "'" + entries[numcol - 1].get() + "'" + ")"
        table_name = "`" + value + "`"

        q = q + "`" + new_var[numcol - 1] + "`" + ")"
        # print (p)
        # print (q)
        cursor2.execute("INSERT INTO {0} {1} VALUES {2} ".format(table_name, q, p))
        # db.commit()
        # for x in entries:
        #     print (x.get())

    def delete_data():
        cursor3 = db.cursor()
        database1 = "movedb"
        table_name = "`" + value + "`"
        r = "`" + new_var[0] + "`"
        if represents_int(entries[0].get()):
            s = entries[0].get()
        else:
            s = "'" + entries[0].get() + "'"

        cursor3.execute("DELETE FROM {0} WHERE {1} ={2} ".format(table_name, r, s))

    def update_data():
        new_var1 = []
        entries1 = []
        cursor4 = db.cursor()
        database1 = "movedb"
        table_name = "`" + value + "`"

        r = "`" + new_var[0] + "`"

        for m in range(0, numcol):
            if represents_int(entries[m].get()):
                entries1.insert(m, entries[m].get())
            else:
                entries1.insert(m, "'" + entries[m].get() + "'")
        for number in range(0, numcol):
            new_var1.insert(number, "`" + new_var[number] + "`")
        if represents_int(entries[0].get()):
            s = entries[0].get()
        else:
            s = "'" + entries[0].get() + "'"

        for l in range(0, numcol):
            cursor4.execute(
                """UPDATE {0} SET {1}={2} WHERE {3} ={4} """.format(table_name, new_var1[l], entries1[l], r, s))

    button_insert = Button(col_window, text="INSERT", command=insert_data)
    button_insert.grid(row=i + 1, column=1, sticky=SW)

    button_update = Button(col_window, text="UPDATE", command=update_data)
    button_update.grid(row=i + 1, column=2, sticky=SW)

    button_delete = Button(col_window, text="Delete", command=delete_data)
    button_delete.grid(row=i + 1, column=3, sticky=SW)


label = Label(root, text="The tables in the database are as follow:")
label.grid(row=0, column=0, sticky=N)
label.configure(background='green')
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

path = 'E:\\Land Database\\WindowsFormsApplication1\\Resources\\Photo.jpg'

#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img = ImageTk.PhotoImage(Image.open(path))

#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = Label(root, image = img)

#The Pack geometry manager packs widgets in rows or columns.
panel.grid(row=1,column=4,sticky=E)
root.configure(background='green')

cursor = db.cursor()
cursor.execute('SELECT table_name FROM information_schema.tables where table_schema=\'movedb\'')
db.commit()
num_tables = int(cursor.rowcount)
for i in range(0, num_tables):
    row = cursor.fetchone()
    listbox1.insert(END, row[0])

root.mainloop()
db.close()
