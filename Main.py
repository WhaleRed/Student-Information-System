from tkinter import *
from tkinter import ttk
import csv

student_path = "StudentData.csv"
program_path = "ProgramData.csv"
college_path = "CollegeData.csv"

#For the rows to be kept when deleting a student
student_keep = []
college_keep = []
program_keep = []

#For adding new student
student_new = []
college_new = []
program_new = []

#For editing student
student_edit = []
college_edit = []
program_edit = []

def sort_year_level():

  def sub_year():
    year = drop_year.get()
    student_list.delete(0, END)
    row_num = 1
    with open(student_path, "r") as f:
      reader = csv.reader(f)
      for row in reader:
        if row[3] == year:
          student_list.insert("end",str(row_num) + ")    " + row[0] + "   " + row[1] + " " + row[2])

  sort_window = Toplevel()
  sort_window.title("Sorting by Year level")
  sort_window.geometry("300x200")
  Label(sort_window,  text="Year level", font=("Helvetica", 12)).pack()
  choices = ["1", "2", "3", "4"]
  drop_year = ttk.Combobox(sort_window, text="None", values=choices, font=("Helvetica", 12))
  drop_year.pack()
  submit = Button(sort_window, text="Sort", command=sub_year)
  submit.pack()

def sort_gender():

  def sub_gender():
    gender = drop_gender.get()
    student_list.delete(0, END)
    row_num = 1
    with open(student_path, "r") as f:
      reader = csv.reader(f)
      for row in reader:
        if row[4] == gender:
          student_list.insert("end",str(row_num) + ")    " + row[0] + "   " + row[1] + " " + row[2])

  sort_window = Toplevel()
  sort_window.title("Sorting Gender")
  sort_window.geometry("300x200")
  Label(sort_window,  text="Gender", font=("Helvetica", 12)).pack()
  choices = ["Female", "Male"]
  drop_gender = ttk.Combobox(sort_window, text="None", values=choices, font=("Helvetica", 12))
  drop_gender.pack()
  submit = Button(sort_window, text="Sort", command=sub_gender)
  submit.pack()
  
def sort_college():

  def sub_college():
    college_index = []
    count = 0
    collegecode = drop_college.get()
    student_list.delete(0, END)
    row_num = 1
    with open(college_path, "r") as f:      #For determining what we will keep
      reader = csv.reader(f)
      for row in reader:
        if row[0] == collegecode:
          college_index.append(count)
        count += 1

    count = 0

    with open(student_path, "r") as f:
      reader = csv.reader(f)
      for row in reader:                    #For showing kept
        if count in college_index:
          student_list.insert("end",str(row_num) + ")    " + row[0] + "   " + row[1] + " " + row[2])
        count += 1
    
    count = 0

  sort_window = Toplevel()
  sort_window.title("Sorting College")
  sort_window.geometry("300x200")
  Label(sort_window,  text="College", font=("Helvetica", 12)).pack()
  choices = ["CASS", "CCS", "CSM", "CEBA", "CED", "CHS", "COE"]
  drop_college = ttk.Combobox(sort_window, text="None", values=choices, font=("Helvetica", 12))
  drop_college.pack()
  submit = Button(sort_window, text="Sort", command=sub_college)
  submit.pack() 

#Show list
def show():
  student_list.delete(0, END)
  row_num = 1
  with open(student_path, "r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        student_list.insert("end",str(row_num) + ")    " + row[0] + "   " + row[1] + " " + row[2])
        row_num += 1

  row_num = 1
  with open(program_path, "r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        program_list.insert("end", str(row_num) + ")   " + row[0] + "   " + row[1])
        row_num += 1

  row_num = 1
  with open(college_path, "r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        college_list.insert("end",str(row_num) + ")    " + row[0] + "       " + row[1])
        row_num += 1

