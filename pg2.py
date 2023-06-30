import sqlite3
from tkinter import *
from tkinter import filedialog
from tkinter import ttk,messagebox
import webbrowser
import subprocess


class client:

    def __init__(self,root):
            self.root=root
        
            self.root.title("PALLPUBB")#.title is used to title a software
            self.root.geometry("1920x780+0+0")#.geometry is used to set the height,weidth, and x,y axis of gui.
            self.root.config(bg="#324370")#.config is used to configure the gui by changing its color,text,etc.
            self.root.focus_force()
           
            #*****************all variables***************************************************************************************

            self.var_name_id=StringVar()
            self.var_postal_id=StringVar()
            self.var_contact_id=StringVar()
            self.var_upload_id=StringVar()
            self.var_instagram_id=StringVar()
            self.var_facebook_id=StringVar()
            self.var_searchby=StringVar()
            self.var_searchtx=StringVar()

            self.lbl_title=Label(self.root,text="CLIENT DETAILS")
            self.lbl_title.config(font=('Helvetica bold', 60,"bold"),bg="#769ADD",fg="#FFFFFF")
            self.lbl_title.place(x=580,y=0)
            self.lbl_title.pack(fill="x")
            self.frame1 = Frame(self.root, bg="#324370", width=1270, height=1000)
            self.frame1.pack(side="left", fill="both", expand=True)
            self.back_button = Button(self.root, text="Back",command=self.on_back_button_click,bg=("#769ADD"),fg=("#FFFFFF"),font=(20))
            self.back_button.place(x=30, y=120)

        #**************************************************search************************************************************
            self.searchframe=LabelFrame(self.root,text="search client",font=(20))
            self.searchframe.place(x=1300,y=100,width=200,height=5)
          
        # Create form elements using Place layout manager
            name_label =Label(self.root, text="Client Name:", font=(40),width=16)
            name_entry = Entry(self.root,textvariable= self.var_name_id,font=(40),width=16)

            postal_label =Label(self.root, text="Postal Address:", font=(40),width=16)
            postal_entry =Entry(self.root,textvariable=self.var_postal_id,font=(40),width=16)

            contact_label = Label(self.root, text="Contact no:", font=(40),width=16)
            contact_entry = Entry(self.root,textvariable=self.var_contact_id,font=(40),width=16)

             
            self.upload_label = Label(self.root, text="Upload Photo:", font=(40),width=16)    
          
            self.upload_button = Button(root, textvariable=self.var_upload_id,font=(40),command=self.upload_image)
            self.var_upload_id.set("Upload image")
            self.upload_button.pack()
            self.upload_button.place(x=900,y=200)
            self.upload_button.bind("<Enter>", self.on_enter)
            self.upload_button.bind("<Leave>", self.on_leave)

            self.instagram_label = Label(self.root, text="Instagram id:", font=(40),width=16)
            self.instagram_entry = Entry(self.root,textvariable= self.var_instagram_id,font=(40),width=16)

            self.facebook_label = Label(self.root, text="Facebook id:", font=(40) ,width=16)
            self.facebook_entry = Entry(self.root,textvariable=self.var_facebook_id,font=(40),width=16)

            submit_button = Button(self.root, text="Submit",command=self.add, font=(40) ,width=13)

            name_label.place(x=100, y=200)
            name_entry.place(x=300, y=200)

            self.postal_label.place(x=100, y=300)
            self.postal_entry.place(x=300, y=300)

            self.contact_label.place(x=100, y=400)
            self.contact_entry.place(x=300, y=400)

            self.name_label.place(x=100, y=200)
            self.name_entry.place(x=300, y=200)

            self.postal_label.place(x=100, y=300)
            self.postal_entry.place(x=300, y=300)

            self.contact_label.place(x=100, y=400)
            self.contact_entry.place(x=300, y=400)

            self.upload_label.place(x=700, y=200)

            self.instagram_entry.place(x=900, y=300)
            self.instagram_label.place(x=700, y=300)

            self.facebook_label.place(x=700, y=400)
            self.facebook_entry.place(x=900, y=400)

            self.submit_button.place(x=550, y=560)
            self.submit_button.bind("<Enter>", self.on_enter_s)
            self.submit_button.bind("<Leave>", self.on_leave_s)

            self.frame2 = Frame(root, bg="#698ED4", width=500, height=1000)
            self.frame2.pack(side="left", fill="both", expand=True)

     #**************************************************search************************************************************
            self.searchframe=LabelFrame(self.root,text="search client",font=(40))
            self.searchframe.place(x=1275,y=100,width=250,height=210)
            self.search=ttk.Combobox(self.searchframe,textvariable=self.var_searchby,values=("SELECT","NAME","CONTACT"),state='readonly',justify=CENTER,font=(40))
            self.search.place(x=30,y=10,width=180)
            self.search.current(0)
            self.search_entry = Entry(self.searchframe,textvariable=self.var_searchtx,font=(40),width=16)
            self.search_entry.place(x=30,y=50)

            self.button1= Button(self.searchframe,text="SEARCH",bg=("#FFFFFF"),fg=("#000000"),width=30,height=5,command=self.searchf)
            self.button1.place(x=19,y=90)
            self.button1.bind("<Enter>", self.on_enter_1)
            self.button1.bind("<Leave>", self.on_leave_1)


            self.button2 = Button(root, text="DELETE",bg=("#FFFFFF"),fg=("#000000"),width=30,height=5,command=self.delete)
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

            #*****************client details************************

            client_frame=Frame(self.root,bd=3,relief=RIDGE)
            client_frame.place(x=0,y=635,relwidth=1,height=150)
            scrolly=Scrollbar(client_frame,orient=VERTICAL)
            scrollx=Scrollbar(client_frame,orient=HORIZONTAL)
            self.clienttable = ttk.Treeview(client_frame, columns=("name", "postal", "contact", "instagram", "facebook"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
            scrollx.pack(side=BOTTOM,fill=X)
            scrolly.pack(side=RIGHT,fill=Y)
            scrollx.config(command=self.clienttable.xview)
            scrolly.config(command=self.clienttable.yview)
            self.clienttable.heading("name",text="name")
            self.clienttable.heading("postal",text="postal address")
            self.clienttable.heading("contact",text="contact no")
            self.clienttable.heading("instagram",text="instagram id")
            self.clienttable.heading("facebook",text="facebook id")
            self.clienttable["show"]="headings"
            self.clienttable.pack(fill=BOTH,expand=1)
            self.clienttable.bind("<ButtonRelease-1>",self.get_data)
            self.show()

            #******************************database****************************************
    def add(self):
        con=sqlite3.connect(database=r'pb.db')
        cur=con.cursor()
        try:
            if self.var_name_id.get()=="":
                messagebox.showerror("Error","client name must be required",parent=self.root)
            else:
                cur.execute("select * from client where name=?",(self.var_name_id.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","this client name is already assigned,try different",parent=self.root)
                else:
              
                    if row!=None:
                        messagebox.showerror("Error","this client name is already assigned,try different",parent=self.root)
                    else:
                        cur.execute("Insert into client (name, postal, contact, instagram, facebook) values(?,?,?,?,?)",(
                                        self.var_name_id.get(),
                                        self.var_postal_id.get(),
                                        self.var_contact_id.get(),
                                        self.var_instagram_id.get(),
                                        self.var_facebook_id.get(),
                    
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Client Added successfully")
                    self.show()
                    self.reset_form()
        except Exception as ex:
                messagebox.showerror("Error",f"error due to : {str(ex)}",parent=self.root)


    def get_data(self,ev):
        f=self.clienttable.focus()
        content= (self.clienttable.item(f))
        row=content['values']
        print(row)
        self.var_name_id.set(row[0])
        self.var_postal_id.set(row[1])
        self.var_contact_id.set(row[2])
        self.var_instagram_id.set(row[3])
        self.var_facebook_id.set(row[4])
        

    def show(self):
        con=sqlite3.connect(database=r'pb.db')
        cur=con.cursor()
        try:
            cur.execute("select * from client")
            rows=cur.fetchall()
            self.clienttable.delete(*self.clienttable.get_children()) 
            for row in rows:
                self.clienttable.insert('',END,values=row)   
        except Exception as ex:
                messagebox.showerror("Error",f"error due to : {str(ex)}",parent=self.root)
    def update(self):
        con = sqlite3.connect(database=r'pb.db')
        cur = con.cursor()
    
        try:
            if self.var_name_id.get() == "":
                messagebox.showerror("Error", "Client name must be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM client WHERE name=?", (self.var_name_id.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid client name", parent=self.root)
                else:
                    cur.execute("UPDATE client SET postal=?, contact=?, instagram=?, facebook=? WHERE name=?", (
                    self.var_postal_id.get(),
                    self.var_contact_id.get(),
                    self.var_instagram_id.get(),
                    self.var_facebook_id.get(),
                    self.var_name_id.get()
                ))
                con.commit()
                messagebox.showinfo("Success", "Client updated successfully")
                self.show()
                self.reset_form()
        except Exception as ex:
            messagebox.showerror("Error", f"Error occurred: {str(ex)}", parent=self.root)
 
    def delete(self):
        con = sqlite3.connect(database=r'pb.db')
        cur = con.cursor()
    
        try:
            if self.var_name_id.get() == "":
                messagebox.showerror("Error", "Client name must be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM client WHERE name=?", (self.var_name_id.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid client name", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                    if op:
                        cur.execute("DELETE FROM client WHERE name=?", (self.var_name_id.get(),))
                        con.commit()
                        messagebox.showinfo("Success", "Client deleted successfully")
        except Exception as ex:
            messagebox.showerror("Error", f"Error occurred: {str(ex)}", parent=self.root)

    
    def searchf(self):
    
        con = sqlite3.connect(database=r'pb.db')
        cur = con.cursor()
        try:
            if self.var_searchby.get()=="SELECT":
                messagebox.showerror("Error", "Select search by option", parent=self.root)
            elif self.var_searchtx.get()=="":
                messagebox.showerror("Error", "Search input should be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM client WHERE "+self.var_searchby.get() + " LIKE '%"+self.var_searchtx.get()+"%'")
                rows = cur.fetchall()
                if len(rows)!=0:
                    self.clienttable.delete(*self.clienttable.get_children())
                    for row in rows:
                        self.clienttable.insert('', END, values=row)
                else:
                    messagebox.showerror("Error", "No record found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
  

#reset

    def reset_form(self):
        self.name_entry.delete(0,END)  
        self.postal_entry.delete(0,END)
        self.contact_entry.delete(0,END)
        self.instagram_entry.delete(0,END)
        self.facebook_entry.delete(0,END)
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

    def upload_image(self):
        self.file_path = filedialog.askopenfilename(filetypes=(("Image files", "*.png *.jpg *.jpeg"), ("All files", "*.*")))
        print("Selected file:",file_path)


    def on_back_button_click(self):
        self.root.destroy()
 


if __name__ == "__main__":
    root = Tk()
    obj=client(root)
    root.mainloop()
    