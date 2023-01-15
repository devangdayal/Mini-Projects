import threading 
from tkinter.ttk import *
from tkinter import *
import speedtest
from convertDataSize import calcData
from PIL import ImageTk, Image




root = Tk()
root.title("Speed Test @ DD")
root.geometry('500x400')
root.resizable(False,False)
root.iconbitmap('speed-icon.ico')
backgr = ImageTk.PhotoImage(Image.open("test.png")) 

_label = Label(root,image=backgr)
_label.place(x=0,y=0,relwidth=1,relheight=1)

# Designing Top Bottom 
Label(root,text ='Test your Internet Speed !',fg='#59AAF7',font='Roboto 40 bold').pack()
Label(root,text ='@devangdayal',fg='#59AAF7',font='Roboto 30 bold').pack(side= BOTTOM)

down_label = Label(root, text ='Download Speed :: ',font= ('Helvetica 18'))
down_label.place(x=70, y=80)

up_label = Label(root,text='Upload Speed :: ', font= ('Helvetica 18'))
up_label.place(x=70,y=110)

ping_label = Label(root,text ="Your Ping :: ", font= ('Helvetica 18'))
ping_label.place(x=70,y=140)

# Check the Net Speed
def check_speed():
    global down_speed
    global upload_speed

    global speed 
    speed = speedtest.Speedtest()
    download = speed.download()
    upload = speed.upload()

    down_speed = calcData(download)
    upload_speed = calcData(upload)

def update_text():

    thread = threading.Thread(target= check_speed,args=())
    thread.start()
    
    progress = Progressbar(root,orient = HORIZONTAL, length=200,mode='indeterminate')

    progress.place(x=180,y=180)
    progress.start()

    while thread.is_alive():
        root.update()
        pass

    down_label.config(text='Download Speed - '+str(down_speed))
    up_label.config(text='Upload Speed - '+str(upload_speed))

    speed.get_servers([])
    ping = speed.results.ping

    ping_label.config(text="Your Ping is - "+str(ping))

    progress.stop()
    progress.destroy()


button = Button(root,text='Check Speed !', width=40,bd=0,fg='#59AAF7',pady=10,command=update_text)
button.place(x=80,y=210)

root.mainloop()