def add_student():
  def submit():
    #Adding row for Student CSV
    student_new.append(id_entry.get())
    student_new.append(fname_entry.get())
    student_new.append(lname_entry.get())
    student_new.append(ylvl_entry.get())
    student_new.append(gender_entry.get())
    student_new.append(pcode_entry.get())
    with open(student_path, 'a', newline="") as f:
      writer = csv.writer(f)
      writer.writerow(student_new)
    student_new.clear()   #Clear list

    #Adding row for Program CSV
    program_new.append(progcode_entry.get())
    program_new.append(pname_entry.get())
    program_new.append(ccode_entry.get())
    with open(program_path, 'a', newline="") as f:
      writer = csv.writer(f)
      writer.writerow(program_new)
    program_new.clear()   #Clear list

    college_new.append(colcode_entry.get())
    college_new.append(colname_entry.get())
    with open(college_path, 'a', newline="") as f:
      writer = csv.writer(f)
      writer.writerow(college_new)
    college_new.clear()   #Clear list

    show()

  add_window = Toplevel()
  add_window.title("Add Student")

  add_frame = Frame(add_window)
  add_frame.grid(row=0, column=0,)

  Label(add_frame, text="Student", font=('Helvetica', 20)).grid(row=0, column=0, columnspan=3, padx=10, pady=10)
  
  Label(add_frame, text="ID#:", font=('Helvetica', 15)).grid(row=1, column=0, padx=10)
  id_entry = Entry(add_frame, font=('Helvetica', 15))
  id_entry.grid(row=1, column=1, padx=10, columnspan=2)

  Label(add_frame, text="First name:", font=('Helvetica', 15)).grid(row=2, column=0, padx=10)
  fname_entry = Entry(add_frame, font=('Helvetica', 15))
  fname_entry.grid(row=2, column=1, padx=10, columnspan=2)

  Label(add_frame, text="Last name:", font=('Helvetica', 15)).grid(row=3, column=0, padx=10)
  lname_entry = Entry(add_frame, font=('Helvetica', 15))
  lname_entry.grid(row=3, column=1, padx=10, columnspan=2)

  Label(add_frame, text="Year level:", font=('Helvetica', 15)).grid(row=4, column=0, padx=10)
  ylvl_entry = Entry(add_frame, font=('Helvetica', 15))
  ylvl_entry.grid(row=4, column=1, padx=10, columnspan=2)

  Label(add_frame, text="Gender:", font=('Helvetica', 15)).grid(row=5, column=0, padx=10)
  gender_entry = Entry(add_frame, font=('Helvetica', 15))
  gender_entry.grid(row=5, column=1, padx=10, columnspan=2)

  Label(add_frame, text="Program code:", font=('Helvetica', 15)).grid(row=6, column=0, padx=10)
  pcode_entry = Entry(add_frame, font=('Helvetica', 15))
  pcode_entry.grid(row=6, column=1, padx=10, columnspan=2)

  Label(add_frame, text="Program", font=('Helvetica', 20)).grid(row=7, column=0, columnspan=3, padx=10, pady=10)
  
  Label(add_frame, text="Program code:", font=('Helvetica', 15)).grid(row=8, column=0, padx=10)
  progcode_entry = Entry(add_frame, font=('Helvetica', 15))
  progcode_entry.grid(row=8, column=1, padx=10, columnspan=2)

  Label(add_frame, text="Program name:", font=('Helvetica', 15)).grid(row=9, column=0, padx=10)
  pname_entry = Entry(add_frame, font=('Helvetica', 15))
  pname_entry.grid(row=9, column=1, padx=10, columnspan=2)

  Label(add_frame, text="College code:", font=('Helvetica', 15)).grid(row=10, column=0, padx=10)
  ccode_entry = Entry(add_frame, font=('Helvetica', 15))
  ccode_entry.grid(row=10, column=1, padx=10, columnspan=2)

  Label(add_frame, text="College", font=('Helvetica', 20)).grid(row=11, column=0, columnspan=3, padx=10, pady=10)

  Label(add_frame, text="College code:", font=('Helvetica', 15)).grid(row=12, column=0, padx=10)
  colcode_entry = Entry(add_frame, font=('Helvetica', 15))
  colcode_entry.grid(row=12, column=1, padx=10, columnspan=2)

  Label(add_frame, text="College name:", font=('Helvetica', 15)).grid(row=13, column=0, padx=10)
  colname_entry = Entry(add_frame, font=('Helvetica', 15))
  colname_entry.grid(row=13, column=1, padx=10, columnspan=2)

  submit_button = Button(add_frame, text="Add Student", font=('Helvetica', 15), command=submit)
  submit_button.grid(row=14, column=0, columnspan=3, pady=10)

  #Have to add check if there is duplicate in ID#

