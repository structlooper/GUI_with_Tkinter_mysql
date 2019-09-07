import tkinter as tk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from tkinter import filedialog

win = tk.Tk()
win.title("Entry Potal")
win.geometry("1000x600")


# fram for regestraction fome..
label_frame = ttk.LabelFrame(win, text = 'Registration Form')
# label_frame.grid(row=0,column=0,sticky=tk.S)
label_frame.pack(side=tk.LEFT,fill=tk.BOTH,padx=15,pady=16)

# labels................
First_name_label=tk.Label(label_frame,text='First name')
First_name_label.grid(row=0,column=0,sticky=tk.W)

Surname_label=tk.Label(label_frame,text='Surname')
Surname_label.grid(row=0,column=2,sticky=tk.W)

Email_address_label=tk.Label(label_frame,text='Email Address')
Email_address_label.grid(row=3,column=0,columnspan=4,sticky=tk.W,pady=5)

Birthday_label=tk.Label(label_frame,text='Date of Birth')
Birthday_label.grid(row=5,columnspan=2,sticky=tk.W,pady=5)

Date_label=tk.Label(label_frame,text='Date')
Date_label.grid(row=6,column=0,sticky=tk.E,pady=5,padx=25)

Month_label=tk.Label(label_frame,text='Month')
Month_label.grid(row=6,column=1,sticky=tk.W,pady=5)

Year_label=tk.Label(label_frame,text='Year')
Year_label.grid(row=6,column=2,sticky=tk.W,pady=5)

Gender_label=tk.Label(label_frame,text='Gender')
Gender_label.grid(row=8,columnspan=2,sticky=tk.W,pady=5)   

New_Password_label=tk.Label(label_frame,text='New Password')
New_Password_label.grid(row=13,columnspan=2,sticky=tk.W,pady=5)   

Confirm_Password_label=tk.Label(label_frame,text='Confirm Password')
Confirm_Password_label.grid(row=15,columnspan=2,sticky=tk.W,pady=5)   

# inputs...
name_var = tk.StringVar()
First_name_entry =  ttk.Entry(label_frame,width=30,textvariable=name_var)
First_name_entry.grid(row=1,column=0,columnspan=2,padx=5,sticky=tk.W)

surname_var = tk.StringVar()
Surname_entry= ttk.Entry(label_frame,width=30,textvariable=surname_var)
Surname_entry.grid(row=1,column=2,padx=5,sticky=tk.W)

email_var = tk.StringVar()
Email_address_entry = ttk.Entry(label_frame, width=63,textvariable=email_var)
Email_address_entry.grid(row=4,columnspan=6,padx=5)

new_pass_var = tk.StringVar()
New_Password_entry = ttk.Entry(label_frame, width=63,textvariable=new_pass_var)
New_Password_entry.grid(row=14,columnspan=6,padx=5)

con_pass_var = tk.StringVar()
Confirm_Password_entry = ttk.Entry(label_frame, width=63,textvariable=con_pass_var)
Confirm_Password_entry.grid(row=16,columnspan=6,padx=5)

# birthday combobox..
date_var =tk.IntVar()
Date_combobox =ttk.Combobox(label_frame,width=4,textvariable=date_var,state='readonly')
Date_combobox['values'] = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31)
Date_combobox.current(0)
Date_combobox.grid(row=7,columnspan=1,padx=5,sticky=tk.E)

month_var = tk.StringVar()
Month_combobox =ttk.Combobox(label_frame,width=10,textvariable=month_var,state='readonly')
Month_combobox['values'] = ('January','February','March','April','May','June','July','August','September','October','Novermber','December')
Month_combobox.current(0)
Month_combobox.grid(row=7,column=1,columnspan=2,sticky=tk.W)

year_var = tk.StringVar()
Year_combobox =ttk.Combobox(label_frame,width=8,textvariable=year_var,state='readonly')
Year_combobox['values'] = (1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019)
Year_combobox.current(0)
Year_combobox.grid(row=7,column=2,columnspan=2,padx=5,sticky=tk.W)

# radio button
gender_var = tk.StringVar()
Female_btn = ttk.Radiobutton(label_frame,text='Female',value='female',variable=gender_var)
Female_btn.grid(row=9,column=0)

Male_btn = ttk.Radiobutton(label_frame,text='Male',value='male',variable=gender_var)
Male_btn.grid(row=10,column=0)

Others_btn = ttk.Radiobutton(label_frame,text='Others',value='other',variable=gender_var)
Others_btn.grid(row=11,column=0)

check_btn_var = tk.StringVar()
check_btn = ttk.Checkbutton(label_frame,text='I Confirm that all details are correct',variable=check_btn_var)
check_btn.grid(row=17,columnspan=2,sticky=tk.W,pady=15,padx=15)


