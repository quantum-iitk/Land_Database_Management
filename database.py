class Database(object):

    @staticmethod
    def represents_int(s):
        try:
            int(s)
            return True
        except ValueError:
            return False
        
    @staticmethod
    def insert_data(db, numcol, entries, new_var, value):
        cursor2 = db.cursor()
        database1 = "movedb"

        # print(entries[j].get())
        p = "("
        q = "("
        for l in range(0, numcol - 1):
            if Database.represents_int(entries[l].get()):
                p = p + entries[l].get() + ","
            else:
                p = p + "'" + entries[l].get() + "'" + ","
            q = q + "`" + new_var[l] + "`" + ","
        if Database.represents_int(entries[numcol - 1].get()):
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

    @staticmethod
    def delete_data(db, value, entries, new_var):
        cursor3 = db.cursor()
        database1 = "movedb"
        table_name = "`" + value + "`"
        r = "`" + new_var[0] + "`"
        if Database.represents_int(entries[0].get()):
            s = entries[0].get()
        else:
            s = "'" + entries[0].get() + "'"

        cursor3.execute("DELETE FROM {0} WHERE {1} ={2} ".format(table_name, r, s))
        
    @staticmethod
    def update_data(db, new_var, entries, value, numcol):
        new_var1 = []
        print("test")
        entries1 = []
        cursor4 = db.cursor()
        database1 = "movedb"
        table_name = "`" + value + "`"

        r = "`" + new_var[0] + "`"

        for m in range(0, numcol):
            if Database.represents_int(entries[m].get()):
                entries1.insert(m, entries[m].get())
            else:
                entries1.insert(m, "'" + entries[m].get() + "'")
        for number in range(0, numcol):
            new_var1.insert(number, "`" + new_var[number] + "`")
        if Database.represents_int(entries[0].get()):
            s = entries[0].get()
        else:
            s = "'" + entries[0].get() + "'"

        for l in range(0, numcol):
            cursor4.execute(
                """UPDATE {0} SET {1}={2} WHERE {3} ={4} """.format(table_name, new_var1[l], entries1[l], r, s))

    def __init__(self):
        pass