def delete_student():

  def deleting():

    count = 0
    row_count = 0
    with open(student_path, "r") as f:
      reader = csv.reader(f)
      for row in reader:
        if row[0] != delstudent.get():
          student_keep.append(row)
          count += 1
        else:
          #Takes the row number, to be used at deleting rows from the other csv
          row_count = count
         
    count = 0     #Reset count

    with open(program_path, "r") as f:
      reader = csv.reader(f)
      for row in reader:
        if row_count != count:
          program_keep.append(row)
          count += 1
        else:
          count += 1
    
    count = 0
    
    with open(college_path, "r") as f:
      reader = csv.reader(f)
      for row in reader:
        if row_count != count:
          college_keep.append(row)
          count += 1
        else:
          count += 1
    
    count = 0
    row_count = 0

    #Write back the kept rows
    with open(student_path, "w", newline="") as f:
      writer = csv.writer(f)
      for row in student_keep:
        writer.writerow(row)
    
    with open(college_path, "w", newline="") as f:
      writer = csv.writer(f)
      for row in college_keep:
        writer.writerow(row)

    with open(program_path, "w", newline="") as f:
      writer = csv.writer(f)
      for row in program_keep:
        writer.writerow(row)
    
    #clear for no duplicates
    student_keep.clear()
    college_keep.clear()
    program_keep.clear()

    show()   #Relist

  def clear_text(e):
    delstudent.delete(0, "end")

  delete_window = Toplevel()
  delete_window.title("Delete Student")

  del_frame = Frame(delete_window)
  del_frame.grid(row=0,column=0, pady=10, padx=10)

  Label(del_frame, text="Delete Student", font=('Helvetica', 20)).grid(row=0, column=0, columnspan=3, padx=10, pady=10)
  Label(del_frame, text="Student ID#", font=('Helvetica', 15)).grid(row=1, column=0,pady=10)
  delstudent = Entry(del_frame, font=("Helvetica", 15))
  delstudent.insert(0, "YYYY-NNNN")
  delstudent.grid(row=1, column=2)
  delstudent.bind("<FocusIn>", clear_text)
  delete_button = Button(del_frame, text="Delete Student", font=('Helvetica', 15), pady=10, padx=10, command=deleting)
  delete_button.grid(row=2, columnspan=3)

  #I have to add verify there is an input

