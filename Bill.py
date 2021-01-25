from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image
import random
# import math
import pymysql
import datetime,time
# import pdb
# pdb.set_trace()
bill=Tk()
bill.title("Billing System")
bill.config(bg="white")
bill.geometry("1500x680+0+0")
# bill.minsize(1500,680)
bill.minsize(1250,450)

#<<<<<<<<<<<<<<<<<    I  M  A  G  E  S    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
logout_button=PhotoImage(file="Images/logoutlogo.png")

#<<<<<<<<<<<<<<<<<<    V A R I A B L E S    >>>>>>>>>>>>>>>>>>>>>>>>>
# random_bill=random.randint(999,99999)
# print(random_bill)


# detail variables====>

customer_name_var=StringVar()
customer_mobile_var=StringVar()
# customer_mobile_var.set()
bill_no_var=StringVar()

# products variables====>

zerox_var=IntVar()
form_fill_var=IntVar()
land_mot_form_fill_var=IntVar()
other_online_serivces_var=IntVar()
gad_service_var=IntVar()
online_recharge_service_var=IntVar()

# bill variables====>
custmoer_service_name_var=StringVar()
total_service_var=IntVar()
total_charges_var=DoubleVar()
gst_var=DoubleVar()
service_tax_var=DoubleVar()
total_ammount_var=DoubleVar()
datetime=StringVar()
# products fix prices====>

zerox_var.set(0)
form_fill_var.set(0)
land_mot_form_fill_var.set(0)
other_online_serivces_var.set(0)
gad_service_var.set(0)
online_recharge_service_var.set(0)

# --------------------------------------------------------------------------------------------------------------------------


# * * * * * * * * * *    B U T T O N S   A C T I O N S    * * * * * * * * * * * * * * * *


def search_action():
    # if customer_name_var.get()=="":
    #     messagebox.showerror("Error","Please Enter Customer's Name")
    # elif customer_name_var.get()!=StringVar():
    #     messagebox.showerror("Error","Customer's Name should be Alphabate only")

    # elif customer_mobile_var.get()=="":
    #     messagebox.showerror("Error","Please Enter Customer's Mobile number")
    if bill_no_var.get()=="":
        messagebox.showerror("Error","Please Enter Customer's Bill number")
        bill_no_field.focus()
    else:
        try:
            int(bill_no_var.get())
            # messagebox.showinfo("success","It is Working...!")
        except:
            messagebox.showwarning("Error","Bill Number shouble be digit only  !!")

    conn=pymysql.connect(host="localhost", user="root",password="",database="sa's inet service")
    curs=conn.cursor()
    # curs.execute("select * FROM  records where Bill Number=(%s)"),str(bill_no_var.get())
    search_data=curs.fetchone()
    if search_data!=None:
        print(search_data)
    else:
        messagebox.showerror("Error","Invalid Bill Number")
    conn.close()


            
def total_services():
    totalservice=0
    if zerox_var.get()!=0:
        totalservice=totalservice+1
    if form_fill_var.get()!=0:
        totalservice=totalservice+1
    if land_mot_form_fill_var.get()!=0:
        totalservice=totalservice+1
    if other_online_serivces_var.get()!=0:
        totalservice=totalservice+1
    if gad_service_var.get()!=0:
        totalservice=totalservice+1
    
    if online_recharge_service_var.get()!=0:
        totalservice+=1
    total_service_var.set(totalservice)


def total_services_list():
    totalservice_name=[]
    if zerox_var.get()!=0:
        totalservice_name.append("Zerox")
    if form_fill_var.get()!=0:
        totalservice_name.append("Form Fill")
    if land_mot_form_fill_var.get()!=0:
        totalservice_name.append("Land Motation Form")
    if other_online_serivces_var.get()!=0:
        totalservice_name.append("Online Services")
    if gad_service_var.get()!=0:
        totalservice_name.append("Gad Service")
    
    if online_recharge_service_var.get()!=0:
        totalservice_name.append("Recharge")
    custmoer_service_name_var.set(totalservice_name)
    # print(custmoer_service_name_var.get())
    




