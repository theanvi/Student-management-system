import tkinter as tk
from tkinter import ttk, messagebox

students = []


def studentadd():
    name = entryname.get()
    enrollment = entryenrollment.get()
    branch = boxbranch.get()
    semester = boxsemster.get()
    marks = entrymarks.get()

    if name == "" or enrollment == "" or branch == "" or semester == "" or marks == "":
        messagebox.showwarning("Missing Information", "Please fill all the fields.")
        return

    if not marks.isdigit() or int(marks) < 0 or int(marks) > 100:
        messagebox.showerror("Invalid Marks", "Marks must be between 0 and 100.")
        return

    for student in students:
        if student[1] == enrollment:
            messagebox.showerror("Duplicate Enrollment", "This enrollment number already exists.")
            return

    student = (name, enrollment, branch, semester, marks)
    students.append(student)

    tablestudents.insert("", "end", values=student)

    studentclear()
    messagebox.showinfo("Success", "Student added successfully.")


def studentclear():
    entryname.delete(0, tk.END)
    entryenrollment.delete(0, tk.END)
    boxbranch.set("")
    boxsemster.set("")
    entrymarks.delete(0, tk.END)


def studentdelete():
    selected = tablestudents.selection()

    if not selected:
        messagebox.showwarning("No Selection", "Please select a student to delete.")
        return

    itemselected = selected[0]
    student = tablestudents.item(itemselected, "values")

    for record in students:
        if record[1] == student[1]:
            students.remove(record)
            break

    tablestudents.delete(itemselected)
    studentclear()

    messagebox.showinfo("Success", "Student deleted successfully.")


def studentupdate():
    selected = tablestudents.selection()

    if not selected:
        messagebox.showwarning("No Selection", "Please select a student to update.")
        return

    name = entryname.get()
    enrollment = entryenrollment.get()
    branch = boxbranch.get()
    semester = boxsemster.get()
    marks = entrymarks.get()

    if name == "" or enrollment == "" or branch == "" or semester == "" or marks == "":
        messagebox.showwarning("Missing Information", "Please fill all the fields.")
        return

    if not marks.isdigit() or int(marks) < 0 or int(marks) > 100:
        messagebox.showerror("Invalid Marks", "Marks must be between 0 and 100.")
        return

    itemselected = selected[0]
    studentold = tablestudents.item(itemselected, "values")

    for record in students:
        if record[1] == enrollment and record[1] != studentold[1]:
            messagebox.showerror("Duplicate Enrollment", "This enrollment number already exists.")
            return

    for index, record in enumerate(students):
        if record[1] == studentold[1]:
            students[index] = (name, enrollment, branch, semester, marks)
            break

    tablestudents.item(itemselected, values=(name, enrollment, branch, semester, marks))

    studentclear()
    messagebox.showinfo("Success", "Student updated successfully.")


def selectstudent(event):
    selected = tablestudents.selection()

    if selected:
        student = tablestudents.item(selected[0], "values")

        entryname.delete(0, tk.END)
        entryname.insert(0, student[0])

        entryenrollment.delete(0, tk.END)
        entryenrollment.insert(0, student[1])

        boxbranch.set(student[2])
        boxsemster.set(student[3])

        entrymarks.delete(0, tk.END)
        entrymarks.insert(0, student[4])

def studentsearch():
    search = entrysearch.get().lower()

    for item in tablestudents.get_children():
        tablestudents.delete(item)

    for student in students:
        if search in student[0].lower() or search in student[1].lower():
            tablestudents.insert("", "end", values=student)

def studentshowall():
    entrysearch.delete(0, tk.END)

    for item in tablestudents.get_children():
        tablestudents.delete(item)

    for student in students:
        tablestudents.insert("", "end", values=student)


Light_Gray = "#F4F6F8"
Dark_Navy = "#17324D"
White = "#FFFFFF"
Dark_Gray = "#1F2933"
Medium_Gray = "#52606D"
Green = "#35A853"
Blue = "#2196F3"
Red = "#F44336"
Gray = "#9E9E9E"
Dark_Blue = "#285A8F"
Light_Blue = "#D7E9FF"
Light_Gray_2 = "#E8EDF2"


window = tk.Tk()
window.title("Student Management System")
window.geometry("1250x750")
window.configure(bg=Light_Gray)

headinglabel = tk.Label(window, text="STUDENT MANAGEMENT SYSTEM", font=("Arial", 24, "bold"), bg=Light_Gray, fg=Dark_Navy)
headinglabel.pack(pady=(25, 10))

line = tk.Frame(window, height=2, bg=Dark_Navy)
line.pack(fill="x", padx=40)

framedetails = tk.LabelFrame(window, text=" Student Details ", font=("Arial", 14, "bold"), bg=White, fg=Dark_Navy, padx=20, pady=20)
framedetails.pack(fill="x", padx=40, pady=25)

