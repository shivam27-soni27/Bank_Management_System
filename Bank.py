from tkinter import *
#from tkinter.ttk import *
import pyautogui
from tkinter import messagebox
import mysql.connector
from requests import get
import random
demodb=mysql.connector.connect(host='localhost',user='root',passwd='shivam1shivam')
democursor=demodb.cursor()
democursor.execute("create database if not exists bms")
demodb.commit()
demodb=mysql.connector.connect(host='localhost',user='root',passwd='shivam1shivam',database='bms')
democursor=demodb.cursor()
democursor.execute("""create table if not exists users (Name varchar(50),
Father_Name varchar(50),
Mother_Name varchar(50),
phone_n varchar(50),
email varchar(50),
address varchar(50),
gender varchar(50),
passcode varchar(50),
password varchar(50),
bday date,
acc_c date,
acc_no varchar(50),
card_n varchar(50),
ifsc varchar(50),
cvv varchar(50),
expiry date,
city varchar(50),
country varchar(50),
branch_c varchar(50),
pan_no varchar(50),
aadhar_no varchar(50),
passport_no varchar(50),
voterid_no varchar(50),
occupation varchar(50),
organisation varchar(50),
income varchar(50),
net_worth varchar(50),
qualification varchar(50))""")
demodb.commit()
democursor.execute("""create table if not exists user03(acc_no varchar(50),
userid varchar(50),
password varchar(50))""")
demodb.commit()
democursor.execute("""create table if not exists users02(acc_no varchar(50),
card_no varchar(50))""")
demodb.commit()
democursor.execute("""create table if not exists email_l(acc_no varchar(30),
email_id varchar(30),
Status varchar(30))""")
demodb.commit()
democursor.execute("""create table if not exists pas_reset(acc_no varchar(30),
old_pas varchar(30),
new_pas varchar(30),
time varchar(30),
date varchar(30))""")
demodb.commit()
#def insert(x,y):
y=Tk()           #First Window
y.title("Welcome To Bank")
y.attributes('-fullscreen', True)
#y.state('zoomed')
y.configure(bg="thistle3")
y.iconbitmap('Py_ICO.ico')
from datetime import datetime
import smtplib
def del_acc1001():
    deac=Tk()
    deac.title("Delete Account")
    deac.attributes('-fullscreen', True)
    deac.configure(bg='white')
    deac.iconbitmap('Py_ICO.ico')
    l=Label(deac,text="ID : ",bg='white',font="LUCIDA 15 bold").place(x=100,y=30)
    s=StringVar(deac)
    s.set("1001")
    e=Entry(deac,textvariable=s,bg='white',borderwidth=3,relief='solid',font="LUCIDA 15 bold").place(x=200,y=30)
    def conf_del():
        ide=str(s.get())
        democursor.execute("delete from users where acc_no="+ide)
        demodb.commit()
        democursor.execute("drop table bal_"+ide)
        demodb.commit()
        democursor.execute("drop table trans_"+ide)
        demodb.commit()
        democursor.execute("drop table user_log"+ide)
        demodb.commit()
        deac.destroy()
    b=Button(deac,text="Delete",bg='white',fg='red',borderwidth=1,relief='solid',activebackground='red',command=conf_del,font="LUCIDA 15 bold").place(x=300,y=100)
