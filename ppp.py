from Tkinter import *
import Tkinter
import base64
import urllib
import MySQLdb
import Tkinter as tk
import tkMessageBox
 


def clear2():
	root.destroy()
	s2()


def s2():
	root1 = Tk()
	root1.geometry("1500x880")
	root1.configure(background='#F1C40F')
	"""path = "tution.jpg"
	img = ImageTk.PhotoImage(Image.open(path))
	panel = tk.Label(root1, image = img)
	panel.pack(side = "bottom", fill = "both", expand = "yes")"""

	L1 = Label(root1, text="USERNAME", bg='black', fg='red', font=("Helvetica", 15))
	L1.pack(anchor=CENTER)
	L1.place(height=70, width=160, x=550, y=100)
	E1 = Entry(root1, bd =5)
	E1.pack(anchor=CENTER)
	E1.place(height=30, width=120, x=750, y=120)
	E1.get()

	L1 = Label(root1, text="PASSWORD", bg='black', fg='red', font=("Helvetica", 15))
	L1.pack(anchor=CENTER)
	L1.place(height=70, width=160, x=550, y=190)
	E2 = Entry(root1,show="#", bd =5)
	E2.pack(anchor=CENTER)
	E2.place(height=30, width=120, x=750, y=210)
	E2.get()

	B = Tkinter.Button(root1, text ="LOGIN",command= lambda:login(E1,E2), activebackground='white', activeforeground='blue', bd=10, bg='black', fg='red', font=("Arial Black", 15))
	B.pack()
	B.place(bordermode=OUTSIDE, height=60, width=200, x=600, y=270)

	B = Tkinter.Button(root1, text ="EXIT",cursor='pirate',command=lambda: bahar1(root1), activebackground='white', activeforeground='blue', bd=10, bg='black', fg='red', font=("Arial Black", 8))
	B.pack()
	B.place(bordermode=OUTSIDE, height=30, width=80, x=1139, y=633)

#	C = Tkinter.Button(top2,text="next")
	#C.pack()

def bahar1(root1):
	root1.destroy()

def login(E1,E2):
	db = MySQLdb.connect("localhost","root","","list")
	cursor = db.cursor()
	val=E1.get()
	val1=E2.get()
	lis=[val,val1]
	fl=tuple(list(lis))
	print(fl)
	sql = """SELECT username, pass FROM akshay"""
	cursor.execute(sql)
	results = cursor.fetchall()
#	print(results)
	q=type(results)
	fin=list(results)
#	print(type(fin))
	print(fin)
	for fin in results:
		if fl == fin:
			print("ENJOY YOU ARE ONLINE NOW")
			board(E1)
	
																																												

