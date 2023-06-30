import sqlite3
from tkinter import *
from tkinter import filedialog
from tkinter import ttk,messagebox
import webbrowser
import subprocess


class book:

    def __init__(self,root):
            self.root=root
        
            self.root.title("PALLPUBB")#.title is used to title a software
            self.root.geometry("1920x780+0+0")#.geometry is used to set the height,weidth, and x,y axis of gui.
            self.root.config(bg="#324370")#.config is used to configure the gui by changing its color,text,etc.
            self.root.focus_force()
           
            self.var_name_id=StringVar()
            self.var_book_id=StringVar()
            self.var_paper_id=StringVar()
            self.var_printing_id=StringVar()
            self.var_language_id=StringVar()
            self.var_availbility_id=StringVar()
            self.var_searchby=StringVar()
            self.var_searchtx=StringVar()


            self.lbl_title=Label(self.root,text="BOOK DETAILS")
            self.lbl_title.config(font=('Helvetica bold', 60,"bold"),bg="#769ADD",fg="#FFFFFF")
            self.lbl_title.place(x=580,y=0)
            self.lbl_title.pack(fill="x")
            self.frame1 = Frame(self.root, bg="#324370", width=1270, height=1000)
            self.frame1.pack(side="left", fill="both", expand=True)
            self.back_button = Button(self.root, text="Back",command=self.on_back_button_click,bg=("#769ADD"),fg=("#FFFFFF"),font=(20))
            self.back_button.place(x=30, y=120)
          
          # ***********************************Create form elements using Place layout manager**********************************************
            self.name_label =Label(self.root, text="Client Name:", font=(40),width=16)
            self.name_entry = Entry(self.root,font=(40),width=16,textvariable=self.var_name_id)

            self.book_label =Label(self.root, text="Book Name:", font=(40),width=16)
            self.book_entry =Entry(self.root,font=(40),width=16,textvariable=self.var_book_id)

            self.paper_label = Label(self.root, text="paperback quality:", font=(40),width=16)
            self.paper_entry = Entry(self.root,font=(40),width=16,textvariable=self.var_paper_id)

            self.printing_label = Label(self.root, text="Printing press name:", font=(40),width=16)
            self.printing_entry = Entry(self.root,font=(40),width=16,textvariable=self.var_printing_id)

            self.language_label = Label(self.root, text="Language:", font=(40),width=16)
            self.language_entry = Entry(self.root,font=(40),width=16,textvariable=self.var_language_id)

            self.availbility_label = Label(self.root, text="Availbility:", font=(40) ,width=16)
            

            self.submit_button = Button(self.root, text="Submit", font=(40) ,width=13,command=self.add)
            self.submit_button.place(x=550, y=560)
            self.submit_button.bind("<Enter>", self.on_enter_s)
            self.submit_button.bind("<Leave>", self.on_leave_s)

            self.avail=ttk.Combobox(self.root,textvariable=self.var_availbility_id,values=("SELECT","AMAZON","FLIPKART","KINDLE","ANY OTHER"),state='readonly',justify=CENTER,font=(40))
            self.avail.place(x=300,y=500,width=180)
            self.avail.current(0)
            self.softcopy_label = Label(self.root, text="Book SoftCopy:", font=(40) ,width=16)

            self.name_label.place(x=100, y=200)
            self.name_entry.place(x=300, y=200)

            self.book_label.place(x=100, y=300)
            self.book_entry.place(x=300, y=300)

            self.paper_label.place(x=100, y=400)
            self.paper_entry.place(x=300, y=400)

            self.printing_label.place(x=700, y=200)
            self.printing_entry.place(x=900, y=200)

            self.language_label.place(x=700, y=300)
            self.language_entry.place(x=900, y=300)

            self.availbility_label.place(x=100, y=500)

            self.softcopy_label.place(x=700, y=400)

            self.submit_button.place(x=550, y=570)

            self.upload_button = Button(root, text="Upload Book", command=self.upload_book,font=(40))
            self.upload_button.pack()
            self.upload_button.place(x=900, y=400) 
            self.upload_button.bind("<Enter>", self.on_enter)
            self.upload_button.bind("<Leave>", self.on_leave)
   

