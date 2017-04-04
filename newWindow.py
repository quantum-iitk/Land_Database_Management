from tkinter import *
from tkinter import ttk
import tkinter.filedialog
import pymysql as psql


# class newWindow:
#     def __init__(self,form_name,column_name):
#         self.form_name = form_name
#         self.column_name = column_name
#
#     root = Tk()
#     root.title("feet to converter")
#
#     mainframe = ttk.Frame(root, padding='3 3 12 12')
#     mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
#     root.columnconfigure(0, weight=1)
#     root.rowconfigure(0, weight=1)
#     mainframe.columnconfigure(1, weight=1)
#     mainframe.columnconfigure(2, weight=1)
#     mainframe.columnconfigure(3, weight=1)
#     mainframe.rowconfigure(1, weight=1)
#     mainframe.rowconfigure(2, weight=1)
#     mainframe.rowconfigure(3, weight=1)
#


class Window(tkinter.Tk):
    def __init__(self, form_name, column, cursor):
        self.column = column
        self.form_name = form_name
        self.column_name = list(column.keys())
        self.column_dttype = list(column.values())
        self.cursor = cursor

        self.col_str = "("
        for name in self.column_name:
            if self.column_name.index(name) != 0:
                self.col_str = self.col_str + ",`" + name + "`"
            else:
                self.col_str = self.col_str + "`" + name + "`"
        self.col_str = self.col_str + ')'


        tkinter.Tk.__init__(self)
        self.title("Insert Your Data")
        # self.geometry("200x200")
        mainframe = ttk.Frame(self, padding='3 3 12 12')
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        mainframe.columnconfigure(1, weight=1)
        mainframe.columnconfigure(2, weight=1)
        mainframe.columnconfigure(3, weight=1)

        # self.data_to_enter = []
        self.data_to_enter_obj = []
        for i,name in enumerate(self.column_name):
            mainframe.rowconfigure(i, weight=1)
            ttk.Label(mainframe, text=name).grid(column=1, row=i, sticky=W)
            data_entry = ttk.Entry(mainframe, width=7)
            self.data_to_enter_obj.append(data_entry)
            data_entry.grid(column=3,row=i,sticky=(W, E))
        ttk.Button(mainframe, text="Submit", command=self.insert, cursor='plus').grid(column=3, row=i+1, sticky=W)

    def insert(self):
        data_to_enter = [a.get() for a in self.data_to_enter_obj]
        print(data_to_enter)
        for data_type, data in zip(list(self.column.values()),data_to_enter):
            if data_type == 'int':
                try:
                    data_to_enter[data_to_enter.index(data)] = int(data)
                except:
                    print("DATA TYPE ERROR",data_type,data)
                    return NONE
            elif data_type == 'float':
                try:
                    data_to_enter[data_to_enter.index(data)] = float(data)
                except:
                    print("DATA TYPE ERROR",data_type,data)
                    return NONE
            else:
                data_to_enter[data_to_enter.index(data)] = data

        command_str = '('

        for name in data_to_enter:
            if data_to_enter.index(name) !=0:
                command_str = command_str + ",'"+str(name)+"'"
            else:
                command_str = command_str + "'" + str(name) + "'"
        command_str = command_str+')'


        query = "INSERT INTO `"+self.form_name+"` "+self.col_str+" VALUES "+command_str
        print(query)
        self.cursor.execute(query)

# if __name__ == "__main__":
#     application = Window()
#     application.mainloop()


def run(form_name, column, dbname):
    connection = psql.connect(host='localhost', user='root', password='', db=dbname, autocommit=True,
                              charset='utf8mb4', cursorclass=psql.cursors.DictCursor)

    cursor = connection.cursor()
    application = Window(form_name, column, cursor)
    application.mainloop()
