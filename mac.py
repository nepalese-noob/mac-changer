from tkinter import *
import os
def cmac():
	def sett():
		print(" ")
		os.system('ifconfig eth0 down')
		dire=E1.get
		os.system('ifconfig eth0 down')
		os.system('macchanger -m'+(dire)+' eth0')
		os.system('ifconfig eth0 up')
		print("done")
	root1=Tk()
	root1.title("costom mac")
	L1 = Label(root1, text="enter costum mac")
	L1.grid(row=0,column=0,sticky="s")
	E1 = Entry(root1)
	E1.grid(row=1,column=0)
	button=Button(root1,text="save",command=sett,padx=10).grid(row=2,column=0)
	root1.mainloop()
def rmac():
	os.system('ifconfig wlan0 down')
	os.system('macchanger -r wlan0')
	os.system('ifconfig wlan0 up')
	print(" ")
	hoho=input("press any key to continue")
	os.system('clear')
	os.system('python3 mac.py')
def smac():
	os.system('macchanger -s wlan0')
def rsmac():
	print(" ")
	os.system('ifconfig wlan0 down')
	os.system('macchanger -p wlan0')
	os.system('ifconfig wlan0 up')
	print(" ")                   
        




root = Tk()
root.title("Mac-Changer")
label=Button(root,text="1.Show my mac-Address............. ",command=smac,font="default 19 bold", bg="black", fg="White").grid(row=1)
label=Button(root,text="2.Change my mac-address randomly",command=rmac, font="default 19 bold", bg="black", fg="White").grid(row=2)
label=Button(root,text="3.Change my mac-address customly",font="default 19 bold", bg="black", fg="White", command=cmac).grid(row=3)
label=Button(root,text="4.Reset original mac-address..........",command=rsmac,font="default 19 bold", bg="black", fg="White").grid(row=4)





root.mainloop()