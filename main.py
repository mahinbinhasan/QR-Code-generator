import qrcode
from tkinter import *



def work():
    p = ent.get("1.0","end-1c")
    print(p)
    im = qrcode.make(p)
    im.save('output.jpg')
    lbp = Label(mainfrm,text="A qr code generated on output.jpg file")
    lbp.pack()

root = Tk()
root.title("Mahin's QR CODE GENERATOR")
root.geometry('800x500')


mainfrm = Frame(root)
mainfrm.pack()

lbl = Label(mainfrm,text ="Enter Your text")
lbl.pack()

ent = Text(mainfrm)
ent.pack()

btn = Button(mainfrm,text="Generate QR CODE",command = lambda : work())
btn.pack()
root.mainloop()