b=Button(y,text="Delete",bg='white',fg='red',borderwidth=1,relief='solid',activebackground='red',command=del_acc1001,font="LUCIDA 15 bold").place(x=1400,y=800)
#def lastp("2025-12-12","s1001",'s','s','s','8799523738','shivam2712.soni@gmail.com','GJ','M','8888','8888','2003-12-27','2023-12-31','1001','1234567891234567','SSBIN1001','888','GJ','IND','SS123','PFPPKS1001','123456789123456','PAS','','N/A','N/A','10000','10000','B.Tech(CS)')
def lastp(expiry,logid,Name,Father,Mother,Phone,Email,Address,Gender,passc,new_pas1,birthdate,Account_Created,account_num,card_num,ifsc_code,cvv,City,Country,branch_code,Pan,Aadhar,Passport,Voter,Occupation,Organization,Income,Net_Worth,Qualification):
    democursor=demodb.cursor()
    democursor.execute("insert into users values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(Name,Father,Mother,Phone,Email,Address,Gender,passc,new_pas1,birthdate,Account_Created,account_num,card_num,ifsc_code,cvv,expiry,City,Country,branch_code,Pan,Aadhar,Passport,Voter,Occupation,Organization,Income,Net_Worth,Qualification))
    demodb.commit()
    democursor=demodb.cursor()
    democursor.execute("insert into user03 values(%s,%s,%s)",(account_num,logid,new_pas1))
    demodb.commit() 
    democursor=demodb.cursor()
    democursor.execute("insert into users02 values(%s,%s)",(account_num,card_num))
    demodb.commit()
    tbname="user_log"+account_num
    democursor=demodb.cursor()
    democursor.execute("create table "+tbname+" (date varchar(30),time varchar(30),acc_no varchar(30),num varchar(100))")
    demodb.commit() 
    democursor=demodb.cursor()
    democursor.execute("create table bal_"+account_num+" (date_t date,current_bal varchar(50),number varchar(255))")
    demodb.commit() 
    democursor=demodb.cursor()
    democursor.execute("create table trans_"+account_num+" (Name VARCHAR(50),acc_no VARCHAR(50),to_acc VARCHAR(50),amt VARCHAR(50),bal VARCHAR(50),to_name varchar(50),num int,date_time varchar(50),date varchar(50))")                       
    demodb.commit()
    democursor=demodb.cursor()
    democursor.execute("insert into bal_"+account_num+" values(%s,%s,%s)",(Account_Created,"0",'0'))
    demodb.commit()
    #print((Name,Father,Mother,Phone,Email,Address,Gender,passc,new_pas1,birthdate,Account_Created,account_num,card_num,ifsc_code,cvv,expiry,City,Country,branch_code,Pan,Aadhar,Passport,Voter,Occupation,Organization,Income,Net_Worth,Qualification))
def cre_acc1001():
    lastp("2025-12-12","s1001",'s','s','s','8799523738','shivam2712.soni@gmail.com','GJ','M','8888','8888','2003-12-27','2023-12-31','1001','1234567891234567','SSBIN1001','888','GJ','IND','SS123','PFPPKS1001','123456789123456','PAS','','N/A','N/A','10000','10000','B.Tech(CS)')
    democursor.execute("insert into email_l values(1001,'shivam2712.soni@gmail.com','Verified')")
    demodb.commit()
b=Button(y,text="Create",bg='white',fg='red',borderwidth=1,relief='solid',activebackground='red',command=cre_acc1001,font="LUCIDA 15 bold").place(x=1200,y=800)                  
def cr_acc():
    #y.destroy()
    b1=Tk()
    b1.title("New Account")
    b1.attributes('-fullscreen', True)
    b1.configure(bg='white')
    b1.iconbitmap('Py_ICO.ico')
    def win_cl1():
        b1.destroy()
    b=Button(b1,text='< Back To Login',borderwidth=0,relief='solid',activebackground='red',command=win_cl1,bg='white',font='LUCIDA 10').place(x=10,y=10)
    pyautogui.press("Alt+Tab")
    name=StringVar(b1)
    name.set("")
    f_name=StringVar(b1)
    f_name.set("")
    m_name=StringVar(b1)
    m_name.set("")
    p_no=StringVar(b1)
    p_no.set("")
    email=StringVar(b1)
    email.set("")
    add=StringVar(b1)
    add.set("")
    gen=StringVar(b1)
    bday_d=StringVar(b1)
    bday_m=StringVar(b1)
    bday_y=StringVar(b1)
    gen.set("-Gender-")
    bday_d.set('-DD-')
    bday_m.set('-MM-')
    bday_y.set('YYYY')
    city=StringVar(b1)
    city.set("")
    country=StringVar(b1)
    country.set("")
    pan=StringVar(b1)
    pan.set("")
    aadhar=StringVar(b1)
    aadhar.set("")
    passp=StringVar(b1)
    passp.set("")
    voter=StringVar(b1)
    voter.set("")
    occu=StringVar(b1)
    occu.set("")
    org=StringVar(b1)
    org.set("")
    inc=StringVar(b1)
    inc.set("")
    net_w=StringVar(b1)
    net_w.set("")
    qual=StringVar(b1)
    qual.set("")
    gens=["Male","Female","Others"]
    bday_date=['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
    bday_month=['January','February','March','April','May','June','July','August','September','October','November','December']
    bday_year=['2021','2020','2019','2018','2017','2016','2015','2014','2013','2012','2011','2010','2009','2008','2007','2006','2005','2004','2003','2002','2001','2000','1999','1998','1997','1996','1995','1994','1993','1992','1991','1990','1989','1988','1987','1986','1985','1984','1983','1982','1981','1980','1979','1978','1977','1976','1975','1974','1973','1972','1971','1970','1969','1968','1967','1966','1965','1964','1963','1962','1961','1960','1959','1958','1957','1956','1955','1954','1953','1952','1951','1950','1949','1948','1947','1946','1945','1944','1943','1942','1941']
    ###########################################################################
    l=Label(b1,text='Fill Following Details',bg='white',font='LUCDIA 20 bold').pack(padx=20,pady=20)
    l=Label(b1,text='Name : ',bg='white',font='LUCIDA 15 bold').place(x=30,y=65)
    l=Label(b1,text="Father's Name : ",bg='white',font='LUCIDA 15 bold').place(x=30,y=115)
    l=Label(b1,text="Mother's Name : ",bg='white',font='LUCIDA 15 bold').place(x=30,y=165)
    l=Label(b1,text='Phone No. : ',bg='white',font='LUCIDA 15 bold').place(x=30,y=215)
    l=Label(b1,text='E-Mail : ',bg='white',font='LUCIDA 15 bold').place(x=30,y=265)
    l=Label(b1,text='Address : ',bg='white',font='LUCIDA 15 bold').place(x=30,y=315)
    l=Label(b1,text='Gender : ',bg='white',font='LUCIDA 15 bold').place(x=30,y=365)
    l=Label(b1,text='Birthday Date : ',bg='white',font='LUCIDA 15 bold').place(x=30,y=415)
    l=Label(b1,text='City,State : ',bg='white',font='LUCIDA 15 bold').place(x=30,y=465)
    l=Label(b1,text='Country : ',bg='white',font='LUCIDA 15 bold').place(x=30,y=515)
    l=Label(b1,text='Pan No. : ',bg='white',font='LUCIDA 15 bold').place(x=30,y=565)
    l=Label(b1,text='Aadhar No. : ',bg='white',font='LUCIDA 15 bold').place(x=30,y=615)
    l=Label(b1,text='Passport ID : ',bg='white',font='LUCIDA 15 bold').place(x=30,y=665)
    l=Label(b1,text='Voter ID : ',bg='white',font='LUCIDA 15 bold').place(x=30,y=715)
    l=Label(b1,text='Occupation : ',bg='white',font='LUCIDA 15 bold').place(x=1100,y=65)
    l=Label(b1,text='Organisation : ',bg='white',font='LUCIDA 15 bold').place(x=1100,y=115)
    l=Label(b1,text='Income : ',bg='white',font='LUCIDA 15 bold').place(x=1100,y=165)
    l=Label(b1,text='Net Worth : ',bg='white',font='LUCIDA 15 bold').place(x=1100,y=215)
    l=Label(b1,text='Qualification : ',bg='white',font='LUCIDA 15 bold').place(x=1100,y=265)
    ############################################################################
    l=Entry(b1,textvariable=name,borderwidth=3,relief='solid',width=30,font='LUCIDA 15 bold').place(x=260,y=65)
    l=Entry(b1,textvariable=f_name,borderwidth=3,relief='solid',font='LUCIDA 15 bold').place(x=260,y=115)
    l=Entry(b1,textvariable=m_name,borderwidth=3,relief='solid',font='LUCIDA 15 bold').place(x=260,y=165)
    l=Entry(b1,textvariable=p_no,borderwidth=3,relief='solid',font='LUCIDA 15 bold').place(x=260,y=215)
    l=Entry(b1,textvariable=email,borderwidth=3,relief='solid',font='LUCIDA 15 bold').place(x=260,y=265)
    l=Entry(b1,textvariable=add,borderwidth=3,relief='solid',font='LUCIDA 15 bold').place(x=260,y=315)
    l=OptionMenu(b1,gen,*gens).place(x=260,y=365)
    l=Entry(b1,textvariable=city,borderwidth=3,relief='solid',font='LUCIDA 15 bold').place(x=260,y=465)
    l=Entry(b1,textvariable=country,borderwidth=3,relief='solid',font='LUCIDA 15 bold').place(x=260,y=515)
    l=Entry(b1,textvariable=pan,borderwidth=3,relief='solid',font='LUCIDA 15 bold').place(x=260,y=565)
    l=Entry(b1,textvariable=aadhar,borderwidth=3,relief='solid',font='LUCIDA 15 bold').place(x=260,y=615)
    l=Entry(b1,textvariable=passp,borderwidth=3,relief='solid',font='LUCIDA 15 bold').place(x=260,y=665)
    l=Entry(b1,textvariable=voter,borderwidth=3,relief='solid',font='LUCIDA 15 bold').place(x=260,y=715)
    l=Entry(b1,textvariable=occu,borderwidth=3,relief='solid',font='LUCIDA 15 bold').place(x=1330,y=65)
    l=Entry(b1,textvariable=org,borderwidth=3,relief='solid',font='LUCIDA 15 bold').place(x=1330,y=115)
    l=Entry(b1,textvariable=inc,borderwidth=3,relief='solid',font='LUCIDA 15 bold').place(x=1330,y=165)
    l=Entry(b1,textvariable=net_w,borderwidth=3,relief='solid',font='LUCIDA 15 bold').place(x=1330,y=215)
    l=Entry(b1,textvariable=qual,borderwidth=3,relief='solid',font='LUCIDA 15 bold').place(x=1330,y=265)
    om=OptionMenu(b1,bday_d,*bday_date).place(x=260,y=415)
    om=OptionMenu(b1,bday_m,*bday_month).place(x=370,y=415)
    om=OptionMenu(b1,bday_y,*bday_year).place(x=500,y=415)
    def check_blank():
        name_g=name.get()
        f_name1=f_name.get()
        m_name1=m_name.get()
        p_no1=p_no.get()
        email1=email.get()
        address1=add.get()
        gender=gen.get()
        city1=city.get()
        country1=country.get()
        pan1=pan.get()
        aadhar1=aadhar.get()
        passp1=passp.get()
        voter1=voter.get()
        occu1=occu.get()
        org1=org.get()
        inc1=inc.get()
        net_w1=net_w.get()
        qual1=qual.get()
        bday_d1=bday_d.get()
        bday_m1=bday_m.get()
        bday_y1=bday_y.get()
        if name_g=='' or f_name1=='' or m_name1=='' or p_no1=='' or email1=='' or address1=='' or gender=='' or city1=='' or country1=='' or pan1=='' or aadhar1=='' or occu1=='' or org1=='' or inc1=='' or net_w1=='' or qual1=='' or name_g==' ' or f_name1==' ' or m_name1==' ' or p_no1==' ' or email1==' ' or address1==' ' or gender==' ' or city1==' ' or country1==' ' or pan1==' ' or aadhar1==' ' or occu1==' ' or org1==' ' or inc1==' ' or net_w1==' ' or qual1==' ':
            if bday_d1=='-DD-' or bday_m1=='-MM-' or bday_y1=='-YYYY-' :
                l=Label(b1,text='Please give Input',bg='white',fg='red',font='LUCIDA 15 bold').place(x=500,y=800)
            if '@' not in email1 or '.' in email1:
                l=Label(b1,text='Please Enter Valid Mail',bg='white',fg='red',font='LUCIDA 15 bold').place(x=500,y=800)
        else:
            if bday_m1=='January':
                bday_m1='01'
            elif bday_m1=='February':
                bday_m1='02'
            elif bday_m1=='March':
                bday_m1='03'
            elif bday_m1=='April':
                bday_m1='04'
            elif bday_m1=='May':
                bday_m1='05'
            elif bday_m1=='June':
                bday_m1='06'
            elif bday_m1=='July':
                bday_m1='07'
            elif bday_m1=='August':
                bday_m1='08'
            elif bday_m1=='September':
                bday_m1='09'
            elif bday_m1=='October':
                bday_m1='10'
            elif bday_m1=='November':
                bday_m1='11'
            elif bday_m1=='December':
                bday_m1='12'
            else:
                None
            from datetime import date
            day1=datetime.now().day
            mont=datetime.now().month
            yers=datetime.now().year
            expyr=int(yers)+10
            expyr1=str(expyr)
            final_expiry=str(expyr1)+'-'+str(mont)+'-'+str(day1)
            birthdate=str(bday_y1)+'-'+str(bday_m1)+'-'+str(bday_d1)
            Password_file=str(bday_y1)+str(bday_m1)+str(bday_d1)
            Name=str(name_g)
            Father=str(f_name1)
            Mother=str(m_name1)
            Phone=str(p_no1)
            Email=str(email1)
            Address=str(address1)
            Gender=str(gender)
            City=str(city1)
            Country=str(country1)
            Pan=str(pan1)
            Aadhar=str(aadhar1)
            Passport=str(passp1)
            Voter=str(voter1)
            Occupation=str(occu1)
            Organization=str(org1)
            Income=str(inc1)
            Net_Worth=str(net_w1)
            Qualification=str(qual1)
            Account_Created=str(date.today())
        
            def passc():
                b1.destroy()
                p=Tk()
                p.title("Set Password")
                p.attributes('-fullscreen', True)
                p.configure(bg="white")
                p.iconbitmap('Py_ICO.ico')
                def win_cl1():
                    p.destroy()
                b=Button(p,text='< Back To Login',borderwidth=0,relief='solid',activebackground='red',command=win_cl1,bg='white',font='LUCIDA 10').place(x=10,y=10)
                card_1=random.randint(1001,9999)
                card_2=random.randint(1001,9999)
                card_3=random.randint(1001,9999)
                card_4=random.randint(1001,9999)
                card_num=str(card_1)+str(card_2)+str(card_3)+str(card_4)
                
                democursor=demodb.cursor()
                democursor.execute("select count(*) from users")
                for i in democursor:
                    account_num=str(1000+int(i[0]))
                    
                ifsc_code="SSIN"+str(random.randint(111111,9999999999))
                #print(ifsc_code)
                cvv_1=str(random.randint(0,9))
                cvv_2=str(random.randint(0,9))
                cvv_3=str(random.randint(0,9))
                cvv=cvv_1+cvv_2+cvv_3
                #print(cvv)
                branch_code="GNGJ"+str(random.randint(11111,9999999))
                #print(branch_code)
                
                l=Label(p,text="",bg='white',font='LUCIDA 20 bold').pack(padx=0,pady=0)
                l=Label(p,text="Set Password",bg='white',font='LUCIDA 20 bold').pack(padx=0,pady=0)
                l=Label(p,text="Set Password : ",bg='white',font='LUCIDA 15 bold').place(x=170,y=200)
                l=Label(p,text="Type Password Once Again: ",bg='white',font='LUCIDA 15 bold').place(x=100,y=300)
                new_pas=StringVar(p)
                new_pas.set('')
                re_pas=StringVar(p)
                re_pas.set('')
                ent=Entry(p,textvariable=new_pas,show='*',borderwidth=3,relief='solid',font='LUCIDA 15 bold').place(x=500,y=200)
                ent=Entry(p,textvariable=re_pas,show='*',borderwidth=3,relief='solid',font='LUCIDA 15 bold').place(x=500,y=300)
                def passcode():
                    new_pas1=new_pas.get()
                    re_pas1=re_pas.get()
                    if new_pas1==re_pas1:
                        if len(new_pas1)>7:
                            p.destroy()
                            n=Tk()
                            n.title("Set Passcode")
                            n.attributes('-fullscreen', True)
                            n.configure(bg='white')
                            n.iconbitmap('Py_ICO.ico')
                            def win_cl1():
                                n.destroy()
                            b=Button(n,text='< Back To Login',borderwidth=0,relief='solid',activebackground='red',command=win_cl1,bg='white',font='LUCIDA 10').place(x=10,y=10)
                            l=Label(n,text="",bg='white',font='LUCIDA 20 bold').pack(padx=0,pady=0)
                            l=Label(n,text="Set Transaction Passcode",bg='white',font='LUCIDA 20 bold').pack(padx=0,pady=0)
                            l=Label(n,text="Set Passcode : ",bg='white',font='LUCIDA 15 bold').place(x=170,y=200)
                            l=Label(n,text="Type Passcode Once Again: ",bg='white',font='LUCIDA 15 bold').place(x=100,y=300)
                            new_pasc=StringVar(n)
                            new_pasc.set('')
                            re_pasc=StringVar(n)
                            re_pasc.set('')
                            digit=StringVar(n)
                            digit.set("-No. of Digits-")
                            ddd=['4-Digit','6-Digit']
                            l=Label(n,text="",bg='white',font='LUCIDA 20 bold').pack(padx=0,pady=0)
                            l=OptionMenu(n,digit,*ddd).pack(padx=0,pady=0)
                            ent=Entry(n,textvariable=new_pasc,show='*',borderwidth=3,relief='solid',font='LUCIDA 15 bold').place(x=500,y=200)
                            ent=Entry(n,textvariable=re_pasc,show='*',borderwidth=3,relief='solid',font='LUCIDA 15 bold').place(x=500,y=300)
                            def last():
                                num_d=digit.get()
                                pasc=str(new_pasc.get())
                                pasc_re=str(re_pasc.get())
                                vale=0
                                valu=0
                                if num_d=="-No. of Digits-":
                                    l=Label(n,text="Please Select Number of Digits",bg='white',fg='red',font='LUCIDA 15 bold').place(x=1100,y=700)
                                elif num_d=="4-Digit":
                                    if pasc==pasc_re and len(pasc)==4:
                                        try:
                                            int(pasc)
                                        except ValueError:
                                            l=Label(n,text="Please input integers",bg='white',fg='red',font='LUCIDA 15 bold').place(x=1100,y=700)
                                            vale=vale+1
                                    else:
                                        vale=vale+1
                                        l=Label(n,text="Passcode Doesn't match or length doesn't match",bg='white',fg='red',font='LUCIDA 15 bold').place(x=1100,y=700)
                                elif num_d=="6-Digit":
                                    if pasc==pasc_re and len(pasc)==6:
                                        try:
                                            int(pasc)
                                        except ValueError:
                                            valu=valu+1
                                            l=Label(n,text="Please input integers",bg='white',fg='red',font='LUCIDA 15 bold').place(x=1100,y=700)
                                    else:
                                        valu=valu+1
                                        l=Label(n,text="Passcode Doesn't match or length doesn't match",bg='white',fg='red',font='LUCIDA 15 bold').place(x=1100,y=700)
                                def ending():
                                    n.destroy()
                                    r=Tk()
                                    r.title("Confirm Email")
                                    r.attributes('-fullscreen', True)
                                    r.configure(bg='white')
                                    r.iconbitmap('Py_ICO.ico')
                                    def win_cl1():
                                        r.destroy()
                                    b=Button(r,text='< Back To Login',borderwidth=0,relief='solid',activebackground='red',command=win_cl1,bg='white',font='LUCIDA 10').place(x=10,y=10)
                                    em12=str(Email)
                                    first_n=Email[1:-10]
                                    ekfk=len(first_n)
                                    ejjj=ekfk*'*'
                                    final_emid=em12.replace(first_n,ejjj)
                                    import random
                                    list1=['S','H','I','V','A','M']
                                    w_1=random.choice(list1)
                                    w_2=str(random.randint(111111,999999))
                                    w_final=w_1+w_2
                                    text1="Verify Email"
                                    text2="A Code Has Been Sent to "+final_emid+" Please Enter That Code Below - "
                                    b=Label(r,text=text1,bg='white',font="LUCIDA 15 bold").pack(padx=0,pady=0)
                                    b=Label(r,text=text2,fg='red',bg='white',font="LUCIDA 15 bold").pack(padx=0,pady=0)
                                    import smtplib
                                    from email.message import EmailMessage
                                    Sender_Email = "codeinterest27@gmail.com"
                                    Reciever_Email = [Email]
                                    Password = "sodjxrgmbrlghznu"
                                    newMessage = EmailMessage()
                                    newMessage['Subject'] = "Secret Code To Verify Email ID for Account : "+account_num
                                    newMessage['From'] = Sender_Email
                                    newMessage['To'] = Reciever_Email
                                    newMessage.set_content("""Hello """+Name+""",
This is Your Secret Code :


            """+w_1+"""-"""+w_2+"""
            

Please Do Not Share This Code With anybody.
This Is Your Secret Code.
Do Not Reply to this Email
For any Complaints contact us at
Mail - codeinterest27@gmail.com
Phone - +918799523738""")
                                    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp3:
                                        smtp3.login(Sender_Email, Password)
                                        smtp3.send_message(newMessage)#'''
                                    f_let=StringVar(r)
                                    f_let.set('↓')
                                    om=OptionMenu(r,f_let,*list1).place(x=700,y=300)
                                    codes=StringVar(r)
                                    e=Entry(r,textvariable=codes,borderwidth=3,relief='solid',bg='white',font='LUCIDA 15 bold').place(x=850,y=300)                                    
                                    def end1():
                                        first_letter=f_let.get()
                                        code_last=codes.get()
                                        final_code=str(first_letter)+str(code_last)
                                        def end2():
                                            r.destroy()
                                            q=Tk()
                                            q.title("Thank You")
                                            q.attributes('-fullscreen', True)
                                            q.configure(bg="white")
                                            q.iconbitmap('Py_ICO.ico')
                                            def win_cl1():
                                                q.destroy()
                                            b=Button(q,text='< Back To Login',borderwidth=0,relief='solid',activebackground='red',command=win_cl1,bg='white',font='LUCIDA 10').place(x=10,y=10)
                                            loginid=str(Name[0:3])+str(account_num)
                                            logsid="Login ID : "+loginid
                                            name="Name : "+Name
                                            fna="Father : "+Father
                                            mna="Mother : "+Mother
                                            phn="Phone No : "+Phone
                                            ema="Email Id : "+Email
                                            Addr="Address : "+Address
                                            Gen="Gender : "+Gender
                                            dobs="Birth Date : "+birthdate
                                            Accountnum="Account No : "+account_num
                                            cardnum="Card No : "+card_num
                                            ifsccode="IFSC Code : "+ifsc_code
                                            cvvs="CVV : "+cvv
                                            Citys="City : "+City
                                            Countrys="Country : "+Country
                                            b_code="Branch Code : "+branch_code
                                            expirys="Expiry : "+final_expiry
                                            current_bal='Current Balance : 0.00 Cr.'
                                            from fpdf import FPDF
                                            pdf = FPDF()
                                            pdf.add_page()
                                            pdf.set_font("Arial",size=25)
                                            pdf.cell(200, 10, txt = Accountnum,ln=1,align='C')
                                            pdf.cell(200, 10, txt = "-----------------------------------------------------------------------", ln = 2, align = 'A')
                                            pdf.cell(200, 10, txt =logsid, ln = 3, align = 'A')
                                            pdf.cell(200, 10, txt =name, ln = 4, align = 'A')
                                            pdf.cell(200, 10, txt =fna, ln = 5, align = 'A')
                                            pdf.cell(200, 10, txt =mna, ln = 6, align = 'A')
                                            pdf.cell(200, 10, txt =phn, ln = 7, align = 'A')
                                            pdf.cell(200, 10, txt =ema, ln = 8, align = 'A')
                                            pdf.cell(200, 10, txt =Addr, ln = 9, align = 'A')
                                            pdf.cell(200, 10, txt =Gen, ln = 10, align = 'A')
                                            pdf.cell(200, 10, txt =dobs, ln = 11, align = 'A')
                                            pdf.cell(200, 10, txt =Accountnum, ln = 12, align = 'A')
                                            pdf.cell(200, 10, txt =cardnum, ln = 13, align = 'A')
                                            pdf.cell(200, 10, txt =ifsccode, ln = 14, align = 'A')
                                            pdf.cell(200, 10, txt =cvvs, ln = 15, align = 'A')
                                            pdf.cell(200, 10, txt =Citys, ln = 16, align = 'A')
                                            pdf.cell(200, 10, txt =Countrys, ln = 17, align = 'A')
                                            pdf.cell(200, 10, txt =b_code, ln = 18, align = 'A')
                                            pdf.cell(200, 10, txt =expirys, ln = 19, align = 'A')
                                            pdf.cell(200, 10, txt =current_bal, ln = 20, align = 'A')
                                            pdf.cell(200, 10, txt ="-------------------------------------------------------------------------", ln = 21, align = 'A')
                                            pdf.cell(200,10,txt="Please Do Not Share This File With Anyone",ln=22,align="A")
                                            pdf.output(loginid+".pdf")
                                            from PyPDF2 import PdfFileWriter, PdfFileReader
                                            out = PdfFileWriter()
                                            pdf_f=str(loginid)+".pdf"
                                            file = PdfFileReader(pdf_f)
                                            num = file.numPages
                                            for idx in range(num):
                                                page = file.getPage(idx)
                                                out.addPage(page)
                                            password =Password_file
                                            out.encrypt(password)
                                            l=Label(q,text="Account Details",bg='white',font="LUCIDA 15 bold").pack(padx=0,pady=0)
                                            l=Label(q,text=logsid,bg='white',fg='red',font="LUCIDA 15 bold").place(x=600,y=70)
                                            l=Label(q,text=name,bg='white',font="LUCIDA 15 bold").place(x=100,y=70)
                                            l=Label(q,text=fna,bg='white',font='LUCIDA 15 bold').place(x=100,y=120)
                                            l=Label(q,text=mna,bg='white',font='LUCIDA 15 bold').place(x=100,y=170)
                                            l=Label(q,text=phn,bg='white',font='LUCIDA 15 bold').place(x=100,y=220)
                                            l=Label(q,text=ema,bg='white',font='LUCIDA 15 bold').place(x=100,y=270)
                                            l=Label(q,text=Addr,bg='white',font='LUCIDA 15 bold').place(x=100,y=320)
                                            l=Label(q,text=Gen,bg='white',font='LUCIDA 15 bold').place(x=100,y=370)
                                            l=Label(q,text=dobs,bg='white',font='LUCIDA 15 bold').place(x=100,y=420)
                                            l=Label(q,text=Accountnum,bg='white',font='LUCIDA 15 bold').place(x=100,y=470)
                                            l=Label(q,text=cardnum,bg='white',font='LUCIDA 15 bold').place(x=100,y=520)
                                            l=Label(q,text=ifsccode,bg='white',font='LUCIDA 15 bold').place(x=100,y=570)
                                            l=Label(q,text=cvvs,bg='white',font='LUCIDA 15 bold').place(x=100,y=620)
                                            l=Label(q,text=Citys,bg='white',font='LUCIDA 15 bold').place(x=100,y=670)
                                            l=Label(q,text=Countrys,bg='white',font='LUCIDA 15 bold').place(x=100,y=720)
                                            l=Label(q,text=b_code,bg='white',font='LUCIDA 15 bold').place(x=100,y=770)
                                            l=Label(q,text=current_bal,bg='white',font='LUCIDA 15 bold').place(x=100,y=820)
                                            l=Label(q,text=expirys,bg='white',font='LUCIDA 15 bold').place(x=100,y=870)
                                            l=Label(q,text="Now You Can Login To Your Account",bg='white',fg='red',font='LUCIDA 15 bold').place(x=1200,y=500)
                                            import smtplib
                                            import imghdr
                                            from email.message import EmailMessage
                                            Sender_Email = "codeinterest27@gmail.com"
                                            Reciever_Email = [Email]
                                            Password = "sodjxrgmbrlghznu"
                                            newMessage = EmailMessage()
                                            newMessage['Subject'] = "Successfully Account Created !!"
                                            newMessage['From'] = Sender_Email
                                            newMessage['To'] = Reciever_Email
                                            newMessage.set_content("""Hello """+Name+""",

Thank You For Creating Bank Account In Our Bank
We Have Attached a File Below Mentioning About Your Account Details

Thank You
Team Shivam

Please Do Not Share This Code With anybody.
This Is Your Secret Code.
Do Not Reply to this Email
For any Complaints contact us at
Mail - codeinterest27@gmail.com
Phone - +918799523738""")
                                            pdf_file=str(loginid)+".pdf"
                                            files = [pdf_file]
                                            for file in files:
                                                with open(file, 'rb') as f:
                                                    file_data = f.read()
                                                    file_name = f.name
                                                    newMessage.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
                                                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp4:
                                                    smtp4.login(Sender_Email, Password)
                                                    smtp4.send_message(newMessage)
                                            import shutil
                                            #source=r"C:\\Users\\Asus\\OneDrive\\Desktop\\BMS\\"+pdf_file
                                            #dest=r"C:\\Users\\Asus\\OneDrive\\Desktop\\BMS\\Accounts\\"+pdf_file
                                            #shutil.move(source,dest)
                                            def screenshot():
                                                s=pyautogui.screenshot()
                                                s.save(str(loginid)+'.png')
                                            def logs():
                                                q.destroy()
                                            b=Button(q,text='Take Screenshot',command=screenshot,bg='white',borderwidth=3,relief='solid',activeforeground='red',activebackground='white',font='LUCIDA 15 bold').place(x=1000,y=700)
                                            b=Button(q,text='Go To Login Page',command=logs,bg='white',borderwidth=3,relief='solid',activeforeground='red',activebackground='white',font='LUCIDA 15 bold').place(x=1300,y=700)
                                        if final_code==w_final:
                                            loginid=str(Name[0:3]).lower()+str(account_num)
                                            democursor.execute("insert into email_l values('"+str(account_num)+"','"+str(Email)+"','Not Verified')")
                                            demodb.commit()
                                            lastp(final_expiry,loginid,str(Name),str(Father),str(Mother),str(Phone),str(Email),str(Address),str(Gender),str(pasc),str(new_pas1),str(birthdate),str(Account_Created),str(account_num),str(card_num),str(ifsc_code),str(cvv),str(City),str(Country),str(branch_code),str(Pan),str(Aadhar),str(Passport),str(Voter),str(Occupation),str(Organization),str(Income),str(Net_Worth),str(Qualification))
                                            democursor.execute("update email_l set status='Verified' where acc_no='"+account_num+"'")
                                            demodb.commit()
                                            end2()
                                        else :
                                            l=Label(n,text="Code Doesn't Match",bg='white',fg='red',font='LUCIDA 15 bold').place(x=1100,y=700)
                                    b=Button(r,text="Verify",command=end1,bg='white',borderwidth=3,relief='solid',activeforeground='red',activebackground='white',font='LUCIDA 15 bold').place(x=1000,y=700)
                                    
                                if vale==0 or valu==0:
                                    ending()
                                    #print(str(Name),str(Father),str(Mother),str(Phone),str(Email),str(Address),str(Gender),str(pasc),str(new_pas1),str(birthdate)
                                    #,str(Account_Created),str(account_num),str(card_num),str(ifsc_code),str(cvv),str(City),str(Country),str(branch_code),str(Pan)
                                    #,str(Aadhar),str(Passport),str(Voter),str(Occupation),str(Organization),str(Income),str(Net_Worth),str(Qualification))
                                    
                                else:
                                    valp=0
                            b=Button(n,text="Next",command=last,borderwidth=3,relief='solid',activeforeground='red',activebackground='white',bg='white',font='LUCIDA 15 bold').place(x=1000,y=700)
                        else:
                            l=Label(p,text="Passwords is Too Short",bg='white',fg='red',font='LUCIDA 15 bold').place(x=1100,y=700)
                    else:
                        l=Label(p,text="Passwords Doesn't Match",bg='white',fg='red',font='LUCIDA 15 bold').place(x=1100,y=700)
                b=Button(p,text="Next",command=passcode,borderwidth=3,relief='solid',activeforeground='red',activebackground='white',bg='white',font='LUCIDA 15 bold').place(x=1000,y=700)
            if '@gmail' not in Email:
                l=Label(b1,text='Please Enter Valid Mail',bg='white',fg='red',font='LUCIDA 15 bold').place(x=500,y=800)
            else:
                passc()
            #democursor=demodb.cursor()
            #democursor.execute("insert into users values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",())
            
    b=Button(b1,text='Create Account',bg='white',command=check_blank,borderwidth=3,activebackground='white',activeforeground='red',relief='solid',font='LUCIDA 15 bold').place(x=1400,y=800)
    ###############################################################################
    #NEW WIN
def login(log,pasw):             #Login Function
    if log=='' or log==' ' or pasw=='' or pasw==' ':    #Checking Null for Input
        l=Label(y,text='Please Enter Details!!',bg='thistle3',fg='red',font='LUCIDA 15 bold').place(x=1250,y=410)
    else:
        democursor=demodb.cursor()
        democursor.execute("select password from user03 where userid='"+log+"'")
        for i in democursor:
            a=i[0]
            if a==pasw: #Checking for Correct Password
                #l=Label(y,text="                                                    ",bg='thistle3',font="LUCIDA 15 bold").place(x=1250,y=410)
                c=Tk()  #Making New Window for Login Page
                #passw.set('sasoni')
                #logid.set('ss')
                #y.destroy()
                c.title("User Login")
                c.attributes('-fullscreen', True)
                c.configure(bg="white")
                c.iconbitmap('Py_ICO.ico')
                pyautogui.press("Alt+Tab")
                democursor=demodb.cursor()
                democursor.execute("select acc_no from user03 where userid='"+log+"'")
                for i in democursor:
                    cd=i[0]
                    import random
                    import socket   
                    comp = socket.gethostname()   
                    ip = socket.gethostbyname(comp)
                    now = datetime.now()
                    cue = now.strftime("%H:%M:%S")
                    from datetime import date
                    today1=date.today()
                    today2= str(today1)
                    democursor.execute("select count(*) from user_log"+cd)
                    for i in democursor:
                        numbers=i[0]
                        n1=int(numbers)
                        y=n1+1
                        y11=str(y)
                    democursor.execute("insert into user_log"+cd+" values('"+today2+"','"+cue+"','"+cd+"','"+y11+"')")
                    demodb.commit()     #Inserting User Log
                    import random
                    democursor.execute("select * from users where acc_no="+cd)
                    for i in democursor:
                        name1= i[0]
                        father1= i[1]
                        mother1= i[2]
                        phone1= i[3]
                        email1= i[4]
                        address1= i[5]
                        gender1= i[6]
                        bday1= i[9]
                        acc_cr1= i[10]
                        acc_nu1= i[11]
                        card1= i[12]
                        ifsc1= i[13]
                        card_exp1= i[15]
                        branch1= i[18]
                        pan_no1= i[19]
                        aadh1= i[20]
                        occ1= i[23]
                        inc1= i[25]
                        net1= i[26]
                        quali1=i[27]
                    pss=str(name1)
                    num=len(acc_nu1)
                    accc=acc_nu1[num-4:num+1]
                    #ipss1=get("https://api.ipify.org").text
                    l=Label(c,text='Welcome '+name1+',',bg='white',font="LUCIDA 15 bold").pack(padx=0,pady=0)
                    #get_data(c)
                    #democursor=demodb.cursor()
###############################################################################
                    f='''import smtplib
                    from email.message import EmailMessage
                    Sender_Email = "codeinterest27@gmail.com"
                    Reciever_Email = [email1]
                    Password = "sodjxrgmbrlghznu"
                    newMessage = EmailMessage()
                    newMessage['Subject'] = "Login Activity in Your Account Ending with "+cd
                    newMessage['From'] = Sender_Email
                    newMessage['To'] = Reciever_Email
                    newMessage.set_content("""Hello """+name1+""",
Someone Has Logged In in your account ending with \nAccount Number : XXXX-XXXX-XXXX-"""+cd+"""

Time : """+cue+"""
Date : """+today2+"""
Computer : """+comp+"""
IP Address : """+ip+"""
Public IP Address : """+ipss1+"""

If You haven't logged in please open Bank Website and Take Necessary Action


Do Not Reply to this Email
For any Complaints contact us at
Mail - python39.programming@gmail.com
Phone - +918799523738""")
                    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp3:
                        smtp3.login(Sender_Email, Password)
                        smtp3.send_message(newMessage)#'''
###############################################################################
                    democursor.execute("select count(*) from user_log"+cd)
                    for i in democursor:
                        a=i[0]
                        if a==0 or a==1:
                            first_login=0
                        else:
                            first_login=1
                        b=a-1
                        c11=str(b)
                    democursor.execute("select * from user_log"+cd+" where num='"+c11+"'")
                    for i in democursor:
                        date_ll=i[0]
                        time_ll=i[1]
                    democursor.execute("select count(*) from bal_"+cd)
                    for i in democursor:
                        lenght_cbal=int(i[0])
                    democursor.execute("Select * from Bal_"+cd+" where number='"+str(lenght_cbal)+"'")
                    for i in democursor:
                        curr_bal=i[1]
                        date_l_b=i[0]
                        f_curr_bal=float(curr_bal)
                        new_bal=f_curr_bal
                        new_f=str(new_bal)
                    democursor.execute("select Status,email_id from email_l where acc_no='"+cd+"'")
                    for i in democursor:
                        status_em=i[0]
                        Email=i[1]
                    def verify_email():
                        r=Tk()
                        r.title("Confirm Email")
                        r.attributes('-fullscreen', True)
                        r.configure(bg='white')
                        r.iconbitmap('Py_ICO.ico')
                        em12=str(Email)
                        first_n=Email[1:-10]
                        ekfk=len(first_n)
                        ejjj=ekfk*'*'
                        final_emid=em12.replace(first_n,ejjj)
                        import random
                        list1=['S','H','I','V','A','M']
                        w_1=random.choice(list1)
                        w_2=str(random.randint(111111,999999))
                        w_final=w_1+w_2
                        text1="Verify Email"
                        text2="A Code Has Been Sent to "+final_emid+" Please Enter That Code Below - "
                        b=Label(r,text=text1,bg='white',font="LUCIDA 15 bold").pack(padx=0,pady=0)
                        b=Label(r,text=text2,fg='red',bg='white',font="LUCIDA 15 bold").pack(padx=0,pady=0)
                        import smtplib
                        from email.message import EmailMessage
                        Sender_Email = "codeinterest27@gmail.com"
                        Reciever_Email = [Email]
                        Password = "sodjxrgmbrlghznu"
                        newMessage = EmailMessage()
                        newMessage['Subject'] = "Secret Code To Verify Email ID for Account : "+cd
                        newMessage['From'] = Sender_Email
                        newMessage['To'] = Reciever_Email
                        newMessage.set_content("""Hello """+name1+""",
This is Your Secret Code :


            """+w_1+"""-"""+w_2+"""
            

Please Do Not Share This Code With anybody.
This Is Your Secret Code.
Do Not Reply to this Email
For any Complaints contact us at
Mail - codeinterest27@gmail.com
Phone - +918799523738""")
                        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp3:
                            smtp3.login(Sender_Email, Password)
                            smtp3.send_message(newMessage)#'''
                        f_let=StringVar(r)
                        f_let.set('↓')
                        om=OptionMenu(r,f_let,*list1).place(x=700,y=300)
                        codes=StringVar(r)
                        e=Entry(r,textvariable=codes,borderwidth=3,relief='solid',bg='white',font='LUCIDA 15 bold').place(x=850,y=300)
                        def end1():
                            first_letter=f_let.get()
                            code_last=codes.get()
                            final_code=str(first_letter)+str(code_last)
                            if final_code==w_final:
                                democursor.execute("Update email_l set Status='Verified' where acc_no='"+cd+"'")
                        b=Button(r,text="Verify",command=end1,bg='white',borderwidth=3,relief='solid',activeforeground='red',activebackground='white',font='LUCIDA 15 bold').place(x=1000,y=700)
                    if status_em=="Not Verified":
                        verify_email()
                    else:
                        abc=1
                    def win_cl():
                        c.destroy()
                    democursor.execute("Select * from Bal_"+cd+" where number='"+str(lenght_cbal)+"'")
                    for i in democursor:
                        curr_bal=i[1]
                        date_l_b=i[0]
                        f_curr_bal=float(curr_bal)
                        new_bal=f_curr_bal
                        new_f=str(new_bal)
                    b=Button(c,text='< Back To Login',borderwidth=0,relief='solid',activebackground='red',command=win_cl,bg='white',font='LUCIDA 10').place(x=10,y=10)
                    l=Label(c,text="Current Balance : "+new_f+" Cr.",fg='red',bg='white',font="LUCIDA 15 bold").place(x=800,y=86)
                    #l=Label(c,text='Cr.',fg='green',bg='white',font='LUCIDA 15 bold').place(x=1110,y=36)
                    if first_login==1:
                        l=Label(c,text='Last Login on '+date_ll+', '+time_ll,fg='red',bg='white',font="LUCIDA 15 bold").pack(padx=0,pady=0)
                    else:
                        l=Label(c,text="This Is Your First Login",fg='red',bg='white',font="LUCIDA 15 bold").pack(padx=0,pady=0)
                    #photo2=PhotoImage(file=r'FT.png')
                    def acc():
                        s=Tk()
                        s.title("Accounts")
                        s.attributes('-fullscreen', True)
                        s.configure(bg='white')
                        s.iconbitmap('Py_ICO.ico')
                        pyautogui.press("Alt+Tab")
                        def win_clo():
                            s.destroy()
                        b=Button(s,text='< Back To Main',borderwidth=0,relief='solid',activebackground='red',command=win_clo,bg='white',font='LUCIDA 10').place(x=10,y=10)
                        l=Label(s,text=name1,bg='white',font="LUCIDA 25 bold").pack(padx=0,pady=0)
                        b=Button(s,text="Mini Statements",borderwidth=3,relief='solid',activebackground='red',command=None,bg='white',font='LUCIDA 20').place(x=1400,y=100)
                    def ft():
                        t=Tk()
                        democursor.execute("select count(*) from bal_"+cd)
                        for i in democursor:
                            len_bal=int(i[0])
                        democursor.execute("Select current_bal from bal_"+cd+" where number='"+str(len_bal)+"'")
                        for i in democursor:
                            curr_bal_ft=float(i[0])
                        t.title("Fund Transfer")
                        t.attributes('-fullscreen', True)
                        t.configure(bg='white')
                        t.iconbitmap('Py_ICO.ico')
                        pyautogui.press("Alt+Tab")
                        def win_clo():
                            t.destroy()
                        to_ac=StringVar(t)
                        amt=StringVar(t)
                        remarks=StringVar(t)
                        from_ac=StringVar(t)
                        name_to=StringVar(t)
                        def clearamt():
                            to_ac.set('')
                            amt.set('')
                            remarks.set('')
                            from_ac.set('')
                            name_to.set('')
                        l=Label(t,text="To Account Number : ",bg='white',font='LUCIDA 15 bold').place(x=100,y=100)
                        l=Label(t,text="Amount : ",bg='white',font='LUCIDA 15 bold').place(x=100,y=200)
                        l=Label(t,text="Remarks : ",bg='white',font='LUCIDA 15 bold').place(x=100,y=300)
                        l=Label(t,text="From Account Number : ",bg='white',font='LUCIDA 15 bold').place(x=100,y=400)
                        L=Label(t,text="To Name : ",bg='white',font='LUCIDA 15 bold').place(x=100,y=500)
                        e=Entry(t,textvariable=to_ac,borderwidth=3,relief='solid',bg='white',font='LUCIDA 15 bold').place(x=500,y=100)
                        e=Entry(t,textvariable=amt,borderwidth=3,relief='solid',bg='white',font='LUCIDA 15 bold').place(x=500,y=200)
                        e=Entry(t,textvariable=remarks,borderwidth=3,relief='solid',bg='white',font='LUCIDA 15 bold').place(x=500,y=300)
                        e=Entry(t,textvariable=from_ac,borderwidth=3,relief='solid',bg='white',font='LUCIDA 15 bold').place(x=500,y=400)
                        e=Entry(t,textvariable=name_to,borderwidth=3,relief='solid',bg='white',font='LUCIDA 15 bold').place(x=500,y=500)
                        b=Button(t,text='< Back To Main',borderwidth=0,relief='solid',activebackground='red',command=win_clo,bg='white',font='LUCIDA 10').place(x=10,y=10)
                        l=Button(t,text='',height=10,activeforeground='thistle3',bg='thistle3',fg='white',activebackground='thistle3',relief='solid',borderwidth=3,command=clearamt,width=40,font='LUCIDA 15 bold').place(x=1150,y=110)
                        l=Button(t,text='',height=9,activeforeground='white',bg='thistle3',fg='white',activebackground='thistle3',relief='solid',borderwidth=3,command=None,width=40,font='LUCIDA 15 bold').place(x=1150,y=610)
                        l=Label(t,text="Current Balance : ",bg='thistle3',font="LUCIDA 20 bold").place(x=1300,y=650)
                        l=Label(t,text=str(curr_bal_ft)+" Cr.",fg='green',bg='thistle3',font="LUCIDA 25 bold").place(x=1340,y=750)
                        democursor.execute("select count(*) from trans_"+cd)
                        for i in democursor:
                            num_trans=int(i[0])
                        if num_trans==0:
                            l=Label(t,text="No Recent Transactions",bg='thistle3',fg='red',font="LUCIDA 20 bold").place(x=1275,y=150)
                        else:
                            l=Button(t,text=" To",activeforeground='black',bg='thistle3',fg='black',activebackground='thistle3',borderwidth=0,command=clearamt,font="LUCIDA 17 bold").place(x=1170,y=120)
                            l=Button(t,text="  Amount",activeforeground='black',bg='thistle3',fg='black',activebackground='thistle3',borderwidth=0,command=clearamt,font="LUCIDA 17 bold").place(x=1270,y=120)
                            l=Button(t,text="    Date",activeforeground='black',bg='thistle3',fg='black',activebackground='thistle3',borderwidth=0,command=clearamt,font="LUCIDA 17 bold").place(x=1420,y=120)
                            l=Button(t,text="      Time",activeforeground='black',bg='thistle3',fg='black',activebackground='thistle3',borderwidth=0,command=clearamt,font="LUCIDA 17 bold").place(x=1570,y=120)
                            if num_trans==1:
                                democursor.execute("select to_acc,amt,date,date_time,remarks,to_name from trans_"+cd+" where num=1")
                                for i in democursor:
                                    to_ac1=i[0]
                                    amout=i[1]
                                    rema=i[4]
                                    tarikh=i[2]
                                    date_samay=i[3]
                                    namest=i[5]
                                def setamt():
                                    to_ac.set(to_ac1)
                                    amt.set(amout)
                                    remarks.set(rema)
                                    from_ac.set(cd)
                                    name_to.set(namest)
                                l=Button(t,text=to_ac1+"     Rs."+amout+"      "+tarikh+"    "+date_samay,activeforeground='green',bg='thistle3',fg='green',activebackground='thistle3',borderwidth=0,command=setamt,font="LUCIDA 16 bold").place(x=1170,y=160)
                            elif num_trans==2:
                                democursor.execute("select to_acc,amt,date,date_time,remarks,to_name from trans_"+cd+" where num=2")
                                for i in democursor:
                                    to_ac2=i[0]
                                    amout2=i[1]
                                    rema2=i[4]
                                    tarikh2=i[2]
                                    date_samay2=i[3]
                                    namest2=i[5]
                                def setamt():
                                    to_ac.set(to_ac2)
                                    amt.set(amout2)
                                    remarks.set(rema2)
                                    from_ac.set(cd)
                                    name_to.set(namest2)
                                democursor.execute("select to_acc,amt,date,date_time,remarks,to_name from trans_"+cd+" where num=1")
                                l=Button(t,text=to_ac2+"     Rs."+amout2+"      "+tarikh2+"    "+date_samay2,activeforeground='green',bg='thistle3',fg='green',activebackground='thistle3',borderwidth=0,command=setamt,font="LUCIDA 16 bold").place(x=1170,y=160)
                                for i in democursor:
                                    to_ac1=i[0]
                                    amout=i[1]
                                    rema=i[4]
                                    tarikh=i[2]
                                    date_samay=i[3]
                                    namest=i[5]
                                def setamt():
                                    to_ac.set(to_ac1)
                                    amt.set(amout)
                                    remarks.set(rema)
                                    from_ac.set(cd)
                                    name_to.set(namest)
                                l=Button(t,text=to_ac1+"     Rs."+amout+"      "+tarikh+"    "+date_samay,activeforeground='green',bg='thistle3',fg='green',activebackground='thistle3',borderwidth=0,command=setamt,font="LUCIDA 16 bold").place(x=1170,y=200)
                            elif num_trans==3:
                                democursor.execute("select to_acc,amt,date,date_time,remarks,to_name from trans_"+cd+" where num=3")
                                for i in democursor:
                                    to_ac3=i[0]
                                    amout3=i[1]
                                    rema3=i[4]
                                    tarikh3=i[2]
                                    date_samay3=i[3]
                                    namest3=i[5]
                                def setamt():
                                    to_ac.set(to_ac3)
                                    amt.set(amout3)
                                    remarks.set(rema3)
                                    from_ac.set(cd)
                                    name_to.set(namest3)
                                l=Button(t,text=to_ac3+"     Rs."+amout3+"      "+tarikh3+"    "+date_samay3,activeforeground='green',bg='thistle3',fg='green',activebackground='thistle3',borderwidth=0,command=setamt,font="LUCIDA 16 bold").place(x=1170,y=160)
                                democursor.execute("select to_acc,amt,date,date_time,remarks,to_name from trans_"+cd+" where num=2")
                                for i in democursor:
                                    to_ac2=i[0]
                                    amout2=i[1]
                                    rema2=i[4]
                                    tarikh2=i[2]
                                    date_samay2=i[3]
                                    namest2=i[5]
                                def setamt():
                                    to_ac.set(to_ac2)
                                    amt.set(amout2)
                                    remarks.set(rema2)
                                    from_ac.set(cd)
                                    name_to.set(namest2)
                                democursor.execute("select to_acc,amt,date,date_time,remarks,to_name from trans_"+cd+" where num=1")
                                l=Button(t,text=to_ac2+"     Rs."+amout2+"      "+tarikh2+"    "+date_samay2,activeforeground='green',bg='thistle3',fg='green',activebackground='thistle3',borderwidth=0,command=setamt,font="LUCIDA 16 bold").place(x=1170,y=200)
                                for i in democursor:
                                    to_ac1=i[0]
                                    amout=i[1]
                                    rema=i[4]
                                    tarikh=i[2]
                                    date_samay=i[3]
                                    namest=i[5]
                                def setamt():
                                    to_ac.set(to_ac1)
                                    amt.set(amout)
                                    remarks.set(rema)
                                    from_ac.set(cd)
                                    name_to.set(namest)
                                l=Button(t,text=to_ac1+"     Rs."+amout+"      "+tarikh+"    "+date_samay,activeforeground='green',bg='thistle3',fg='green',activebackground='thistle3',borderwidth=0,command=setamt,font="LUCIDA 16 bold").place(x=1170,y=240)
                            else:
                                democursor.execute("select to_acc,amt,date,date_time,remarks,to_name from trans_"+cd+" where num="+str(num_trans))
                                for i in democursor:
                                    to_ac4=i[0]
                                    amout4=i[1]
                                    rema4=i[4]
                                    tarikh4=i[2]
                                    date_samay4=i[3]
                                    namest4=i[5]
                                def setamt():
                                    to_ac.set(to_ac4)
                                    amt.set(amout4)
                                    remarks.set(rema4)
                                    from_ac.set(cd)
                                    name_to.set(namest4)
                                l=Button(t,text=to_ac4+"     Rs."+amout4+"      "+tarikh4+"    "+date_samay4,activeforeground='green',bg='thistle3',fg='green',activebackground='thistle3',borderwidth=0,command=setamt,font="LUCIDA 16 bold").place(x=1170,y=180)
                                democursor.execute("select to_acc,amt,date,date_time,remarks,to_name from trans_"+cd+" where num="+str(num_trans-1))
                                for i in democursor:
                                    to_ac3=i[0]
                                    amout3=i[1]
                                    rema3=i[4]
                                    tarikh3=i[2]
                                    date_samay3=i[3]
                                    namest3=i[5]
                                def setamt():
                                    to_ac.set(to_ac3)
                                    amt.set(amout3)
                                    remarks.set(rema3)
                                    from_ac.set(cd)
                                    name_to.set(namest3)
                                l=Button(t,text=to_ac3+"     Rs."+amout3+"      "+tarikh3+"    "+date_samay3,activeforeground='green',bg='thistle3',fg='green',activebackground='thistle3',borderwidth=0,command=setamt,font="LUCIDA 16 bold").place(x=1170,y=240)
                                democursor.execute("select to_acc,amt,date,date_time,remarks,to_name from trans_"+cd+" where num="+str(num_trans-2))
                                for i in democursor:
                                    to_ac2=i[0]
                                    amout2=i[1]
                                    rema2=i[4]
                                    tarikh2=i[2]
                                    date_samay2=i[3]
                                    namest2=i[5]
                                def setamt():
                                    to_ac.set(to_ac2)
                                    amt.set(amout2)
                                    remarks.set(rema2)
                                    from_ac.set(cd)
                                    name_to.set(namest2)
                                democursor.execute("select to_acc,amt,date,date_time,remarks,to_name from trans_"+cd+" where num="+str(num_trans-3))
                                l=Button(t,text=to_ac2+"     Rs."+amout2+"      "+tarikh2+"    "+date_samay2,activeforeground='green',bg='thistle3',fg='green',activebackground='thistle3',borderwidth=0,command=setamt,font="LUCIDA 16 bold").place(x=1170,y=300)
                                for i in democursor:
                                    to_ac1=i[0]
                                    amout=i[1]
                                    rema=i[4]
                                    tarikh=i[2]
                                    date_samay=i[3]
                                    namest=i[5]
                                def setamt():
                                    to_ac.set(to_ac1)
                                    amt.set(amout)
                                    remarks.set(rema)
                                    from_ac.set(cd)
                                    name_to.set(namest)
                                l=Button(t,text=to_ac1+"     Rs."+amout+"      "+tarikh+"    "+date_samay,activeforeground='green',bg='thistle3',fg='green',activebackground='thistle3',borderwidth=0,command=setamt,font="LUCIDA 16 bold").place(x=1170,y=360)
                        def proceed():
                            to_ac1=to_ac.get()
                            amt1=float(amt.get())
                            remarks1=remarks.get()
                            amt_val=0
                            try:
                                int(amt1)
                            except:
                                amt_val=1
                            from_ac1=from_ac.get()
                            name_to1=name_to.get()
                            value1=0
                            democursor.execute("select acc_no from users")
                            for i in democursor:
                                for j in range(len(i)):
                                    if to_ac1==i[j]:
                                        value1+=1
                            democursor.execute("select count(*) from bal_"+cd)
                            for i in democursor:
                                lengths_cbal=int(i[0])
                            democursor.execute("Select current_bal from bal_"+cd+" where number='"+str(lengths_cbal)+"'")
                            for i in democursor:
                                cbal_cur=float(i[0])
                            if to_ac1=="" or amt1=="" or remarks1=="" or from_ac1=="" or name_to1=="" or to_ac1==" " or amt1==" " or remarks1==" " or from_ac1==" " or name_to1==" " or amt_val==1:
                                l=Label(t,text="                                                   ",bg='white',fg='red',font="LUCIDA 15").place(x=100,y=900)
                                l=Label(t,text="Please Enter Valid Details                   ",bg='white',fg='red',font="LUCIDA 15").place(x=100,y=900)
                            elif value1==0:
                                l=Label(t,text="                                                   ",bg='white',fg='red',font="LUCIDA 15").place(x=100,y=900)
                                l=Label(t,text="Please Enter Valid Account Number          ",bg='white',fg='red',font="LUCIDA 15").place(x=100,y=900)
                            elif from_ac1==to_ac1:
                                l=Label(t,text="                                                   ",bg='white',fg='red',font="LUCIDA 15").place(x=100,y=900)
                                l=Label(t,text="Both Account Number Should Not Be Same!",bg='white',fg='red',font="LUCIDA 15").place(x=100,y=900)
                            elif from_ac1!=cd:
                                l=Label(t,text="                                                   ",bg='white',fg='red',font="LUCIDA 15").place(x=100,y=900)
                                l=Label(t,text="Please Enter Your Account Number Correctly",bg='white',fg='red',font="LUCIDA 15").place(x=100,y=900)
                            elif cbal_cur<amt1:
                                l=Label(t,text="                                                   ",bg='white',fg='red',font="LUCIDA 15").place(x=100,y=900)
                                l=Label(t,text="   Please Enter Valid Amount                        ",bg='white',fg='red',font="LUCIDA 15").place(x=100,y=900)
                            else:
                                o=Tk()
                                o.geometry("900x200")
                                o.configure(bg='white')
                                o.title("Terms & Conditions")
                                o.iconbitmap('Py_ICO.ico')
                                tick=IntVar(o)
                                def transfer():
                                    final_amt_aft_tra=cbal_cur-amt1
                                    democursor.execute("select count(*) from bal_"+to_ac1)
                                    for i in democursor:
                                        len_opp_acc_no=int(i[0])
                                    opp_acc_bal1=0
                                    democursor.execute("select current_bal from bal_"+to_ac1+" where number="+str(len_opp_acc_no))
                                    for j in democursor:
                                        opp_acc_bal1+=float(j[0])
                                        new_opp_ac=opp_acc_bal1
                                    opp_bal_aft_tra=opp_acc_bal1+amt1
                                    from datetime import date
                                    tra_today=date.today()
                                    democursor.execute("insert into bal_"+cd+" values(%s,%s,%s)",(tra_today,str(final_amt_aft_tra),lengths_cbal+1))
                                    demodb.commit()
                                    democursor.execute("insert into bal_"+to_ac1+" values(%s,%s,%s)",(tra_today,str(opp_bal_aft_tra),len_opp_acc_no+1))
                                    demodb.commit()
                                    democursor.execute("select count(*) from trans_"+cd)
                                    for i in democursor:
                                        num_tran_st=int(i[0])+1
                                    now1 = datetime.now()
                                    cue1 = now1.strftime("%H:%M:%S")
                                    democursor.execute("insert into trans_"+cd+" values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(name1,from_ac1,to_ac1,str(amt1),str(final_amt_aft_tra),name_to1,str(num_tran_st),cue1,tra_today,remarks1))
                                    demodb.commit()
                                    l=Label(c,text="Current Balance : "+str(final_amt_aft_tra)+" Cr.     ",fg='red',bg='white',font="LUCIDA 15 bold").place(x=800,y=86)
                                    o.destroy()
                                    t.destroy()
                                    o1=Tk()
                                    o1.geometry("900x200")
                                    o1.configure(bg='white')
                                    o1.title("Transaction Status")
                                    o1.iconbitmap('Py_ICO.ico')
                                    b=Label(o1,text="Yay! Your Transaction of Rs."+str(amt1)+" was Successfull!",bg='white',activebackground='white',font="LUCIDA 15").pack(padx=0,pady=0)
                                    from fpdf import FPDF
                                    pdf = FPDF()
                                    pdf.add_page()
                                    pdf.set_font("Arial",size=25)
                                    pdf.cell(200, 10, txt = cd,ln=1,align='C')
                                    pdf.cell(200, 10, txt = "-----------------------------------------------------------------------", ln = 2, align = 'A')
                                    pdf.cell(200, 10, txt ="From Account Number : "+str(cd), ln = 3, align = 'A')
                                    pdf.cell(200,10,txt="To Account Number : "+str(to_ac1),ln=4,align='A')
                                    pdf.cell(200,10,txt="Amount : "+str(amt1),ln=5,align="A")
                                    pdf.cell(200,10,txt="To : "+str(name_to1),ln=6,align="A")
                                    pdf.cell(200,10,txt="Time : "+str(cue1),ln=7,align="A")
                                    pdf.cell(200,10,txt="Date : "+str(tra_today),ln=8,align="A")
                                    pdf.cell(200,10,txt="Amount Before Transaction : "+str(cbal_cur),ln=9,align="A")
                                    pdf.cell(200,10,txt="Amount After Transaction : "+str(final_amt_aft_tra),ln=10,align="A")
                                    pdf.cell(200,10,txt="Transaction Status : Successful",ln=11,align="A")
                                    pdf.cell(200,10,txt='',ln=12,align="A")
                                    pdf.cell(200,10,txt='',ln=13,align="A")
                                    pdf.cell(200,10,txt='',ln=14,align="A")
                                    pdf.cell(200,10,txt='',ln=15,align="A")
                                    pdf.cell(200,10,txt="Thank You",ln=16,align="A")
                                    pdf.cell(200,10,txt="Team BMS",ln=17,align="A")
                                    pdf.cell(200, 10, txt ="-------------------------------------------------------------------------", ln = 21, align = 'A')
                                    pdf.cell(200,10,txt="Please Do Not Share This File With Anyone",ln=22,align="A")
                                    pdf.output(cd+"_Debited"+str(lengths_cbal+1)+".pdf")
                                    pdf = FPDF()
                                    pdf.add_page()
                                    pdf.set_font("Arial",size=25)
                                    pdf.cell(200, 10, txt = to_ac1,ln=1,align='C')
                                    pdf.cell(200, 10, txt = "-----------------------------------------------------------------------", ln = 2, align = 'A')
                                    pdf.cell(200, 10, txt ="From Account Number : "+str(cd), ln = 3, align = 'A')
                                    pdf.cell(200,10,txt="To Account Number : "+str(to_ac1),ln=4,align='A')
                                    pdf.cell(200,10,txt="Amount : "+str(amt1),ln=5,align="A")
                                    pdf.cell(200,10,txt="From : "+str(name1),ln=6,align="A")
                                    pdf.cell(200,10,txt="Time : "+str(cue1),ln=7,align="A")
                                    pdf.cell(200,10,txt="Date : "+str(tra_today),ln=8,align="A")
                                    pdf.cell(200,10,txt="Amount Before Transaction : "+str(opp_acc_bal1),ln=9,align="A")
                                    pdf.cell(200,10,txt="Amount After Transaction : "+str(opp_bal_aft_tra),ln=10,align="A")
                                    pdf.cell(200,10,txt="Transaction Status : Successful",ln=11,align="A")
                                    pdf.cell(200,10,txt='',ln=12,align="A")
                                    pdf.cell(200,10,txt='',ln=13,align="A")
                                    pdf.cell(200,10,txt='',ln=14,align="A")
                                    pdf.cell(200,10,txt='',ln=15,align="A")
                                    pdf.cell(200,10,txt="Thank You",ln=16,align="A")
                                    pdf.cell(200,10,txt="Team BMS",ln=17,align="A")
                                    pdf.cell(200, 10, txt ="-------------------------------------------------------------------------", ln = 21, align = 'A')
                                    pdf.cell(200,10,txt="Please Do Not Share This File With Anyone",ln=22,align="A")
                                    pdf.output(to_ac1+"_Credited"+str(len_opp_acc_no+1)+".pdf")
                                    import smtplib
                                    import imghdr
                                    from email.message import EmailMessage
                                    Sender_Email = "codeinterest27@gmail.com"
                                    Reciever_Email = [email1]
                                    Password = "sodjxrgmbrlghznu"
                                    newMessage = EmailMessage()
                                    newMessage['Subject'] = "Rs."+str(amt1)+" Debited From Your Account "+cd
                                    newMessage['From'] = Sender_Email
                                    newMessage['To'] = Reciever_Email
                                    newMessage.set_content("""Hello """+name1+""",
Rs."""+str(amt1)+""" Debited From Your Account
Transaction Slip Attached Below for Rs."""+str(amt1)+""" to Account Number """+str(to_ac1)+"""
                                    
Thank You
Team Shivam

Please Do Not Share This Code With anybody.
This Is Your Secret Code.
Do Not Reply to this Email
For any Complaints contact us at
Mail - codeinterest27@gmail.com
Phone - +918799523738""")
                                    pdf_file=str(cd)+"_Debited"+str(lengths_cbal+1)+".pdf"
                                    files = [pdf_file]
                                    for file in files:
                                        with open(file, 'rb') as f:
                                            file_data = f.read()
                                            file_name = f.name
                                            newMessage.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
                                        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp4:
                                            smtp4.login(Sender_Email, Password)
                                            smtp4.send_message(newMessage)
                                    democursor.execute("select email from users where acc_no="+to_ac1)
                                    for i in democursor:
                                        email_to_ac=str(i[0])
                                    Sender_Email = "codeinterest27@gmail.com"
                                    Reciever_Email = [email_to_ac]
                                    Password = "sodjxrgmbrlghznu"
                                    newMessage = EmailMessage()
                                    newMessage['Subject'] = "Rs."+str(amt1)+" Credited To Your Account "+to_ac1
                                    newMessage['From'] = Sender_Email
                                    newMessage['To'] = Reciever_Email
                                    newMessage.set_content("""Hello """+name_to1+""",
Rs."""+str(amt1)+""" Credited To Your Account
Transaction Slip Attached Below for Rs."""+str(amt1)+""" From Account Number """+str(cd)+"""
                                    
Thank You
Team Shivam

Please Do Not Share This Code With anybody.
This Is Your Secret Code.
Do Not Reply to this Email
For any Complaints contact us at
Mail - codeinterest27@gmail.com
Phone - +918799523738""")
                                    pdf_file=to_ac1+"_Credited"+str(len_opp_acc_no+1)+".pdf"
                                    files = [pdf_file]
                                    for file in files:
                                        with open(file, 'rb') as f:
                                            file_data = f.read()
                                            file_name = f.name
                                            newMessage.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
                                        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp4:
                                            smtp4.login(Sender_Email, Password)
                                            smtp4.send_message(newMessage)
                                def pas_get():
                                    def pin_4_t():
                                        a=Tk()
                                        a.title("Enter Login Pin")
                                        a.attributes('-fullscreen', True)
                                        a.configure(bg="white")
                                        a.iconbitmap('Py_ICO.ico')
                                        pyautogui.press("Alt+Tab")
                                        def win_cl1():
                                            a.destroy()
                                        b=Button(a,text='< Back To Login',borderwidth=0,relief='solid',activebackground='red',command=win_cl1,bg='white',font='LUCIDA 10').place(x=10,y=10)
                                        democursor=demodb.cursor()
                                        democursor.execute("select acc_no from user03 where userid='"+log+"'")
                                        for i in democursor:
                                            cd=i[0]
                                        democursor.execute("select * from users where acc_no="+cd)
                                        for i in democursor:
                                            name1= i[0]
                                        l=Label(a,text='Welcome '+name1+',',bg='white',font="LUCIDA 15 bold").pack(padx=0,pady=0)
                                        l=Label(a,text='',bg='white',font='LUCIDA 20 bold').pack(padx=0,pady=0)
                                        l=Label(a,text='Enter Transaction PIN : ',bg='white',font='LUCIDA 20 bold').pack(padx=0,pady=0)
                                        p1=StringVar(a)
                                        p2=StringVar(a)
                                        p3=StringVar(a)
                                        p4=StringVar(a)
                                        p1.set('8')
                                        p2.set('8')
                                        p3.set('8')
                                        p4.set('8')
                                        l=Entry(a,textvariable=p1,width=3,show='*',borderwidth=3,relief='solid',font='LUCIDA 15 bold').place(x=800,y=200)
                                        l=Entry(a,textvariable=p2,width=3,show='*',borderwidth=3,relief='solid',font='LUCIDA 15 bold').place(x=880,y=200)
                                        l=Entry(a,textvariable=p3,width=3,show='*',borderwidth=3,relief='solid',font='LUCIDA 15 bold').place(x=960,y=200)
                                        l=Entry(a,textvariable=p4,width=3,show='*',borderwidth=3,relief='solid',font='LUCIDA 15 bold').place(x=1040,y=200)
                                        def clear():
                                            p1.set('')
                                            p2.set('')
                                            p3.set('')
                                            p4.set('')
                                        l=Button(a,text='Clear',command=clear,borderwidth=3,bg='white',activebackground='red',relief='solid',font='LUCIDA 15 bold').place(x=1220,y=200)
                                        def loginf():
                                            d1=p1.get()
                                            d2=p2.get()
                                            d3=p3.get()
                                            d4=p4.get()
                                            d=d1+d2+d3+d4
                                            democursor.execute("select passcode from users where acc_no='"+cd+"'")
                                            for i in democursor:
                                                passcodes=i[0]
                                                if d==passcodes:
                                                    a.destroy()
                                                    transfer()
                                                else:
                                                    clear()
                                                    l=Label(y,text='Incorrect Passcode',fg='red',bg='thistle3',font="LUCIDA 15 bold").place(x=1350,y=410)
                                        
                                        def b1():
                                            d1=p1.get()
                                            d2=p2.get()
                                            d3=p3.get()
                                            d4=p4.get()
                                            if d1=='' or d1==' ':
                                                p1.set('1')
                                            else:
                                                if d2=='' or d2==' ':
                                                    p2.set('1')
                                                else:
                                                    if d3=='' or d3==' ':
                                                        p3.set('1')
                                                    else:
                                                        if d4=='' or d4==' ':
                                                            p4.set('1')
                                                            loginf()
                                                        else:
                                                            loginf()
                                        def b2():
                                            d1=p1.get()
                                            d2=p2.get()
                                            d3=p3.get()
                                            d4=p4.get()
                                            if d1=='' or d1==' ':
                                                p1.set('2')
                                            else:
                                                if d2=='' or d2==' ':
                                                    p2.set('2')
                                                else:
                                                    if d3=='' or d3==' ':
                                                        p3.set('2')
                                                    else:
                                                        if d4=='' or d4==' ':
                                                            p4.set('2')
                                                            loginf()
                                                        else:
                                                            loginf()
                                        def b3():
                                            d1=p1.get()
                                            d2=p2.get()
                                            d3=p3.get()
                                            d4=p4.get()
                                            if d1=='' or d1==' ':
                                                p1.set('3')
                                            else:
                                                if d2=='' or d2==' ':
                                                    p2.set('3')
                                                else:
                                                    if d3=='' or d3==' ':
                                                        p3.set('3')
                                                    else:
                                                        if d4=='' or d4==' ':
                                                            p4.set('3')
                                                            loginf()
                                                        else:
                                                            loginf()
                                        def b4():
                                            d1=p1.get()
                                            d2=p2.get()
                                            d3=p3.get()
                                            d4=p4.get()
                                            if d1=='' or d1==' ':
                                                p1.set('4')
                                            else:
                                                if d2=='' or d2==' ':
                                                    p2.set('4')
                                                else:
                                                    if d3=='' or d3==' ':
                                                        p3.set('4')
                                                    else:
                                                        if d4=='' or d4==' ':
                                                            p4.set('4')
                                                            loginf()
                                                        else:
                                                            loginf()
                                        def b5():
                                            d1=p1.get()
                                            d2=p2.get()
                                            d3=p3.get()
                                            d4=p4.get()
                                            if d1=='' or d1==' ':
                                                p1.set('5')
                                            else:
                                                if d2=='' or d2==' ':
                                                    p2.set('5')
                                                else:
                                                    if d3=='' or d3==' ':
                                                        p3.set('5')
                                                    else:
                                                        if d4=='' or d4==' ':
                                                            p4.set('5')
                                                            loginf()
                                                        else:
                                                            loginf()
                                        def b6():
                                            d1=p1.get()
                                            d2=p2.get()
                                            d3=p3.get()
                                            d4=p4.get()
                                            if d1=='' or d1==' ':
                                                p1.set('6')
                                            else:
                                                if d2=='' or d2==' ':
                                                    p2.set('6')
                                                else:
                                                    if d3=='' or d3==' ':
                                                        p3.set('6')
                                                    else:
                                                        if d4=='' or d4==' ':
                                                            p4.set('6')
                                                            loginf()
                                                        else:
                                                            loginf()
                                        def b7():
                                            d1=p1.get()
                                            d2=p2.get()
                                            d3=p3.get()
                                            d4=p4.get()
                                            if d1=='' or d1==' ':
                                                p1.set('7')
                                            else:
                                                if d2=='' or d2==' ':
                                                    p2.set('7')
                                                else:
                                                    if d3=='' or d3==' ':
                                                        p3.set('7')
                                                    else:
                                                        if d4=='' or d4==' ':
                                                            p4.set('7')
                                                            loginf()
                                                        else:
                                                            loginf()
                                        def b8():
                                            d1=p1.get()
                                            d2=p2.get()
                                            d3=p3.get()
                                            d4=p4.get()
                                            if d1=='' or d1==' ':
                                                p1.set('8')
                                            else:
                                                if d2=='' or d2==' ':
                                                    p2.set('8')
                                                else:
                                                    if d3=='' or d3==' ':
                                                        p3.set('8')
                                                    else:
                                                        if d4=='' or d4==' ':
                                                            p4.set('8')
                                                            loginf()
                                                        else:
                                                            loginf()
                                        def b9():
                                            d1=p1.get()
                                            d2=p2.get()
                                            d3=p3.get()
                                            d4=p4.get()
                                            if d1=='' or d1==' ':
                                                p1.set('9')
                                            else:
                                                if d2=='' or d2==' ':
                                                    p2.set('9')
                                                else:
                                                    if d3=='' or d3==' ':
                                                        p3.set('9')
                                                    else:
                                                        if d4=='' or d4==' ':
                                                            p4.set('9')
                                                            loginf()
                                                        else:
                                                            loginf()
                                        def b0():
                                            d1=p1.get()
                                            d2=p2.get()
                                            d3=p3.get()
                                            d4=p4.get()
                                            if d1=='' or d1==' ':
                                                p1.set('0')
                                            else:
                                                if d2=='' or d2==' ':
                                                    p2.set('0')
                                                else:
                                                    if d3=='' or d3==' ':
                                                        p3.set('0')
                                                    else:
                                                        if d4=='' or d4==' ':
                                                            p4.set('0')
                                                            loginf()
                                                        else:
                                                            loginf()
                                        b=Button(a,text='1',bg='white',width=5,height=3,activebackground='red',relief='solid',command=b1,borderwidth=2,font='LUCIDA 15 bold').place(x=800,y=300)
                                        b=Button(a,text='2',bg='white',width=5,height=3,activebackground='red',relief='solid',command=b2,borderwidth=2,font='LUCIDA 15 bold').place(x=900,y=300)
                                        b=Button(a,text='3',bg='white',width=5,height=3,activebackground='red',relief='solid',command=b3,borderwidth=2,font='LUCIDA 15 bold').place(x=1000,y=300)
                                        b=Button(a,text='4',bg='white',width=5,height=3,activebackground='red',relief='solid',command=b4,borderwidth=2,font='LUCIDA 15 bold').place(x=800,y=450)
                                        b=Button(a,text='5',bg='white',width=5,height=3,activebackground='red',relief='solid',command=b5,borderwidth=2,font='LUCIDA 15 bold').place(x=900,y=450)
                                        b=Button(a,text='6',bg='white',width=5,height=3,activebackground='red',relief='solid',command=b6,borderwidth=2,font='LUCIDA 15 bold').place(x=1000,y=450)
                                        b=Button(a,text='7',bg='white',width=5,height=3,activebackground='red',relief='solid',command=b7,borderwidth=2,font='LUCIDA 15 bold').place(x=800,y=600)
                                        b=Button(a,text='8',bg='white',width=5,height=3,activebackground='red',relief='solid',command=b8,borderwidth=2,font='LUCIDA 15 bold').place(x=900,y=600)
                                        b=Button(a,text='9',bg='white',width=5,height=3,activebackground='red',relief='solid',command=b9,borderwidth=2,font='LUCIDA 15 bold').place(x=1000,y=600)
                                        b=Button(a,text='0',bg='white',width=5,height=3,activebackground='red',relief='solid',command=b0,borderwidth=2,font='LUCIDA 15 bold').place(x=900,y=750)
                                        #b=Button(a,text='Login',bg='white',activebackground='red',relief='solid',command=loginf,borderwidth=2,font='LUCIDA 15 bold').place(x=1400,y=270)
                                        #loginf()
                                        
                                    def pin_6_t():
                                        a=Tk()  #Making New Window for Login Page
                                        passw.set('')
                                        logid.set('')
                                        #y.destroy()
                                        a.title("Enter Login Pin")
                                        a.attributes('-fullscreen', True)
                                        a.configure(bg="white")
                                        a.iconbitmap('Py_ICO.ico')
                                        pyautogui.press("Alt+Tab")
                                        def win_cl1():
                                            a.destroy()
                                        b=Button(a,text='< Back To Login',borderwidth=0,relief='solid',activebackground='red',command=win_cl1,bg='white',font='LUCIDA 10').place(x=10,y=10)
                                        democursor=demodb.cursor()
                                        democursor.execute("select acc_no from user03 where userid='"+log+"'")
                                        for i in democursor:
                                            cd=i[0]
                                        democursor.execute("select * from users where acc_no="+cd)
                                        for i in democursor:
                                            name1= i[0]
                                        l=Label(a,text='Welcome '+name1+',',bg='white',font="LUCIDA 15 bold").pack(padx=0,pady=0)
                                        l=Label(a,text='',bg='white',font='LUCIDA 20 bold').pack(padx=0,pady=0)
                                        l=Label(a,text='Enter Transaction PIN : ',bg='white',font='LUCIDA 20 bold').pack(padx=0,pady=0)
                                        p1=StringVar(a)
                                        p2=StringVar(a)
                                        p3=StringVar(a)
                                        p4=StringVar(a)
                                        p5=StringVar(a)
                                        p6=StringVar(a)
                                        p1.set('')
                                        p2.set('')
                                        p3.set('')
                                        p4.set('')
                                        p5.set('')
                                        p6.set('')
                                        l=Entry(a,textvariable=p1,width=3,show='*',borderwidth=3,relief='solid',font='LUCIDA 15 bold').place(x=720,y=200)
                                        l=Entry(a,textvariable=p2,width=3,show='*',borderwidth=3,relief='solid',font='LUCIDA 15 bold').place(x=800,y=200)
                                        l=Entry(a,textvariable=p3,width=3,show='*',borderwidth=3,relief='solid',font='LUCIDA 15 bold').place(x=880,y=200)
                                        l=Entry(a,textvariable=p4,width=3,show='*',borderwidth=3,relief='solid',font='LUCIDA 15 bold').place(x=960,y=200)
                                        l=Entry(a,textvariable=p5,width=3,show='*',borderwidth=3,relief='solid',font='LUCIDA 15 bold').place(x=1040,y=200)
                                        l=Entry(a,textvariable=p6,width=3,show='*',borderwidth=3,relief='solid',font='LUCIDA 15 bold').place(x=1120,y=200)
                                        
                                        def clear():
                                            p1.set('')
                                            p2.set('')
                                            p3.set('')
                                            p4.set('')
                                            p5.set('')
                                            p6.set('')
                                        l=Button(a,text='Clear',command=clear,borderwidth=3,bg='white',activebackground='red',relief='solid',font='LUCIDA 15 bold').place(x=1220,y=200)
                                        def loginf():
                                            d1=p1.get()
                                            d2=p2.get()
                                            d3=p3.get()
                                            d4=p4.get()
                                            d5=p5.get()
                                            d6=p6.get()
                                            d=d1+d2+d3+d4+d5+d6
                                            democursor.execute("select passcode from users where acc_no='"+cd+"'")
                                            for i in democursor:
                                                passcodes=i[0]
                                                if d==passcodes:
                                                    a.destroy()
                                                    transfer()
                                                else:
                                                    #a.destroy()
                                                    clear()
                                                    l=Label(y,text='Incorrect Passcode',fg='red',bg='thistle3',font="LUCIDA 15 bold").place(x=1350,y=410)
                                        
                                        def b1():
                                            d1=p1.get()
                                            d2=p2.get()
                                            d3=p3.get()
                                            d4=p4.get()
                                            d5=p5.get()
                                            d6=p6.get()
                                            if d1=='' or d1==' ':
                                                p1.set('1')
                                            else:
                                                if d2=='' or d2==' ':
                                                    p2.set('1')
                                                else:
                                                    if d3=='' or d3==' ':
                                                        p3.set('1')
                                                    else:
                                                        if d4=='' or d4==' ':
                                                            p4.set('1')
                                                        else:
                                                            if d5=='' or d5==' ':
                                                                p5.set('1')
                                                            else:
                                                                if d6=='' or d6==' ':
                                                                    p6.set('1')
                                                                    loginf()
                                                                else:
                                                                    loginf()
                                        def b2():
                                            d1=p1.get()
                                            d2=p2.get()
                                            d3=p3.get()
                                            d4=p4.get()
                                            d5=p5.get()
                                            d6=p6.get()
                                            if d1=='' or d1==' ':
                                                p1.set('2')
                                            else:
                                                if d2=='' or d2==' ':
                                                    p2.set('2')
                                                else:
                                                    if d3=='' or d3==' ':
                                                        p3.set('2')
                                                    else:
                                                        if d4=='' or d4==' ':
                                                            p4.set('2')
                                                        else:
                                                            if d5=='' or d5==' ':
                                                                p5.set('2')
                                                            else:
                                                                if d6=='' or d6==' ':
                                                                    p6.set('2')
                                                                    loginf()
                                                                else:
                                                                    loginf()
                                        def b3():
                                            d1=p1.get()
                                            d2=p2.get()
                                            d3=p3.get()
                                            d4=p4.get()
                                            d5=p5.get()
                                            d6=p6.get()
                                            if d1=='' or d1==' ':
                                                p1.set('3')
                                            else:
                                                if d2=='' or d2==' ':
                                                    p2.set('3')
                                                else:
                                                    if d3=='' or d3==' ':
                                                        p3.set('3')
                                                    else:
                                                        if d4=='' or d4==' ':
                                                            p4.set('3')
                                                        else:
                                                            if d5=='' or d5==' ':
                                                                p5.set('3')
                                                            else:
                                                                if d6=='' or d6==' ':
                                                                    p6.set('3')
                                                                    loginf()
                                                                else:
                                                                    loginf()
                                        def b4():
                                            d1=p1.get()
                                            d2=p2.get()
                                            d3=p3.get()
                                            d4=p4.get()
                                            d5=p5.get()
                                            d6=p6.get()
                                            if d1=='' or d1==' ':
                                                p1.set('4')
                                            else:
                                                if d2=='' or d2==' ':
                                                    p2.set('4')
                                                else:
                                                    if d3=='' or d3==' ':
                                                        p3.set('4')
                                                    else:
                                                        if d4=='' or d4==' ':
                                                            p4.set('4')
                                                        else:
                                                            if d5=='' or d5==' ':
                                                                p5.set('4')
                                                            else:
                                                                if d6=='' or d6==' ':
                                                                    p6.set('4')
                                                                    loginf()
                                                                else:
                                                                    loginf()
                                        def b5():
                                            d1=p1.get()
                                            d2=p2.get()
                                            d3=p3.get()
                                            d4=p4.get()
                                            d5=p5.get()
                                            d6=p6.get()
                                            if d1=='' or d1==' ':
                                                p1.set('5')
                                            else:
                                                if d2=='' or d2==' ':
                                                    p2.set('5')
                                                else:
                                                    if d3=='' or d3==' ':
                                                        p3.set('5')
                                                    else:
                                                        if d4=='' or d4==' ':
                                                            p4.set('5')
                                                        else:
                                                            if d5=='' or d5==' ':
                                                                p5.set('5')
                                                            else:
                                                                if d6=='' or d6==' ':
                                                                    p6.set('5')
                                                                    loginf()
                                                                else:
                                                                    loginf()
                                        def b6():
                                            d1=p1.get()
                                            d2=p2.get()
                                            d3=p3.get()
                                            d4=p4.get()
                                            d5=p5.get()
                                            d6=p6.get()
                                            if d1=='' or d1==' ':
                                                p1.set('6')
                                            else:
                                                if d2=='' or d2==' ':
                                                    p2.set('6')
                                                else:
                                                    if d3=='' or d3==' ':
                                                        p3.set('6')
                                                    else:
                                                        if d4=='' or d4==' ':
                                                            p4.set('6')
                                                        else:
                                                            if d5=='' or d5==' ':
                                                                p5.set('6')
                                                            else:
                                                                if d6=='' or d6==' ':
                                                                    p6.set('6')
                                                                    loginf()
                                                                else:
                                                                    loginf()
                                        def b7():
                                            d1=p1.get()
                                            d2=p2.get()
                                            d3=p3.get()
                                            d4=p4.get()
                                            d5=p5.get()
                                            d6=p6.get()
                                            if d1=='' or d1==' ':
                                                p1.set('7')
                                            else:
                                                if d2=='' or d2==' ':
                                                    p2.set('7')
                                                else:
                                                    if d3=='' or d3==' ':
                                                        p3.set('7')
                                                    else:
                                                        if d4=='' or d4==' ':
                                                            p4.set('7')
                                                        else:
                                                            if d5=='' or d5==' ':
                                                                p5.set('7')
                                                            else:
                                                                if d6=='' or d6==' ':
                                                                    p6.set('7')
                                                                    loginf()
                                                                else:
                                                                    loginf()
                                        def b8():
                                            d1=p1.get()
                                            d2=p2.get()
                                            d3=p3.get()
                                            d4=p4.get()
                                            d5=p5.get()
                                            d6=p6.get()
                                            if d1=='' or d1==' ':
                                                p1.set('8')
                                            else:
                                                if d2=='' or d2==' ':
                                                    p2.set('8')
                                                else:
                                                    if d3=='' or d3==' ':
                                                        p3.set('8')
                                                    else:
                                                        if d4=='' or d4==' ':
                                                            p4.set('8')
                                                        else:
                                                            if d5=='' or d5==' ':
                                                                p5.set('8')
                                                            else:
                                                                if d6=='' or d6==' ':
                                                                    p6.set('8')
                                                                    loginf()
                                                                else:
                                                                    loginf()
                                        def b9():
                                            d1=p1.get()
                                            d2=p2.get()
                                            d3=p3.get()
                                            d4=p4.get()
                                            d5=p5.get()
                                            d6=p6.get()
                                            if d1=='' or d1==' ':
                                                p1.set('9')
                                            else:
                                                if d2=='' or d2==' ':
                                                    p2.set('9')
                                                else:
                                                    if d3=='' or d3==' ':
                                                        p3.set('9')
                                                    else:
                                                        if d4=='' or d4==' ':
                                                            p4.set('9')
                                                        else:
                                                            if d5=='' or d5==' ':
                                                                p5.set('9')
                                                            else:
                                                                if d6=='' or d6==' ':
                                                                    p6.set('9')
                                                                    loginf()
                                                                else:
                                                                    loginf()
                                        def b0():
                                            d1=p1.get()
                                            d2=p2.get()
                                            d3=p3.get()
                                            d4=p4.get()
                                            d5=p5.get()
                                            d6=p6.get()
                                            if d1=='' or d1==' ':
                                                p1.set('0')
                                            else:
                                                if d2=='' or d2==' ':
                                                    p2.set('0')
                                                else:
                                                    if d3=='' or d3==' ':
                                                        p3.set('0')
                                                    else:
                                                        if d4=='' or d4==' ':
                                                            p4.set('0')
                                                        else:
                                                            if d5=='' or d5==' ':
                                                                p5.set('0')
                                                            else:
                                                                if d6=='' or d6==' ':
                                                                    p6.set('0')
                                                                    loginf()
                                                                else:
                                                                    loginf()
                                    
                                    democursor.execute("select passcode from users where acc_no="+cd)
                                    for j in democursor:
                                        if len(j[0])==4:
                                            pin_4_t()
                                        elif len(j[0])==6:
                                            pin_6_t()
                                def next_pro():
                                    tick1=tick.get()
                                    if tick1==0:
                                        b=Label(o,text="       ",bg='white',font='LUCIDA 34').place(x=400,y=50)
                                    else:
                                        b=Button(o,text="Proceed",bg='white',borderwidth=1,activebackground='white',relief='solid',command=pas_get,font='LUCIDA 15').place(x=400,y=50)
                                b=Checkbutton(o,text="Are You Sure You Want to Transfer Rs."+str(amt1)+" to "+name_to1,bg='white',activebackground='white',command=next_pro,variable=tick,onvalue=1,offvalue=0,font="LUCIDA 15").pack(padx=0,pady=0)        
                                b=Label(o,text='',bg='white',font='LUCIDA 15').pack(padx=0,pady=0)
                        b=Button(t,text="Next",bg='white',borderwidth=1,activebackground='white',relief='solid',command=proceed,font='LUCIDA 15').place(x=700,y=600)
                    def deb_c():
                        u=Tk()
                        u.title("Debit Card")
                        u.attributes('-fullscreen', True)
                        u.configure(bg='white')
                        u.iconbitmap('Py_ICO.ico')
                        pyautogui.press("Alt+Tab")
                        def win_clo():
                            u.destroy()
                        b=Button(u,text='< Back To Main',borderwidth=0,relief='solid',activebackground='red',command=win_clo,bg='white',font='LUCIDA 10').place(x=10,y=10)
                        
                    def m_pas():
                        v=Tk()
                        v.title("m-Passbook")
                        v.attributes('-fullscreen', True)
                        v.configure(bg='white')
                        v.iconbitmap('Py_ICO.ico')
                        pyautogui.press("Alt+Tab")
                        def win_clo():
                            v.destroy()
                        b=Button(v,text='< Back To Main',borderwidth=0,relief='solid',activebackground='red',command=win_clo,bg='white',font='LUCIDA 10').place(x=10,y=10)
                        
                    def trans_h():
                        w=Tk()
                        w.title("Transaction History")
                        w.attributes('-fullscreen', True)
                        w.configure(bg='white')
                        w.iconbitmap('Py_ICO.ico')
                        pyautogui.press("Alt+Tab")
                        def win_clo():
                            w.destroy()
                        b=Button(w,text='< Back To Main',borderwidth=0,relief='solid',activebackground='red',command=win_clo,bg='white',font='LUCIDA 10').place(x=10,y=10)
                        
                    def dep():
                        x=Tk()
                        x.title("Deposit Money")
                        x.attributes('-fullscreen', True)
                        x.configure(bg='white')
                        x.iconbitmap('Py_ICO.ico')
                        pyautogui.press("Alt+Tab")
                        def win_clo():
                            x.destroy()
                        b=Button(x,text='< Back To Main',borderwidth=0,relief='solid',activebackground='red',command=win_clo,bg='white',font='LUCIDA 10').place(x=10,y=10)
                        
                    l=Label(c,text="                  ",fg='grey',bg='white',font="LUCIDA 15 bold").place(x=800,y=400)
                    b=Button(c,text="Accounts",borderwidth=3,relief='solid',width=15,activebackground='red',command=acc,bg='white',font='LUCIDA 20').place(x=500,y=200)
                    b=Button(c,text="Fund Transfer",borderwidth=3,relief='solid',width=15,activebackground='red',command=ft,bg='white',font='LUCIDA 20').place(x=1100,y=200)
                    l=Label(c,text='_________________________________________________________________',bg='white',fg='red',font='LUCIDA 20').place(x=400,y=350)
                    b=Button(c,text="Debit Cards",borderwidth=3,relief='solid',width=15,activebackground='red',command=deb_c,bg='white',font='LUCIDA 20').place(x=500,y=500)
                    b=Button(c,text="m-Passbook",borderwidth=3,relief='solid',width=15,activebackground='red',command=m_pas,bg='white',font='LUCIDA 20').place(x=1100,y=500)
                    l=Label(c,text='_________________________________________________________________',bg='white',fg='red',font='LUCIDA 20').place(x=400,y=650)
                    b=Button(c,text="Transaction History",borderwidth=3,relief='solid',width=15,activebackground='red',command=trans_h,bg='white',font='LUCIDA 20').place(x=500,y=800)
                    b=Button(c,text="Deposit Money",borderwidth=3,relief='solid',width=15,activebackground='red',command=dep,bg='white',font='LUCIDA 20').place(x=1100,y=800)
            else:
                l=Label(y,text="Incorrect Password or Login ID",fg='red',bg='thistle3',font="LUCIDA 15 bold").place(x=1250,y=410)
            ################    Create A New Account    **********
def pin_4(log,pasw):
    l=Label(y,text='                                                        ',fg='red',bg='thistle3',font="LUCIDA 25 bold").place(x=1150,y=410)
    if log=='' or log==' ' or pasw=='' or pasw==' ':    #Checking Null for Input
        l=Label(y,text='Please Enter Details!!',bg='thistle3',fg='red',font='LUCIDA 15 bold').place(x=1250,y=410)
    else:
        democursor=demodb.cursor()
        democursor.execute("select password from user03 where userid='"+log+"'")
        for i in democursor:
            a=i[0]
            
            if a=='' or a==' ':
                l=Label(y,text="Incorrect Password or Login ID",fg='red',bg='thistle3',font="LUCIDA 15 bold").place(x=1250,y=410)
            elif a is None:
                l=Label(y,text="Incorrect Password or Login ID",fg='red',bg='thistle3',font="LUCIDA 15 bold").place(x=1250,y=410)
            elif a==pasw: #Checking for Correct Password
                #l=Label(y,text="                                                    ",bg='thistle3',font="LUCIDA 15 bold").place(x=1250,y=410)
                a=Tk()  #Making New Window for Login Page
                passw.set('')
                logid.set('')
                #y.destroy()
                a.title("Enter Login Pin")
                a.attributes('-fullscreen', True)
                a.configure(bg="white")
                a.iconbitmap('Py_ICO.ico')
                pyautogui.press("Alt+Tab")
                def win_cl1():
                    a.destroy()
                b=Button(a,text='< Back To Login',borderwidth=0,relief='solid',activebackground='red',command=win_cl1,bg='white',font='LUCIDA 10').place(x=10,y=10)
                democursor=demodb.cursor()
                democursor.execute("select acc_no from user03 where userid='"+log+"'")
                for i in democursor:
                    cd=i[0]
                democursor.execute("select * from users where acc_no="+cd)
                for i in democursor:
                    name1= i[0]
                l=Label(a,text='Welcome '+name1+',',bg='white',font="LUCIDA 15 bold").pack(padx=0,pady=0)
                l=Label(a,text='',bg='white',font='LUCIDA 20 bold').pack(padx=0,pady=0)
                l=Label(a,text='Enter Login PIN : ',bg='white',font='LUCIDA 20 bold').pack(padx=0,pady=0)
                p1=StringVar(a)
                p2=StringVar(a)
                p3=StringVar(a)
                p4=StringVar(a)
                p1.set('8')
                p2.set('8')
                p3.set('8')
                p4.set('8')
                l=Entry(a,textvariable=p1,width=3,show='*',borderwidth=3,relief='solid',font='LUCIDA 15 bold').place(x=800,y=200)
                l=Entry(a,textvariable=p2,width=3,show='*',borderwidth=3,relief='solid',font='LUCIDA 15 bold').place(x=880,y=200)
                l=Entry(a,textvariable=p3,width=3,show='*',borderwidth=3,relief='solid',font='LUCIDA 15 bold').place(x=960,y=200)
                l=Entry(a,textvariable=p4,width=3,show='*',borderwidth=3,relief='solid',font='LUCIDA 15 bold').place(x=1040,y=200)
                def clear():
                    p1.set('')
                    p2.set('')
                    p3.set('')
                    p4.set('')
                l=Button(a,text='Clear',command=clear,borderwidth=3,bg='white',activebackground='red',relief='solid',font='LUCIDA 15 bold').place(x=1220,y=200)
                def loginf():
                    d1=p1.get()
                    d2=p2.get()
                    d3=p3.get()
                    d4=p4.get()
                    d=d1+d2+d3+d4
                    democursor.execute("select passcode from users where acc_no='"+cd+"'")
                    for i in democursor:
                        passcodes=i[0]
                        if d==passcodes:
                            a.destroy()
                            login(log,pasw)
                        else:
                            #a.destroy()
                            l=Label(y,text='Incorrect Passcode',fg='red',bg='thistle3',font="LUCIDA 15 bold").place(x=1350,y=410)
                            clear()
                
                def b1():
                    d1=p1.get()
                    d2=p2.get()
                    d3=p3.get()
                    d4=p4.get()
                    if d1=='' or d1==' ':
                        p1.set('1')
                    else:
                        if d2=='' or d2==' ':
                            p2.set('1')
                        else:
                            if d3=='' or d3==' ':
                                p3.set('1')
                            else:
                                if d4=='' or d4==' ':
                                    p4.set('1')
                                    loginf()
                                else:
                                    loginf()
                def b2():
                    d1=p1.get()
                    d2=p2.get()
                    d3=p3.get()
                    d4=p4.get()
                    if d1=='' or d1==' ':
                        p1.set('2')
                    else:
                        if d2=='' or d2==' ':
                            p2.set('2')
                        else:
                            if d3=='' or d3==' ':
                                p3.set('2')
                            else:
                                if d4=='' or d4==' ':
                                    p4.set('2')
                                    loginf()
                                else:
                                    loginf()
                def b3():
                    d1=p1.get()
                    d2=p2.get()
                    d3=p3.get()
                    d4=p4.get()
                    if d1=='' or d1==' ':
                        p1.set('3')
                    else:
                        if d2=='' or d2==' ':
                            p2.set('3')
                        else:
                            if d3=='' or d3==' ':
                                p3.set('3')
                            else:
                                if d4=='' or d4==' ':
                                    p4.set('3')
                                    loginf()
                                else:
                                    loginf()
                def b4():
                    d1=p1.get()
                    d2=p2.get()
                    d3=p3.get()
                    d4=p4.get()
                    if d1=='' or d1==' ':
                        p1.set('4')
                    else:
                        if d2=='' or d2==' ':
                            p2.set('4')
                        else:
                            if d3=='' or d3==' ':
                                p3.set('4')
                            else:
                                if d4=='' or d4==' ':
                                    p4.set('4')
                                    loginf()
                                else:
                                    loginf()
                def b5():
                    d1=p1.get()
                    d2=p2.get()
                    d3=p3.get()
                    d4=p4.get()
                    if d1=='' or d1==' ':
                        p1.set('5')
                    else:
                        if d2=='' or d2==' ':
                            p2.set('5')
                        else:
                            if d3=='' or d3==' ':
                                p3.set('5')
                            else:
                                if d4=='' or d4==' ':
                                    p4.set('5')
                                    loginf()
                                else:
                                    loginf()
                def b6():
                    d1=p1.get()
                    d2=p2.get()
                    d3=p3.get()
                    d4=p4.get()
                    if d1=='' or d1==' ':
                        p1.set('6')
                    else:
                        if d2=='' or d2==' ':
                            p2.set('6')
                        else:
                            if d3=='' or d3==' ':
                                p3.set('6')
                            else:
                                if d4=='' or d4==' ':
                                    p4.set('6')
                                    loginf()
                                else:
                                    loginf()
                def b7():
                    d1=p1.get()
                    d2=p2.get()
                    d3=p3.get()
                    d4=p4.get()
                    if d1=='' or d1==' ':
                        p1.set('7')
                    else:
                        if d2=='' or d2==' ':
                            p2.set('7')
                        else:
                            if d3=='' or d3==' ':
                                p3.set('7')
                            else:
                                if d4=='' or d4==' ':
                                    p4.set('7')
                                    loginf()
                                else:
                                    loginf()
                def b8():
                    d1=p1.get()
                    d2=p2.get()
                    d3=p3.get()
                    d4=p4.get()
                    if d1=='' or d1==' ':
                        p1.set('8')
                    else:
                        if d2=='' or d2==' ':
                            p2.set('8')
                        else:
                            if d3=='' or d3==' ':
                                p3.set('8')
                            else:
                                if d4=='' or d4==' ':
                                    p4.set('8')
                                    loginf()
                                else:
                                    loginf()
                def b9():
                    d1=p1.get()
                    d2=p2.get()
                    d3=p3.get()
                    d4=p4.get()
                    if d1=='' or d1==' ':
                        p1.set('9')
                    else:
                        if d2=='' or d2==' ':
                            p2.set('9')
                        else:
                            if d3=='' or d3==' ':
                                p3.set('9')
                            else:
                                if d4=='' or d4==' ':
                                    p4.set('9')
                                    loginf()
                                else:
                                    loginf()
                def b0():
                    d1=p1.get()
                    d2=p2.get()
                    d3=p3.get()
                    d4=p4.get()
                    if d1=='' or d1==' ':
                        p1.set('0')
                    else:
                        if d2=='' or d2==' ':
                            p2.set('0')
                        else:
                            if d3=='' or d3==' ':
                                p3.set('0')
                            else:
                                if d4=='' or d4==' ':
                                    p4.set('0')
                                    loginf()
                                else:
                                    loginf()
                b=Button(a,text='1',bg='white',width=5,height=3,activebackground='red',relief='solid',command=b1,borderwidth=2,font='LUCIDA 15 bold').place(x=800,y=300)
                b=Button(a,text='2',bg='white',width=5,height=3,activebackground='red',relief='solid',command=b2,borderwidth=2,font='LUCIDA 15 bold').place(x=900,y=300)
                b=Button(a,text='3',bg='white',width=5,height=3,activebackground='red',relief='solid',command=b3,borderwidth=2,font='LUCIDA 15 bold').place(x=1000,y=300)
                b=Button(a,text='4',bg='white',width=5,height=3,activebackground='red',relief='solid',command=b4,borderwidth=2,font='LUCIDA 15 bold').place(x=800,y=450)
                b=Button(a,text='5',bg='white',width=5,height=3,activebackground='red',relief='solid',command=b5,borderwidth=2,font='LUCIDA 15 bold').place(x=900,y=450)
                b=Button(a,text='6',bg='white',width=5,height=3,activebackground='red',relief='solid',command=b6,borderwidth=2,font='LUCIDA 15 bold').place(x=1000,y=450)
                b=Button(a,text='7',bg='white',width=5,height=3,activebackground='red',relief='solid',command=b7,borderwidth=2,font='LUCIDA 15 bold').place(x=800,y=600)
                b=Button(a,text='8',bg='white',width=5,height=3,activebackground='red',relief='solid',command=b8,borderwidth=2,font='LUCIDA 15 bold').place(x=900,y=600)
                b=Button(a,text='9',bg='white',width=5,height=3,activebackground='red',relief='solid',command=b9,borderwidth=2,font='LUCIDA 15 bold').place(x=1000,y=600)
                b=Button(a,text='0',bg='white',width=5,height=3,activebackground='red',relief='solid',command=b0,borderwidth=2,font='LUCIDA 15 bold').place(x=900,y=750)
                #b=Button(a,text='Login',bg='white',activebackground='red',relief='solid',command=loginf,borderwidth=2,font='LUCIDA 15 bold').place(x=1400,y=270)
                #loginf()
            else:
                l=Label(y,text="Incorrect Password or Login ID",fg='red',bg='thistle3',font="LUCIDA 15 bold").place(x=1250,y=410)
def pin_6(log,pasw):
    l=Label(y,text='                                                        ',fg='red',bg='thistle3',font="LUCIDA 25 bold").place(x=1150,y=410)
    if log=='' or log==' ' or pasw=='' or pasw==' ':    #Checking Null for Input
        l=Label(y,text='Please Enter Details!!',bg='thistle3',fg='red',font='LUCIDA 15 bold').place(x=1250,y=410)
    else:
        democursor=demodb.cursor()
        democursor.execute("select password from user03 where userid='"+log+"'")
        for i in democursor:
            a=i[0]
            
            if a=='' or a==' ':
                l=Label(y,text="Incorrect Password or Login ID",fg='red',bg='thistle3',font="LUCIDA 15 bold").place(x=1250,y=410)
            elif a is None:
                l=Label(y,text="Incorrect Password or Login ID",fg='red',bg='thistle3',font="LUCIDA 15 bold").place(x=1250,y=410)
            elif a==pasw: #Checking for Correct Password
                #l=Label(y,text="                                                    ",bg='thistle3',font="LUCIDA 15 bold").place(x=1250,y=410)
                a=Tk()  #Making New Window for Login Page
                passw.set('')
                logid.set('')
                #y.destroy()
                a.title("Enter Login Pin")
                a.attributes('-fullscreen', True)
                a.configure(bg="white")
                a.iconbitmap('Py_ICO.ico')
                pyautogui.press("Alt+Tab")
                def win_cl1():
                    a.destroy()
                b=Button(a,text='< Back To Login',borderwidth=0,relief='solid',activebackground='red',command=win_cl1,bg='white',font='LUCIDA 10').place(x=10,y=10)
                democursor=demodb.cursor()
                democursor.execute("select acc_no from user03 where userid='"+log+"'")
                for i in democursor:
                    cd=i[0]
                democursor.execute("select * from users where acc_no="+cd)
                for i in democursor:
                    name1= i[0]
                l=Label(a,text='Welcome '+name1+',',bg='white',font="LUCIDA 15 bold").pack(padx=0,pady=0)
                l=Label(a,text='',bg='white',font='LUCIDA 20 bold').pack(padx=0,pady=0)
                l=Label(a,text='Enter Login PIN : ',bg='white',font='LUCIDA 20 bold').pack(padx=0,pady=0)
                p1=StringVar(a)
                p2=StringVar(a)
                p3=StringVar(a)
                p4=StringVar(a)
                p5=StringVar(a)
                p6=StringVar(a)
                p1.set('')
                p2.set('')
                p3.set('')
                p4.set('')
                p5.set('')
                p6.set('')
                l=Entry(a,textvariable=p1,width=3,show='*',borderwidth=3,relief='solid',font='LUCIDA 15 bold').place(x=720,y=200)
                l=Entry(a,textvariable=p2,width=3,show='*',borderwidth=3,relief='solid',font='LUCIDA 15 bold').place(x=800,y=200)
                l=Entry(a,textvariable=p3,width=3,show='*',borderwidth=3,relief='solid',font='LUCIDA 15 bold').place(x=880,y=200)
                l=Entry(a,textvariable=p4,width=3,show='*',borderwidth=3,relief='solid',font='LUCIDA 15 bold').place(x=960,y=200)
                l=Entry(a,textvariable=p5,width=3,show='*',borderwidth=3,relief='solid',font='LUCIDA 15 bold').place(x=1040,y=200)
                l=Entry(a,textvariable=p6,width=3,show='*',borderwidth=3,relief='solid',font='LUCIDA 15 bold').place(x=1120,y=200)
                
                def clear():
                    p1.set('')
                    p2.set('')
                    p3.set('')
                    p4.set('')
                    p5.set('')
                    p6.set('')
                l=Button(a,text='Clear',command=clear,borderwidth=3,bg='white',activebackground='red',relief='solid',font='LUCIDA 15 bold').place(x=1220,y=200)
                def loginf():
                    d1=p1.get()
                    d2=p2.get()
                    d3=p3.get()
                    d4=p4.get()
                    d5=p5.get()
                    d6=p6.get()
                    d=d1+d2+d3+d4+d5+d6
                    democursor.execute("select passcode from users where acc_no='"+cd+"'")
                    for i in democursor:
                        passcodes=i[0]
                        if d==passcodes:
                            a.destroy()
                            login(log,pasw)
                        else:
                            a.destroy()
                            l=Label(y,text='Incorrect Passcode',fg='red',bg='thistle3',font="LUCIDA 15 bold").place(x=1350,y=410)
                
                def b1():
                    d1=p1.get()
                    d2=p2.get()
                    d3=p3.get()
                    d4=p4.get()
                    d5=p5.get()
                    d6=p6.get()
                    if d1=='' or d1==' ':
                        p1.set('1')
                    else:
                        if d2=='' or d2==' ':
                            p2.set('1')
                        else:
                            if d3=='' or d3==' ':
                                p3.set('1')
                            else:
                                if d4=='' or d4==' ':
                                    p4.set('1')
                                else:
                                    if d5=='' or d5==' ':
                                        p5.set('1')
                                    else:
                                        if d6=='' or d6==' ':
                                            p6.set('1')
                                            loginf()
                                        else:
                                            loginf()
                def b2():
                    d1=p1.get()
                    d2=p2.get()
                    d3=p3.get()
                    d4=p4.get()
                    d5=p5.get()
                    d6=p6.get()
                    if d1=='' or d1==' ':
                        p1.set('2')
                    else:
                        if d2=='' or d2==' ':
                            p2.set('2')
                        else:
                            if d3=='' or d3==' ':
                                p3.set('2')
                            else:
                                if d4=='' or d4==' ':
                                    p4.set('2')
                                else:
                                    if d5=='' or d5==' ':
                                        p5.set('2')
                                    else:
                                        if d6=='' or d6==' ':
                                            p6.set('2')
                                            loginf()
                                        else:
                                            loginf()
                def b3():
                    d1=p1.get()
                    d2=p2.get()
                    d3=p3.get()
                    d4=p4.get()
                    d5=p5.get()
                    d6=p6.get()
                    if d1=='' or d1==' ':
                        p1.set('3')
                    else:
                        if d2=='' or d2==' ':
                            p2.set('3')
                        else:
                            if d3=='' or d3==' ':
                                p3.set('3')
                            else:
                                if d4=='' or d4==' ':
                                    p4.set('3')
                                else:
                                    if d5=='' or d5==' ':
                                        p5.set('3')
                                    else:
                                        if d6=='' or d6==' ':
                                            p6.set('3')
                                            loginf()
                                        else:
                                            loginf()
                def b4():
                    d1=p1.get()
                    d2=p2.get()
                    d3=p3.get()
                    d4=p4.get()
                    d5=p5.get()
                    d6=p6.get()
                    if d1=='' or d1==' ':
                        p1.set('4')
                    else:
                        if d2=='' or d2==' ':
                            p2.set('4')
                        else:
                            if d3=='' or d3==' ':
                                p3.set('4')
                            else:
                                if d4=='' or d4==' ':
                                    p4.set('4')
                                else:
                                    if d5=='' or d5==' ':
                                        p5.set('4')
                                    else:
                                        if d6=='' or d6==' ':
                                            p6.set('4')
                                            loginf()
                                        else:
                                            loginf()
                def b5():
                    d1=p1.get()
                    d2=p2.get()
                    d3=p3.get()
                    d4=p4.get()
                    d5=p5.get()
                    d6=p6.get()
                    if d1=='' or d1==' ':
                        p1.set('5')
                    else:
                        if d2=='' or d2==' ':
                            p2.set('5')
                        else:
                            if d3=='' or d3==' ':
                                p3.set('5')
                            else:
                                if d4=='' or d4==' ':
                                    p4.set('5')
                                else:
                                    if d5=='' or d5==' ':
                                        p5.set('5')
                                    else:
                                        if d6=='' or d6==' ':
                                            p6.set('5')
                                            loginf()
                                        else:
                                            loginf()
                def b6():
                    d1=p1.get()
                    d2=p2.get()
                    d3=p3.get()
                    d4=p4.get()
                    d5=p5.get()
                    d6=p6.get()
                    if d1=='' or d1==' ':
                        p1.set('6')
                    else:
                        if d2=='' or d2==' ':
                            p2.set('6')
                        else:
                            if d3=='' or d3==' ':
                                p3.set('6')
                            else:
                                if d4=='' or d4==' ':
                                    p4.set('6')
                                else:
                                    if d5=='' or d5==' ':
                                        p5.set('6')
                                    else:
                                        if d6=='' or d6==' ':
                                            p6.set('6')
                                            loginf()
                                        else:
                                            loginf()
                def b7():
                    d1=p1.get()
                    d2=p2.get()
                    d3=p3.get()
                    d4=p4.get()
                    d5=p5.get()
                    d6=p6.get()
                    if d1=='' or d1==' ':
                        p1.set('7')
                    else:
                        if d2=='' or d2==' ':
                            p2.set('7')
                        else:
                            if d3=='' or d3==' ':
                                p3.set('7')
                            else:
                                if d4=='' or d4==' ':
                                    p4.set('7')
                                else:
                                    if d5=='' or d5==' ':
                                        p5.set('7')
                                    else:
                                        if d6=='' or d6==' ':
                                            p6.set('7')
                                            loginf()
                                        else:
                                            loginf()
                def b8():
                    d1=p1.get()
                    d2=p2.get()
                    d3=p3.get()
                    d4=p4.get()
                    d5=p5.get()
                    d6=p6.get()
                    if d1=='' or d1==' ':
                        p1.set('8')
                    else:
                        if d2=='' or d2==' ':
                            p2.set('8')
                        else:
                            if d3=='' or d3==' ':
                                p3.set('8')
                            else:
                                if d4=='' or d4==' ':
                                    p4.set('8')
                                else:
                                    if d5=='' or d5==' ':
                                        p5.set('8')
                                    else:
                                        if d6=='' or d6==' ':
                                            p6.set('8')
                                            loginf()
                                        else:
                                            loginf()
                def b9():
                    d1=p1.get()
                    d2=p2.get()
                    d3=p3.get()
                    d4=p4.get()
                    d5=p5.get()
                    d6=p6.get()
                    if d1=='' or d1==' ':
                        p1.set('9')
                    else:
                        if d2=='' or d2==' ':
                            p2.set('9')
                        else:
                            if d3=='' or d3==' ':
                                p3.set('9')
                            else:
                                if d4=='' or d4==' ':
                                    p4.set('9')
                                else:
                                    if d5=='' or d5==' ':
                                        p5.set('9')
                                    else:
                                        if d6=='' or d6==' ':
                                            p6.set('9')
                                            loginf()
                                        else:
                                            loginf()
                def b0():
                    d1=p1.get()
                    d2=p2.get()
                    d3=p3.get()
                    d4=p4.get()
                    d5=p5.get()
                    d6=p6.get()
                    if d1=='' or d1==' ':
                        p1.set('0')
                    else:
                        if d2=='' or d2==' ':
                            p2.set('0')
                        else:
                            if d3=='' or d3==' ':
                                p3.set('0')
                            else:
                                if d4=='' or d4==' ':
                                    p4.set('0')
                                else:
                                    if d5=='' or d5==' ':
                                        p5.set('0')
                                    else:
                                        if d6=='' or d6==' ':
                                            p6.set('0')
                                            loginf()
                                        else:
                                            loginf()
                b=Button(a,text='1',bg='white',width=5,height=3,activebackground='red',relief='solid',command=b1,borderwidth=2,font='LUCIDA 15 bold').place(x=800,y=300)
                b=Button(a,text='2',bg='white',width=5,height=3,activebackground='red',relief='solid',command=b2,borderwidth=2,font='LUCIDA 15 bold').place(x=900,y=300)
                b=Button(a,text='3',bg='white',width=5,height=3,activebackground='red',relief='solid',command=b3,borderwidth=2,font='LUCIDA 15 bold').place(x=1000,y=300)
                b=Button(a,text='4',bg='white',width=5,height=3,activebackground='red',relief='solid',command=b4,borderwidth=2,font='LUCIDA 15 bold').place(x=800,y=450)
                b=Button(a,text='5',bg='white',width=5,height=3,activebackground='red',relief='solid',command=b5,borderwidth=2,font='LUCIDA 15 bold').place(x=900,y=450)
                b=Button(a,text='6',bg='white',width=5,height=3,activebackground='red',relief='solid',command=b6,borderwidth=2,font='LUCIDA 15 bold').place(x=1000,y=450)
                b=Button(a,text='7',bg='white',width=5,height=3,activebackground='red',relief='solid',command=b7,borderwidth=2,font='LUCIDA 15 bold').place(x=800,y=600)
                b=Button(a,text='8',bg='white',width=5,height=3,activebackground='red',relief='solid',command=b8,borderwidth=2,font='LUCIDA 15 bold').place(x=900,y=600)
                b=Button(a,text='9',bg='white',width=5,height=3,activebackground='red',relief='solid',command=b9,borderwidth=2,font='LUCIDA 15 bold').place(x=1000,y=600)
                b=Button(a,text='0',bg='white',width=5,height=3,activebackground='red',relief='solid',command=b0,borderwidth=2,font='LUCIDA 15 bold').place(x=900,y=750)
                #b=Button(a,text='Login',bg='white',activebackground='red',relief='solid',command=loginf,borderwidth=2,font='LUCIDA 15 bold').place(x=1400,y=270)
                #loginf()
            else:
                l=Label(y,text="Incorrect Password or Login ID",fg='red',bg='thistle3',font="LUCIDA 15 bold").place(x=1250,y=410)
photo=PhotoImage(file=r'BMS.png')
photo1=PhotoImage(file=r'RAP.png')
photo3=PhotoImage(file=r'IMG.png')
photo4=PhotoImage(file=r'PP.png')
photo2 = photo4.subsample(1,1)
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
if current_time>='00:00:00' and current_time<'12:00:00':
    wish="Good Morning ! Welcome To Bank"
elif current_time>='12:00:00' and current_time<'16:00:00':
    wish="Good Afternoon ! Welcome To Bank"
else:
    wish="Good Evening ! Welcome To Bank"
from PIL import Image, ImageTk

l=Button(y,text="",bg='thistle3',height=8,activeforeground='thistle3',activebackground='thistle3',relief='solid',borderwidth=3,command=None,width=40,font='LUCIDA 15 bold').place(x=1150,y=110)
l1=Label(y,text=wish,bg='thistle3',fg='red',font='LUCIDA 20 bold').pack(padx=20,pady=20)
#l=Label(y,text="_____________________________________________",bg='thistle3',font='LUCIDA 15 bold').place(x=1150,y=110)
#l=Label(y,text="_____________________________________________",bg='thistle3',font='LUCIDA 15 bold').place(x=1150,y=310)
def Shivam():
    y.title("Shivam Soni")
    import webbrowser as w
    label=Label(y,text="            ",bg='white',font='LUCIDA 1000 bold').place(x=0,y=0)
    def dest():
        y.destroy()
        import Bank as bn
        while True:
            import Bank
    b=Button(y,text='< Back To Main',borderwidth=0,relief='solid',activebackground='red',command=dest,bg='white',font='LUCIDA 10').place(x=0,y=0)
    b=Button(y,image=photo2,borderwidth=3,relief='solid',bg='black',command=None,activebackground='black').place(x=30,y=30)
    l=Label(y,text="Shivam Soni",bg='white',fg='black',font=('Arial',25,'bold')).place(x=1200,y=10)
    te="""Age : 19
City : Gandhinagar,Gujarat
Nationality : Indian
Projects Made : EquineSQL,Flight Management System,
                Bank Management System,Websites,etc.
Badges : 
"""
    l=Label(y,text="Age : 19",bg='white',fg='black',font=('Arial',15)).place(x=750,y=100)
    l=Label(y,text="Date Of Birth : 27th December 2003",bg='white',fg='black',font=('Arial',15)).place(x=750,y=140)
    l=Label(y,text="Gandhinagar,Gujarat",bg='white',fg='black',font=('Arial',15)).place(x=750,y=180)
    l=Label(y,text="India",bg='white',fg='black',font=('Arial',15,'bold')).place(x=750,y=220)
    l=Label(y,text="Projects Made : EquineSQL,Flight Management System,",bg='white',fg='black',font=('Arial',15)).place(x=750,y=260)
    l=Label(y,text="                         Bank Management System,Websites,etc.",bg='white',fg='black',font=('Arial',15)).place(x=750,y=300)
    l=Label(y,text="Badges : ",bg='white',fg='black',font=('Arial',15)).place(x=750,y=340)
    l=Label(y,text="LinkedIn : ",bg='white',fg='black',font=('Arial',15)).place(x=750,y=380)
    l=Label(y,text="Instagram : ",bg='white',fg='black',font=('Arial',15)).place(x=750,y=420)
    l=Label(y,text="E-Mail ID : shivam2712.soni@gmail.com",bg='white',fg='black',font=('Arial',15)).place(x=750,y=460)
    l=Label(y,text="Branch : B.Tech CSE(Cyber Security)",bg='white',fg='black',font=('Arial',15)).place(x=750,y=500)
    l=Label(y,text="University : ICT Ganpat University",bg='white',fg='black',font=('Arial',15)).place(x=750,y=540)
    
    def Insagram():
        w.open("https://www.instagram.com/shivam_soni.2712/")
    def badges():
        w.open("https://www.credly.com/users/shivam-soni.2445a7d1/badges")
    def linkedin():
        w.open("https://www.linkedin.com/in/shivam-soni-859191221/")
    b=Button(y,text="Badges",command=badges,bg='white',borderwidth=0,activebackground='white',fg='blue',font=('Arial',15,'underline')).place(x=860,y=335)
    b=Button(y,text="Instagram",command=Insagram,bg='white',borderwidth=0,activebackground='white',fg='blue',font=('Arial',15,'underline')).place(x=880,y=415)
    b=Button(y,text="LinkedIn",command=linkedin,bg='white',borderwidth=0,activebackground='white',fg='blue',font=('Arial',15,'underline')).place(x=870,y=375)
l=Button(y,text="Made By Shivam Soni",bg='thistle3',command=Shivam,borderwidth=0,activebackground='thistle3',fg='grey',font='LUCIDA 13 bold underline').place(x=1600,y=50)
l=Label(y,text='Login ID :',bg='thistle3',font="LUCIDA 15 bold").place(x=1200,y=160)
logid=StringVar(y)
logid.set('ss')
passw=StringVar(y)
passw.set('sasoni')
l=Button(y,text="    Create A New Account    ",command=cr_acc,activeforeground='black',activebackground='skyblue',fg='red',bg='white',font="LUCIDA 20 bold").place(x=1250,y=510)
l=Entry(y,textvariable=logid,font="LUCIDA 15 bold").place(x=1400,y=160)
l=Label(y,text='Password :',bg='thistle3',font="LUCIDA 15 bold").place(x=1200,y=210)
l=Entry(y,textvariable=passw,show='*',font="LUCIDA 15 bold").place(x=1400,y=210)
def forget_pas():
    p=Tk()
    p.title("Forget ID or Password")
    p.attributes('-fullscreen', True)
    p.configure(bg="white")
    p.iconbitmap('Py_ICO.ico')
    def win_cl1():
        p.destroy()
    b=Button(p,text='< Back To Login',borderwidth=0,relief='solid',activebackground='red',command=win_cl1,bg='white',font='LUCIDA 10').place(x=10,y=10)
                
    pyautogui.press("Alt+Tab")
    l=Label(p,text="Please Enter Following Details : ",bg='white',font='LUCIDA 20 bold').pack(padx=0,pady=0)
    acc_num=StringVar(p)
    card_num=StringVar(p)
    ifsc_code=StringVar(p)
    l=Label(p,text="Account Number : ",bg='white',font='LUCIDA 20 bold').place(x=500,y=150)
    l=Label(p,text="Card Number : ",bg='white',font='LUCIDA 20 bold').place(x=500,y=200)
    l=Label(p,text="IFSC Code : ",bg='white',font='LUCIDA 20 bold').place(x=500,y=250)
    e=Entry(p,textvariable=acc_num,bg='white',borderwidth=1,relief='solid',font='LUCIDA 20 bold').place(x=800,y=150)
    e=Entry(p,textvariable=card_num,bg='white',borderwidth=1,relief='solid',font='LUCIDA 20 bold').place(x=800,y=200)
    e=Entry(p,textvariable=ifsc_code,bg='white',borderwidth=1,relief='solid',font='LUCIDA 20 bold').place(x=800,y=250)
    def next_p():
        acc_n=acc_num.get()
        card_n=card_num.get()
        ifsc_c=ifsc_code.get()
        if acc_n=='' or card_n=='' or ifsc_c=='':
            l=Label(p,text="Please Give Valid Input",bg='white',fg='red',font='LUCIDA 15 bold').place(x=1100,y=700)
        else:
            acc=[]
            card=[]
            ifsc=[]
            democursor.execute("select count(*) from users")
            for i in democursor:
                num=i[0]
            democursor.execute("select acc_no from users")
            for i in democursor:
                for j in range(0,num):
                    acc.append(i[j])
            democursor.execute("select card_n from users")
            for i in democursor:
                for j in range(0,num):
                    card.append(i[j])
            democursor.execute("select ifsc from users")
            for i in democursor:
                for j in range(0,num):
                    ifsc.append(i[j])
            def otp(Email,name):
                p.destroy()
                q=Tk()
                q.title("Enter OTP")
                q.attributes('-fullscreen', True)
                q.configure(bg="white")
                q.iconbitmap('Py_ICO.ico')
                em12=str(Email)
                first_n=Email[1:-10]
                ekfk=len(first_n)
                ejjj=ekfk*'*'
                final_emid=em12.replace(first_n,ejjj)
                import random
                list1=['S','H','I','V','A','M']
                w_1=random.choice(list1)
                w_2=str(random.randint(111111,999999))
                w_final=w_1+w_2
                text1="Verify Email"
                text2="A Code Has Been Sent to "+final_emid+" Please Enter That Code Below - "
                b=Label(q,text=text1,bg='white',font="LUCIDA 15 bold").pack(padx=0,pady=0)
                b=Label(q,text=text2,fg='red',bg='white',font="LUCIDA 15 bold").pack(padx=0,pady=0)
                import smtplib
                from email.message import EmailMessage
                Sender_Email = "codeinterest27@gmail.com"
                Reciever_Email = [Email]
                Password = "sodjxrgmbrlghznu"
                newMessage = EmailMessage()
                newMessage['Subject'] = "Secret Code To Reset Password for Account : "+acc_n
                newMessage['From'] = Sender_Email
                newMessage['To'] = Reciever_Email
                newMessage.set_content("""Hello """+name+""",
This is Your Secret Code :


            """+w_1+"""-"""+w_2+"""
            

Please Do Not Share This Code With anybody.
This Is Your Secret Code.
Do Not Reply to this Email
For any Complaints contact us at
Mail - codeinterest27@gmail.com
Phone - +918799523738""")
                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp3:
                    smtp3.login(Sender_Email, Password)
                    smtp3.send_message(newMessage)#'''
                f_let=StringVar(q)
                f_let.set('↓')
                om=OptionMenu(q,f_let,*list1).place(x=700,y=300)
                codes=StringVar(q)
                e=Entry(q,textvariable=codes,borderwidth=3,relief='solid',bg='white',font='LUCIDA 15 bold').place(x=850,y=300) 
                pyautogui.press("Alt+Tab")
                def reset_pas():
                    otp_c=str(f_let.get())+str(codes.get())
                    if otp_c==w_final:
                        q.destroy()
                        r=Tk()
                        r.title("Reset Password")
                        r.attributes('-fullscreen', True)
                        r.configure(bg="white")
                        r.iconbitmap('Py_ICO.ico')
                        l=Label(r,text="",bg='white',font='LUCIDA 20 bold').pack(padx=0,pady=0)
                        l=Label(r,text="Reset Password",bg='white',font='LUCIDA 20 bold').pack(padx=0,pady=0)
                        l=Label(r,text="Reset Password : ",bg='white',font='LUCIDA 15 bold').place(x=170,y=200)
                        l=Label(r,text="Type Password Once Again: ",bg='white',font='LUCIDA 15 bold').place(x=100,y=300)
                        new_pas=StringVar(r)
                        new_pas.set('')
                        re_pas=StringVar(r)
                        re_pas.set('')
                        ent=Entry(r,textvariable=new_pas,show='*',borderwidth=3,relief='solid',font='LUCIDA 15 bold').place(x=500,y=200)
                        ent=Entry(r,textvariable=re_pas,show='*',borderwidth=3,relief='solid',font='LUCIDA 15 bold').place(x=500,y=300)
                        def check_and():
                            ren_pas=new_pas.get()
                            ren_re=re_pas.get()
                            democursor.execute("select password from user03 where acc_no='"+acc_n+"'")
                            for i in democursor:
                                old_pas=str(i[0])
                            if ren_pas=='' or ren_re=='':
                                b=Label(r,text="Please Enter Valid Password",fg='red',bg='white',font='LUCIDA 15 bold').place(x=1100,y=700)
                            elif ren_pas!=ren_re:
                                b=Label(r,text="Password Doesn't Match",fg='red',bg='white',font='LUCIDA 15 bold').place(x=1100,y=700)
                            elif ren_pas==ren_re and len(ren_pas)<6:
                                b=Label(r,text="Password is Too Short",fg='red',bg='white',font='LUCIDA 15 bold').place(x=1100,y=700)
                            elif ren_pas==ren_re and ren_pas==old_pas:
                                b=Label(r,text="This Password Was Used Before",fg='red',bg='white',font='LUCIDA 15 bold').place(x=1100,y=700)
                            else:
                                r.destroy()
                                democursor.execute("update users set password='"+ren_pas+"' where email='"+Email+"' and acc_no='"+acc_n+"' and ifsc='"+ifsc_c+"'")
                                demodb.commit()
                                democursor.execute("update user03 set password='"+ren_pas+"' where acc_no='"+acc_n+"'")
                                demodb.commit()
                                now = datetime.now()
                                cue = str(now.strftime("%H:%M:%S"))
                                from datetime import date
                                today1=date.today()
                                today2= str(today1)
                                democursor.execute("insert into pas_reset values('"+acc_n+"','"+old_pas+"','"+ren_pas+"','"+cue+"','"+today2+"')")
                                demodb.commit()
                                import smtplib
                                democursor.execute("select userid from user03 where acc_no='"+acc_n+"' and password='"+ren_pas+"'")
                                for i in democursor:
                                    usid=str(i[0])
                                from email.message import EmailMessage
                                Sender_Email = "codeinterest27@gmail.com"
                                Reciever_Email = [Email]
                                Password = "sodjxrgmbrlghznu"
                                newMessage = EmailMessage()
                                newMessage['Subject'] = "Secret Code To Reset Password for Account : "+acc_n
                                newMessage['From'] = Sender_Email
                                newMessage['To'] = Reciever_Email
                                newMessage.set_content("""Hello """+name+""",
Your Password For USER ID : """+usid+"""
Has Been Reset
On """+cue+""" """+today2+"""



Please Do Not Share This Code With anybody.
This Is Your Secret Code.
Do Not Reply to this Email
For any Complaints contact us at
Mail - codeinterest27@gmail.com
Phone - +918799523738""")
                                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp3:
                                    smtp3.login(Sender_Email, Password)
                                    smtp3.send_message(newMessage)#'''
                        b=Button(r,text="Next",command=check_and,borderwidth=3,relief='solid',activeforeground='red',activebackground='white',bg='white',font='LUCIDA 15 bold').place(x=1000,y=700)
                    else:
                        l=Label(q,text="Invalid OTP",bg='white',fg='red',font='LUCIDA 15 bold').place(x=1100,y=700)
                b=Button(q,text="Verify",command=reset_pas,bg='white',borderwidth=3,relief='solid',activeforeground='red',activebackground='white',font='LUCIDA 15 bold').place(x=1000,y=700)
            if acc_n in acc:
                if card_n in card:
                    if ifsc_c in ifsc:
                        democursor.execute("select email,name from users where acc_no='"+acc_n+"' and card_n='"+card_n+"' and ifsc='"+ifsc_c+"'")
                        for i in democursor:
                            Email=i[0]
                            name=i[1]
                        otp(Email,name)
                    else:
                        l=Label(p,text="Invalid Input",bg='white',fg='red',font='LUCIDA 15 bold').place(x=1100,y=700)
                else:
                    l=Label(p,text="Invalid Input",bg='white',fg='red',font='LUCIDA 15 bold').place(x=1100,y=700)
            else:
                l=Label(p,text="Invalid Input",bg='white',fg='red',font='LUCIDA 15 bold').place(x=1100,y=700)
    b=Button(p,text="Next",command=next_p,bg='white',borderwidth=1,relief='solid',activebackground='white',width=6,font='LUCIDA 20 bold').place(x=1100,y=600)
l=Button(y,text='Forgot Login ID or Password?',bg='thistle3',activeforeground='black',activebackground='thistle3',borderwidth=0,command=forget_pas,font="LUCIDA 7 bold").place(x=1200,y=290)
import emoji
emojis=emoji.emojize(":eye:")
def shows():
    passs=passw.get()
    passw.set(passs)
    l=Entry(y,textvariable=passw,font="LUCIDA 15 bold").place(x=1400,y=210)
    def showes():
        passs=passw.get()
        passw.set(passs)
        l=Entry(y,textvariable=passw,show='*',font="LUCIDA 15 bold").place(x=1400,y=210)
        b=Button(y,text=emojis,command=shows,borderwidth=0,activebackground='thistle3',bg='thistle3',width=4,font='LUCIDA 11').place(x=1700,y=210)
    b=Button(y,text=emojis,command=showes,bg='thistle3',borderwidth=0,activebackground='thistle3',width=4,font='LUCIDA 11').place(x=1700,y=210)
l=Button(y,image=photo,borderwidth=3,relief='solid',bg='black',command=None,activebackground='black').place(x=50,y=110)
#y=1
b=Button(y,text=emojis,command=shows,bg='thistle3',activebackground='thistle3',borderwidth=0,width=4,font='LUCIDA 11').place(x=1700,y=210)
l=Button(y,image=photo1,command=None).place(x=1600,y=750)
l=Label(y,text="""

Hello,
Welcome to Bank Management System
This System is Made By Shivam Soni
Using Python and MySQL as Database


Thank You for Using our Bank Management System!!!!
You Can Continue by Creating an account or login into an account.""",bg='thistle3',font="LUCIDA 15 bold").place(x=180,y=610)
#st=Style()
def pins():
    l=Label(y,text='                                                        ',fg='red',bg='thistle3',font="LUCIDA 25 bold").place(x=1150,y=410)
    log=logid.get()     #Get Login ID
    log=log.lower()
    pasw=passw.get()    #Get Password
    if log=='' or log==' ' or pasw=='' or pasw==' ':    #Checking Null for Input
        l=Label(y,text='Please Enter Details!!',bg='thistle3',fg='red',font='LUCIDA 15 bold').place(x=1250,y=410)
    else:
        l=[]
        democursor=demodb.cursor()
        democursor.execute("select count(*) from user03")
        for i in democursor:
            p=int(i[0])
        democursor.execute("select userid from user03")
        for i in democursor:
            for j in range(p-2):
                l.append(i[j])
        
        if log in l:
            democursor.execute("select password from user03 where userid='"+log+"'")
            for i in democursor:
                if pasw==i[0]:
                    democursor.execute("select acc_no from user03 where userid='"+log+"'")
                    for k in democursor:
                        acc_n=k[0]
                    democursor.execute("select passcode from users where acc_no='"+acc_n+"' and password='"+pasw+"'")
                    for j in democursor:
                        if len(j[0])==4:
                            pin_4(log,pasw)
                        elif len(j[0])==6:
                            pin_6(log,pasw)
                else:
                    l=Label(y,text='Incorrect Password',bg='thistle3',fg='red',font='LUCIDA 15 bold').place(x=1250,y=410)
        else:
            l=Label(y,text=log+'-User Not Found',bg='thistle3',fg='red',font='LUCIDA 15 bold').place(x=1250,y=410)
def win_all():
    abc=True
    while abc:
        y.destroy()
        exit()
    else:
        exit()
b=Button(y,text='Exit',borderwidth=1,relief='solid',activebackground='red',command=win_all,bg='thistle3',font='LUCIDA 15 bold').place(x=10,y=10)
l=Button(y,text="Login",command=pins,bg='white',activebackground='skyblue',activeforeground='black',borderwidth=1,relief='solid',font="LUCIDA 15 bold").place(x=1600,y=270)
y.mainloop()
