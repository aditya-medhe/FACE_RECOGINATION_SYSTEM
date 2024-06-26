from tkinter import *
from tkinter import ttk 
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import csv
import numpy as np
from PIL import Image
import pandas as pd
import datetime
class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
         #******** variables*********#
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
         # first image 
        img = Image.open(r"C:\Users\Admin\Documents\FACE_RECOGINATION_SYSTEM\college_images\face-recognition.png")
        img = img.resize((500, 130), Image.LANCZOS) # Changed from ANTIALIAS to LANCZOS
        self.photoimg= ImageTk.PhotoImage(img)
        
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)
        
        #second image 
        img1 = Image.open(r"C:\Users\Admin\Documents\FACE_RECOGINATION_SYSTEM\college_images\smart-attendance.jpg")
        img1 = img1.resize((500, 130), Image.LANCZOS) # Changed from ANTIALIAS to LANCZOS
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=130)
        
        # Third Image
        img2 = Image.open(r"C:\Users\Admin\Documents\FACE_RECOGINATION_SYSTEM\college_images\attend1.jpg")
        img2 = img2.resize((500, 130), Image.LANCZOS) # Changed from ANTIALIAS to LANCZOS
        self.photoimg2 = ImageTk.PhotoImage(img2)
        
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=450, height=130)
        
        
         
         #bg Image
         
        img3 = Image.open(r"C:\Users\Admin\Documents\FACE_RECOGINATION_SYSTEM\college_images\wp2551980.jpg")
        img3 = img3.resize((1530, 700), Image.LANCZOS) # Changed from ANTIALIAS to LANCZOS"
        self.photoimg3 = ImageTk.PhotoImage(img3)
        
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=100, width=1500, height=700)
        
        title_lbl=Label(bg_img,text="STUDENT MANAGHEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1400,height=44)
        
        
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=45,width=1300,height=700)
        
        # left label frame
        
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Detalis",font=("times new roman",12,"bold",))
        Left_frame.place(x=10,y=10,width=620,height=580)
        
        img_left = Image.open(r"C:\Users\Admin\Documents\FACE_RECOGINATION_SYSTEM\college_images\attend1.jpg")
        img_left = img_left.resize((500, 130), Image.LANCZOS) # Changed from ANTIALIAS to LANCZOS
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        
        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=620, height=130)
        
        # current course
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current course information",font=("times new roman",12,"bold",))
        current_course_frame.place(x=5,y=138,width=700,height=115)
        
        # department
        
        dep_label=Label(current_course_frame,text="Department",textvariable=self.var_dep,font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10)
       
        dep_combo=ttk.Combobox(current_course_frame,font=("times new roman",12,"bold"),state="readonly")
        dep_combo["values"]=("Select department","computer","IT","civil","mechnical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1)
        dep_combo.grid(row=0,column=1,padx=2,pady=5)
        
         # course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10)
        
        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly")
        course_combo["values"]=("Select Course","computer","IT","civil","mechnical")
        course_combo.current(0)
        course_combo.grid(row=0,column=3)
        course_combo.grid(row=0,column=3,padx=2,pady=5)
        
        # year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10)
        
        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly")
        year_combo["values"]=("Select Year","20-2021","21-2022","22-2023","23-2024")
        year_combo.current(0)
        year_combo.grid(row=1,column=1)
        year_combo.grid(row=1,column=1,padx=2,pady=5)
        
        
        # semester
        semester_label=Label(current_course_frame,text="semester",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10)
        
        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="readonly")
        semester_combo["values"]=("Select semester","computer","IT","civil","mechnical")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3)
        semester_combo.grid(row=1,column=3,padx=2,pady=5)
        
         #  class Student information
        class_Student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold",))
        class_Student_frame.place(x=5,y=250,width=700,height=280)
        
        #student Id
        studentId_label=Label(class_Student_frame,text="StudentID",font=("times new roman",12,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10)
        
        studentID_entry=ttk.Entry(class_Student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",12,"bold"))
        studentID_entry.grid(row=0,column=1,padx=5)
        
        #student name
        studentName_label=Label(class_Student_frame,text="Student Name",font=("times new roman",12,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10)
        
        studentName_entry=ttk.Entry(class_Student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",12,"bold"))
        studentName_entry.grid(row=0,column=3,padx=5)
        
        #class dibvision
        
        class_div_label=Label(class_Student_frame,text="Class Division",font=("times new roman",12,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5)
        
       
        
        div_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),state="readonly")
        div_combo["values"]=("A","B","C")
        div_combo.current(0)
        div_combo.grid(row=1,column=1)
        div_combo.grid(row=1,column=1,padx=2,pady=5)
        
        
        # Roll No
        
        Roll_no_label=Label(class_Student_frame,text="Roll NO:",font=("times new roman",12,"bold"),bg="white")
        Roll_no_label.grid(row=1,column=2,padx=10,pady=5)
        
        Roll_no_entry=ttk.Entry(class_Student_frame,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        Roll_no_entry.grid(row=1,column=3,padx=10,pady=5)
        
        #Gender
        
        gender_label=Label(class_Student_frame,text="Gender",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5)
        
       
        
        gender_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="readonly")
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=1,column=1)
        gender_combo.grid(row=2,column=1,padx=2,pady=5)
        
        
        
        
        # DoB
        dob_label=Label(class_Student_frame,text="DOB:",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5)
        
        dob_entry=ttk.Entry(class_Student_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5)
        
        # Email
        
        email_label=Label(class_Student_frame,text="email:",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5)
        
        email_entry=ttk.Entry(class_Student_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5)
        
        #phone no
        
        phone_label=Label(class_Student_frame,text="Phone no:",font=("times new roman",12,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5)
        
        phone_entry=ttk.Entry(class_Student_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5)
        
        # Address
        
        address_label=Label(class_Student_frame,text="Address",font=("times new roman",12,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5)
        
        address_entry=ttk.Entry(class_Student_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5)
          
          
          # Teacher name
          
        teacher_label=Label(class_Student_frame,text="Teacher Name:",font=("times new roman",12,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5)
        
        teacher_entry=ttk.Entry(class_Student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",12,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5)
        
        # radio buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1, text="Take Photo Sample",value="yes")
        radiobtn1.grid(row=6,column=0)
        
        self.var_radio2=StringVar()
        radiobtn2=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=6,column=1)
        
        # bbutton frame
        btn_frame=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=715,height=40)
        
        #save
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=16,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0,)
        
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=16,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1,)
        
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=16,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2,)
        
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=16,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3,)
        
        btn_frame1=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=230,width=715,height=40)
        
        take_photo_btn=Button(btn_frame1,text="Take Photo Sample",command=self.generate_dataset,width=35,font=("times new roman",12,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0,)
        
        update_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=35,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1,)
        
        
        #right  label frames
        
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Detalis",font=("times new roman",12,"bold",))
        Right_frame.place(x=600,y=10,width=700,height=580)

        img_right = Image.open(r"C:\Users\Admin\Documents\FACE_RECOGINATION_SYSTEM\college_images\student.jpg")
        img_right = img_left.resize((500, 130), Image.LANCZOS) # Changed from ANTIALIAS to LANCZOS
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        
        f_lbl = Label(Right_frame, image=self.photoimg_right)
        f_lbl.place(x=5, y=0, width=620, height=130)
        
        
        
      #************Search System ************#
         # frame
        search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold",))
        search_frame.place(x=5,y=135,width=685,height=70)
        
        search_label=Label(search_frame,text=" Search By:",font=("times new roman",12,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),state="readonly",width=15)
        search_combo["values"]=("Select ","Roll_No","Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10)
        
        search_entry=ttk.Entry(search_frame,width=15,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5)
        
        
        # buttons
        search_btn=Button(search_frame,text="Search",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)
        
        showAll_btn=Button(search_frame,text="Show All",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=4)
        
        #************table frame ****************#
        
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=685,height=350)
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="photoSampleStatus")
        self.student_table["show"]="headings"
        
        
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
        #*****************function decreation******************#
        
    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
              try:
               conn = mysql.connector.connect(host="localhost", username="root", password="programmer@123", database="face_recognizer")
               my_cursor = conn.cursor()
               my_cursor.execute(
                "insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_id.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get()
                ))
            
               conn.commit()
               self.fetch_data()
               conn.close()
               messagebox.showinfo("Success", "Student details has been added Successfully", parent=self.root)
              except Exception as es:
               messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)
               
                 
      # ***************fetch data*****************
    def  fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="programmer@123",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
        
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
        #********** get cursor**********
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])
        
        #***********Update function***********
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
          try:
                Update=messagebox.askyesno("Update","Do you want to update this student detalis",parent=self.root)
                if Update>0:
                 conn=mysql.connector.connect(host="localhost",username="root",password="programmer@123",database="face_recognizer")
                 my_cursor=conn.cursor()
                 my_cursor.execute("update student set Dep=%s, course=%s, Year=%s, Semester=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s where Student_id=%s",
                                (
                  
                                    self.var_dep.get(),
                                    self.var_course.get(),
                                    self.var_year.get(),
                                    self.var_semester.get(),
                                    self.var_std_name.get(),
                                    self.var_div.get(),
                                    self.var_roll.get(),
                                    self.var_gender.get(),
                                    self.var_dob.get(),
                                    self.var_email.get(),
                                    self.var_phone.get(),
                                    self.var_address.get(),
                                    self.var_teacher.get(),
                                    self.var_std_id.get()
                                        
                                ))
                else:
                   if  not Update:
                        return
                messagebox.showinfo("success","Student detalis successfully update completed",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
          except Exception as es:
            messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root) 
   #delete function
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="programmer@123",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id = %s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                    
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Sucessfully deleted student detalis",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
       # reset
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_radio1.set("")

    
        

        # generate data set or Take photo sample **********
    def generate_dataset(self):
     if self.var_dep.get()=="Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
     else:
          try:
                conn=mysql.connector.connect(host="localhost",username="root",password="programmer@123",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for X in myresult:
                    id+=1
                my_cursor.execute("update student set Dep=%s, course=%s, Year=%s, Semester=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s where Student_id=%s",
                                 (
                    
                                        self.var_dep.get(),
                                         self.var_course.get(),
                                        self.var_year.get(),
                                        self.var_semester.get(),
                                        self.var_std_name.get(),
                                        self.var_div.get(),
                                        self.var_roll.get(),
                                        self.var_gender.get(),
                                        self.var_dob.get(),
                                        self.var_email.get(),
                                        self.var_phone.get(),
                                        self.var_address.get(),
                                        self.var_teacher.get(),
                                        self.var_std_id.get()==id+1
                                            
                                    ))
                
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

    #========== Load predifiend data on face frontals from opencv================================


                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                           #scaling factor=1.3
                           #minimum neighbor=5

                    for(x,y,w,h) in faces:
                       face_cropped=img[y:y+h,x:x+w]
                       return face_cropped

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                   ret,my_frame=cap.read()
                   if ret:
                    cv2.imshow("Original Face", my_frame)
                    if face_cropped(my_frame) is not None:
                       img_id+=1
                       face_image=cv2.resize(face_cropped(my_frame),(450,450))
                       face_image=cv2.cvtColor(face_image,cv2.COLOR_BGR2GRAY)
                       file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                       cv2.imwrite(file_name_path, face_image)
                       cv2.putText(face_image,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                       cv2.imshow("Cropped Face",face_image)


                   if cv2.waitKey(1)==13 or int(img_id)==100:
                       break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("result","Generating data sets completes!!!")
          except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)      

if __name__ == "__main__": 
    root = Tk() 
    obj = Student(root) 
    root.mainloop()