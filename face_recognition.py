# import re
from sys import path
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
import mysql.connector
import cv2
import numpy as np
from tkinter import messagebox
from time import strftime
from datetime import datetime
import subprocess

class Face_Recognition:

     def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition Pannel")

        # Header image
        img = Image.open("d:/Automated Attendance System/Main Window/Images_GUI/banner.jpg")  
        img = img.resize((1366, 130), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        # Set image as label
        f_lb1 = Label(self.root, image=self.photoimg)
        f_lb1.place(x=0, y=0, width=1366, height=130)

        # Background image
        bg1 = Image.open("d:/Automated Attendance System/Main Window/Images_GUI/bg3.jpg") 
        bg1 = bg1.resize((1366, 768), Image.ANTIALIAS)
        self.photobg1 = ImageTk.PhotoImage(bg1)

        # Set image as label
        bg_img = Label(self.root, image=self.photobg1)
        bg_img.place(x=0, y=130, width=1366, height=768)

        # Title section
        title_lb1 = Label(bg_img, text="Welcome to Face Detector Panel", font=("verdana", 30, "bold"), bg="white", fg="navyblue")
        title_lb1.place(x=0, y=0, width=1366, height=45)

        # Create buttons below the section
        # Training button 1
        std_img_btn = Image.open("d:/Automated Attendance System/Main Window/Images_GUI/f_det.jpg") 
        std_img_btn = std_img_btn.resize((180, 180), Image.ANTIALIAS)
        self.std_img1 = ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img, image=self.std_img1, cursor="hand2")
        std_b1.place(x=600, y=170, width=180, height=180)

        std_b1_1 = Button(bg_img, text="Face Detector", cursor="hand2", font=("tahoma", 15, "bold"),
                          bg="white", fg="navyblue", command=self.face_rec)
        std_b1_1.place(x=600, y=350, width=180, height=45)

     def face_rec(self):
        script_directory = r'D:\Automated Attendance System\studentsdetails'


        script_path = os.path.join(script_directory)

        subprocess.Popen(['start', 'cmd', '/k', 'python', script_path], cwd=script_directory, shell=True)

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
