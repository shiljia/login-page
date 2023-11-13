
import trinter as tk

root.tk.Tk()
root.title('Login Page')

u=tk.Label(root,text='USER NAME',fg='black',height=1,width=10,font=('arial',9))
u.grid(row=1,column=1)

un=tk.Entry(root,bg='gray',fg='white',width=10,font=('PanRoman',16))
un.grid(row=2,column=1)

p=tk.Label(root,text='PASSWORD',fg='black',height=1,width=10,font=('arial',9))
p.grid(row=3,column=1)

pw=tk.Entry(root,bg='gray',fg='white',width=10,font=('PanRoman',16))
pw.grid(row=4,column=1)

def stt():
    a=un.get()
    b=pw.get()

    import mysql.connector

    connection=mysql.connector.connect(host='localhost',
                                       user='root',
                                       db='db',
                                       passward='Caddcentre@123',
                                       port='3306')
    print('Connection Established')

    cr.connectiuon.cursor()
    cr.execute('select*from data where user_name=%s and passward=%s',[a,b])
    d=cr.fetchone()

    if d:
        l.config(text='Login Success')
    else:
        l.config(text='Errorconnection')

    connection.commit()
    connection.close()


st=tk.Button(root,text='SUBMIT',bg='black',fg='white',width=10,font=('arial',9),command=stt)
st.grid(row=5,column=1)

l=tk.label(root,text='')
l.grid(row=6,column=1)

root.mainloop()
