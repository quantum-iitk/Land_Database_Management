from tkinter import *
from tkinter import ttk
import pymysql as psql
from newWindow import run
from test_draft import print_data

def main1(dbname):
    connection = psql.connect(host='localhost', user='root', password='', db=dbname, charset='utf8mb4',
                              autocommit=TRUE, cursorclass=psql.cursors.DictCursor)

    cursor = connection.cursor()

    cursor.execute('SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = \'BASE TABLE\' AND TABLE_SCHEMA=\'%s\''%(dbname))

    data = (cursor.fetchall())
    table_name = []
    for a in data:
        table_name.append(a['TABLE_NAME'])



    def open_form(*args):
        try:
            form_name = table_name[lsb.curselection()[0]]
            cursor.execute("SELECT `COLUMN_NAME`,`DATA_TYPE` FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA='%s' AND TABLE_NAME='%s'"%(dbname,form_name))
            column={}
            # print(cursor.fetchall())
            col_data = cursor.fetchall()
            for a in col_data:
                column[a['COLUMN_NAME']]=a['DATA_TYPE']
            # form = newWindow(form_no, column_name)
            print(list(column.keys()))
            # print(column)
            run(form_name,column,dbname)
            # value = float(feet.get())
            # meters.set((0.3048 * value * 10000.0 + 0.5) / 10000.0)
        except ValueError:
            pass

    def print_details(*args):
        try:
            form_name = table_name[lsb_query.curselection()[0]]
            print_data(form_name,dbname)
        except ValueError:
            pass


    root = Tk()
    root.title(dbname)

    root.wm_geometry("1120x650+20+40")

    gui_style = ttk.Style()
    gui_style.configure('My.TButton', foreground='#334353')
    gui_style.configure('My.TFrame', background='#334353')

    mainframe = ttk.Frame(root,padding='3 3 12 12',style='My.TFrame')
    mainframe.grid(column=0,row=0,sticky=(N, W, E, S))

    # root.columnconfigure(0,weight=1)
    # root.columnconfigure(1, weight=1)
    # root.rowconfigure(0,weight=1)
    # mainframe.columnconfigure(1,weight=1)
    # mainframe.columnconfigure(2,weight=1)
    # mainframe.columnconfigure(3,weight=1)
    # mainframe.columnconfigure(4,weight=5)
    # mainframe.rowconfigure(1,weight=1)
    # mainframe.rowconfigure(2,weight=1)
    # mainframe.rowconfigure(3,weight=1)
    ttk.Label(mainframe, text="Forms").grid(column=1, row=1, sticky=(W,E))

    lsb = Listbox(mainframe, selectmode='SINGLE',height=35,bg="yellow",width=30)
    lsb.grid(column=1, row=2, rowspan=5, sticky=(W,E))
    for i, data in enumerate(table_name):
        lsb.insert(i, data)

    ttk.Button(mainframe, text="INSERT", command=open_form, cursor='plus').grid(column=1, row=7, sticky=(W,E))

    ttk.Label(mainframe, text="Queries").grid(column=2, row=1, sticky=(W,E))

    lsb_query = Listbox(mainframe, selectmode='SINGLE',height=35,bg="yellow",width=30)
    lsb_query.grid(column=2, row=2, rowspan=5, sticky=(W,E))
    for i, data in enumerate(table_name):
        lsb_query.insert(i, data)

    ttk.Button(mainframe, text="PRINT", command=print_details, cursor='plus').grid(column=2, row=7, sticky=(W,E))


    background_image = PhotoImage(file="E:\\3647.jpg")
    background_label = Label(mainframe, image=background_image)
    background_label.grid(column = 3,row=2,columnspan=6 ,rowspan=6,sticky=(N,W,E,S),pady=(5,5))
    # background_label.place(x=0, y=0, relwidth=1, relheight=1)


    # ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))



    # ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

    for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
    # feet_entry.focus()
    # root.bind('<Return>', calculate)

    root.mainloop()
