from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image
import pymysql
login=Tk()
login.title("Login")
login.geometry("1500x675+0+0")
login.minsize(1250,450)
# login.config(bg="black",bd=10,relief=GROOVE)

#<<<<<<<<<<<<<<<<<<    V A R I A B L E S    >>>>>>>>>>>>>>>>>>>>>>>>>

username_var=StringVar()
password_var=StringVar()



#<<<<<<<<<<<<<<<<<    I  M  A  G  E  S    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

background_img=ImageTk.PhotoImage(file="Images/background.jpg")
main_logo=PhotoImage(file="Images/main_logo.png")
side_logo=ImageTk.PhotoImage(file="Images/side.jpg")
username_logo=PhotoImage(file="Images/user2.png")
password_logo=PhotoImage(file="Images/password2.png")
login_button=PhotoImage(file="Images/login.png")


#================    F   R   A   M   E    ====================================
title_frame=Label(login,text="SA'S INET Service",bd=10,relief=GROOVE,bg="#074463",fg="gold",pady=15,font=("Algerian","30","bold")).pack(fill=X)

bg_img=Label(login,image=background_img,bd=0).pack(padx=0,pady=0)

side_img=Label(login,image=side_logo,bd=0).place(x=20,y=210,height=390,width=450)


login_frame=Frame(login,bg="silver",bd=0)
login_frame.place(x=470,y=210,height=390,width=800)
# main_img=Label(login_frame,image=main_logo,pady=15).place(x=200,y=5,height=120,width=150)


#* * * * * * * * * * * Username And Password  & Entry field * * * * * * * * * * * * * *
username=Label(login_frame,bg="silver",text="UserName",image=username_logo,compound=LEFT,fg="red",font=("Chiller",50,"bold")).grid(row=0,column=0,padx=20,pady=25)
password=Label(login_frame,bg="silver",text="Password ",image=password_logo,compound=LEFT,fg="red",font=("Chiller",50,"bold")).grid(row=1,column=0,padx=20,)

username_entry=Entry(login_frame,bd=3,width=30,font=("times new roman",15),textvariable=username_var)
username_entry.grid(row=0,column=1,padx=100)
username_entry.focus()
password_entry=Entry(login_frame,bd=3,width=30,textvariable=password_var,font=("times new roman",15),show="#")
password_entry.grid(row=1,column=1,padx=100)


# * * * * * * * * * *    B U T T O N S   A C T I O N S    * * * * * * * * * * * * * * * *

def login_action():
    if username_var.get()=="":
        messagebox.showerror("Error","Please Enter your Username !!")
        username_entry.focus()
    elif password_var.get()=="":
        messagebox.showerror("Error","Please Enter your Password !!")
        password_entry.focus()
    # elif username_var.get()=="MyAdmin" and password_var.get()=="merapassword":
    #     # messagebox.showinfo("Success","Welcome")
    #     login.destroy()
    #     import Bill
    else:
        try:
            conn=pymysql.connect(host="localhost",user="root",password="",database="sa's inet service")
            curs=conn.cursor()
            curs.execute("select * from admin_pannel where UserName=%s and Password=%s",(username_var.get(),password_var.get()))
            login_credential=curs.fetchone()
            if login_credential!=None:
                login.destroy()
                import Bill
            
            else:
                messagebox.showerror("Error","Invalid Username or Pasword !!")
                username_entry.focus()
                password_var.set("")
            conn.close()
        except Exception:
            if Exception == True:
                messagebox.showerror("ERROR",f"Error due to : {Exception}")
            else:
                messagebox.showwarning("NETWORK ERROR","Please check your Internet conection")
            
            


def reset_action():
    username_var.set("")
    password_var.set("")


def exit_action():
    option=messagebox.askyesno("Exit","Do you really want to Exit?")
    if option==1:
        login.destroy()