def edit_student():

  def submit_edit():
    student_e = []
    program_e = []
    college_e = []

    count = 0

    #Apendiing row for Student CSV
    student_e.append(id_entry.get())
    student_e.append(fname_entry.get())
    student_e.append(lname_entry.get())
    student_e.append(ylvl_entry.get())
    student_e.append(gender_entry.get())
    student_e.append(pcode_entry.get())

    #Apendiing row for Program CSV
    program_e.append(progcode_entry.get())
    program_e.append(pname_entry.get())
    program_e.append(ccode_entry.get())


    #Apending row for College csv
    college_e.append(colcode_entry.get())
    college_e.append(colname_entry.get())

    #Reading for insert
    with open(student_path, "r") as f:
      reader = csv.reader(f)
      for row in reader:
        if editing == count:
          student_edit.append(student_e)
          count += 1
        else:
          student_edit.append(row)
          count += 1

    count = 0

    with open(college_path, "r") as f:
      reader = csv.reader(f)
      for row in reader:
        if editing == count:
          college_edit.append(college_e)
          count += 1
        else:
          college_edit.append(row)
          count += 1

    count = 0

    with open(program_path, "r") as f:
      reader = csv.reader(f)
      for row in reader:
        if editing == count:
          program_edit.append(program_e)
          count += 1
        else:
          program_edit.append(row)
          count += 1

    count = 0

    #Write back
    with open(student_path, "w", newline="") as f:
      writer = csv.writer(f)
      for row in student_edit:
        writer.writerow(row)

    with open(college_path, "w", newline="") as f:
      writer = csv.writer(f)
      for row in college_edit:
        writer.writerow(row)

    with open(program_path, "w", newline="") as f:
      writer = csv.writer(f)
      for row in program_edit:
        writer.writerow(row)
    
    #clear
    student_edit.clear()
    college_edit.clear()
    program_edit.clear()

    student_e.clear()
    college_e.clear()
    program_e.clear()

    show()

  editing = 0
  count = 0
  for student in student_list.curselection():     #For reference which student user is editing
    editing = student+1
  
  #Read first
  with open(student_path, "r") as f:
    reader = csv.reader(f)
    for row in reader:
      if count == editing:
        student_edit.append(row)
      count += 1
  
  count = 0

  with open(college_path, "r") as f:
    reader = csv.reader(f)
    for row in reader:
      if count == editing:
        college_edit.append(row)
      count += 1
  
    count = 0

  with open(program_path, "r") as f:
    reader = csv.reader(f)
    for row in reader:
      if count == editing:
        program_edit.append(row)
      count += 1
  
  count = 0

  edit_window = Toplevel()
  edit_window.title("Editing Student")

  edit_frame = Frame(edit_window)
  edit_frame.grid(row=0, column=0,)

  Label(edit_frame, text="Student", font=('Helvetica', 20)).grid(row=0, column=0, columnspan=3, padx=10, pady=10)
  
  Label(edit_frame, text="ID#:", font=('Helvetica', 15)).grid(row=1, column=0, padx=10)
  id_entry = Entry(edit_frame, font=('Helvetica', 15))
  id_entry.grid(row=1, column=1, padx=10, columnspan=2)
  id_entry.insert(0, student_edit[0][0])

  Label(edit_frame, text="First name:", font=('Helvetica', 15)).grid(row=2, column=0, padx=10)
  fname_entry = Entry(edit_frame, font=('Helvetica', 15))
  fname_entry.grid(row=2, column=1, padx=10, columnspan=2)
  fname_entry.insert(0, student_edit[0][1])

  Label(edit_frame, text="Last name:", font=('Helvetica', 15)).grid(row=3, column=0, padx=10)
  lname_entry = Entry(edit_frame, font=('Helvetica', 15))
  lname_entry.grid(row=3, column=1, padx=10, columnspan=2)
  lname_entry.insert(0, student_edit[0][2])

  Label(edit_frame, text="Year level:", font=('Helvetica', 15)).grid(row=4, column=0, padx=10)
  ylvl_entry = Entry(edit_frame, font=('Helvetica', 15))
  ylvl_entry.grid(row=4, column=1, padx=10, columnspan=2)
  ylvl_entry.insert(0, student_edit[0][3])

  Label(edit_frame, text="Gender:", font=('Helvetica', 15)).grid(row=5, column=0, padx=10)
  gender_entry = Entry(edit_frame, font=('Helvetica', 15))
  gender_entry.grid(row=5, column=1, padx=10, columnspan=2)
  gender_entry.insert(0, student_edit[0][4])

  Label(edit_frame, text="Program code:", font=('Helvetica', 15)).grid(row=6, column=0, padx=10)
  pcode_entry = Entry(edit_frame, font=('Helvetica', 15))
  pcode_entry.grid(row=6, column=1, padx=10, columnspan=2)
  pcode_entry.insert(0, student_edit[0][5])

  Label(edit_frame, text="Program", font=('Helvetica', 20)).grid(row=7, column=0, columnspan=3, padx=10, pady=10)
  
  Label(edit_frame, text="Program code:", font=('Helvetica', 15)).grid(row=8, column=0, padx=10)
  progcode_entry = Entry(edit_frame, font=('Helvetica', 15))
  progcode_entry.grid(row=8, column=1, padx=10, columnspan=2)
  progcode_entry.insert(0, program_edit[0][0])

  Label(edit_frame, text="Program name:", font=('Helvetica', 15)).grid(row=9, column=0, padx=10)
  pname_entry = Entry(edit_frame, font=('Helvetica', 15))
  pname_entry.grid(row=9, column=1, padx=10, columnspan=2)
  pname_entry.insert(0, program_edit[0][1])

  Label(edit_frame, text="College code:", font=('Helvetica', 15)).grid(row=10, column=0, padx=10)
  ccode_entry = Entry(edit_frame, font=('Helvetica', 15))
  ccode_entry.grid(row=10, column=1, padx=10, columnspan=2)
  ccode_entry.insert(0, program_edit[0][2])

  Label(edit_frame, text="College", font=('Helvetica', 20)).grid(row=11, column=0, columnspan=3, padx=10, pady=10)

  Label(edit_frame, text="College code:", font=('Helvetica', 15)).grid(row=12, column=0, padx=10)
  colcode_entry = Entry(edit_frame, font=('Helvetica', 15))
  colcode_entry.grid(row=12, column=1, padx=10, columnspan=2)
  colcode_entry.insert(0, college_edit[0][0])

  Label(edit_frame, text="College name:", font=('Helvetica', 15)).grid(row=13, column=0, padx=10)
  colname_entry = Entry(edit_frame, font=('Helvetica', 15))
  colname_entry.grid(row=13, column=1, padx=10, columnspan=2)
  colname_entry.insert(0, college_edit[0][1])

  #Clear
  student_edit.clear()
  program_edit.clear()
  college_edit.clear()

  submit_button = Button(edit_frame, text="Submit", font=('Helvetica', 15), command=submit_edit)
  submit_button.grid(row=14, column=0, columnspan=3, pady=10)

  

