from tkinter import *
import csv

sort_name = "None"

def sort_year_level():
  print("Sorting by Year level")
  global sort_name
  sort_name = "Year level"

def sort_gender():
  print("Sorting by gender")

def sort_program():
  print("Sorting by program")

def sort_college():
  print("Sorting by college")

def sort_age():
  print("Sorting by age")

def add_student():
  print("Adding student")

def delete_student():
  print("Deleting student")

#Updates list
def update(Student):
  #clear
  student_list.delete(0, END)

  #Add students
  for student in Student:
    student_list.insert(END, student)

#Checks if searched is on the list and updates the list
def search(event):
  searched = search_box.get()
  if searched == '':
    student = names
  else:
    student = []
    for item in names:
      if searched.lower() in item.lower():
        student.append(item)
  update(student)

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

#Test students, to be deleted
names = ["Dababy", "Cench", "Bruno", "50", "Slim", "Snoop", "Dre"]

update(names)

search_box.bind("<KeyRelease>", search)


main_window.mainloop()