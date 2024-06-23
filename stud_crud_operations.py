from tkinter import *
import tkinter.messagebox as msgbox
import mysql.connector as mysql

def insert():
    id=e_id.get()
    name= e_name.get()
    phn= e_phn.get()

    if(id=="" or name=="" or phn==""):
        msgbox.showinfo("Insert status","All fields required")
    else:
        con= mysql.connect(host="localhost", user="root", password="Samarth@11",database="python-tkinter")
        cursor = con.cursor()
        cursor.execute("insert into student values('"+id+"','"+name+"','"+phn+"')")
        cursor. execute("commit")
        
        e_id.delete(0,'end')
        e_name.delete(0,'end')
        e_phn.delete(0,'end')
        show()

        msgbox.showinfo("Insert Status","Inserted Successfully");
        con.close();

def delete():
    if(e_id.get()==""):
        msgbox.showinfo("Delete status","ID is required")
    else:
        con= mysql.connect(host="localhost", user="root", password="Samarth@11",database="python-tkinter")
        cursor = con.cursor()
        cursor.execute("delete from student where id='"+e_id.get()+"'")
        cursor. execute("commit")
        
        e_id.delete(0,'end')
        e_name.delete(0,'end')
        e_phn.delete(0,'end')
        show()

        msgbox.showinfo("Delete Status","Deleted Successfully");
        con.close();

def update():
    id=e_id.get()
    name= e_name.get()
    phn= e_phn.get()

    if(id=="" or name=="" or phn==""):
        msgbox.showinfo("Update status","All fields required")
    else:
        con= mysql.connect(host="localhost", user="root", password="Samarth@11",database="python-tkinter")
        cursor = con.cursor()
        cursor.execute("update student set name='"+name+"',phn='"+phn+"'where id='"+id+"'")
        cursor. execute("commit")
        
        e_id.delete(0,'end')
        e_name.delete(0,'end')
        e_phn.delete(0,'end')
        show()

        msgbox.showinfo("Update Status","Updated Successfully");
        con.close();

def get():
    if(e_id.get()==""):
        msgbox.showinfo("Fetch status","ID is required")
    else:
        con= mysql.connect(host="localhost", user="root", password="Samarth@11",database="python-tkinter")
        cursor = con.cursor()
        cursor.execute("select * from student where id='"+e_id.get()+"'")
        rows=cursor.fetchall()

        for row in rows:
            e_name.insert(0,row[1])
            e_phn.insert(0,row[2])

        msgbox.showinfo("Fetch Status","Fetched Successfully");
        con.close();

def show():
    con= mysql.connect(host="localhost", user="root", password="Samarth@11",database="python-tkinter")
    cursor = con.cursor()
    cursor.execute("select * from student")
    rows=cursor.fetchall()
    list.delete(0,list.size())

    for row in rows:
        insertData=str(row[0])+'            '+row[1]
        list.insert(list.size()+1,insertData)
        
    con.close()

root = Tk()
root.title("samarth")
root.geometry("600x300")

id = Label(root, text='Enter ID', font=('bold',10))
id.place(x=20,y=30)

name = Label(root, text='Enter Name', font=('bold',10))
name.place(x=20,y=60)

phn = Label(root, text='Enter Phone no', font=('bold',10))
phn.place(x=20,y=90)

e_id = Entry()
e_id.place(x=150, y=30)

e_name = Entry()
e_name.place(x=150, y=60)

e_phn = Entry()
e_phn.place(x=150, y=90)

insert = Button(root,text='Insert', font=("italic",10), bg ="white", command=insert)
insert.place(x=20, y=140)

delete = Button(root,text='Delete', font=("italic",10), bg ="white", command=delete)
delete.place(x=70, y=140)

update = Button(root,text='Update', font=("italic",10), bg ="white", command=update)
update.place(x=130, y=140)

get = Button(root,text='Get', font=("italic",10), bg ="white", command=get)
get.place(x=190, y=140)

list= Listbox(root)
list.place(x=290,y=30)
show()

root.mainloop()