#Checks if searched is on the list and updates the list
def search(event):

  def update_stud(students):
    student_list.delete(0, END)
    row_num = 1
    for student in students:
      student_list.insert("end",str(row_num) + ")    " + student[0] + "   " + student[1] + " " + student[2])
      row_num += 1
  
  def update_prog(programs):
    program_list.delete(0, END)
    row_num = 1
    for program in programs:
      program_list.insert("end", str(row_num) + ")    " + program[0] + "   " + program[1])
      row_num += 1
  
  def update_col(colleges):
    college_list.delete(0, END)
    row_num = 1
    for college in colleges:
      college_list.insert("end", str(row_num) + ")    " + college[0] + "   " + college[1])
      row_num += 1

  prog_col = []
  count = 0
  searched = search_box.get()

  #Student List
  with open(student_path, "r") as f:
    reader = csv.reader(f)
    if searched == '':
      student = []
      next(reader)
      student = reader
    else:
      student = []
      for row in reader:
        if searched in row[0]:
          student.append([row[0], row[1], row[2]])
          prog_col.append(count)
          count += 1
        else:
          count += 1

    update_stud(student)

  #Program List
  count = 0
  with open(program_path, "r") as f:
    reader = csv.reader(f)
    if searched == '':
      program = []
      next(reader)
      program = reader
    else:
      program = []
      for row in reader:
        if count in prog_col:
          program.append([row[0], row[1]])
          count += 1
        else:
          count += 1
    
    update_prog(program)
  
  #College list
  count = 0
  with open(college_path, "r") as f:
    reader = csv.reader(f)
    if searched == '':
      college = []
      next(reader)
      college = reader
    else:
      college = []
      for row in reader:
        if count in prog_col:
          college.append([row[0], row[1]])
          count += 1
        else:
          count += 1

    update_col(college)



main_window = Tk()

main_window.title("Student Information System")
main_window.geometry("1354x768")


menubar = Menu(main_window)
main_window.config(menu=menubar)

#Menu for Managing student
manage_menu = Menu(menubar, tearoff=0, font=("Helvetica", 11))
menubar.add_cascade(label="Manage Student", menu=manage_menu)
manage_menu.add_command(label="Add Student", command=add_student)
manage_menu.add_command(label="Delete Student", command=delete_student)
manage_menu.add_command(label="Edit Student", command=edit_student)     #Have to make function

sort_menu = Menu(menubar, tearoff=0, font=("Helvetica", 11))
menubar.add_cascade(label="Sort Students", menu=sort_menu)
sort_menu.add_command(label="None", command=show)
sort_menu.add_command(label="Year Level", command=sort_year_level)
sort_menu.add_command(label="Gender", command=sort_gender)
sort_menu.add_command(label="College", command=sort_college)

view_menu = Menu(menubar, tearoff=0, font=("Helvetica", 11))
menubar.add_cascade(label="View", menu=view_menu)
view_menu.add_command(label="Student")
view_menu.add_command(label="Program")
view_menu.add_command(label="College")

#for search box
search_frame = Frame(main_window)
search_frame.pack(side=TOP, padx=20, pady=10)


search_box = Entry(search_frame, font=('Helvetica', 15))
search_box.pack(side=RIGHT)

#Label for search box
Label(search_frame, text="Search by ID#").pack(side=RIGHT)

#Listing students

main_frame = Frame(main_window)
main_frame.pack(side=LEFT)

list_frame = Frame(main_frame)
scroll = Scrollbar(list_frame, orient=VERTICAL)
Label(list_frame, text="STUDENT", font=("Helvetica", 15)).pack(side=TOP)
student_list = Listbox(list_frame, width=50, height=25, font=("Helvetica", 15), yscrollcommand=scroll.set)
scroll.config(command=student_list.yview)
scroll.pack(side=RIGHT, fill=Y)
list_frame.pack(side=LEFT)
student_list.pack(pady=30, padx=20)

program_frame = Frame(main_frame)
program_scroll = Scrollbar(program_frame, orient=VERTICAL)
Label(program_frame, text="PROGRAM", font=("Helvetica", 15)).pack(side=TOP)
program_list = Listbox(program_frame, width=60, height=10, font=("Helvetica", 15), yscrollcommand=program_scroll.set)
program_scroll.config(command=program_list.yview)
program_scroll.pack(side=RIGHT, fill=Y)
program_frame.pack(side=TOP)
program_list.pack(pady=30, padx=20)

college_frame = Frame(main_frame)
college_scroll = Scrollbar(college_frame, orient=VERTICAL)
Label(college_frame, text="COLLEGE", font=("Helvetica", 15)).pack(side=TOP)
college_list = Listbox(college_frame, width=60, height=10, font=("Helvetica", 15), yscrollcommand=college_scroll.set)
college_scroll.config(command=college_list.yview)
college_scroll.pack(side=RIGHT, fill=Y)
college_frame.pack(side=TOP)
college_list.pack(pady=30, padx=20)


show()

search_box.bind("<KeyRelease>", search)


main_window.mainloop()