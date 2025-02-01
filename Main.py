from tkinter import *
import csv

student_list = []
program_list = []
college_list = []

student_path = "StudentData.csv"
program_path = "ProgramData.csv"
college_path = "CollegeData.csv"

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

def submit_add():
  print("Submitted the newly added student")

def add_student():
  add_window = Toplevel()
  add_window.title("Add Student")

  Label(add_window, text="STUDENT", font=('Helvetica', 20)).grid(row=0, column=0, columnspan=2, pady=10)
  Label(add_window, text="ID#: ", font=('Helvetica', 15)).grid(row=1, column=0, padx=10)
  Entry(add_window,font=('Helvetica', 15)).grid(row=1, column=1, padx=10)
  Label(add_window, text="First name: ", font=('Helvetica', 15)).grid(row=2, column=0,)
  Entry(add_window,font=('Helvetica', 15)).grid(row=2, column=1,)
  Label(add_window, text="Last name: ", font=('Helvetica', 15)).grid(row=3, column=0,)
  Entry(add_window,font=('Helvetica', 15)).grid(row=3, column=1,)
  Label(add_window, text="Year Level: ", font=('Helvetica', 15)).grid(row=4, column=0,)
  Entry(add_window,font=('Helvetica', 15)).grid(row=4, column=1,)
  Label(add_window, text="Gender: ", font=('Helvetica', 15)).grid(row=5, column=0,)
  Entry(add_window,font=('Helvetica', 15)).grid(row=5, column=1,)
  Label(add_window, text="Program Code: ", font=('Helvetica', 15)).grid(row=6, column=0,)
  Entry(add_window,font=('Helvetica', 15)).grid(row=6, column=1,)

  Label(add_window, text="PROGRAM", font=('Helvetica', 20)).grid(row=7, column=0, columnspan=2, pady=10)
  Label(add_window, text="Program Code: ", font=('Helvetica', 15)).grid(row=8, column=0,)
  Entry(add_window,font=('Helvetica', 15)).grid(row=8, column=1,)
  Label(add_window, text="Name: ", font=('Helvetica', 15)).grid(row=9, column=0,)
  Entry(add_window,font=('Helvetica', 15)).grid(row=9, column=1,)
  Label(add_window, text="College: ", font=('Helvetica', 15)).grid(row=10, column=0,)
  Entry(add_window,font=('Helvetica', 15)).grid(row=10, column=1,)

  Label(add_window, text="College", font=('Helvetica', 20)).grid(row=11, column=0, columnspan=2, pady=10)
  Label(add_window, text="Code: ", font=('Helvetica', 15)).grid(row=12, column=0,)
  Entry(add_window,font=('Helvetica', 15)).grid(row=12, column=1,)
  Label(add_window, text="Name: ", font=('Helvetica', 15)).grid(row=13, column=0,)
  Entry(add_window,font=('Helvetica', 15)).grid(row=13, column=1,)

  Button(add_window, text="Add Student", font=('Helvetica', 15), command=submit_add).grid(row=14, column=0, columnspan=2, pady=10)


def delete_student():
  print("Deleting student")


#Show list
def show():
  with open(student_path, "r") as f:
    reader = csv.reader(f)
    for row in reader:
        student_list.insert("end", row)

#Updates list for search
def update(students):
  for student in students:
    student_list.insert(student)

    

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

#for add delete, and sort
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

#Sort by buttons
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