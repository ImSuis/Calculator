from tkinter import *
from PIL import Image, ImageTk
window = Tk()
window.geometry("550x550")
img1 = ImageTk.PhotoImage(Image.open("images/apple.jpg").resize((500,500)))
img2 = ImageTk.PhotoImage(Image.open("images/banana.jpg").resize((500,500)))
img3 = ImageTk.PhotoImage(Image.open("images/mango.jpg").resize((500,500)))
img4 = ImageTk.PhotoImage(Image.open("images/orange.jpg").resize((500,500)))



count = 1
label = Label()
label.pack()


def show():
    if count == 1:
        label.config(image=img1)
    elif count == 2:
        label.config(image=img2)
    elif count == 3:
        label.config(image=img3)
    elif count == 4:
        label.config(image=img4)
    else:
        print()




def Previous():
    global count
    count  = count - 1
    if count >= 4:
        nex['state']='disabled'
    else:
        nex['state']='normal'
    if count <= 1:
        pre['state']='disabled'
    else:
        pre['state']='normal'
    print(count)
    show()

def Next():
    global count
    count  = count + 1
    if count >= 4:
        nex['state']='disabled'
    else:
        nex['state']='normal'
    if count <= 1:
        pre['state']='disabled'
    else:
        pre['state']='normal'
    print(count)
    show()




pre = Button(window,text="Previous",command=Previous,)
pre.place(x = 0,y = 500)

nex = Button(window,text="Next",command=Next)
nex.place(x = 460,y = 500)
exi = Button(window,text="Exit",command=window.quit)
exi.place(x = 230,y=500)

if count >= 5:
    nex['state'] = 'disabled'
else:
    nex['state'] = 'normal'
if count <= 1:
    pre['state'] = 'disabled'
else:
    pre['state'] = 'normal'
show()

window.mainloop()