labelname = tk.Label(framedetails, text="Name", font=("Arial", 11), bg=White, fg=Dark_Gray)
labelname.grid(row=0, column=0, padx=10, pady=10, sticky="w")

entryname = tk.Entry(framedetails, font=("Arial", 11), width=30)
entryname.grid(row=0, column=1, padx=10, pady=10)

labelenrollment = tk.Label(framedetails, text="Enrollment Number", font=("Arial", 11), bg=White, fg=Dark_Gray)
labelenrollment.grid(row=1, column=0, padx=10, pady=10, sticky="w")

entryenrollment = tk.Entry(framedetails, font=("Arial", 11), width=30)
entryenrollment.grid(row=1, column=1, padx=10, pady=10)

labelbranch = tk.Label(framedetails, text="Branch", font=("Arial", 11), bg=White, fg=Dark_Gray)
labelbranch.grid(row=2, column=0, padx=10, pady=10, sticky="w")

boxbranch = ttk.Combobox(framedetails, values=["CSE", "IT", "ECE", "ME", "CE"], state="readonly", width=28)
boxbranch.grid(row=2, column=1, padx=10, pady=10)

labelsemester = tk.Label(framedetails, text="Semester", font=("Arial", 11), bg=White, fg=Dark_Gray)
labelsemester.grid(row=3, column=0, padx=10, pady=10, sticky="w")

boxsemster = ttk.Combobox(framedetails, values=["1", "2", "3", "4", "5", "6", "7", "8"], state="readonly", width=28)
boxsemster.grid(row=3, column=1, padx=10, pady=10)

labelmarks = tk.Label(framedetails, text="Marks", font=("Arial", 11), bg=White, fg=Dark_Gray)
labelmarks.grid(row=4, column=0, padx=10, pady=10, sticky="w")

entrymarks = tk.Entry(framedetails, font=("Arial", 11), width=30)
entrymarks.grid(row=4, column=1, padx=10, pady=10)

framebuttons = tk.Frame(framedetails, bg=White)
framebuttons.grid(row=5, column=0, columnspan=2, pady=15)

buttonadd = tk.Button(framebuttons, text="ADD", font=("Arial", 10, "bold"), bg=Green, fg=White, width=12, command=studentadd)
buttonadd.grid(row=0, column=0, padx=5)

buttonupdate = tk.Button(framebuttons, text="UPDATE", font=("Arial", 10, "bold"), bg=Blue, fg=White, width=12, command=studentupdate)
buttonupdate.grid(row=0, column=1, padx=5)

buttondelete = tk.Button(framebuttons, text="DELETE", font=("Arial", 10, "bold"), bg=Red, fg=White, width=12, command=studentdelete)
buttondelete.grid(row=0, column=2, padx=5)

buttonclear = tk.Button(framebuttons, text="CLEAR", font=("Arial", 10, "bold"), bg=Gray, fg=White, width=12, command=studentclear)
buttonclear.grid(row=0, column=3, padx=5)

framesearch = tk.Frame(window, bg=Light_Gray)
framesearch.pack(fill="x", padx=40, pady=(0, 15))

labelsearch = tk.Label(framesearch, text="Search Student", font=("Arial", 11, "bold"), bg=Light_Gray, fg=Dark_Gray)
labelsearch.pack(side="left", padx=(0, 10))

entrysearch = tk.Entry(framesearch, font=("Arial", 11), width=35)
entrysearch.pack(side="left", padx=5)

buttonsearch = tk.Button(framesearch, text="SEARCH", font=("Arial", 10, "bold"), bg=Dark_Blue, fg=White, width=12, command=studentsearch)
buttonsearch.pack(side="left", padx=5)

buttonshowall = tk.Button(framesearch, text="SHOW ALL", font=("Arial", 10, "bold"), bg=Gray, fg=White, width=12, command=studentshowall)
buttonshowall.pack(side="left", padx=5)

framerecords = tk.LabelFrame(window, text=" Student Records ", font=("Arial", 14, "bold"), bg=White, fg=Dark_Navy, padx=15, pady=15)
framerecords.pack(fill="both", expand=True, padx=40, pady=(0, 25))

columns = ("Name", "Enrollment No.", "Branch", "Semester", "Marks")

tablestudents = ttk.Treeview(framerecords, columns=columns, show="headings", height=8)

for column in columns:
    tablestudents.heading(column, text=column)
    tablestudents.column(column, anchor="center", width=150)

tablestudents.pack(side="left", fill="both", expand=True)

scrollbar = ttk.Scrollbar(framerecords, orient="vertical", command=tablestudents.yview)
tablestudents.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")

tablestudents.bind("<<TreeviewSelect>>", selectstudent)

window.mainloop()