def board(E1):
	root2 = Tk()
	root2.geometry("1500x880")
	root2.configure(background='#27AE60')
	#path = "ppp.png"
	#img = ImageTk.PhotoImage(Image.open(path))
	#panel = tk.Label(root2, image = img)
	#panel.pack(side = "bottom", fill = "both", expand = "yes")


	db = MySQLdb.connect("localhost","root","","list")
	cursor = db.cursor()
	vall=E1.get()
	sql = """SELECT fname FROM akshay WHERE username = '%s'""" % (vall)
	cursor.execute(sql)
	results = cursor.fetchone()

	sql1 = """SELECT lname FROM akshay WHERE username = '%s'""" % (vall)
	cursor.execute(sql1)
	results1 = cursor.fetchone()

	sql2 = """SELECT mno FROM akshay WHERE username = '%s'""" % (vall)
	cursor.execute(sql2)
	results2 = cursor.fetchone()


	sql3 = """SELECT email FROM akshay WHERE username = '%s'""" % (vall)
	cursor.execute(sql3)
	results3 = cursor.fetchone()

	print(results)
	print(results1)
	print(results2)
	print(results3)

	L1 = Label(root2, text="INFORMATION", bg='black', fg='red', font=("Comic Sans MS", 25))
	L1.pack(anchor=CENTER)
	L1.place(height=70, width=300, x=640, y=50)

	L1 = Label(root2, text="NAME=>", bg='black', fg='red', font=("Hoefler Text", 15))
	L1.pack(anchor=CENTER)
	L1.place(height=70, width=180, x=240, y=150)

	L1 = Label(root2, text="LAST NAME==>", bg='black', fg='red', font=("Hoefler Text", 15))
	L1.pack(anchor=CENTER)
	L1.place(height=70, width=180, x=240, y=250)

	L1 = Label(root2, text="MOBILE NMBER==>", bg='black', fg='red', font=("Hoefler Text", 15))
	L1.pack(anchor=CENTER)
	L1.place(height=70, width=180, x=240, y=400)

	L1 = Label(root2, text="EMAIL-ID==>", bg='black', fg='red', font=("Hoefler Text", 15))
	L1.pack(anchor=CENTER)
	L1.place(height=70, width=180, x=240, y=500)

	L1 = Label(root2, text=results , bg='black', fg='red', font=("Hoefler Text", 15))
	L1.pack(anchor=CENTER)
	L1.place(height=70, width=600, x=440, y=150)

	L1 = Label(root2, text=results1 , bg='black', fg='red', font=("Hoefler Text", 15))
	L1.pack(anchor=CENTER)
	L1.place(height=70, width=600, x=440, y=250)

	L1 = Label(root2, text=results2 , bg='black', fg='red', font=("Hoefler Text", 15))
	L1.pack(anchor=CENTER)
	L1.place(height=70, width=600, x=440, y=400)

	L1 = Label(root2, text=results3 , bg='black', fg='red', font=("Hoefler Text", 15))
	L1.pack(anchor=CENTER)
	L1.place(height=70, width=600, x=440, y=500)

	B = Tkinter.Button(root2, text ="EXIT",cursor='pirate',command=lambda: bahar(root2), activebackground='white', activeforeground='blue', bd=10, bg='black', fg='red', font=("Arial Black", 8))
	B.pack()
	B.place(bordermode=OUTSIDE, height=30, width=80, x=1139, y=633)


	#C = Tkinter.Button(top2,text="next")
	#C.pack()

def bahar(root2):
	root2.destroy()




def signup(E1,E2,E3,E4,E5,E6,E7,root1):
	val=E1.get()
	val1=E2.get()
	val2=E3.get()
	val3=E4.get()
	val4=E5.get()
	val5=E6.get()
	val6=E7.get()
	if val5 == val6:
		if len(val) == 0:
			tkMessageBox.showinfo("USername", "Please input Username")
		else:
			db = MySQLdb.connect("localhost","root","","list")
			cursor = db.cursor()

			sql = """INSERT INTO akshay(username,fname,lname,mno,email,pass,rpass)
					 VALUES ('%s','%s','%s','%s','%s','%s','%s')""" %(val,val1,val2,val3,val4,val5,val6)
			try:
			   cursor.execute(sql)
			   db.commit()
			except:
			   db.rollback()
			print("DATA INSERT")
			db.close()
			root1.destroy();
			s1()
	else:
		tkMessageBox.showinfo("Password", "Please input same password")



