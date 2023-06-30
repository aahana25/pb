from tkinter import *
from tkinter import filedialog
from pg2 import client
from pg3 import book
import webbrowser
import subprocess


class main:

    def __init__(self,root):
            self.root=root
        
            self.root.title("PALLPUBB")#.title is used to title a software
            self.root.geometry("1920x780+0+0")#.geometry is used to set the height,weidth, and x,y axis of gui.
            self.root.config(bg="#324370")#.config is used to configure the gui by changing its color,text,etc.
            self.root.focus_force()
           

            self.lbl_title=Label(self.root,text="PALLPUBB")
            self.lbl_title.config(font=('Helvetica bold', 60,"bold"),bg="#769ADD",fg="#FFFFFF")
            self.lbl_title.place(x=580,y=0)
            self.lbl_title.pack(fill="x")
            self.frame1 = Frame(self.root, bg="#324370", width=1270, height=1000)
            self.frame1.pack(side="left", fill="both", expand=True)
            self.back_button = Button(self.root, text="Back",bg=("#769ADD"),fg=("#FFFFFF"),font=(20),command=self.on_back_button_click)
            self.back_button.place(x=30, y=120)

            self.frame_packages=Frame(self.root,bg="#2F4D99",width=650,height=250,padx=25,pady=25)
            self.frame_packages.place(relx=0.5,rely=0.5,anchor="center")

            self.name_label = Label(root, text="PUBLISHING PACKAGES",font=('helvetica bold',40,'bold'),bg=("#254D99"),fg=("#ffffff"))
            self.name_label.place(x=450, y=300)

            self.button1 = Button(root, text="Client",bg=("#769ADD"),fg=("#FFFFFF"),width=10,font=(20),command=self.client)
            self.button1.place(x=600,y=450)
          
            self.button2 =Button(root, text="Book",bg=("#769ADD"),fg=("#FFFFFF"),width=10,font=(20),command=self.book)
            self.button2.place(x=800,y=450)
         


    def client(self):
        
         self.new_win=Toplevel(self.root)
         self.new_obj=client(self.new_win)

         
    def book(self):
         self.new_win=Toplevel(self.root)
         self.new_obj=book(self.new_win)

    def on_back_button_click(self):
          self.root.destroy()
        
    
    

 


if __name__ == "__main__":
    root = Tk()
    obj=main(root)
    root.mainloop()
    