def sign_up(event=None):
    user_name = name_var.get()
    user_surname = surname_var.get()
    user_email = email_var.get()
    user_date = date_var.get()
    user_month = month_var.get()
    user_year = year_var.get()
    user_new_pass = new_pass_var.get()
    user_con_pass = con_pass_var.get()
    user_gender = gender_var.get()
    click_check_btn = check_btn_var.get()
    # print(f"{user_name}:{user_surname}:{user_email}:{user_date}:{user_month}:{user_year}:{user_new_pass}:{user_con_pass}")

    if user_name and user_surname and user_email and user_gender and user_new_pass and user_con_pass:
        if user_new_pass == user_con_pass:
            if click_check_btn:

                conn = mysql.connector.connect(host='localhost',username='root',password='',database = 'pro_data')
   
                cursor = conn.cursor()

                query = 'INSERT INTO user_detail(user_names,user_surnames,user_emails,user_dd,user_mm,user_yy,user_passwords,user_genders) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)'
                value = (user_name,user_surname,user_email,user_date,user_month,user_year,user_new_pass,user_gender)
                cursor.execute(query,value)
                conn.commit()
                conn.close()
                print("Done!")
                messagebox.showinfo("Registraction",'Your Details are register Succesfully!\nNow you can login')
                New_Password_entry.delete(0,tk.END)
                Email_address_entry.delete(0,tk.END)
                Confirm_Password_entry.delete(0,tk.END)
                First_name_entry.delete(0,tk.END)
                Surname_entry.delete(0,tk.END)
                Date_combobox.current(0)
                Month_combobox.current(0)
                Year_combobox.current(0)
                
                
            else:
                mbox= messagebox.showerror('Error','Please click the Check Box')
        else:
            mbox = messagebox.showwarning("Warning","The password you entered not matched!!\nEnter again")
            New_Password_entry.delete(0,tk.END)
            Confirm_Password_entry.delete(0,tk.END)
    else:
        mbox = messagebox.showwarning('Warning','Please fill all required details')
        

    

# submit butn...
Submit_btn = ttk.Button(label_frame,width=25,text='Sign Up',command =sign_up)
Submit_btn.grid(row=18,column=2,sticky=tk.W)

# label_frame.bind("<Enter>", sign_up )

# ###### login_surface.............
label_frame_2 = ttk.LabelFrame(win,text = 'Login Form')
label_frame_2.pack(side=tk.RIGHT,fill=tk.BOTH,padx=15,pady=16)


Login_id = tk.Label(label_frame_2,text="Email Address")
Login_id.grid(row=0,column=0,sticky=tk.W,pady=5)

password = tk.Label(label_frame_2,text ="Password")
password.grid(row=3,column=0,sticky=tk.W,pady=5)

# inputs........
login_var = tk.StringVar()
Login_id_input = tk.Entry(label_frame_2,width=63,textvariable=login_var)
Login_id_input.grid(row=2,column=0,columnspan=5,pady=5,padx=5)
Login_id_input.focus_set()

password_var = tk.StringVar()
password_input = tk.Entry(label_frame_2,width=63,textvariable=password_var)
password_input.grid(row=4,column=0,columnspan=5,pady=5,padx=5)

def login_func(event=None):
    entered_login = login_var.get()
    entered_password = password_var.get()
    print(f'{entered_login}:{entered_password}')
    conn = mysql.connector.connect(host='localhost',username='root',password='',database = 'pro_data')
   
    cursor = conn.cursor()

    query = 'SELECT user_emails,user_passwords FROM user_detail'
    
    cursor.execute(query)
    counter = 0
    password = []
    email = []
    for i in cursor:
        
        for j in i:
            if counter%2 == 0:
                email.append(j)
            else:
                password.append(j)
            counter += 1
    temp = ''
    wemp = ''
    if entered_login and entered_password:
        for login in email:
            if entered_login == login:
                temp += 'yes'
        
        for p in password:
            if entered_password == p:
                wemp += 'yes'
    else:
        return messagebox.showinfo('Information','Please enter email id and Password')
    
    if len(wemp) > 0 and len(temp) > 0:
        messagebox.showinfo('login','done')
        Login_id_input.delete(0,tk.END)
        password_input.delete(0,tk.END)
        new_win = tk.Toplevel()
        new_win.geometry('1000x600+500+200')
        new_win.title('Home')
    else:
        messagebox.showerror('Error',f"Either email and password is incorrect!!\n please type correct email id and password to Login")
        Login_id_input.delete(0,tk.END)
        password_input.delete(0,tk.END)
    
    query_2 = "SELECT user_names from user_detail"
    cursor.execute(query_2)
    for i in cursor:
        print(i)
    
    
    # work on home frame.......


    
    conn.commit()
    conn.close()



login_btn = ttk.Button(label_frame_2,width=25,text='Login',command=login_func)
login_btn.grid(row=5,column=4,sticky=tk.E,padx=5,pady=40)

win.mainloop()