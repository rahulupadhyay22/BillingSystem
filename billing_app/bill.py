from tkinter import*
import math,random,os
from tkinter import messagebox
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing software")
        bg_color="LightSlateGray"
        title=Label(self.root,text="Shri GURU & CO",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold",),pady=2).pack(fill=X)
        #.......variablr water 
        self.one=IntVar()
        self.half=IntVar()
        self.ml=IntVar()

        #.......coolodrink variable
        self.TS1=IntVar()
        self.TS2=IntVar()
        self.TS3=IntVar()
        self.S1=IntVar()
        self.S2=IntVar()
        self.S3=IntVar()
    
        #.......mazza appy variable
        self.mazzate=IntVar()
        self.mazza250=IntVar()
        self.mazza600=IntVar()
        self.appy250=IntVar()
        self.appy600=IntVar()
        #===========total price varialble
        self.t1=StringVar()
        #=========contacts details variable
        self.cname=StringVar()
        self.phone=StringVar()
        
        self.address=StringVar()
        x=random.randint(1000,9999)
        self.address.set(str(x))
        self.searchbill=StringVar()

    
    
        #customer frame
        F1=LabelFrame(self.root,bd=5,relief=GROOVE,text="Customer Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)

        cname_lbl=Label(F1,text="Customer Name",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=15,pady=3)
        cname_txt=Entry(F1,width=20,textvariable=self.cname,font="arial 15",bd=2).grid(row=0,column=1,pady=3,padx=10)

        cphone_lbl=Label(F1,text="PhoneNumber",font=("times new roman",15,"bold")).grid(row=0,column=2,padx=15,pady=3)
        cphone_txt=Entry(F1,width=20,textvariable=self.phone,font="arial 15",bd=2).grid(row=0,column=3,pady=3,padx=10)

        caddress_lbl=Label(F1,text="BillNo",font=("times new roman",15,"bold")).grid(row=0,column=4,padx=15,pady=3)
        caddress_txt=Entry(F1,width=20,textvariable=self.address,font="arial 15",bd=2).grid(row=0,column=5,pady=3,padx=10)

        bill_btn= Button(F1,text="Search",command=self.find_bill,width=8,bd=3,font="arial 12 bold").grid(row=0,column=6)

        #.............WATERBOTTLESFRAME
        F2=LabelFrame(self.root,bd=9,relief=GROOVE,text="Water sale",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=5,y=155,width=325,height=380)
            
        one_lbl=Label(F2,text="OneLitre",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        one_txt=Entry(F2,width=10,textvariable=self.one,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        half_lbl=Label(F2,text="HalfLitre",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        half_txt=Entry(F2,width=10,textvariable=self.half,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        ml_lbl=Label(F2,text="250ML",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        ml_txt=Entry(F2,width=10,textvariable=self.ml,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)



        ##COOLDRINK
        F3=LabelFrame(self.root,bd=9,relief=GROOVE,text="CoolDrinks",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F3.place(x=340,y=155,width=325,height=380)
            
        TS1_lbl=Label(F3,text="ThumsUp250ml",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        TS1_txt=Entry(F3,width=10,textvariable=self.TS1,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        TS2_lbl=Label(F3,text="ThumsUp750ml",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        TS2_txt=Entry(F3,width=10,textvariable=self.TS2,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        TS3_lbl=Label(F3,text="ThumsUp2l",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        TS3_txt=Entry(F3,width=10,textvariable=self.TS3,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        S1_lbl=Label(F3,text="Sprite250ml",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        S1_txt=Entry(F3,width=10,textvariable=self.S1,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        S2_lbl=Label(F3,text="Sprite750ml",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        S2_txt=Entry(F3,width=10,textvariable=self.S2,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        S3_lbl=Label(F3,text="Sprite2l",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        S3_txt=Entry(F3,width=10,textvariable=self.S3,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)


         ##MAZZAFROOTIFRAME
        F4=LabelFrame(self.root,bd=9,relief=GROOVE,text="Mazza/Appy",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F4.place(x=670,y=155,width=325,height=380)
            
        mazzate_lbl=Label(F4,text="MazzaTetra",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        mazzate_txt=Entry(F4,width=10,textvariable=self.mazzate,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        mazza250_lbl=Label(F4,text="Mazza250ml",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        mazza250_txt=Entry(F4,width=10,textvariable=self.mazza250,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        mazza600_lbl=Label(F4,text="Mazza600ml",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        mazza600_txt=Entry(F4,width=10,textvariable=self.mazza600,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        appy250_lbl=Label(F4,text="AppyFizz250ml",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        appy250_txt=Entry(F4,width=10,textvariable=self.appy250,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        appy600_lbl=Label(F4,text="AppyFizz600ml",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        appy600_txt=Entry(F4,width=10,textvariable=self.appy600,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)
        #bill frame
        F5=Frame(self.root,bd=9,relief=GROOVE)
        F5.place(x=1000,y=155,width=345,height=380)
        bill_title=Label(F5,text="Bill Amount",font="arial 15 bold",bd=7,relief=FLAT).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack()


        #########last frame

        F6=LabelFrame(self.root,bd=10,relief=GROOVE,text="BillMenu",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F6.place(x=0,y=540,relwidth=1,height=140)
        t1_lbl=Label(F6,text="Total bill Amount",bg=bg_color,fg="Black",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=10,pady=1,sticky="w")
        t1_txt=Entry(F6,width=20,textvariable=self.t1,font=("arial 20 bold"),bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)


        btn_F= Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=700,width=625,height=105)

        total_btn=Button(btn_F,text="Total",command=self.total,bg="cadetblue",fg="white",pady=15,width=8,bd=3,font="arial 18 bold").grid(row=0,column=0,padx=5,pady=5)

        gbill_btn=Button(btn_F,text="Generate Bill",command=self.bill_area,bg="cadetblue",fg="white",pady=15,width=10,bd=3,font="arial 18 bold").grid(row=0,column=1,padx=5,pady=5)

        clear_btn=Button(btn_F,text="Clear",bg="cadetblue",command=self.clear_data,fg="white",pady=15,width=8,bd=3,font="arial 18 bold").grid(row=0,column=2,padx=5,pady=5)

        exit_btn=Button(btn_F,text="Exit",bg="cadetblue",fg="white",command=self.Exit_app,pady=15,width=8,bd=3,font="arial 18 bold").grid(row=0,column=3,padx=5,pady=5)
        self.welcome_bill()

    def total(self):
        self.a=self.one.get()*20
        self.b=self.half.get()*10
        self.c=self.ml.get()*100
        self.d=self.TS1.get()*525
        self.e=self.TS2.get()*860
        self.f=self.TS3.get()*720
        self.g=self.S1.get()*525
        self.h=self.S2.get()*860
        self.i=self.S3.get()*720
        self.j=self.mazzate.get()*330
        self.k=self.mazza250.get()*550
        self.l=self.mazza600.get()*720
        self.m=self.appy250.get()*410
        self.n=self.appy600.get()*800
        self.totalbillamou=float(
                            self.a+
                            self.b+
                            self.c+
                            self.d+
                            self.e+
                            self.f+
                            self.g+
                            self.h+
                            self.i+
                            self.j+
                            self.k+
                            self.l+
                            self.m+
                            self.n
                            )
        self.t1.set("Rs."+str(self.totalbillamou))

        self.totalbillprice=float(self.totalbillamou)

    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\t Welcomes You..! \n ")
        self.txtarea.insert(END,f"\n BillNumber : {self.address.get()} ")
        self.txtarea.insert(END,f"\n CustomerName : {self.cname.get()} ")
        self.txtarea.insert(END,f"\n PhoneNo : {self.phone.get()} \n")
        self.txtarea.insert(END,f"======================================")
        self.txtarea.insert(END,f"\n Product\t\tQty\t\tPrice")
        self.txtarea.insert(END,f"\n======================================")

    def bill_area(self):
        if self.cname.get()=="" or self.phone.get()=="":
            messagebox.showerror("Error","Please Fill the customer details")  
        else:    
            self.welcome_bill()
            if self.one.get()!=0:
                self.txtarea.insert(END,f"\n AraOneLitre\t\t{self.one.get()}\t\t{self.a}")
            if self.half.get()!=0:
                self.txtarea.insert(END,f"\n AraHalfLitre\t\t{self.half.get()}\t\t{self.b}")
            if self.ml.get()!=0:
                self.txtarea.insert(END,f"\n Ara250Ml\t\t{self.ml.get()}\t\t{self.c}")
            if self.TS1.get()!=0:
                self.txtarea.insert(END,f"\n ThumsUp250ml\t\t{self.TS1.get()}\t\t{self.d}")
            if self.TS2.get()!=0:
                self.txtarea.insert(END,f"\n ThumsUp750ml\t\t{self.TS2.get()}\t\t{self.e}")                
            if self.TS3.get()!=0:
                self.txtarea.insert(END,f"\n ThumsUp2L\t\t{self.TS3.get()}\t\t{self.f}")
            if self.S1.get()!=0:
                self.txtarea.insert(END,f"\n Sprite250Ml\t\t{self.S1.get()}\t\t{self.g}")
            if self.S2.get()!=0:
                self.txtarea.insert(END,f"\n Sprite750Ml\t\t{self.S2.get()}\t\t{self.h}")    
            if self.S3.get()!=0:
                self.txtarea.insert(END,f"\n Sprite2L\t\t{self.S3.get()}\t\t{self.i}")
            if self.mazzate.get()!=0:
                self.txtarea.insert(END,f"\n MazzaTetra\t\t{self.mazzate.get()}\t\t{self.j}")
            if self.mazza250.get()!=0:
                self.txtarea.insert(END,f"\n Mazza250ml\t\t{self.mazza250.get()}\t\t{self.k}")
            if self.mazza600.get()!=0:
                self.txtarea.insert(END,f"\n Mazza600ml\t\t{self.mazza600.get()}\t\t{self.l}")
            if self.appy250.get()!=0:
                self.txtarea.insert(END,f"\n Mazza600ml\t\t{self.appy250.get()}\t\t{self.m}")
            if self.appy600.get()!=0:
                self.txtarea.insert(END,f"\n Mazza600ml\t\t{self.appy600.get()}\t\t{self.n}")        

            self.txtarea.insert(END,f"\n--------------------------------------")
            self.txtarea.insert(END,f"\nTotalBill\t\t\tRs.{self.totalbillprice}")
            self.txtarea.insert(END,f"\n--------------------------------------") 
            self.save_bill()               

    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the bill?")
        if op>0:
            self.bill_data=self.txtarea.get('1.0',END)
            f1=open("billdata/"+str(self.address.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved","Bill Has Been Saved ")
        else:
            return    
    def find_bill(self):
        present="no"
        for i in os.listdir("billdata/"):
            if i.split('.')[0]==self.searchbill.get():
                f1=open(f"billdata/{i}","r")
                self.txtarea.delete('1.0',END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Invalid bill no")

    def clear_data(self):
        #.......variablr water 
        self.one.set(0)
        self.half.set(0)
        self.ml.set(0)

         #.......coolodrink variable
        self.TS1.set(0)
        self.TS2.set(0)
        self.TS3.set(0)
        self.S1.set(0)
        self.S2.set(0)
        self.S3.set(0)
    
        #.......mazza appy variable
        self.mazzate.set(0)
        self.mazza250.set(0)
        self.mazza600.set(0)
        self.appy250.set(0)
        self.appy600.set(0)
        #===========total price varialble
        self.t1.set("")
        #=========contacts details variable
        self.cname.set("")
        self.phone.set("")
        
        self.address.set("")
        x=random.randint(1000,9999)
        self.address.set(str(x))
        self.searchbill.set("")
        self.welcome_bill()


    def Exit_app(self):
        op=messagebox.askyesno("Exit","Do you really want to Exit")
        if op>0:
            self.root.destroy()







root=Tk()

obj = Bill_App(root)
root.mainloop()    