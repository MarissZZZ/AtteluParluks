from tkinter import*
from turtle import backward, forward
from PIL import ImageTk, Image
from matplotlib import image
from matplotlib.axis import XAxis

myObj=Tk()
myObj.title('Attēlu pārlūks')
myObj.resizable(0, 0)

def previous():
    global i
    i = i - 1
    try:
        image_label.config(image=images[i])
    except:
        i = 0
        previous()
        
def next():
    global i
    i = i + 1
    try:
        image_label.config(image=images[i])
    except:
        i = -1
        next()

frame=Frame(myObj, width=600, height=500, bg='white', relief=GROOVE, bd=2)
frame.pack(padx=10, pady=10)

Img1 = Image.open('1.jpg')
Img1.thumbnail((550, 450))
Img2 = Image.open('2.jpg')
Img2.thumbnail((550, 450))
Img3 = Image.open('3.jpg')
Img3.thumbnail((550, 450))
Img4 = Image.open('4.jpg')
Img4.thumbnail((550, 450))
Img5 = Image.open('5.jpg')
Img5.thumbnail((550, 450))
Img6 = Image.open('6.jpg')
Img6.thumbnail((550, 450))
Img7 = Image.open('7.jpg')
Img7.thumbnail((550, 450))
Img8 = Image.open('8.jpg')
Img8.thumbnail((550, 450))
Img9 = Image.open('9.jpg')
Img9.thumbnail((550, 450))
Img10 = Image.open('10.jpg')
Img10.thumbnail((550, 450))
Img11 = Image.open('11.jpg')
Img11.thumbnail((550, 450))



#Img2=ImageTk.PhotoImage(Image.open('2.jpg'))
#Img3=ImageTk.PhotoImage(Image.open('3.jpg'))
#Img4=ImageTk.PhotoImage(Image.open('4.jpg'))
#Img5=ImageTk.PhotoImage(Image.open('5.jpg'))
#Img6=ImageTk.PhotoImage(Image.open('6.jpg'))
#Img7=ImageTk.PhotoImage(Image.open('7.jpg'))
#Img8=ImageTk.PhotoImage(Image.open('8.jpg'))
#Img9=ImageTk.PhotoImage(Image.open('9.jpg'))
#Img10=ImageTk.PhotoImage(Image.open('10.jpg'))
#Img11=ImageTk.PhotoImage(Image.open('11.jpg'))

image1 = ImageTk.PhotoImage(Img1)
image2 = ImageTk.PhotoImage(Img2)
image3 = ImageTk.PhotoImage(Img3)
image4 = ImageTk.PhotoImage(Img4)
image5 = ImageTk.PhotoImage(Img5)
image6 = ImageTk.PhotoImage(Img6)
image7 = ImageTk.PhotoImage(Img7)
image8 = ImageTk.PhotoImage(Img8)
image9 = ImageTk.PhotoImage(Img9)
image10 = ImageTk.PhotoImage(Img10)
image11 = ImageTk.PhotoImage(Img11)

images=[image1,image2,image3,image4,image5,image6,image7,image8,image9,image10,image11]
i=0
image_label = Label(frame, image=images[i])
image_label.pack()


#imageList=[Img1,Img2,Img3,Img4,Img5,Img6,Img7,Img8,Img9,Img10,Img11]
#myLabel=Label(image=Img1)
#myLabel.grid(row=0,column=0,columnspan=3)

btnBack=Button(myObj,text='<<',relief=GROOVE,command=previous)
btnBack.pack(side=LEFT, padx=60, pady=5)

btnQuit=Button(myObj,text='IZIET',relief=GROOVE,command=myObj.quit)
btnQuit.pack(side=LEFT, padx=60, pady=5)

btnForward=Button(myObj,text='>>',relief=GROOVE,command=next)
btnForward.pack(side=LEFT, padx=60, pady=5)

#btnBack.grid(row=1,column=0)
#btnQuit.grid(row=1,column=1)
#btnForward.grid(row=1,column=2)

myObj.mainloop()