def forgot_password_action():
    forgot=Toplevel()
    forgot.title("Forgot Password")
    forgot.config(bg="blue",bd=10,relief=GROOVE)
    forgot.geometry("830x340+410+210")
    forgot.minsize(830,340)
    forgot.maxsize(830,340)
    forgot.focus_force()
    forgot.grab_set()

#* * * * * *    F O R G O T   W I N D O W    * * * * * * * *
        
    #<<<<<<<<    V A R I A B L E S    >>>>>>
    email_option_var=StringVar()
    username_option_entry_var=StringVar()
    security_question_var=StringVar()
    security_answer_var=StringVar()

    #  <<<<  T  I  T  L  E  >>>>
    
    f_title=Label(forgot,text="FORGOT PASSWORD",bg="sky blue",fg="red",font=("",20,"bold"),pady=5).pack(fill=X) 
    
    #  <<<<    O  P  T  I  O  N  S   &   B U T T O N S    >>>>
    # options_fram=Label(forgot,bg="gray",bd=5,relief=GROOVE).place(x=10,y=55,height=250,width=680)

    email_option=Label(forgot,text="Email Addres",bg="blue",fg="white",font=("",15,"bold")).place(x=20,y=80)
    email_entry=Entry(forgot,bd=3,width=30,font=("times new roman",15),textvariable=email_option_var)
    email_entry.place(x=250,y=80)
    email_entry.focus()
    # email_entry.focus()
    username_option=Label(forgot,text="Username",bg="blue",fg="white",font=("",15,"bold")).place(x=20,y=120)
    username_option_entry=Entry(forgot,bd=3,width=30,font=("times new roman",15),textvariable=username_option_entry_var).place(x=250,y=120)


    security_question_option=Label(forgot,text="Security Question",bg="blue",fg="white",font=("",15,"bold")).place(x=20,y=160)
    security_question_menu=ttk.Combobox(forgot,width=29,font=("times new roman",15),state="readonly",justify=CENTER,textvariable=security_question_var)
    security_question_menu['values']=('--------------- Select ---------------',"What is Your Birth Place ?","What is Your Childhood name ?","What is Your Mobile Number ?",
    "What is Your favorite movie ?","What is Your favorite sport ?","What is Your Hobbie",)
    security_question_menu.place(x=250,y=160)
    security_question_menu.current(0)
    security_answer=Label(forgot,text="Answer",bg="blue",fg="white",font=("",15,"bold")).place(x=20,y=200)
    security_answer=Entry(forgot,bd=3,show="#",width=30,font=("times new roman",15),textvariable=security_answer_var).place(x=250,y=200)

      
    # Submit Button and it's function =======>>
    def submit_action():
        if email_option_var.get()=="":
            messagebox.showerror("Eror","Please Enter your Email Address to reset your password !!",parent=forgot)
        elif username_option_entry_var.get()=="":
            messagebox.showerror("Eror","Please Enter your Username to reset your password !!",parent=forgot)
        elif security_question_var.get()=='--------------- Select ---------------':
            messagebox.showerror("Eror","Please select your Security Question to reset your password !!",parent=forgot)
        elif security_answer_var.get()=="":
            messagebox.showerror("Eror","Please enter your security answer to reset your password !!",parent=forgot)

        else:
            try:
                conn=pymysql.connect(host="localhost",user="root",password="",database="sa's inet service")
                curs=conn.cursor()
                curs.execute("select * from admin_pannel where Email=%s and UserName=%s and Security_Question=%s and Security_Answer=%s ",(email_option_var.get(),username_option_entry_var.get(),security_question_var.get(),security_answer_var.get()))
                reset_credential=curs.fetchone()
                if reset_credential!=None:
                    # elif email_option_var.get()=="dkbalya@gmail.com" and username_option_entry_var.get()=="MyAdmin" and security_question_var.get()=="What is Your Mobile Number ?"and security_answer_var.get()=="7250800499":
                    forgot.destroy()