def total_action():
    total_charges_var.set(zerox_var.get()+
    form_fill_var.get()+
    land_mot_form_fill_var.get()+ 
    other_online_serivces_var.get()+
    gad_service_var.get()+
    online_recharge_service_var.get()
    )
    total_ammount_var.set(total_charges_var.get()+((total_charges_var.get()*gst_var.get())/100)+service_tax_var.get())
    total_services()
    total_services_list()
     # if (zerox_var.get()!=0 and
        #     form_fill_var.get()!=0 and
        #     land_mot_form_fill_var.get()!=0 and
        #     other_online_serivces_var.get()!=0 and
        #     gad_service_var.get()!=0 and
        #     online_recharge_service_var.get()!=0):
        #         totalservice+=1
        #         total_service_var.set(totalservice.get())
def genrate_bill_area():
    bill_area_textbox.config(state=NORMAL)
    bill_area_textbox.delete("1.0",END)
    bill_area_textbox.insert(END,"\t\tWelcome to SA'S INET Service\n")
    bill_area_textbox.insert(END,"=====================================================")
    bill_area_textbox.insert(END,f"\n Customer Name :{customer_name_var.get()}")
    bill_area_textbox.insert(END,f"\n Mobile No     :{customer_mobile_var.get()}")
    bill_area_textbox.insert(END,f"\n Bill No.      :{bill_no_var.get()}")
    bill_area_textbox.insert(END,"\n=====================================================")
    bill_area_textbox.insert(END,"\n Service Name\t")
    bill_area_textbox.insert(END,"\t\t\t\tPrice")
    bill_area_textbox.insert(END,"\n=====================================================")
    if zerox_var.get()!=0:
        bill_area_textbox.insert(END,f"\n Zerox\t\t\t\t\t{zerox_var.get()}")
    if form_fill_var.get()!=0:
        bill_area_textbox.insert(END,f"\n Online Form Apply\t\t\t\t\t{form_fill_var.get()}")
    if land_mot_form_fill_var.get()!=0:
        bill_area_textbox.insert(END,f"\n Land Motation Form Apply\t\t\t\t\t{land_mot_form_fill_var.get()}")
    if other_online_serivces_var.get()!=0:
        bill_area_textbox.insert(END,f"\n Other Online Services\t\t\t\t\t{other_online_serivces_var.get()}")
    if gad_service_var.get()!=0:
        bill_area_textbox.insert(END,f"\n GAD Services\t\t\t\t\t{gad_service_var.get()}")
    if online_recharge_service_var.get()!=0:
        bill_area_textbox.insert(END,f"\n Recharge\t\t\t\t\t{online_recharge_service_var.get()}")
    
    
    bill_area_textbox.insert(END,f"\n GST\t\t\t\t\t{((total_charges_var.get()*gst_var.get())/100)}")
    bill_area_textbox.insert(END,f"\n Service Tax\t\t\t\t\t{service_tax_var.get()}")
    bill_area_textbox.insert(END,"\n-----------------------------------------------------")
    bill_area_textbox.insert(END,"\n Total Price   :")
    bill_area_textbox.insert(END,f"\t\t\t\t    Rs {total_ammount_var.get()}")
    bill_area_textbox.insert(END,"\n=====================================================\n\n")
    bill_area_textbox.insert(END,"\tThank You for vist on SA'S INET Service\n")
    bill_area_textbox.insert(END,"\t\t(Hasanganj,Munger)")
    bill_area_textbox.config(state=DISABLED)
def genrate_bill_action():
    if customer_name_var.get()=="":
        messagebox.showerror("Error","Please Enter Customer's Name")
        customer_name_field.focus()
    elif customer_mobile_var.get()=="":
        messagebox.showerror("Error","Please Enter Customer's Mobile number")
    elif zerox_var.get()==0 and form_fill_var.get()==0 and land_mot_form_fill_var.get()==0 and other_online_serivces_var.get()==0 and gad_service_var.get()==0 and online_recharge_service_var.get()==0:
        messagebox.showerror("Error","There is no any service select for calculate")
    else:
        optbill=messagebox.askokcancel("Genrate Bill","Are you sure to genrate bill of this transaction ?")
        if optbill==1:
            random_bill=random.randint(999,99999)
            bill_no_var.set(random_bill) 
            # print(bill_no_var.get())
            bill_no_field.config(state=DISABLED)
            genrate_bill_area()
            total_ammount_var.set(total_charges_var.get()+((total_charges_var.get()*gst_var.get())/100)+service_tax_var.get())
            
            date_time=time.ctime()
            datetime.set(date_time)
            save_bill()
            # print(datetime)



