from tkinter import *
# from tkinter.font import Font
from tkinter.font import Font

import geocoder
from PIL import ImageTk, Image
import cv2, os, pickle
import logging
import tkinter as tk
import cv2
import tkinter as tk
import cv2
from PIL import Image, ImageTk
import face_recognition
import pickle
import time
import numpy as np
from PIL import Image, ImageTk
import face_recognition
import pickle
import time
import numpy as np
import face_recognition as fr
from tkinter import simpledialog
from tkinter import messagebox
import datetime, face_recognition
import cv2
import pickle
import face_recognition
from tkinter import filedialog
import os
import glob
import datetime
import cv2
from win32gui import GetWindowText, GetForegroundWindow
import win32gui
from pynput import keyboard, mouse
from pynput.keyboard import Key
from pynput.mouse import Listener
import logging
import threading, time
import cv2
import pickle
import face_recognition
import numpy as np
import PIL.Image, PIL.ImageTk
import pyttsx3
import win32gui
from pynput import keyboard, mouse
from pynput.keyboard import Key
from pynput.mouse import Listener
from selenium import webdriver
from geopy.geocoders import GoogleV3
import requests
import time
import mysql.connector as mysql
import pynput

# from rwcc.thrd import *
# db = mysql.connect(host="52.66.188.47", user="testuser", passwd="ihealthpharm@123", database="rwc")
db = mysql.connect(host="localhost", user="root", passwd="root", database="rwc")
mycursor = db.cursor(buffered=True)
print(db)

flag = 0