def s1():
	root1 = Tk()
	root1.geometry("1500x880")
	root1.configure(background='#F1C40F')
	"""path = "tution.jpg"
	img = ImageTk.PhotoImage(Image.open(path))
	panel = tk.Label(root1, image = img)
	panel.pack(side = "bottom", fill = "both", expand = "yes")"""

	L1 = Label(root1, text="USERNAME", bg='black', fg='red', font=("Hoefler Text", 15))
	L1.pack(anchor=CENTER)
	L1.place(height=70, width=130, x=220, y=100)
	E1 = Entry(root1, bd =5)
	E1.pack(anchor=CENTER)
	E1.place(height=30, width=120, x=225, y=180)
	# B = Tkinter.Button(root1, text ="NEXT", command = lambda:clear1(E1,root1), activebackground='white', activeforeground='blue')
	# B.pack()
	# B.place(bordermode=OUTSIDE, height=50, width=100, x=220, y=240)

	L2 = Label(root1, text="FIRST NAME", bg='black', fg='red', font=("Hoefler Text", 15))
	L2.pack(anchor=CENTER)
	L2.place(height=70, width=130, x=360, y=100)
	E2 = Entry(root1, bd =5)
	E2.pack(anchor=CENTER)
	E2.place(height=30, width=120, x=365, y=180)
	# B1 = Tkinter.Button(root1, text ="NEXT", command= lambda:clear2(E1,root2) , activebackground='white', activeforeground='blue')
	# B1.pack()
	# B1.place(bordermode=OUTSIDE, height=50, width=100, x=370, y=240)


	L1 = Label(root1, text="LAST NAME", bg='black', fg='red', font=("Hoefler Text", 15))
	L1.pack(anchor=CENTER)
	L1.place(height=70, width=130, x=500, y=100)
	E3 = Entry(root1, bd =5)
	E3.pack(anchor=CENTER)
	E3.place(height=30, width=120, x=505, y=180)
	# B = Tkinter.Button(root2, text ="NEXT", command= lambda:clear2(E1,root2) , activebackground='white', activeforeground='blue')
	# B.pack()
	# B.place(bordermode=OUTSIDE, height=50, width=100, x=650, y=280)

	L1 = Label(root1, text="MOBILE NO.", bg='black', fg='red', font=("Hoefler Text", 15))
	L1.pack(anchor=CENTER)
	L1.place(height=70, width=130, x=640, y=100)
	E4 = Entry(root1, bd =5)
	E4.pack(anchor=CENTER)
	E4.place(height=30, width=120, x=650, y=180)

	L1 = Label(root1, text="EMAIL-ID", bg='black', fg='red', font=("Hoefler Text", 15))
	L1.pack(anchor=CENTER)
	L1.place(height=70, width=130, x=780, y=100)
	E5 = Entry(root1, bd =5)
	E5.pack(anchor=CENTER)
	E5.place(height=30, width=120, x=790, y=180)

	L1 = Label(root1, text="PASSWORD", bg='black', fg='red', font=("Hoefler Text", 15))
	L1.pack(anchor=CENTER)
	L1.place(height=70, width=130, x=920, y=100)
	E6 = Entry(root1,show="#", bd =5)
	E6.pack(anchor=CENTER)
	E6.place(height=30, width=120, x=925, y=180)

	L1 = Label(root1, text="CONFIRM PASSWORD", bg='black', fg='red', font=("Hoefler Text", 15))
	L1.pack(anchor=CENTER)
	L1.place(height=70, width=220, x=1060, y=100)
	E7 = Entry(root1,show="#", bd =5)
	E7.pack(anchor=CENTER)
	E7.place(height=30, width=220, x=1060, y=180)

	

	B = Tkinter.Button(root1, text ="SUBMIT", command =lambda:signup(E1,E2,E3,E4,E5,E6,E7,root1), activebackground='white', activeforeground='blue', bd=10, bg='black', fg='red', font=("Arial Black", 20))
	B.pack()
	B.place(bordermode=OUTSIDE, height=60, width=250, x=575, y=420)

	B = Tkinter.Button(root1, text ="EXIT",cursor='pirate',command=lambda: bahar1(root1), activebackground='white', activeforeground='blue', bd=10, bg='black', fg='red', font=("Arial Black", 8))
	B.pack()
	B.place(bordermode=OUTSIDE, height=30, width=80, x=1139, y=633)

	

def clear():
	root.destroy()
	s1()

def bahar2(root):
	root.destroy()

# root1 = Tk()


root = Tk()
root.geometry("1500x880")
root.configure(background='#34495E')
"""path = "tution.jpg"
img = ImageTk.PhotoImage(Image.open(path))
panel = tk.Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")"""
L1 = Label(root, text="TECHNO-MED", bg='black', fg='red', font=("Comic Sans MS", 25))
L1.pack(anchor=CENTER)
L1.place(height=70, width=300, x=540, y=50)

B = Tkinter.Button(root, text ="REGISTRATION",cursor='man', command = clear, activebackground='white', activeforeground='blue', bd=10, bg='black', fg='red', font=("Arial Black", 20))
B.pack()
B.place(bordermode=OUTSIDE, height=60, width=250, x=400, y=250)


B = Tkinter.Button(root, text ="LOGIN",cursor='heart', command = clear2, activebackground='white', activeforeground='blue', bd=10, bg='black', fg='red', font=("Arial Black", 20))
B.pack()
B.place(bordermode=OUTSIDE, height=60, width=250, x=750, y=250)

B = Tkinter.Button(root, text ="EXIT",cursor='pirate',command=lambda: bahar(root), activebackground='white', activeforeground='blue', bd=10, bg='black', fg='red', font=("Arial Black", 8))
B.pack()
B.place(bordermode=OUTSIDE, height=30, width=80, x=1139, y=633)

root.mainloop()