def save_bill():
    if total_ammount_var.get()==0:
        messagebox.showerror("Bill Error","Please Add your Bill first then Genreate Bill...!!")
    else:
        conn=pymysql.connect(host="localhost", user="root",password="",database="sa's inet service")
        curs=conn.cursor()
        curs.execute("insert into records values(%s,%s,%s,%s,%s,%s,%s,%s)",("",bill_no_var.get(),
                                                                        customer_name_var.get(),
                                                                        customer_mobile_var.get(),
                                                                        custmoer_service_name_var.get(),
                                                                        total_service_var.get(),
                                                                        total_ammount_var.get(),
                                                                        datetime.get()  
                                                                        ))
        conn.commit()
        conn.close()




def clear_btn_action():
    clear_opt=messagebox.askyesno("Reset Window","Do you really want to clear the Screen ?")
    if clear_opt==1:
        customer_name_var.set("")
        customer_mobile_var.set("")
        bill_no_field.config(state=NORMAL)
        bill_no_var.set("")
        zerox_var.set(0)
        form_fill_var.set(0)
        land_mot_form_fill_var.set(0)
        other_online_serivces_var.set(0)
        gad_service_var.set(0)
        online_recharge_service_var.set(0)
        total_service_var.set(0)
        total_charges_var.set(0.00)
        gst_var.set(0.00)
        service_tax_var.set(0.00)
        total_ammount_var.set(0.00)
        bill_area_textbox.config(state=NORMAL)
        bill_area_textbox.delete("1.0",END)
        bill_area_textbox.insert(END,"\t\tWelcome to SA'S INET Service\n")
        bill_area_textbox.insert(END,"=====================================================")
        bill_area_textbox.insert(END,"\n Customer Name :")
        bill_area_textbox.insert(END,"\n Mobile No     :")
        bill_area_textbox.insert(END,"\n Bill No.      :")
        bill_area_textbox.insert(END,"\n=====================================================")
        bill_area_textbox.insert(END,"\n Service Name\t")
        bill_area_textbox.insert(END,"\t\t\t\tPrice")
        bill_area_textbox.insert(END,"\n=====================================================")
        bill_area_textbox.insert(END,"\n\n\n\n\n\n\n\n\n=====================================================\n\n")
        bill_area_textbox.insert(END,"\tThank You for vist on SA'S INET Service\n")
        bill_area_textbox.insert(END,"\t\t (Hasanganj,Munger)")
        bill_area_textbox.config(state=DISABLED)

def exit_btn_action():
    exit_opt=messagebox.askyesno("Exit Window","Do you really want to Exit from the Software Window")
    if exit_opt==1:
        bill.destroy()

def logout_action():
    logout_opt=messagebox.askyesno("Logout","Are you sure you want to Logout ?")
    if logout_opt==1:
        bill.destroy()
        import Login
#=====================================    F   R   A   M   E    ==================================================================================

title_frame=Label(bill,text="SA'S INET Service",bd=10,relief=GROOVE,bg="#074463",fg="gold",pady=15,font=("Algerian","30","bold")).pack(fill=X)
customer_details_frame=LabelFrame(bill,text="Customer Details",fg="orange",font=("",12,"bold"),bd=6,relief=GROOVE,bg="#074463").place(x=0,y=98,height=80,width=1365)
# =================== C U S T O M E R   D E T A I L S =============================
customer_name=Label(customer_details_frame,text="Customer Name",bg="#074463",padx=25,pady=6,fg="white",font=("",13,"bold")).place(x=10,y=120)
customer_mobile=Label(customer_details_frame,text="Mobile No.",bg="#074463",pady=6,fg="white",font=("",13,"bold")).place(x=430,y=120)
bill_no=Label(customer_details_frame,text="Bill No.",bg="#074463",pady=6,fg="white",font=("",13,"bold")).place(x=785,y=120)
bill_area=Frame(bill,bd=5,relief=GROOVE,bg="white")
bill_area.place(x=915,y=180,height=375,width=445)