#*********************************************************frame 2************************************************************************

            self.frame2 = Frame(root, bg="#698ED4", width=500, height=1000)
            self.frame2.pack(side="left", fill="both", expand=True)

            self.searchframe=LabelFrame(self.root,text="search client",font=(40))
            self.searchframe.place(x=1275,y=100,width=250,height=210)
            self.search=ttk.Combobox(self.searchframe,textvariable=self.var_searchby,values=("SELECT","NAME","BOOK"),state='readonly',justify=CENTER,font=(40))
            self.search.place(x=30,y=10,width=180)
            self.search.current(0)
            self.search_entry = Entry(self.searchframe,font=(40),width=16,textvariable=self.var_searchtx)
            self.search_entry.place(x=30,y=50)

            self.button1= Button(self.searchframe, text="SEARCH",bg=("#FFFFFF"),fg=("#000000"),width=30,height=5,command=self.searchf)
            self.button1.place(x=19,y=90)
            self.button1.bind("<Enter>", self.on_enter_1)
            self.button1.bind("<Leave>", self.on_leave_1)


            self.button2 = Button(root, text="Delete",bg=("#FFFFFF"),fg=("#000000"),width=30,height=5,command=self.delete)
            self.button2.place(x=1300,y=340)
            self.button2.bind("<Enter>", self.on_enter_2)
            self.button2.bind("<Leave>", self.on_leave_2)

            
            self.button3 = Button(root, text="RESET",command=self.reset_form,bg=("#FFFFFF"),fg=("#000000"),width=30,height=5)
            self.button3.place(x=1300,y=440)
            self.button3.bind("<Enter>", self.on_enter_3)
            self.button3.bind("<Leave>", self.on_leave_3)

            
            self.button = Button(root, text="EDIT",width=30,height=5,command=self.update)
            self.button.place(x=1300,y=540)
            self.button.bind("<Enter>", self.on_enter_4)
            self.button.bind("<Leave>", self.on_leave_4)

                        #*****************book details************************

            book_frame=Frame(self.root,bd=3,relief=RIDGE)
            book_frame.place(x=0,y=635,relwidth=1,height=150)
            scrolly=Scrollbar(book_frame,orient=VERTICAL)
            scrollx=Scrollbar(book_frame,orient=HORIZONTAL)
            self.booktable = ttk.Treeview(book_frame, columns=( "name", "book", "paper", "printing", "language", "availbility"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
            scrollx.pack(side=BOTTOM,fill=X)
            scrolly.pack(side=RIGHT,fill=Y)
            scrollx.config(command=self.booktable.xview)
            scrolly.config(command=self.booktable.yview)
     
            self.booktable.heading("name",text="name")
            self.booktable.heading("book",text="book name")
            self.booktable.heading("paper",text="paper")
            self.booktable.heading("printing",text="printing")
            self.booktable.heading("language",text="language")
            self.booktable.heading("availbility",text="availbility")
           
            self.booktable["show"]="headings"
            self.booktable.pack(fill=BOTH,expand=1)
            self.booktable.bind("<ButtonRelease-1>",self.get_data)
            self.show()
    def add(self):
        con=sqlite3.connect(database=r'pb1.db')
        cur=con.cursor()
        try:
            if self.var_name_id.get()=="":
                messagebox.showerror("Error","book name must be required",parent=self.root)
            else:
                cur.execute("select * from books where name=?",(self.var_name_id.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","this books name is already assigned,try different",parent=self.root)
                else:
              
                    if row!=None:
                        messagebox.showerror("Error","this books name is already assigned,try different",parent=self.root)
                    else:
                        cur.execute("Insert into books(name,book,paper,printing,language,availbility) values(?,?,?,?,?,?)",(
                                        self.var_name_id.get(),
                                        self.var_book_id.get(),
                                        self.var_paper_id.get(),
                                        self.var_printing_id.get(),
                                        self.var_language_id.get(),
                                        self.var_availbility_id.get()
                    
                    ))
                    con.commit()
                    messagebox.showinfo("Success","book Added successfully")
                    self.show()
                    self.reset_form()
        except Exception as ex:
                messagebox.showerror("Error",f"error due to : {str(ex)}",parent=self.root)



    def get_data(self,ev):
        f=self.booktable.focus()
        content= (self.booktable.item(f))
        row=content['values']
        print(row)
        self.var_name_id.set(row[0])
        self.var_book_id.set(row[1])
        self.var_paper_id.set(row[2])
        self.var_printing_id.set(row[3])
        self.var_language_id.set(row[4])
        self.var_availbility_id.set(row[5])   


    def show(self):
        con=sqlite3.connect(database=r'pb1.db')
        cur=con.cursor()
        try:
            cur.execute("select * from books")
            rows=cur.fetchall()
            self.booktable.delete(*self.booktable.get_children()) 
            for row in rows:
                self.booktable.insert('',END,values=row)   
        except Exception as ex:
                messagebox.showerror("Error",f"error due to : {str(ex)}",parent=self.root)  

    def update(self):
        con = sqlite3.connect(database=r'pb1.db')
        cur = con.cursor()
    
        try:
            if self.var_name_id.get() == "":
                messagebox.showerror("Error", "Client name must be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM books WHERE name=?", (self.var_name_id.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid client name", parent=self.root)
                else:
                    cur.execute("UPDATE books SET book=?, paper=?, printing=?, language=? ,availbility=? WHERE name=?", (
                    self.var_book_id.get(),
                    self.var_paper_id.get(),
                    self.var_printing_id.get(),
                    self.var_language_id.get(),
                    self.var_availbility_id.get(),
                    self.var_name_id.get()
                ))
                con.commit()
                messagebox.showinfo("Success", "book updated successfully")
                self.reset_form()
        except Exception as ex:
            messagebox.showerror("Error", f"Error occurred: {str(ex)}", parent=self.root)  

    def delete(self):
        con = sqlite3.connect(database=r'pb1.db')
        cur = con.cursor()
    
        try:
            if self.var_name_id.get() == "":
                messagebox.showerror("Error", "Client name must be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM books WHERE name=?", (self.var_name_id.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid client name", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                    if op:
                        cur.execute("DELETE FROM books WHERE name=?", (self.var_name_id.get(),))
                        con.commit()
                        messagebox.showinfo("Success", "book deleted successfully")
        except Exception as ex:
            messagebox.showerror("Error", f"Error occurred: {str(ex)}", parent=self.root)
       
    def searchf(self):
    
        con = sqlite3.connect(database=r'pb1.db')
        cur = con.cursor()
        try:
            if self.var_searchby.get()=="SELECT":
                messagebox.showerror("Error", "Select search by option", parent=self.root)
            elif self.var_searchtx.get()=="":
                messagebox.showerror("Error", "Search input should be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM books WHERE "+self.var_searchby.get() + " LIKE '%"+self.var_searchtx.get()+"%'")
                rows = cur.fetchall()
                if len(rows)!=0:
                    self.booktable.delete(*self.booktable.get_children())
                    for row in rows:
                        self.booktable.insert('', END, values=row)
                else:
                    messagebox.showerror("Error", "No record found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)     

#reset

    def reset_form(self):
        self.name_entry.delete(0,END)  
        self.book_entry.delete(0,END)
        self.paper_entry.delete(0,END)
        self.printing_entry.delete(0,END)
        self.language_entry.delete(0,END)
        self.avail.delete(0,END)
        self.var_availbility_id.set("")
        self.var_searchtx.set("")
        self.var_searchby.set("SELECT")
        self.show()
#submit button hover
    def on_enter_s(self, event):
        self.submit_button.config(bg='blue', fg='white')

    def on_leave_s(self, event):
        self.submit_button.config(bg='white', fg='black')
#upload button hover   
    def on_enter(self, event):
        self.upload_button.config(bg='blue', fg='white')

    def on_leave(self, event):
        self.upload_button.config(bg='white', fg='black')
#button 1 hover
    def on_enter_1(self, event):
        self.button1.config(bg='blue', fg='white')

    def on_leave_1(self, event):
        self.button1.config(bg='white', fg='black')
#button 2 hover
    def on_enter_2(self, event):
        self.button2.config(bg='blue', fg='white')

    def on_leave_2(self, event):
        self.button2.config(bg='white', fg='black')
#button 3 hover
    def on_enter_3(self, event):
        self.button3.config(bg='blue', fg='white')

    def on_leave_3(self, event):
        self.button3.config(bg='white', fg='black')
#button 4 hover
    def on_enter_4(self, event):
        self.button.config(bg='blue', fg='white')

    def on_leave_4(self, event):
        self.button.config(bg='white', fg='black')

#upload book
    def upload_book(self):
        self.file_path = filedialog.askopenfilename(filetypes=(("Image files", "*.png *.jpg *.jpeg"), ("All files", "*.*")))
        print("Selected file:",file_path)


    def on_back_button_click(self):
        self.root.destroy()
 


if __name__ == "__main__":
    root = Tk()
    obj=book(root)
    root.mainloop()
    
