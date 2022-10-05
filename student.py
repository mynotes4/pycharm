from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk #to show images on windows #pip install pillow

class Student:
    #to initialise constructor
    #name of window is root here
    def __init__(self,root):
        self.root=root
        #to set geometry i.e size and title
        self.root.geometry("1530x790+0+0")
        self.root.title("STUDENT MANAGEMENT SYSTEM")

        #1st img
        img=Image.open("college_image/7th.jpg")
        img=img.resize((540,160),Image.ANTIALIAS) #to give width and height of image..
        #ANTIALIAS is used to covert high level image to low level image
        self.photoimg=ImageTk.PhotoImage(img) #self is written to access whole class


        self.btn_1=Button(self.root,image=self.photoimg,cursor="hand2")
        self.btn_1.place(x=0,y=0,width=540,height=160)

        #2nd img
        img_2=Image.open("college_image/5th.jpg")
        img_2=img.resize((540,160),Image.ANTIALIAS) #to give width and height of image..
        #ANTIALIAS is used to covert high level image to low level image
        self.photoimg=ImageTk.PhotoImage(img_2) #self is written to access whole class


        self.btn_1=Button(self.root,image=self.photoimg,cursor="hand2")
        self.btn_1.place(x=540,y=0,width=540,height=160)

        #3rd
        img_3=Image.open("college_image/6th.jpg")
        img_3=img.resize((540,160),Image.ANTIALIAS) #to give width and height of image..
        #ANTIALIAS is used to covert high level image to low level image
        self.photoimg=ImageTk.PhotoImage(img_3) #self is written to access whole class


        self.btn_1=Button(self.root,image=self.photoimg,cursor="hand2")
        self.btn_1.place(x=1000,y=0,width=540,height=160)
    #to pass class object
if __name__ == "__main":
        #pass root and Tk()is toolkit of root
    root=Tk()
    obj=Student(root)
    root.mainloop() #to prevent window from closing