#Entry filed for customer details----------->
customer_name_field=Entry(customer_details_frame,width=30,bd=5,bg="white",font=("",10,"bold"),textvariable=customer_name_var)
customer_name_field.place(x=190,y=122)
customer_name_field.focus()
customer_mobile_field=Entry(customer_details_frame,width=30,bd=5,bg="white",font=("",10,"bold"),justify=CENTER,textvariable=customer_mobile_var).place(x=545,y=122)
bill_no_field= Entry(customer_details_frame,width=30,bd=5,bg="white",font=("",10,"bold"),justify=CENTER,textvariable=bill_no_var,state=DISABLED)
bill_no_field.place(x=875,y=122)
#------------------------------------------------------------------------------------------------------------------------------------
#Search Button

search_btn=Button(customer_details_frame,text="Search",fg="black",font=("elephant",15),bd=3,cursor="hand2",justify=CENTER,command=search_action,state=DISABLED)
search_btn.place(x=1145,y=122,height=33,width=150)
#------------------------------------------------------------------------------------------------------------------------------------
logout=Button(customer_details_frame,image=logout_button,bd=0,cursor="hand2",bg="#074463",activebackground="#074463",command=logout_action).place(x=1310,y=122,height=35,width=35)


#---------------------------------------------------------------------------------------------------------------
product_frame=LabelFrame(bill,text="Products",fg="orange",font=("",12,"bold"),bd=8,relief=GROOVE,bg="#074463").place(x=0,y=180,height=375,width=910)
bill_menu_frame=coutmer_details_frame=LabelFrame(bill,text="Bill Menu",fg="orange",font=("",12,"bold"),bd=7,relief=RIDGE,bg="#074463").place(x=0,y=560,height=100,width=1370)
copyright_frmae=Frame(bill,bg="#074463").place(x=0,y=664,height=25,width=1370)
copyright=Label(copyright_frmae,text="Copyright @ Powerd by - Yaduwanshi Pvt.Ltd.",font=("",9,"bold")).place(x=360,y=666,width=700)
button_frame=LabelFrame(bill_menu_frame,bd=7,relief=RIDGE,bg="white").place(x=780,y=574,height=75,width=568)

# ========================================================================================================================================================================

# - - - - - - - - - - -  P R O D C U T   F R A M E   C O N T E N T  - - - - - - - - - - - -

#Content =======>

zerox_lbl=Label(product_frame,text= "Zerox",bg="#074463",fg="white",font=("",15,"bold"),pady=10).place(x=20,y=200)
form_fill_lbl=Label(product_frame,text= "Online Form Apply",bg="#074463",fg="white",font=("",15,"bold"),pady=10).place(x=220,y=200)
land_mot_form_fill_lbl=Label(product_frame,text= "Land Motation Form Apply",bg="#074463",fg="white",font=("",15,"bold"),pady=10).place(x=530,y=200)
other_online_serivces_lbl=Label(product_frame,text= "Other Online Services",bg="#074463",fg="white",font=("",15,"bold"),pady=10).place(x=20,y=300)
gad_service_lbl=Label(product_frame,text= "GAD Services",bg="#074463",fg="white",font=("",15,"bold"),pady=10).place(x=370,y=300)
online_recharge_service_lbl=Label(product_frame,text= "Recharge",bg="#074463",fg="white",font=("",15,"bold"),pady=10).place(x=640,y=300)



# content Entry Field ======>
zerox_field=Entry(product_frame,width=10,bd=3,font=("",12,"bold"),justify=RIGHT,textvariable=zerox_var).place(x=90,y=210)
form_fill_field=Entry(product_frame,width=10,bd=3,font=("",12,"bold"),justify=RIGHT,textvariable=form_fill_var).place(x=410,y=210)
land_mot_form_fill_field=Entry(product_frame,width=10,bd=3,font=("",12,"bold"),justify=RIGHT,textvariable=land_mot_form_fill_var).place(x=795,y=210)
other_online_serivces_field=Entry(product_frame,width=10,bd=3,font=("",12,"bold"),justify=RIGHT,textvariable=other_online_serivces_var).place(x=240,y=310)
gad_service_field=Entry(product_frame,width=10,bd=3,font=("",12,"bold"),justify=RIGHT,textvariable=gad_service_var).place(x=510,y=310)
online_recharge_service_field=Entry(product_frame,width=10,bd=3,font=("",12,"bold"),justify=RIGHT,textvariable=online_recharge_service_var).place(x=740,y=310)
# ========================================================================================================================================================================

