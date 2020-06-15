from tkinter import *
import datetime

rt1 = Toplevel()
# rt1.geometry('600x600')
rt1.minsize(600, 500)
rt1.maxsize(700, 600)
rt1.geometry("1000x500+100+100")

rt1.title("Registration Form")
currentDT = datetime.datetime.now()
date = currentDT.strftime("%I:%M:%S")
d = datetime.date.today()


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
        li = inc.readlines()
        if li:
            prv = li[-1]
            prvs = prv[2:]
            print(prvs)
            j = int(prvs) + 1
            i = "DC" + str(j)
            Employee_ID.set(i)
        else:
            i = "DC100"
            Employee_ID.set(i)


def save():
    print("hello")
    emp_id = Employee_ID.get()

    firstName = FirstName.get()
    lastName = LastName.get()
    email = Email.get()
    # gender = var.get()
    emp_role = Employee_Role.get()
    desig = Designation.get()
    contact = Contact.get()
    print(contact)
    manager = Manager.get()
    dept = Department.get()
    # co = str(contact)
    con = list(contact)
    row = emp_id
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    for letter in FirstName.get():
        if not letter.isalpha() and letter not in "'-":
            errorLblFirst["text"] = "* must be string"
            return False
        else:
            errorLblFirst["text"] = " "

    if firstName == " " or lastName == "" or email == " " or emp_role == " " or desig == " " or contact == " " or manager == " " or dept == " ":
        errorLblPhone["text"] = "* all fields are required !"
        print('do')

    elif not contact.isdigit() or len(con) != 10:
        errorLblPhone["text"] = "* Must be 10-digit phone number "
    elif not re.search(regex, email):
        errorLblPhone["text"] = "* Invalid Email "

    elif not dept.isalpha():
        errorLblPhone["text"] = "* Digits are not allowed in department label"
    else:
        # success()
        errorLblPhone["text"] = " "

        print(emp_id, firstName, lastName, emp_role, desig, contact, manager, dept)
        with open("increment.txt", 'a+') as incr:

            incr.write(row)
            incr.seek(0)
            incr.write('\n')
            print()

        # emp_details = d.strftime("%d_%B" + ".csv")
        # with open(emp_details, 'a')as file_data:
        #     print(date)
    #
    #     file_data.write(str(
    #         emp_id) + " , " + firstName + "," + lastName + " , " + email + " , " + " , " + emp_role + " , " + desig + " , " + contact + " , " + manager + " , " + dept + "," + date + "\n")
    #     print("file created")
    # # file_data.close()


def close():
    rt1.destroy()


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
        i = 'DC' + str(j)
        Employee_ID.set(i)
    else:
        i = 'DC' + str(100)
        Employee_ID.set(i)

label_0 = Label(rt1, text="Registration form", font=("bold", 20), background="SlateGray2")
label_0.place(x=150, y=53)

label_1 = Label(rt1, text="Employee ID", font=("bold", 10))
label_1.place(x=80, y=130)

entry_1 = Entry(rt1, textvariable=Employee_ID, justify=LEFT, bg='pink')
entry_1.configure(state='readonly')
entry_1.config({"background": "pink"})
# entry_1.insert({"bg":"pink"})
entry_1.place(x=240, y=130)
errorLblEmployee = Label(rt1, fg="red")
errorLblEmployee.grid(row=4, column=4)
# x=240, y=120

label_2 = Label(rt1, text="FirstName", font=("bold", 10))
label_2.place(x=80, y=160)

entry_2 = Entry(rt1, textvariable=FirstName)
entry_2.place(x=240, y=160)  # place(x=240, y=150)
# place(x=240, y=150)
errorLblFirst = Label(rt1, fg="red")
errorLblFirst.grid(row=7, column=4)

label_3 = Label(rt1, text="LastName", font=("bold", 10))
label_3.place(x=80, y=190)

entry_3 = Entry(rt1, textvariable=LastName)
entry_3.place(x=240, y=190)  # place(x=240, y=180)
errorLblLast = Label(rt1, fg="red")
errorLblLast.grid(row=240, column=400)

label_4 = Label(rt1, text="Email", font=("bold", 10))
label_4.place(x=80, y=220)  # place(x=68, y=210)

entry_4 = Entry(rt1, textvariable=Email)
entry_4.place(x=240, y=220)
errorLblEmail = Label(rt1, fg="red")
errorLblEmail.grid(row=280, column=240)
#
label_6 = Label(rt1, text="Employee Role", font=("bold", 10))
label_6.place(x=80, y=250)  # place(x=70, y=240)

entry_6 = Entry(rt1, textvariable=Employee_Role)
entry_6.place(x=240, y=250)  # place(x=240, y=240)

label_7 = Label(rt1, text="Designation", font=("bold", 10))
label_7.place(x=80, y=280)

entry_7 = Entry(rt1, textvariable=Designation)
entry_7.place(x=240, y=280)

label_8 = Label(rt1, text="Contact", font=("bold", 10), name="con")
label_8.place(x=80, y=310)

entry_8 = Entry(rt1, textvariable=Contact)
entry_8.place(x=240, y=310)
errorLblPhone = Label(rt1, fg="red")
errorLblPhone.grid(row=17, column=4)

label_9 = Label(rt1, text="Manager", font=("bold", 10))
label_9.place(x=80, y=340)

entry_9 = Entry(rt1, textvariable=Manager)
entry_9.place(x=240, y=340)

label_10 = Label(rt1, text="Company", font=("bold", 10))
label_10.place(x=80, y=370)

entry_10 = Entry(rt1, textvariable=Company)
entry_10.place(x=240, y=370)

label_11 = Label(rt1, text="Department", font=("bold", 10))
label_11.place(x=80, y=400)

entry_11 = Entry(rt1, textvariable=Department)
entry_11.place(x=240, y=400)

Button(rt1, text='Submit', width=20, bg='pink', fg='black', command=save).place(x=80, y=460)
Button(rt1, text='Cancel', width=20, bg='indian red', fg='white', command=close).place(x=280, y=460)
# Button(rt1, text='Reset', width=20, bg='indian red', fg='white', command=resetForm).place(x=180, y=360)

rt1.mainloop()
