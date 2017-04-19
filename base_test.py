import pymysql as psql
from tkinter import *
from tkinter import ttk
from time import sleep
from sql_query_table import query as table_query


class FirstWindow:
    def Connect(self):
        if (self.District.get().strip() == "") | (self.tehsil.get().strip() == "") | (
                    self.village.get().strip() == "") | (self.paragana.get().strip() == ""):
            print("Enter correct data")
            return
        self.db_name = "land_records_" + self.District.get().strip() + "_" + self.tehsil.get().strip() + "_" + self.village.get().strip() + "_" + self.paragana.get().strip()
        try:
            print(self.db_name)
            # connection = psql.connect(host='localhost', user='root', password='', db=self.db_name, charset='utf8mb4',
            #                           cursorclass=psql.cursors.DictCursor)
            connection = self.connection
            print("Databse already exists and connected")
            self.root.destroy()
            # main1(self.db_name)
        except:
            # connection = psql.connect(host='localhost', user='root', password='', charset='utf8mb4',
            #                           cursorclass=psql.cursors.DictCursor
            #                           )
            connection = self.connection
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE `%s`" % self.db_name)
            print("New database created")

            connection = psql.connect(host='localhost', user='root', password='', db=self.db_name, charset='utf8mb4',
                                      cursorclass=psql.cursors.DictCursor)
            cursor = connection.cursor()
            cursor.execute(table_query)
            sleep(10)
            self.root.destroy()
            # main1(self.db_name)

    def __init__(self, connection):
        self.root = Tk()
        self.root.title("Database Connection")
        self.connection = connection

        gui_style = ttk.Style()
        gui_style.configure('My.TButton', foreground='#334353')
        gui_style.configure('My.TFrame', background='#334353')

        mainframe = ttk.Frame(self.root, padding='3 3 12 12', style='My.TFrame')
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

        self.District = StringVar()
        self.village = StringVar()
        self.tehsil = StringVar()
        self.paragana = StringVar()

        ttk.Label(mainframe, text='District').grid(column=1, row=1, sticky=(W, E), padx=3, pady=4)
        self.District = ttk.Entry(mainframe, textvariable=self.District)
        self.District.grid(row=1, column=2, sticky=(E,), padx=3, pady=4)

        ttk.Label(mainframe, text='Tehsil').grid(column=3, row=1, sticky=(W, E), padx=3, pady=4)
        self.tehsil = ttk.Entry(mainframe, textvariable=self.tehsil)
        self.tehsil.grid(row=1, column=4, sticky=(E,), padx=3, pady=4)

        ttk.Label(mainframe, text='Village').grid(column=1, row=2, sticky=(W, E), padx=3, pady=4)
        self.vilage = ttk.Entry(mainframe, textvariable=self.village)
        self.vilage.grid(row=2, column=2, sticky=(E,), padx=3, pady=4)

        ttk.Label(mainframe, text='Paragana').grid(column=3, row=2, sticky=(W, E), padx=3, pady=4)
        self.paragana = ttk.Entry(mainframe, textvariable=self.paragana)
        self.paragana.grid(row=2, column=4, sticky=(E,), padx=3, pady=4)

        ttk.Button(mainframe, text="Connect", command=self.Connect, cursor='plus', style="My.TButton").grid(column=5,
                                                                                                            row=1,
                                                                                                            columnspan=2,
                                                                                                            sticky=(
                                                                                                                E, W),
                                                                                                            pady=5,
                                                                                                            padx=3)

        background_image = PhotoImage(file="E:\\photo.png")
        # background_image = PhotoImage(file="E:\\LandDatabase\\WindowsFormsApplication1\\Resources\\Photo.jpg")
        background_label = Label(mainframe, image=background_image)
        background_label.grid(column=1, row=3, columnspan=6, rowspan=6, sticky=(N, W, E, S), pady=(5, 5))
        # data = (cursor.fetchall())
        # table_name = []
        # for a in data:
        #     table_name.append(a['TABLE_NAME'])
        #
        # print(table_name)

        self.root.bind('<Return>', self.Connect)
        self.District.focus()
        self.root.mainloop()
