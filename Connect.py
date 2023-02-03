import pyodbc


class Connect:
    def __init__(self, db, user, password, server):
        self.connect = pyodbc.connect("Driver={SQL Server};"
                                      "Server=" + server + ";"
                                                           "Database=" + db + ";"
                                                                              "UID=" + user + ";"
                                                                                              "PWD=" + password + ";",
                                      autocommit=True)

    def insert_staff(self, insertDict):
        con = self.connect
        cur = con.cursor()
        query = f"INSERT INTO staff " \
                f"values ('{insertDict['Surname']}'," \
                f"'{insertDict['Lastname']}'," \
                f"'{insertDict['BirthDay']}'," \
                f"'{insertDict['Phone']}'," \
                f"'{insertDict['Post']}'," \
                f"'{insertDict['Date_input']}'," \
                f"'{insertDict['Type_post']}')"
        try:
            cur.execute(query)
        except pyodbc.Error as err:
            print("Error", err)
        cur.close()

    def update_staff(self, insertDict):
        con = self.connect
        cur = con.cursor()
        query = f"UPDATE staff " \
                f"set Surname='{insertDict['Surname']}'," \
                f"Lastname='{insertDict['Lastname']}'," \
                f"BirthDay='{insertDict['BirthDay']}'," \
                f"Phone='{insertDict['Phone']}'," \
                f"Post='{insertDict['Post']}'," \
                f"Date_input='{insertDict['Date_input']}'," \
                f"Type_post='{insertDict['Type_post']}' " \
                f"where T_Number={insertDict['T_Number']}"
        try:
            cur.execute(query)
        except pyodbc.Error as err:
            print("Error", err)
        cur.close()

    def get_staff_all(self):
        con = self.connect
        cur = con.cursor()
        query = f"SELECT * FROM staff"
        try:
            cur.execute(query)
            rows = cur.fetchall()
        except pyodbc.Error as err:
            print("Error", err)
        cur.close()
        return rows

    def get_staff_by_surname(self, name):
        con = self.connect
        cur = con.cursor()
        query = f"SELECT * FROM staff WHERE Surname='" + name + "'"
        try:
            cur.execute(query)
            rows = cur.fetchall()
        except pyodbc.Error as err:
            print("Error", err)
        cur.close()
        return list(rows)

    def delete_staff(self, id_staff):
        con = self.connect
        cur = con.cursor()
        query = f"DELETE FROM staff WHERE T_Number=" +id_staff
        try:
            cur.execute(query)
        except pyodbc.Error as err:
            print("Error", err)
        cur.close()
