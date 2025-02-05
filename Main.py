from tkinter import *
import csv

student_path = "StudentData.csv"
program_path = "ProgramData.csv"
college_path = "CollegeData.csv"

#Array for the rows to be kept when deleting a student
student_keep = []
college_keep = []
program_keep = []

#Array for adding new student
student_new = []
college_new = []
program_new = []

def sort_year_level():
  print("Sorting by Year level")

def sort_gender():
  print("Sorting by gender")

def sort_program():
  print("Sorting by program")

def sort_college():
  print("Sorting by college")

def sort_age():
  print("Sorting by age")

def printing(list):
  for field in list:
    print(field)

#Show list
def show():
  student_list.delete(0, END)
  with open(student_path, "r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        student_list.insert("end", row)

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

  

#Checks if searched is on the list and updates the list
#def search(event):
# searched = search_box.get()
# with open(student_path, "r") as f:
#   reader = csv.reader(f)
# if searched == '':
#    student = reader
# else:
#    student = []
#    for item in reader:
#      if searched.lower() in item.lower():
#        student.append(item)
# update(student)

main_window = Tk()

main_window.title("Student Information System")
main_window.geometry("1024x768")

#for sort
menu_frame = Frame(main_window)
menu_frame.place(x=0, y=0)
menu_frame.config(padx=20, pady=10)

#for search box
search_frame = Frame(main_window)
search_frame.pack(side=TOP, anchor=NE, padx=20, pady=10)


add_button = Button(menu_frame, text="Add Student", command=add_student)
add_button.pack(side=LEFT)

del_button = Button(menu_frame, text="Delete Student", command=delete_student)
del_button.pack(side=LEFT)

sort_label = Label(menu_frame, text="      Sort by: ")
sort_label.pack(side=LEFT)


#Sort by buttons Should be changed to Menubar for cascade
Button(menu_frame, text="None", command=show).pack(side=LEFT)
Button(menu_frame, text="Year Level", command=sort_year_level).pack(side=LEFT)
Button(menu_frame, text="Gender", command=sort_gender).pack(side=LEFT)
Button(menu_frame, text="Program", command=sort_program).pack(side=LEFT)
Button(menu_frame, text="College", command=sort_college).pack(side=LEFT)
Button(menu_frame, text="Age", command=sort_age).pack(side=LEFT)

search_box = Entry(search_frame, font=('Helvetica', 15))
search_box.pack(side=RIGHT)

#Label for search box
Label(search_frame, text="Search by ID#").pack(side=RIGHT)

student_list = Listbox(main_window, width=300, height=300, font=("Helvetica", 15))
student_list.pack(pady=50, padx=20)

show()

#search_box.bind("<KeyRelease>", search)


main_window.mainloop()