# * * * * *  * * After match the details reset window ===>>
                       #* * * * * *    R E S E T   W I N D O W    * * * * * * * *
                    reset=Toplevel()
                    reset.title("Reset Password")
                    reset.config(bg="silver",bd=10,relief=GROOVE)
                    reset.geometry("950x340+280+150")
                    reset.minsize(580,400)
                    reset.maxsize(1150,500)
                    reset.focus_force()
                    reset.grab_set()

                #<<<<<<<<    V A R I A B L E S    >>>>>>
                    reset_security_question_var=StringVar()
                    reset_security_answer_var=StringVar()
                    reset_create_password_var=StringVar()
                    reset_retype_create_password_var=StringVar()

                #  <<<<  T  I  T  L  E  >>>>
                
                    reset_f_title=Label(reset,text="RESET PASSWORD",bg="sky blue",fg="red",font=("",20,"bold"),pady=5).pack(fill=X)

                # = = = = = = = = = =  =    O P T I O N S  &  E N T R Y  F I E L D    = = = = = = = = = 
                    reset_security_question_option=Label(reset,text="Security Question",bg="silver",fg="blue",font=("",15,"bold")).place(x=10,y=60)
                    reset_security_question_menu=ttk.Combobox(reset,width=18,font=("times new roman",16),state="readonly",justify=CENTER,textvariable=reset_security_question_var)
                    reset_security_question_menu['values']=('- - - - -Select- - - - -',"What is Your Birth Place ?","What is Your Childhood name ?","What is Your Mobile Number ?",
                    "What is Your favorite movie ?","What is Your favorite sport ?","What is Your Hobbie",)
                    reset_security_question_menu.place(x=200,y=60)
                    reset_security_question_menu.current(0)
                    reset_security_answer=Label(reset,text="Answer",bg="silver",fg="blue",font=("",15,"bold")).place(x=460,y=60)
                    reset_security_answer=Entry(reset,show="#",width=20,font=("times new roman",15),textvariable=reset_security_answer_var)
                    reset_security_answer.place(x=650,y=60)

                    reset_create_password_option=Label(reset,text="Create Password",bg="silver",fg="blue",font=("",15,"bold")).place(x=10,y=100)
                    retype_create_password_option=Label(reset,text="Re type Password",bg="silver",fg="blue",font=("",15,"bold")).place(x=460,y=100)
                    reset_create_password=Entry(reset,show="#",width=20,font=("times new roman",15),textvariable=reset_create_password_var)
                    reset_create_password.place(x=200,y=100)
                    retype_create_password=Entry(reset,show="#",width=20,font=("times new roman",15),textvariable=reset_retype_create_password_var)
                    retype_create_password.place(x=650,y=100)

                    #* * * * * * * * R E S E T  B U T T O N  A C T I O N S * * * * * * * * * * * 
                    def reset_password_btn_action():
                        
                        if reset_security_question_var.get()=="- - - - -Select- - - - -":
                            messagebox.showerror("Eror","Please select a security question in security question menu to reset your password !!",parent=reset)
                            reset_security_question_menu.focus()
                        elif reset_security_answer_var.get()=="":
                            messagebox.showerror("Eror","Please enter the answer of security question to reset your password !!",parent=reset)
                            reset_security_answer.focus()
                        elif reset_create_password_var.get()=="":
                            messagebox.showerror("Eror","Please enter a new password to reset your password !!",parent=reset)
                            reset_create_password.focus()
                        elif  reset_retype_create_password_var.get()=="":
                            messagebox.showerror("Eror","Please enter password again to reset your password !!",parent=reset)
                            retype_create_password.focus()
                        elif reset_retype_create_password_var.get()!=reset_create_password_var.get():
                            messagebox.showerror("Eror","Create password and Re type create password should be same !!",parent=reset)
                            reset_create_password_var.set("")
                            reset_retype_create_password_var.set("")
                            reset_create_password.focus()

                        else:
                            try:
                                # print(reset_security_question_var.get())
                                conn=pymysql.connect(host="localhost",user="root",password="",database="sa's inet service")
                                curs=conn.cursor()
                                # curs.execute("update admin_pannel set Password=%s and Security_Question=%s and Security_Answer=%s)",(reset_create_password_var.get(),reset_security_question_var.get(),reset_security_answer_var.get()))
                                curs.execute("update admin_pannel set Password=%s" ,(reset_create_password_var.get()))
                                curs.execute("update admin_pannel set Security_Question=%s" ,(reset_security_question_var.get()))
                                curs.execute("update admin_pannel set Security_Answer=%s" ,(reset_security_answer_var.get()))
                                conn.commit()
                                conn.close()
                                messagebox.showinfo("Sucessfull","Password has been chnaged sucessfully",parent=reset)
                                reset.destroy()
                            except Exception:
                                if Exception == True:
                                    messagebox.showwarning("ERROR",f"Error due to : {Exception}")
                                else:
                                    messagebox.showwarning("NETWORK ERROR","Please check your Internet conection",parent=reset)


                    reset_password_btn=Button(reset,text="RESET",bg="red",width=20,fg="white",font=("",12,"bold"),cursor="hand2",command=reset_password_btn_action).place(x=320,y=200)




                else:
                    messagebox.showerror("Eror","Invalid details Please enter a valid details to reset your password !!",parent=forgot)
                    email_option_var.set("")
                    username_option_entry_var.set("")
                    security_question_var.set('--------------- Select ---------------')
                    security_answer_var.set("")
                    email_entry.focus()

                conn.close()
            except Exception:
                if Exception == True:
                    messagebox.showerror("ERROR",f"Error due to : {Exception}")
                else:
                    messagebox.showwarning("NETWORK ERROR","Please check your Internet conection")




    def cencel_btn_action():
        cencel_btn_option=messagebox.askyesno("Exit","Don't want to reset your password",parent=forgot)
        if cencel_btn_option==1:
            forgot.destroy()


    submit_btn=Button(forgot,text="SUBMIT",bg="#dcedc1",bd=5,font=("",10,"bold"),fg="#ff4040",command=submit_action).place(x=250,y=260,width=110)
    cencel_btn=Button(forgot,text="CENCEL",bg="#dcedc1",bd=5,font=("",10,"bold"),fg="#ff4040",command=cencel_btn_action).place(x=450,y=260,width=110)
   
    







