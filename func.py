import sqlite3

db=sqlite3.connect('data.db')
cur = db.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS func (id TEXT,son TEXT,amal TEXT,son_2 TEXT,belgi TEXT)""")
db.commit()
db.close()

def add_user(id):

    db = sqlite3.connect('data.db')
    cur = db.cursor()
    # func=cur.execute(f"""SELECT * FROM func """).fetchall()


    cur.execute(f"""INSERT INTO func VALUES ("{id}",'0','0','0','0')""")

    db.commit()
    db.close()

def get_son(id):
    db = sqlite3.connect('data.db')
    cur = db.cursor()
    func = cur.execute(f"""SELECT * FROM func""").fetchall()
    for i in func:
        if i[0]== str(id):
            if i[1]==str(0):
                return 0
            elif i[2]==str(0):
                return i[1]
            elif i[3]==str(0):
                return [i[1],i[2]]
            else :
                return [i[1],i[2],i[3]]

def  change_belgi(id):
    db = sqlite3.connect('data.db')
    cur = db.cursor()
    func = cur.execute("""SELECT * FROM func """).fetchall()
    for i in func:
        if i[0] == str(id):
                cur.execute(F"""UPDATE func SET belgi='1' WHERE id='{id}' """)
    db.commit()
    db.close()

def changeson(id, n):
    db = sqlite3.connect('data.db')
    cur = db.cursor()
    func = cur.execute(F"""SELECT * FROM func """).fetchall()
    for i in func:
        if i[0] == str(id):
            if i[4] == '0':
                son = int(f"{i[1]}{n}")
                cur.execute(F"""Update func SET son='{son}' WHERE id='{id}' """)
            else:
                son_2 = int(f"{i[3]}{n}")
                cur.execute(F"""Update func SET son_2='{son_2}' WHERE id='{id}' """)


    db.commit()
    db.close()

def changeamal(id,amal):
    db = sqlite3.connect('data.db')
    cur = db.cursor()
    func=cur.execute("""SELECT * FROM func """).fetchall()
    for i in func:
        if i[0]==str(id):

            cur.execute(F"""UPDATE func SET amal='{amal}' WHERE id='{id}' """)



    db.commit()
    db.close()

def clear(id):
    db = sqlite3.connect('data.db')
    cur = db.cursor()
    func = cur.execute("""SELECT * FROM func """).fetchall()
    for i in func:
        if i[0] == str(id):
            cur.execute(F"""UPDATE func SET son ='0',belgi='0', amal='0',son_2='0' WHERE id ='{id}'""")
    db.commit()
    db.close()
    return "tozalandi,yangi aperatsiyani boshlash mumkin"

def GetRes(id):
    db = sqlite3.connect('data.db')
    cur = db.cursor()
    func = cur.execute("""SELECT * FROM func """).fetchall()
    for i in func:
        if i[0] == str(id):
            if i[2]=='0':
                db.commit()
                db.close()
                return i[1]

            else:
                cur.execute(F"""UPDATE func SET son='{eval(f"{i[1]} {i[2]} {i[3]}")}' , amal='0',son_2='0',belgi='0' WHERE id ='{id}' """)
                db.commit()
                db.close()
                if i[2]=='*' or i[2]=="/" and i[3]=="0":
                    return eval(f"{i[1]} {i[2]} 1")
                else:
                    return eval(f"{i[1]} {i[2]} {i[3]}")