# - - - - - - - - - - -  B I L L   M E N U   C O N T E N T  - - - - - - - - - - - -
#Content =======>

total_service_lbl=Label(bill_menu_frame,text= "Total Services",bg="#074463",fg="white",font=("",10,"bold"),pady=10).place(x=50,y=580)
total_charges_lbl=Label(bill_menu_frame,text= "Total Charges",bg="#074463",fg="white",font=("",10,"bold"),pady=10).place(x=50,y=610)
gst_lbl=Label(bill_menu_frame,text= "G.S.T",bg="#074463",fg="white",font=("",10,"bold"),pady=10).place(x=300,y=580)
service_tax_lbl=Label(bill_menu_frame,text= "Service Tax",bg="#074463",fg="white",font=("",10,"bold"),pady=10).place(x=300,y=610)
total_ammount_lbl=Label(bill_menu_frame,text= "Total Ammount",bg="#074463",fg="white",font=("",10,"bold"),pady=10).place(x=480,y=580)



# content Entry Field ======>
total_service_field=Entry(bill_menu_frame,width=7,bd=3,font=("",10,"bold"),justify=RIGHT,textvariable=total_service_var).place(x=200,y=585)
total_charges_field=Entry(bill_menu_frame,width=7,bd=3,font=("",10,"bold"),justify=RIGHT,state=DISABLED,textvariable=total_charges_var).place(x=200,y=615)
gst_field=Entry(bill_menu_frame,width=7,bd=3,font=("",10,"bold"),justify=RIGHT,textvariable=gst_var).place(x=400,y=585)
service_tax_field=Entry(bill_menu_frame,width=7,bd=3,font=("",10,"bold"),justify=RIGHT,textvariable=service_tax_var).place(x=400,y=615)
total_ammount_field=Entry(bill_menu_frame,width=10,bd=3,font=("",10,"bold"),justify=RIGHT,state=DISABLED,textvariable=total_ammount_var).place(x=600,y=585)


# - - - - - - - - - - - B U T T O N   M E N U   C O N T E N T - - - - - - - - - - -
#BUTONS =======>

total_btn=Button(button_frame,text="Total",fg="white",width=11,height=2,bg="red",font=("",13,"bold"),bd=7,cursor="hand2",justify=CENTER,command=total_action).place(x=790,y=582)
Genrate_bill_btn=Button(button_frame,text="Genrate Bill",fg="white",width=11,height=2,bg="red",font=("",13,"bold"),bd=7,cursor="hand2",justify=CENTER,command=genrate_bill_action).place(x=930,y=582)
clear_btn=Button(button_frame,text="Clear",fg="white",width=11,height=2,bg="red",font=("",13,"bold"),bd=7,cursor="hand2",justify=CENTER,command=clear_btn_action).place(x=1070,y=582)
exit_btn=Button(button_frame,text="Exit",fg="white",width=11,height=2,bg="red",font=("",13,"bold"),bd=7,cursor="hand2",justify=CENTER,command=exit_btn_action).place(x=1210,y=582)


# = = = = = = = =  = = B I L L    A R E A ======================================================



bill_area_title=Label(bill_area,text="CUSTOMER'S BILL",font=("times new roman",15,"bold"),bd=5,relief=GROOVE).pack(fill=X)
bill_area_textbox=Text(bill_area)
bill_area_textbox.pack(fill=BOTH)
bill_area_textbox.insert(END,"\t\tWelcome to SA'S INET Service\n")
bill_area_textbox.insert(END,"=====================================================")
bill_area_textbox.insert(END,"\n Customer Name :")
bill_area_textbox.insert(END,"\n Mobile No     :")
bill_area_textbox.insert(END,"\n Bill No.      :")
bill_area_textbox.insert(END,"\n=====================================================")
bill_area_textbox.insert(END,"\n Service Name\t")
bill_area_textbox.insert(END,"\t\t\t\tPrice")
bill_area_textbox.insert(END,"\n=====================================================")
bill_area_textbox.insert(END,"\n\n\n\n\n\n\n\n\n=====================================================\n\n")
bill_area_textbox.insert(END,"\tThank You for vist on SA'S INET Service\n")
bill_area_textbox.insert(END,"\t\t(Hasanganj,Munger)")
bill_area_textbox.config(state=DISABLED)

bill.mainloop()