class MasterWindow:

    def __init__(self, master):

        # self.top = Toplevel()
        self.os = None
        master.title("Auto Remote Working")
        master['bg'] = "#ECF0F9"
        # topframe = Frame(master)
        canvas = Canvas(master, width=1200, height=800, bg="#ECF0F9")
        canvas.pack()
        title = Label(master, text="Remote Working Companion", font=("bold", 30))
        title.place(x=300, y=33)

        my_font = Font(family="Rekha", size=30, weight="bold", slant="italic")
        self.clock_photo = PhotoImage(file=os.getcwd() + '/clock.png')
        self.cam_photo = PhotoImage(file=os.getcwd() + '/cam.png')
        self.upload_img_photo = PhotoImage(file=os.getcwd() + '/upimg.png')
        self.location_checkocation_photo = PhotoImage(file=os.getcwd() + '/location.png')
        self.register_button = tk.Button(master, text="Add", height=1, width=10, fg='white', bg='#172146',
                                         font="Verdana 19 bold",
                                         command=self.registerForm).place(x=900, y=100)

        # button_1.pack(side=RIGHT)

        self.location_checkogin_button = tk.Button(master, text="Start", height=1, width=10, fg='white', bg='#172146',
                                      activebackground="lightgreen",
                                      font="Verdana 19 bold", command=login).place(x=900, y=180)
        # button_2.pack(side=RIGHT, pady=10)

        self.location_checkogout_button = tk.Button(master, text="Stop", height=1, width=10, fg='white', bg='#172146',
                                       activebackground="red",
                                       font="Verdana 19 bold", command=cl.stopMonitor).place(x=900, y=260)
        # button_3.pack(side=RIGHT, pady=10)

        self.upload_img_button = tk.Button(master, text="Files", height=1, width=10, fg='white', bg='#172146',
                                           font="Verdana 19 bold", command=self.openFile).place(x=900, y=340)
        # button_3.pack(side=RIGHT, pady=10)
        self.exit_button = tk.Button(master, text="Exit", height=1, width=10, fg='white', bg='#172146',
                                     font="Verdana 19 bold", command=cl.exit).place(x=900, y=420)

        main_menu = Menu(root)
        root.config(menu=main_menu)
        #
        # self.frame1 = LabelFrame(master, text="Input", padx=5, pady=5)
        self.time_check = StringVar(master)
        self.check_bt = Checkbutton(master, text="Set Time", variable=self.time_check, offvalue="uncheck", onvalue="",
                                    state=DISABLED,
                                    activeforeground="green", width=5, compound=TOP).place(x=750, y=500)
        # self.check_bt.pack(fill=X, pady=10)
        self.image_check = StringVar(master)
        self.check_bt = Checkbutton(master, text="Upload Image", variable=self.image_check, offvalue="uncheck",
                                    onvalue="check",
                                    activeforeground="green", width=10, compound=TOP).place(x=840, y=500)
        # self.check_bt.pack(fill=X, pady=10)
        self.camera_check = StringVar(master)
        self.check_bt = Checkbutton(master, text="Set Camera", variable=self.camera_check, offvalue="cameraoff",
                                    onvalue="",
                                    state=DISABLED,
                                    activeforeground="green", width=10, compound=TOP).place(x=950, y=500)
        # self.check_bt.pack(fill=X, pady=10)
        self.location_check = BooleanVar()
        self.check_button = Checkbutton(master, text="Find Location", variable=self.location_check, onvalue="check",

                                        activeforeground="green", width=10, compound=TOP).place(x=1050, y=500)
        self.location_check.set(True)

        bottom_frame = Frame(master, pady=50)
        bottom_frame.pack(side=LEFT)
        left_frame = Frame(bottom_frame, bg='black')
        canvas = Canvas(left_frame, width=627, height=663)
        canvas.pack()

        canvas.create_image(50, 10, anchor=NW)
        left_frame.pack(side=LEFT)

        right_frame = Frame(bottom_frame, padx=50)
        bt_font = Font(family="Rekha", size=45, weight="bold", slant="italic")

        # check_bt=Checkbutton(rightframe,text="Set Time",variable=h, offvalue="uncheck",onvalue="check",activeforeground="green",selectcolor="red",width=50)
        # check_bt.pack()
        right_frame.pack(side=RIGHT)
        # self.frame1.pack()
        bottom_frame.pack()

        main_menu = Menu(root)
        root.config(menu=main_menu)

        file_menu = Menu(main_menu, tearoff=False)
        main_menu.add_cascade(label="More Options", menu=file_menu)
        file_menu.add_command(label="Open files")
        file_menu.add_separator()
        file_menu.add_command(label="Images")
        file_menu.add_separator()
        file_menu.add_command(label="Remote Working Count")
        file_menu.add_command(label="Remote Working Search")
        file_menu.add_separator()

        New_file = Menu(file_menu, tearoff=False)
        New_file.add_command(label=" Company Website")
        New_file.add_command(label="About")
        file_menu.add_cascade(label="More options")

        # self.root.minsize(1280, 800)
        # self.root.maxsize(1280, 800)
        # self.root.geometry("1280x750+150+150")
        # self.root.mainloop()

    def showImages(self):

        self.result = filedialog.askopenfile(initialdir=os.getcwd() + "/dataset_images/", title="Select file",
                                             filetypes=(("text", ".jpg"), ("all file", "*.*")))
        img = os.path.abspath(self.result.name)
        print(img)
        # photoimg = PhotoImage(os.getcwd()+"/dataset_images/"+ img)
        top = Toplevel()
        top.title("show images")
        button = Button(top, text="Exit", bg='red', command=top.destroy)
        button.pack(side=BOTTOM)
        cv_img = cv2.cvtColor(cv2.imread(img), cv2.COLOR_BGR2RGB)
        height, width, no_channels = cv_img.shape
        canvas = Canvas(top, width=width, height=height)
        canvas.pack()
        photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
        canvas.create_image(0, 0, image=photo, anchor=NW)
        top.mainloop()

    def openFile(self):
        self.result = filedialog.askopenfile(initialdir=os.getcwd(), title="Select file",
                                             filetypes=(("Remote Working files", ".csv"), ("all file", "*.*")))
        dir_ = os.path.basename(self.result.name)
        print(dir_)
        txt = self.result.read()
        top = Toplevel()
        top.title(dir_)
        button = Button(top, text="Exit", bg='red', command=top.destroy)
        button.pack(side=BOTTOM)
        top.geometry("400x400+150+150")
        top.configure()
        text_area = Text(top, undo=True)
        text_area.pack(fill=BOTH, expand=1)
        if self.result is not None:
            i = 1
            for c in txt:
                text_area.insert(END, c)

            exit_file = self.result.name
        self.result.close()

    def registerForm(self):
        self.top = Toplevel()
        # self.top.minsize(600, 500)
        # self.top.maxsize(700, 600)
        # self.top.geometry("1000x500+100+100")

        self.top.geometry('500x500')
        self.top.configure(bg='#ECF0F9')
        # top['bg'] = "#ECF0F9"
        self.top.title("Registration Form")

        def resetForm():
            Employee_ID.set('')
            errorLblEmployee["text"] = ''
            Contact.set('')
            errorLblPhone["text"] = ''
            FirstName.set('')
            errorLblFirst["text"] = ''
            LastName.set('')
            errorLblLast["text"] = ''

            Email.set('')
            errorLblEmail["text"] = ''
            with open('increment.txt', 'r') as inc:
                lines = inc.readlines()
                if lines:
                    previous = lines[-1]
                    previous_id = previous[2:]
                    print(previous_id)
                    increment_id = int(previous_id) + 1
                    next_id = "DC" + str(increment_id)
                    Employee_ID.set(next_id)
                else:
                    next_id = "DC100"
                    Employee_ID.set(next_id)

        Employee_ID = StringVar()
        FirstName = StringVar()
        LastName = StringVar()
        Email = StringVar()
        # var = IntVar()
        Employee_Role = StringVar()
        Designation = StringVar()
        Contact = StringVar()
        Manager = StringVar()
        Company = StringVar()
        Department = StringVar()

        with open('increment.txt', 'r') as inc:
            li = inc.readlines()
            if li:
                prv = li[-1]  # DC100
                prvs = prv[2:]
                j = int(prvs) + 1
                i = str('DC') + str(j)
                Employee_ID.set(i)
            else:
                i = 'DC' + str(100)
                Employee_ID.set(i)

        def save():
            print("hello")
            emp_id = Employee_ID.get()

            first_name = FirstName.get()
            last_name = LastName.get()
            email = Email.get()
            # gender = var.get()
            emp_role = Employee_Role.get()
            designation = Designation.get()
            contact_no = Contact.get()
            print(contact_no)
            manager = Manager.get()
            deptartment = Department.get()
            emp_company = Company.get()
            # co = str(contact)
            con = list(contact_no)
            row = emp_id
            regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

            for letter in FirstName.get():
                if not letter.isalpha() and letter not in "'-":
                    errorLblFirst["text"] = "* must be string"
                    return False
                else:
                    errorLblFirst["text"] = " "

                if first_name == " " or last_name == "" or email == " " or emp_role == " " or designation == " " or contact_no == " " or manager == " " or deptartment == " ":
                    errorLblPhone["text"] = "* all fields are required !"
                    print('do')

                elif not contact_no.isdigit() or len(con) != 10:
                    errorLblPhone["text"] = "* Must be 10-digit phone number "

                elif not re.search(regex, email):
                    errorLblPhone["text"] = "* Invalid Email "

                elif not deptartment.isalpha():
                    errorLblPhone["text"] = "* Digits are not allowed in department label"
                else:
                    # success()
                    errorLblPhone["text"] = " "

                    print(emp_id, first_name, last_name, emp_role, designation, contact_no, manager, deptartment)
                    with open("increment.txt", 'a+') as increase_file:

                        increase_file.write(row)
                        increase_file.seek(0)
                        increase_file.write('\n')
                        print()

            current_dates = datetime.datetime.now()
            date = current_dates.strftime("%I:%M:%S")
            d = datetime.date.today()
            known_face_encodings_list = []
            known_names = []
            known_lastname = []
            known_email = []
            employee_role = []
            designation = []
            phone = []
            manager_company = []
            Company_name = []
            department = []
            ids = []
            font = cv2.FONT_HERSHEY_SIMPLEX

            # creating image's directory
            try:
                cwd = os.getcwd()
                print(cwd)
                os.mkdir(cwd + "/dataset_images")
            except:
                print()

            def image_taker(dirctory_name, emp_id):
                cam = cv2.VideoCapture(0)
                counter = 0
                flag = 0
                while cam.isOpened():
                    frame = cam.read()[1]

                    # converting BGR frame to RGB frame
                    rgb_frame = frame[:, :, ::-1]

                    # getting locations of faces present
                    faces = fr.face_locations(rgb_frame)

                    for (top, right, bottom, left) in faces:
                        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

                    cv2.putText(frame, "Press 'C' -> capture image\n q -> Quit", (0, 35), font, 1.0,
                                (255, 255, 255), 2)
                    cv2.imshow("live", frame)
                    # handler
                    if cv2.waitKey(100) & 0xFF == ord('q'):
                        if flag == 0:
                            # remove if image is not created to avoid any issue
                            os.rmdir(dirctory_name)
                        break
                    if cv2.waitKey(100) & 0xFF == ord('c'):
                        # saving imaegs
                        cv2.imwrite(dirctory_name + "/image," + str(emp_id) + "," + str(counter) + ".jpg", frame)
                        flag = 1
                        print("captured")
                        cv2.destroyAllWindows()
                cam.release()
                cv2.destroyAllWindows()

            # setting up student Id
            choice = 'yes'
            # getting last student id and creating next id
            try:
                with open("ids.txt", 'rb') as file_data:
                    labels = pickle.load(file_data)
                emp_id = Employee_ID.get()
            except FileNotFoundError:
                emp_id = Employee_ID.get()

            while choice == 'yes':

                print(emp_id)
                #
                # emp_name = simpledialog.askstring("Input string", "Enter employee name: ")
                # if emp_name is None:
                #     break

                # defining directory name where images will be stored
                cwd = os.getcwd() + "/dataset_images/"
                dir_name = cwd + first_name + "," + str(
                    emp_id) + "," + last_name + "," + email + "," + emp_role + "," + str(designation) + "," + str(
                    contact_no) + "," + manager + "," + emp_company + "," + deptartment
                # using try to avoid error when directory is already present
                try:
                    os.mkdir(dir_name)
                    print("check")
                    if self.image_check.get() == "check":
                        result = filedialog.askopenfile(initialdir=os.getcwd(), title="Select file",
                                                        filetypes=(
                                                            ("Remote Working files", ".jpg"), ("all file", "*.*")))
                        image_path = os.path.abspath(result.name)
                        print(image_path)
                        counter = 0
                        flag = 0
                        frame = cv2.imread(image_path)
                        rgb_frame = frame[:, :, ::-1]
                        faces = fr.face_locations(rgb_frame)
                        for (top, right, bottom, left) in faces:
                            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                        cv2.putText(frame, '''Press 'C' -> capture image
                								q -> Quit''', (0, 35), font, 1.0, (255, 255, 255), 2)
                        # cv2.imshow("live",frame)
                        # if cv2.waitKey(100) & 0xFF==ord('q'):
                        cv2.imwrite(dir_name + "/image," + str(emp_id) + "," + str(counter) + ".jpg", frame)
                        flag = 1
                        print("captured")
                        cv2.destroyAllWindows()

                    else:
                        image_taker(dir_name, emp_id)
                        print("check")
                except:
                    messagebox.showerror("Error", "employee name already exits.")

                choice = messagebox.askquestion("Input string", "Add another:")
                if choice == 'yes':
                    emp_id = Employee_ID.get()

            data_set_dir_name = os.getcwd() + "/dataset_images"
            folder_names = os.listdir(data_set_dir_name)
            for i in folder_names:
                dir_name = data_set_dir_name + "/" + i
                face_names = os.listdir(dir_name)
                for face_name in face_names:
                    image_name = dir_name + "/" + face_name
                    print(image_name)

                    # loading images using face_recognition library
                    known_face = fr.load_image_file(image_name)
                    print(known_face)

                    # getting encodings of faces
                    known_face_encoding = fr.face_encodings(known_face)
                    if len(known_face_encoding) > 0:
                        known_face_encoding = fr.face_encodings(known_face)[0]
                        student_name = i.split(",")[0]
                        student_id_in = str(i.split(",")[1])
                        last_name = i.split(",")[2]
                        email = i.split(",")[3]
                        emp_role = i.split(",")[4]
                        designation = i.split(",")[5]
                        contact_no = i.split(",")[6]
                        manager = i.split(",")[7]
                        company = i.split(",")[8]
                        deptartment = i.split(",")[9]
                        # appending encodings,ids, names, last_name, email,gender,emp_role,desig,contact,manager,
                        # dept into lists 
                        known_face_encodings_list.append(known_face_encoding)
                        known_names.append(student_name)
                        ids.append(student_id_in)
                        known_lastname.append(last_name)
                        known_email.append(email)
                        employee_role.append(emp_role)
                        designation.append(designation)
                        phone.append(contact_no)
                        manager_company.append(manager)
                        Company_name.append(company)
                        department.append(deptartment)
                        sql = "insert into employee_details(Employee_Id,First_Name,Last_Name,Email,Employee_Role," \
                              "Designation,Contact,Manager,Company,Department) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                        val = (
                            emp_id, first_name, last_name, email, emp_role, designation, contact_no, manager,
                            emp_company,
                            deptartment)

                        mycursor.execute(sql, val)
                        db.commit()
                        print("details stored")

                    else:
                        print("fail")

            print(known_names)
            print(ids)
            print(known_lastname)
            print(known_email)
            print(employee_role)
            print(designation)
            print(phone)
            print(manager_company)
            print(Company_name)
            print(department)

            # storing data in files using pickle
            with open("encodings.txt", 'wb') as file_data:
                pickle.dump(known_face_encodings_list, file_data)

            with open("name.txt", 'wb') as file_data:
                pickle.dump(known_names, file_data)

            with open("ids.txt", 'wb') as file_data:
                pickle.dump(ids, file_data)

            with open("lastName.txt", 'wb') as file_data:
                pickle.dump(known_lastname, file_data)

            with open("email.txt", 'wb') as file_data:
                pickle.dump(known_email, file_data)

            with open("emp_role.txt", 'wb') as file_data:
                pickle.dump(employee_role, file_data)

            with open("designation.txt", 'wb') as file_data:
                pickle.dump(designation, file_data)

            with open("contact.txt", 'wb') as file_data:
                pickle.dump(phone, file_data)
            with open("manager.txt", 'wb') as file_data:
                pickle.dump(manager_company, file_data)

            with open('company_name.txt', 'wb') as file_data:
                pickle.dump(Company_name, file_data)

            with open("dept.txt", 'wb') as file_data:
                pickle.dump(department, file_data)

        def close():
            self.top.destroy()

        form_title = Label(self.top, text="Registration form", font=("bold", 20), background="#ECF0F9")
        form_title.place(x=150, y=53)

        id_label = Label(self.top, text="Employee ID", font=("bold", 10))
        id_label.place(x=80, y=130)

        id_entry = Entry(self.top, textvariable=Employee_ID, justify=LEFT, bg='pink')
        id_entry.configure(state='readonly')
        id_entry.config({"background": "pink"})
        # entry_1.insert({"bg":"pink"})
        id_entry.place(x=240, y=130)
        errorLblEmployee = Label(self.top, fg="red")
        errorLblEmployee.grid(row=4, column=4)
        # x=240, y=120

        fName_label = Label(self.top, text="FirstName", font=("bold", 10))
        fName_label.place(x=80, y=160)

        fName_entry = Entry(self.top, textvariable=FirstName)
        fName_entry.place(x=240, y=160)  # place(x=240, y=150)
        # place(x=240, y=150)
        errorLblFirst = Label(self.top, fg="red")
        errorLblFirst.grid(row=7, column=4)

        lName_label = Label(self.top, text="LastName", font=("bold", 10))
        lName_label.place(x=80, y=190)

        lName_entry = Entry(self.top, textvariable=LastName)
        lName_entry.place(x=240, y=190)  # place(x=240, y=180)
        errorLblLast = Label(self.top, fg="red")
        errorLblLast.grid(row=240, column=400)

        email_label = Label(self.top, text="Email", font=("bold", 10))
        email_label.place(x=80, y=220)  # place(x=68, y=210)

        email_entry = Entry(self.top, textvariable=Email)
        email_entry.place(x=240, y=220)
        errorLblEmail = Label(self.top, fg="red")
        errorLblEmail.grid(row=280, column=240)
        #
        role_label = Label(self.top, text="Employee Role", font=("bold", 10))
        role_label.place(x=80, y=250)  # place(x=70, y=240)

        role_entry = Entry(self.top, textvariable=Employee_Role)
        role_entry.place(x=240, y=250)  # place(x=240, y=240)

        des_label = Label(self.top, text="Designation", font=("bold", 10))
        des_label.place(x=80, y=280)

        des_entry = Entry(self.top, textvariable=Designation)
        des_entry.place(x=240, y=280)

        con_label = Label(self.top, text="Contact", font=("bold", 10), name="con")
        con_label.place(x=80, y=310)

        con_entry = Entry(self.top, textvariable=Contact)
        con_entry.place(x=240, y=310)
        errorLblPhone = Label(self.top, fg="red")
        errorLblPhone.grid(row=17, column=4)

        man_label = Label(self.top, text="Manager", font=("bold", 10))
        man_label.place(x=80, y=340)

        man_entry = Entry(self.top, textvariable=Manager)
        man_entry.place(x=240, y=340)

        com_label = Label(self.top, text="Company", font=("bold", 10))
        com_label.place(x=80, y=370)

        com_entry = Entry(self.top, textvariable=Company)
        com_entry.place(x=240, y=370)

        depart_label = Label(self.top, text="Department", font=("bold", 10))
        depart_label.place(x=80, y=400)

        depart_entry = Entry(self.top, textvariable=Department)
        depart_entry.place(x=240, y=400)

        Button(self.top, text='Submit', width=20, bg='#172146', fg='white', command=save).place(x=80, y=460)
        Button(self.top, text='Cancel', width=20, bg='#172146', fg='white', command=close).place(x=280, y=460)
        # Button(self.top, text='Reset', width=20, bg='indian red', fg='white', command=resetForm).place(x=180, y=360)

        self.top.mainloop()

        # defining directory name where images will be stored

    def login(self):  # start button
        global talk, start_time, name

        def save_att(emp_id, name_employee, lastName, email, emp_role, desig, contact, manager, company, dept):
            d = datetime.date.today()
            ids = []
            global flag

            current_dates = datetime.datetime.now()
            # time_now = current_dates.strftime("%I:%M:%S")
            file_name = d.strftime("%d_%B" + ".csv")
            print("hello")
            current_dates = datetime.datetime.now()
            dateshow = current_dates.strftime("%H")
            minuteshow = current_dates.strftime("%M")
            intdate = int(dateshow)
            event = ['morning', 'envening']

            current_time = current_dates.strftime('%H:%M:%S')
            Time_Out = '00:00:00'
            update_id = str(emp_id)
            global update_name
            global update_date
            update_name = name_employee

            update_date = current_dates.strftime('%Y-%m-%d')
            # time_now = current_dates.strftime("%I:%M:%S")
            tm_out = current_dates.strftime('%H:%M:%S')
            # if intdate < 14:
            #     file_name = d.strftime("%d_%B_" + event[0] + ".csv")
            # elif (intdate >= 14):
            #     file_name = d.strftime("%d_%B_" + event[1] + ".csv")

            try:
                with open(file_name, 'r+') as file_data:
                    file_data.seek(0)
                    print("read data")
                    for line in file_data:
                        id, name, last_name, mail, Emp_role, Desig, Contact, Manager, comp, Dept, state, dt = line.split(
                            ",")
                        ids.append(str(id))
                        print(ids)

                    if emp_id not in ids:
                        print("not present")
                        print("start...1")
                        sql = "INSERT INTO employee_monitor(Employee_Id,First_Name,Last_Name,Time_In,Time_Out," \
                              "Time_Duration,Today,Location_Latitude,Location_Longitude,Location_Name,Detection_Status," \
                              "Online_Status,Active_Window) VALUES(%s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "

                        val = (
                            str(emp_id), name_employee, lastName, current_dates.strftime('%H:%M:%S'), '00:00:00',
                            '00:00:00', current_dates.strftime('%Y-%m-%d'), "null", "null", "null", "null", 'null',
                            'null'

                        )
                        mycursor.execute(sql, val)
                        db.commit()
                        print("data stored")
                        file_data.write(str(
                            emp_id) + "," + name_employee + "," + lastName + "," + email + "," + emp_role + "," + desig + "," + str(
                            contact) + "," + manager + "," + company + "," + dept + ",p," + date + "\n")
                        file_data.seek(0)
                        print("marked", name_employee, "present")
                        flag = 0

                    else:
                        print("hello")
                        current_time = current_dates.strftime('%H:%M:%S')
                        Time_Out = '00:00:00'
                        update_id = str(emp_id)
                        update_date = current_dates.strftime('%Y-%m-%d')
                        # time_now = current_dates.strftime("%I:%M:%S")
                        tm_out = current_dates.strftime('%H:%M:%S')
                        mycursor.execute("SELECT First_Name FROM employee_monitor where Employee_Id=%s and Today=%s",
                                         (update_id, update_date))
                        exist_row = mycursor.fetchone()

                        print(exist_row)
                        if exist_row:
                            print("updating..")

                            mycursor.execute(
                                "UPDATE employee_monitor SET Time_Out=%s WHERE Time_Out =%s and First_Name=%s and "
                                "Today=%s",
                                (current_time, Time_Out, update_name, update_date))
                            db.commit()
                            print(mycursor.rowcount, "record(s) affected")
                            mycursor.execute(
                                "SELECT Time_In,Time_Out from employee_monitor where Employee_Id=%s and Today=%s",
                                (update_id, update_date))
                            a, b = mycursor.fetchone()
                            # diff=mycursor.execute("select TIMESTAMPDIFF(Time_In,Time_Out) from employee_monitor")
                            #
                            # lst = list(a)

                            datetimeFormat = '%H:%M:%S'
                            diff = datetime.datetime.strptime(str(b), datetimeFormat) \
                                   - datetime.datetime.strptime(str(a), datetimeFormat)

                            print("Difference:", diff)
                            mycursor.execute("update employee_monitor set Time_Duration=%s where Employee_Id=%s and "
                                             "First_Name=%s and Today=%s",
                                             (diff, update_id, update_name, update_date))
                            db.commit()

                            print("modified")
                            flag = 1
                            print(flag)
                            if flag == 1:
                                cl.stopMonitor()
                        else:
                            print("start...")
                            sql = "INSERT INTO employee_monitor(Employee_Id,First_Name,Last_Name,Time_In,Time_Out," \
                                  "Time_Duration,Today,Location_Latitude,Location_Longitude,Location_Name," \
                                  "Detection_Status," \
                                  "Online_Status,Active_Window) VALUES(%s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "

                            val = (
                                str(emp_id), name_employee, lastName, current_dates.strftime('%H:%M:%S'), '00:00:00',
                                '00:00:00',
                                current_dates.strftime('%Y-%m-%d'), "null", "null", "null", "null", "null", "null"

                            )
                            mycursor.execute(sql, val)
                            db.commit()
                            print("data stored")
                        #
                        file_data.write(str(
                            emp_id) + "," + name_employee + "," + lastName + "," + email + "," + emp_role + "," + desig + "," + str(
                            contact) + "," + manager + "," + company + "," + dept + ",p," + date + "\n")
                        file_data.seek(0)
                        print("marked", name_employee, "present")
            #             flag = 0
            except FileNotFoundError:
                print("not connected")

                with open(file_name, 'w') as file_data:

                    print(date)
                    file_data.write(str(
                        emp_id) + "," + name_employee + "," + lastName + "," + email + "," + emp_role + "," + desig + "," + str(
                        contact) + "," + manager + "," + company + "," + dept + ",p," + date + "\n")
                    print("file created")

                    current_dates = datetime.datetime.now()

                    # update_time = current_dates.strftime('%H:%M:%S')
                    Time_Out = '00:00:00'
                    update_id = str(emp_id)
                    update_date = current_dates.strftime('%Y-%m-%d')
                    current_time = current_dates.strftime("%I:%M:%S")
                    exist_row = mycursor.execute(
                        "SELECT First_Name FROM employee_monitor where Employee_Id=%s and Today=%s",
                        (update_id, update_date))
                    print("enter")
                    if exist_row == 1:
                        mycursor.execute("UPDATE employee_monitor SET Time_Out=%s WHERE Time_Out =%s and "
                                         "First_Name=%s and "
                                         "Today=%s",
                                         (current_time, Time_Out, update_name, update_date))
                        db.commit()
                        print(mycursor.rowcount, "record(s) affected")
                        # mycursor.execute("select TIMESTAMPDIFF(hour,Time_In,Time_Out) from emp_trail")
                    else:
                        print("start...2")
                        sql = "INSERT INTO employee_monitor(Employee_Id,First_Name,Last_Name,Time_In,Time_Out," \
                              "Time_Duration,Today,Location_Latitude,Location_Longitude,Location_Name,Detection_Status," \
                              "Online_Status,Active_Window) VALUES(%s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                        val = (
                            str(emp_id), name_employee, lastName, current_dates.strftime('%H:%M:%S'), '00:00:00',
                            '00:00:00',
                            current_dates.strftime('%Y-%m-%d'), "null", "null", "null", "null", 'null', 'null'
                        )
                        mycursor.execute(sql, val)
                        db.commit()
                        print("data stored")
                        flag = 0

        # setting font for puttext
        font = cv2.FONT_HERSHEY_SIMPLEX

        # laoding data files and storing in lists
        with open("encodings.txt", 'rb') as file_data:
            known_face_encodings = pickle.load(file_data)

        with open("name.txt", 'rb') as file_data:
            known_names = pickle.load(file_data)
            print(known_names)

        with open("ids.txt", 'rb') as file_data:
            student_ids = pickle.load(file_data)
            print(student_ids)
        with open("lastName.txt", 'rb') as file_data:
            known_lastname = pickle.load(file_data)
            print(known_lastname)
        with open("email.txt", 'rb') as file_data:
            known_email = pickle.load(file_data)
            print(known_email)
        with open("emp_role.txt", 'rb') as file_data:
            emp_role = pickle.load(file_data)
            print(emp_role)
        with open("designation.txt", 'rb') as file_data:
            desig = pickle.load(file_data)
            print(desig)
        with open("contact.txt", 'rb') as file_data:
            contact = pickle.load(file_data)
            print(contact)
        with open("manager.txt", 'rb') as file_data:
            manager = pickle.load(file_data)
            print(manager)
        with open('company_name.txt', 'rb') as file_data:
            Company_name = pickle.load(file_data)

        with open("dept.txt", 'rb') as file_data:
            dept = pickle.load(file_data)
            print(dept)

        if self.camera_check.get() == "cameraon":
            cameraNumber = simpledialog.askstring("Input string", "Camera Number or ip:port")
            print(cameraNumber)
            print(type(cameraNumber))
            if cameraNumber == '0' or cameraNumber == '1':
                camera = int(cameraNumber)
                print(camera)
                cam = cv2.VideoCapture(camera)

            else:
                os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;udp"
                st = "rtsp://" + cameraNumber + "/onvif1"
                # st="rtsp://"+cameraNumber+"/video?x.mjpg"
                print(st)
                cam = cv2.VideoCapture(st)

        else:
            cam = cv2.VideoCapture(0)
        if self.time_check.get() == "check":
            playtime = simpledialog.askinteger("Input string", "Enter Time in Minutes")
            capture_duration = playtime * 60
            start_time = time.time()
            time_play = int(time.time() - start_time)
        else:
            time_play = 1
            capture_duration = 2

        while time_play < capture_duration:
            frame = cam.read()[1]
            # converting BGR frame to RGB frame
            rgb_frame = frame[:, :, ::-1]

            # getting face locations
            face_locations = face_recognition.face_locations(rgb_frame)

            # getting face encodings
            current_dates = datetime.datetime.now()
            date = current_dates.strftime("%I:%M:%S")
            current_face_encoding = face_recognition.face_encodings(rgb_frame, face_locations)

            for (top, right, bottom, left), face_encoding in zip(face_locations, current_face_encoding):

                # comparing face with known faces
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                # print(matches)
                name = "unknown"

                if True in matches:
                    # getting index for matched face
                    match_index = matches.index(True)

                    # getting name of the person
                    # global name
                    name = known_names[match_index]
                    student_id_det = student_ids[match_index]
                    last_Name = known_lastname[match_index]
                    Email = known_email[match_index]
                    employee_role = emp_role[match_index]
                    phone = contact[match_index]
                    designation = desig[match_index]
                    manager_company = manager[match_index]
                    company_name = Company_name[match_index]
                    department = dept[match_index]

                    # current_dates = datetime.datetime.now()
                    # date = current_dates.strftime("%I:%M:%S")
                    def talk(name):

                        speech = messagebox.askquestion("confirm", "Are you sure, you are " + name + " ?")
                        if speech == 'yes':
                            engine = pyttsx3.init()
                            engine.say("Thank you")
                            engine.runAndWait()

                            save_att(student_id_det, name, last_Name, Email, employee_role, designation, phone,
                                     manager_company, company_name, department)
                            # display_ip(name)

                        if speech == "No":
                            print('please start again')


                else:
                    continue

                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 1)
                if self.time_check.get() == "check":
                    hk = int(time.time() - start_time)
                    cv2.putText(frame, str(hk), (0, 35), font, 1.0, (255, 255, 255), 2)
                    cv2.putText(frame, name, (left, top), font, 1.0, (255, 255, 255), 2)
                else:
                    cv2.putText(frame, name, (left, top), font, 1.0, (255, 255, 255), 2)
            if self.time_check.get() == "check":
                time_play = int(time.time() - start_time)

            cv2.imshow("Live", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cam.release()
        cv2.destroyAllWindows()
        engine = pyttsx3.init()
        engine.say("Are you" + name + " ?")
        engine.runAndWait()
        talk(name)
        print(flag)
        self.displayIP()
        T.run()

    def displayIP(self):
        """ Function To Print GeoIP Latitude & Longitude """

        ip_request = requests.get('https://get.geojs.io/v1/ip.json')
        my_ip = ip_request.json()['ip']
        geo_request = requests.get('https://get.geojs.io/v1/ip/geo/' + my_ip + '.json')
        geo_data = geo_request.json()
        x = str(geo_data['latitude'])
        y = str(geo_data['longitude'])
        print(x, y)

        geo_locator = GoogleV3(api_key='AIzaSyDGjLG4boPLUirqpbEQ71ea6zxB4dEkTiw')
        locations = geo_locator.reverse((geo_data['latitude'], geo_data['longitude']))
        # print(locations)
        if locations:
            z = str(locations[0].address).split()

            # print(z[10])
        mycursor.execute("UPDATE employee_monitor SET Location_latitude=%s, Location_Longitude=%s WHERE "
                         "Location_Latitude=%s "
                         "and Location_Longitude=%s", (x, y, 'null', 'null'))
        db.commit()
        print(mycursor.rowcount, "  location record(s) affected")

        db.commit()
        print(mycursor.rowcount, " row affected")

        # print(z[10])

    # display_ip()
    def openWeb(self):
        self.browser = webdriver.Chrome()
        self.browser.get('')

    def openSite(self):
        self.browser.get('https://www.derivativesconnect.com/')

    def remoteWorkingCount(self):
        self.os.chdir(os.getcwd())
        self.wordcount = {}
        self.top = Toplevel()
        self.top.title("Remote Working count")
        bt1 = Button(self.top, text="Exit", bg='red', command=self.top.destroy)
        bt1.pack(side=BOTTOM)
        self.top.geometry("400x400+150+150")
        text_area = Text(self.top, undo=True)
        text_area.pack(fill=BOTH, expand=1)
        new_list = []
        files_list = []
        for all_files in glob.glob("*.csv"):
            af = all_files
            files_list.append(af)

        print(files_list)

        for files in files_list:
            # d=datetime.date.today()
            # file_name=d.strftime("%B")
            # print(file_name)
            print(files)
            pk = re.search(r'\d\d\w(?:Jan|Feb|March|April|May|June|Jul|Aug|Sep|Oct|Nov|December).(?:csv)', files)
            if pk is None:
                print("files not found")
            else:
                mk = pk.group()
                print(mk)
                file = open(mk, "r+")
                new = file.read().split(',')

                for l in range(1, len(new), 3):
                    p = new[l]
                    new_list.append(p)

        print(new_list)
        for word in new_list:
            if word not in self.wordcount:
                self.wordcount[word] = 1

            else:
                self.wordcount[word] += 1

        print(self.wordcount)

        # for l in range(0,len(wordcount)+1):
        # k = wordcount[l]import win32con

        for k, v in self.wordcount.items():
            # print (k , v)

            text_area.insert(INSERT, k)
            text_area.insert(INSERT, "=")
            text_area.insert(INSERT, v)
            text_area.insert(INSERT, "\n")

    def searchRemoteWorking(self):
        hk1 = simpledialog.askstring("Input string", "Enter Search name")
        os.chdir(os.getcwd())
        wordcount = {}
        d = {}
        new_list = []
        files_list = []
        for all_files in glob.glob("*.csv"):
            af = all_files
            files_list.append(af)
        print(files_list)
        for files in files_list:
            pk = re.search(r'\d\d\w(?:Jan|Feb|March|April|May|June|Jul|Aug|Sep|Oct|Nov|December).(?:csv)', files)
            if pk is None:
                print("files not found")
            else:
                mk = pk.group()
                print(mk)
                file = open(mk, "r+")
                new = file.read().split(',')

                for l in range(1, len(new), 3):
                    p = new[l]
                    new_list.append(p)

        for word in new_list:
            if word not in wordcount:
                wordcount[word] = 1
            else:
                wordcount[word] += 1

        for k, v in wordcount.items():
            d[k] = str(v)

        if hk1 in d:
            messagebox.showinfo("Remote Working Count", "Successfully count\n\n" + "         " + d[hk1])
        else:
            messagebox.showerror("Error", '   ' + hk1 + "\nName Not Found")


class CountdownTask:

    def __init__(self):
        self._is_running = True

    def terminate(self):
        self._is_running = False

    def run(self):
        current_title = None
        while self._is_running:
            moment2 = datetime.datetime.now().strftime(" %H:%M:%S")
            new_title = GetWindowText(GetForegroundWindow())
            if new_title != current_title:
                if len(new_title) > 0:
                    # logging.info(" Moved to : " + new_title)
                    current_title = new_title
                    time.sleep(0.1)
                    # print(new_title)
                    ff = (moment2 + " : " + "Moved T0 : " + new_title)
                    mycursor.execute("UPDATE employee_monitor SET Active_Window=%s WHERE First_Name=%s and Today=%s",
                                     (ff, update_name, update_date))

                    print(ff)

    def do_run(self):
        global lmain
        global cam
        width, height = 800, 600
        # Set up GUI
        self.top = Toplevel()
        self.top.withdraw()
        # Create a frame
        app = Frame(self.top, bg="white")
        app.grid()
        # Create a label in the frame
        lmain = Label(app)
        lmain.grid()
        # top.withdraw()
        # Graphics window
        sdThresh = 10
        font = cv2.FONT_HERSHEY_SIMPLEX
        # if flag < 1:
        cam = cv2.VideoCapture(0)

        facecount = 0

        def show_frame():
            global name

            def distMap():
                """outputs pythagorean distance between two frames"""
                frame1_32 = np.float32(frame1)
                frame2_32 = np.float32(frame2)
                diff32 = frame1_32 - frame2_32
                norm32 = np.sqrt(
                    diff32[:, :, 0] ** 2 + diff32[:, :, 1] ** 2 + diff32[:, :, 2] ** 2) / np.sqrt(
                    255 ** 2 + 255 ** 2 + 255 ** 2)
                dist = np.uint8(norm32 * 255)
                return dist

            _, frame1 = cam.read()
            _, frame2 = cam.read()

            _, frame = cam.read()

            rows, cols, _ = np.shape(frame)
            # cv2.imshow('dist', frame3)
            frame = cv2.flip(frame, 1)
            dist = distMap()
            # converting BGR frame to RGB frame
            rgb_frame = frame[:, :, ::-1]

            # gettting face locations
            face_locations = face_recognition.face_locations(rgb_frame)

            # getting face encodings
            current_face_encoding = face_recognition.face_encodings(rgb_frame, face_locations)

            # apply Gaussian smoothing
            mod = cv2.GaussianBlur(dist, (9, 9), 0)

            # apply thresholding
            _, thresh = cv2.threshold(mod, 100, 255, 0)

            # calculate st dev test
            _, stDev = cv2.meanStdDev(mod)

            # cv2.imshow('dist', mod)

            # cv2.putText(frame2, "Standard Deviation - {}".format(round(stDev[0][0], 0)), (70, 70), font, 1,
            #             (255, 0, 255),
            #             1,
            #             cv2.LINE_AA)

            with open("encodings.txt", 'rb') as file_data:
                known_face_encodings = pickle.load(file_data)

            with open("name.txt", 'rb') as file_data:
                known_names = pickle.load(file_data)

            with open("ids.txt", 'rb') as file_data:
                student_ids = pickle.load(file_data)

            for (top, right, bottom, left), face_encoding in zip(face_locations,
                                                                 current_face_encoding):

                # compariong face with known faces
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                # print(matches)
                name = "unknown"
                if True in matches:
                    # getting index for matched face
                    match_index = matches.index(True)

                    # getting name of the person
                    name = known_names[match_index]
                    student_id_det = student_ids[match_index]
                else:
                    continue

                # cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 1)
                # cv2.putText(frame, (0, 35), font, 1.0, (255, 255, 255), 2, "Standard Deviation - {}".format(round(stDev[0][0], 0)), (70, 70))
                # # cv2.putText(frame, name, (left, top), font, 1.0, (255, 255, 255), 2)
                # # else:
                cv2.putText(frame, name + " " + "Standard Deviation - {}".format(
                    round(stDev[0][0], 0)),
                            (70, 70), font, 1,
                            (255, 0, 255))
                print(name)
                # if (h.get() == "check"):
                # print("Standard Deviation - {}".format(round(stDev[0][0], 0)))

            if stDev > sdThresh:

                print('is there')
                det_std = name + " is there"
                mycursor.execute("UPDATE employee_monitor SET Detection_Status=%s WHERE "
                                 "First_Name=%s and Today=%s", (det_std, name, update_date))
                db.commit()
                print(mycursor.rowcount, " row affected")
                print("Motion detected.. Do something!!!")
                time.sleep(2)

            else:

                print('not there')
                det_std = name + " is not there"
                mycursor.execute(
                    "UPDATE employee_monitor SET Detection_Status=%s WHERE First_Name=%s and Today=%s",
                    (det_std, name, update_date))
                db.commit()
                print(mycursor.rowcount, " row affected")
                print("employee is not working now")
                time.sleep(1)
                # TODO: Face Detection 2

            # cv2.imshow('frame', frame)
            # scale_percent = 70
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            # width = int(cv2image.shape[1] * scale_percent / 100)
            # height = int(cv2image.shape[0] * scale_percent / 100)
            # dim = (width, height)
            # resize image
            resized = cv2.resize(cv2image, (380, 280))
            img = Image.fromarray(resized)
            img_tk = ImageTk.PhotoImage(image=img)
            lmain.img_tk = img_tk
            lmain.configure(image=img_tk)
            c = lmain.after(1, show_frame)

        Button(self.top, text="Quit", command=lmain.destroy).grid(row=1, column=0)
        Button(self.top, text="Quit", command=cam.release).grid(row=1, column=2)
        # Slider window (slider controls stage position)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            lmain.destroy()
            cam.release()
            cv2.destroyAllWindows()
            self.top.destroy()
        show_frame()  # Display 2
        self.top.mainloop()


c = CountdownTask()
t = threading.Thread(target=c.do_run)
t1 = threading.Thread(target=c.run)


class Monitor:

    def __init__(self):
        # super().__init__(master)
        self._is_running = True

    def terminate(self):
        self._is_running = False

    def startMonitoring(self):
        global previous_state, current_state, readable_time, time_now, disconnected_time, listener
        previous_state = 'Monitoring started'
        current_state = 'Monitoring started'
        readable_time = None
        time_now = None
        disconnected_time = None
        time_now = datetime.datetime.now()
        readable_time = datetime.date.strftime(time_now, "%Y/%m/%d - %H:%M:%S")

        file = open('connection-log.txt', 'a')
        file.write(readable_time + ' - Mouse Monitoring started\n')
        file.close()
        print(readable_time + ' - ' + current_state)

        while self._is_running:
            time_now = datetime.datetime.now()
            readable_time = datetime.datetime.strftime(time_now, "%Y/%m/%d - %H:%M:%S")
            listener = mouse.Listener(on_click=on_click, on_move=on_move)
            try:
                listener.join()
                # if cl.stopmonitor:
                #     m_listener.stop()
                #     pynput.mouse.Listener.stop()
            except:
                pass

            program_run = onClick
            move = onMove

            if program_run or move != previous_state:
                file = open('connection-log.txt', 'a')
                if program_run or move == True:
                    print('Mouse last used- > ' + readable_time)
                    file.write(readable_time + ' - Online\n')
                    file.close()

                else:
                    file.close()

                previous_state = program_run, move

            time.sleep(10)

    def startMonitoringMouse(self):
        global previous_state, current_state, readable_time, time_now, disconnected_time, listener
        previous_state = 'Monitoring started'
        current_state = 'Monitoring started'
        readable_time = None
        time_now = None
        disconnected_time = None
        time_now = datetime.datetime.now()
        readable_time = datetime.date.strftime(time_now, "%Y/%m/%d - %H:%M:%S")

        file = open('connection-log.txt', 'a')
        file.write(readable_time + ' - Mouse Monitoring started\n')
        file.close()
        print(readable_time + ' - ' + current_state)

        while self._is_running:
            time_now = datetime.datetime.now()
            readable_time = datetime.datetime.strftime(time_now, "%Y/%m/%d - %H:%M:%S")
            listener = keyboard.Listener(on_press=on_press, on_release=on_release)
            try:
                listener.join()

                # if cl.stopmonitor:
                #     k_listener.stop()
                #     pynput.keyboard.Listener.stop()
            except:
                pass

            program_run = onPress
            key = onRelease

            if program_run or key != previous_state:
                file = open('connection-log.txt', 'a')
                if program_run or key == True:
                    print('keyboard last used- > ' + readable_time)
                    file.write(readable_time + ' - Online\n')
                    file.close()

                else:
                    file.close()

                previous_state = program_run, key

            time.sleep(100)


def onClick(x, y, button, pressed):
    if pressed:
        # logging.info('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))
        # print('clicked')
        return True
    if previous_state:
        # print('no clicks')
        return False


def onMove(x, y):
    if onMove:
        return True
    if previous_state:
        return False


def onPress(key):
    if hasattr(key, 'char'):
        return True
    if previous_state:
        return False


def onRelease(key):
    if hasattr(key, 'char'):
        return True
    if previous_state:
        return False


m = Monitor()
t2 = threading.Thread(target=m.startMonitoring)
t3 = threading.Thread(target=m.startMonitoringMouse)


# ...
class close(CountdownTask, MasterWindow):

    def exit(self):

        answer = messagebox.askquestion("exit", "Are you sure to exit")
        if answer == 'yes':
            m.terminate()
            c.terminate()
            root.quit()

    def stopMonitor(self):
        global lmain
        global cam
        global listener
        m.terminate()
        c.terminate()
        lmain.destroy()
        cam.release()
        c.top.destroy()
        if listener:
            listener.stop()
            listener.join()
            listener = None


cl = close()


class ThreadStart(threading.Thread):
    def run(self):
        if flag == 0:
            t1.start()
            t.start()
            t2.start()
            t3.start()


T = ThreadStart()

# Wait for actual termination (if needed)
if __name__ == "__main__":
    root = Tk()
    root['bg'] = "#ECF0F9"
    # root.configure(background='blue')
    main_ui = MasterWindow(root)

    # t3.start()
    root.mainloop()