#===========================    B U T T O N S    ===============================


# login=Button(login_frame,image=login_button,bg="silver",bd=0)
# login.grid(row=4,column=1,pady=50)

login_btn=Button(login_frame,text="LOGIN",bg="blue",activebackground="silver",bd=6,font=("elephant",22,"bold"),fg="silver",cursor="hand2",command=login_action)
login_btn.place(x=120,y=250,width=150,height=60)
# login.grid(row=4,column=0,padx=5,pady=50)
reset_btn=Button(login_frame,text="RESET",bg="yellow",activebackground="silver",bd=6,font=("elephant",22,"bold"),fg="silver",cursor="hand2",command=reset_action)
reset_btn.place(x=310,y=250,width=150,height=60)
# reset.grid(row=4,column=1,pady=50)
exit_btn=Button(login_frame,text="EXIT",bg="red",activebackground="silver",bd=6,font=("elephant",22,"bold"),fg="silver",cursor="hand2",command=exit_action)
exit_btn.place(x=500,y=250,width=150,height=60)
# Exit.grid(row=4,column=2,pady=50)


forgot_password=Button(login_frame,text="Forgot Password ?",bg="silver",bd=0,fg="red",font=("",10,"bold"),cursor="hand2",command=forgot_password_action).place(x=567,y=189)
# forgot_password.grid(row=2,column=1,pady=1)

login.mainloop()