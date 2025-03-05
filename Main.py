from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import csv
import re
import operator

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

#Check
def valid_id(idnumber):
  pattern = r"^\d{4}-\d{4}$"  
  return bool(re.match(pattern, idnumber))

def exists(idnumber):
  idnums = []
  with open(student_path, "r") as f:
    reader = csv.reader(f)
    for row in reader:
      idnums.append(row[0])
  return bool(idnumber in idnums)

#Student
def sync_scroll_student(*args):
    id_list.yview(*args)
    fname_list.yview(*args)
    lname_list.yview(*args)
    ylevel_list.yview(*args)
    gender_list.yview(*args)
    pcode_list.yview(*args)

def add_student():

   def filled_in():
      info = []
      info.append(id_entry.get())
      info.append(fname_entry.get())
      info.append(lname_entry.get())
      info.append(ylvl_entry.get())
      info.append(gender_entry.get())
      info.append(pcode_entry.get())

      if "" in info:
         return False
      else:
         return True
   
   def submit():
      if exists(id_entry.get()) == True:
        messagebox.showerror("Invalid ID Number", "ID Number already exists")
      elif valid_id(id_entry.get()) == False:
        messagebox.showerror("Invalid Format", "ID Number Invalid Format")
      elif filled_in() == False:
        messagebox.showerror("Field(s) is  not Filled", "All Fields must be filled in")
      else:
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
        
        show_students()
    
   add_window = Toplevel()
   add_window.title("Add Student")
   add_window.resizable(FALSE,FALSE)

   add_frame = Frame(add_window)
   add_frame.grid(row=0, column=0,)


   Label(add_frame, text="Student", font=('Helvetica', 20)).grid(row=0, column=0, columnspan=3, padx=10, pady=10)
  
   Label(add_frame, text="ID#:", font=('Helvetica', 15)).grid(row=1, column=0, padx=10, pady=5)
   id_entry = Entry(add_frame, font=('Helvetica', 15),width=40)
   id_entry.grid(row=1, column=1, padx=10, pady=5, columnspan=2)

   Label(add_frame, text="First name:", font=('Helvetica', 15)).grid(row=2, column=0, padx=10, pady=5)
   fname_entry = Entry(add_frame, font=('Helvetica', 15),width=40)
   fname_entry.grid(row=2, column=1, padx=10, pady=5, columnspan=2)

   Label(add_frame, text="Last name:", font=('Helvetica', 15)).grid(row=3, column=0, padx=10, pady=5)
   lname_entry = Entry(add_frame, font=('Helvetica', 15),width=40)
   lname_entry.grid(row=3, column=1, padx=10, pady=5, columnspan=2)

   Label(add_frame, text="Year level:", font=('Helvetica', 15)).grid(row=4, column=0, padx=10, pady=5)
   ychoices = ["1", "2", "3", "4"]
   ylvl_entry = ttk.Combobox(add_frame, font=('Helvetica', 15), values=ychoices, state="readonly", width=38)
   ylvl_entry.grid(row=4, column=1, padx=10, pady=5, columnspan=2)

   Label(add_frame, text="Gender:", font=('Helvetica', 15)).grid(row=5, column=0, padx=10, pady=5)
   gchoices = ["Male", "Female"]
   gender_entry = ttk.Combobox(add_frame, font=('Helvetica', 15), values=gchoices, state="readonly", width=38)
   gender_entry.grid(row=5, column=1, padx=10, pady=5, columnspan=2)

   Label(add_frame, text="Program code:", font=('Helvetica', 15)).grid(row=6, column=0, padx=10, pady=5)
   pcode_entry = Entry(add_frame, font=('Helvetica', 15), width=40)
   pcode_entry.grid(row=6, column=1, padx=10, pady=5, columnspan=2)

   submit_button = Button(add_frame, text="Add Student", font=('Helvetica', 15),command=submit)
   submit_button.grid(row=14, column=0, columnspan=3, pady=10)

def delete_student():

   def deleting():
      if valid_id(delstudent.get()) == False:
         messagebox.showerror("Invalid Format", "Invalid ID Number Format")
         delete_window.destroy()
      elif exists(delstudent.get()) == False:
         messagebox.showerror("Invalid ID", "Student does not Exist")
         delete_window.destroy()
      else:
         with open(student_path, "r") as f:
            reader = csv.reader(f)
            for row in reader:
               if row[0] != delstudent.get():
                  student_keep.append(row)

         with open(student_path, "w", newline="") as f:
            writer = csv.writer(f)
            for row in student_keep:
               writer.writerow(row)

         student_keep.clear()
         show_students()


   def clear_text(e):
      delstudent.delete(0,"end")
      
   delete_window = Toplevel()
   delete_window.title("Delete Student")
   delete_window.resizable(FALSE,FALSE)
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

def edit_student():
   def editing():

      def filled_in():
         info = []
         info.append(id_entry.get())
         info.append(fname_entry.get())
         info.append(lname_entry.get())
         info.append(ylvl_entry.get())
         info.append(gender_entry.get())
         info.append(pcode_entry.get())

         if "" in info:
            return False
         else:
            return True

      def submit_edit():
         if valid_id(id_entry.get()) == False:
            messagebox.showerror("Invalid Format", "ID Number Invalid Format")
         elif exists(id_entry.get()) == True and id_entry.get() != student:
            messagebox.showerror("Invalid ID Number", "ID Number Already Exists")
         elif  filled_in() == False:
            messagebox.showerror("Field(s) is not Filled", "All Fields must be filled in")
         else:
            student_e = []

         #Apendiing row for Student CSV
            student_e.append(id_entry.get())
            student_e.append(fname_entry.get())
            student_e.append(lname_entry.get())
            student_e.append(ylvl_entry.get())
            student_e.append(gender_entry.get())
            student_e.append(pcode_entry.get())

            with open(student_path, "r") as f:  #Read first
               reader = csv.reader(f)
               for row in reader:
                  if row[0] == student:
                     student_edit.append(student_e)
                  else:
                     student_edit.append(row)

            with open(student_path, "w", newline="") as f:  #Write Back
               writer = csv.writer(f)
               for row in student_edit:
                  writer.writerow(row)
            
            student_e.clear()
            student_edit.clear()

            show_students()
            
            

      if valid_id(editstudent.get()) == False:
         messagebox.showerror("Invalid Format", "Invalid ID Number Format")
      elif exists(editstudent.get()) == False:
         messagebox.showerror("ID Does Not Exist", "ID Number Does Not Exist")
      else: 
         student = editstudent.get()
         edit_window.destroy()

         #Read first
         with open(student_path, "r") as f:
            reader = csv.reader(f)
            for row in reader:
               if row[0] == student:
                  student_edit.append(row)

         editing_window = Toplevel()
         editing_window.title("Editing Student")
         editing_window.resizable(FALSE,FALSE)
         edit_frame = Frame(editing_window)
         edit_frame.grid(row=0, column=0)

         Label(edit_frame, text="Student", font=('Helvetica', 20)).grid(row=0, column=0, columnspan=3, padx=10, pady=10)
         
         Label(edit_frame, text="ID#:", font=('Helvetica', 15)).grid(row=1, column=0, padx=10)
         id_entry = Entry(edit_frame, font=('Helvetica', 15), width=40)
         id_entry.grid(row=1, column=1, padx=10, columnspan=2, pady=5)
         id_entry.insert(0, student_edit[0][0])

         Label(edit_frame, text="First name:", font=('Helvetica', 15)).grid(row=2, column=0, padx=10)
         fname_entry = Entry(edit_frame, font=('Helvetica', 15), width=40)
         fname_entry.grid(row=2, column=1, padx=10, columnspan=2, pady=5)
         fname_entry.insert(0, student_edit[0][1])

         Label(edit_frame, text="Last name:", font=('Helvetica', 15)).grid(row=3, column=0, padx=10)
         lname_entry = Entry(edit_frame, font=('Helvetica', 15), width=40)
         lname_entry.grid(row=3, column=1, padx=10, columnspan=2, pady=5)
         lname_entry.insert(0, student_edit[0][2])

         Label(edit_frame, text="Year level:", font=('Helvetica', 15)).grid(row=4, column=0, padx=10)
         ychoices = ["1","2","3","4"]
         ylvl_entry = ttk.Combobox(edit_frame, font=('Helvetica', 15), values=ychoices, state="readonly", width=38)
         ylvl_entry.grid(row=4, column=1, padx=10, columnspan=2, pady=5)
         #Default Value
         run = 0
         for choices in ychoices:
            if choices == student_edit[0][3]:         
               ylvl_entry.current(run)
            run += 1

         Label(edit_frame, text="Gender:", font=('Helvetica', 15)).grid(row=5, column=0, padx=10)
         gchoices = ["Male", "Female"]
         gender_entry = ttk.Combobox(edit_frame, font=('Helvetica', 15), values=gchoices, state="readonly", width=38)
         gender_entry.grid(row=5, column=1, padx=10, columnspan=2,pady=5)
         #Default Value
         run = 0
         for choices in gchoices:
            if choices == student_edit[0][4]:         
               gender_entry.current(run)
            run += 1

         Label(edit_frame, text="Program code:", font=('Helvetica', 15)).grid(row=6, column=0, padx=10)
         pcode_entry = Entry(edit_frame, font=('Helvetica', 15),width=40)
         pcode_entry.grid(row=6, column=1, padx=10, columnspan=2,pady=5)
         pcode_entry.insert(0, student_edit[0][5])
         
         student_edit.clear() #Clear

         submit_button = Button(edit_frame, text="Submit", font=('Helvetica', 15), command=submit_edit)
         submit_button.grid(row=14, column=0, columnspan=3, pady=10)

   def clear_text(e):
      editstudent.delete(0, "end")

   edit_window = Toplevel()
   edit_window.title("Edit Student")
   edit_window.resizable(FALSE,FALSE)
   del_frame = Frame(edit_window)
   del_frame.grid(row=0,column=0, pady=10, padx=10)

   Label(del_frame, text="Editing Student", font=('Helvetica', 20)).grid(row=0, column=0, columnspan=3, padx=10, pady=10)
   Label(del_frame, text="Student ID#", font=('Helvetica', 15)).grid(row=1, column=0,pady=10)
   editstudent = Entry(del_frame, font=("Helvetica", 15))
   editstudent.insert(0, "YYYY-NNNN")
   editstudent.grid(row=1, column=2)
   editstudent.bind("<FocusIn>", clear_text)
   edit_button = Button(del_frame, text="Edit Student", font=('Helvetica', 15), pady=10, padx=10, command=editing)
   edit_button.grid(row=2, columnspan=3)

def sort_year_level():
   def update(students):
      id_list.delete(0, END)
      fname_list.delete(0, END)
      lname_list.delete(0, END)
      ylevel_list.delete(0, END)
      gender_list.delete(0, END)
      pcode_list.delete(0, END)

      for row in students:
         id_list.insert("end", row[0])
         fname_list.insert("end", row[1])
         lname_list.insert("end", row[2])
         ylevel_list.insert("end", row[3])
         gender_list.insert("end", row[4])
         pcode_list.insert("end", row[5])

   with open(student_path, "r") as f:
      reader = csv.reader(f)
      next(reader)
      sorted_y = sorted(reader, key=operator.itemgetter(3))
   update(sorted_y)

def sort_gender():
   def update(students):
      id_list.delete(0, END)
      fname_list.delete(0, END)
      lname_list.delete(0, END)
      ylevel_list.delete(0, END)
      gender_list.delete(0, END)
      pcode_list.delete(0, END)

      for row in students:
         id_list.insert("end", row[0])
         fname_list.insert("end", row[1])
         lname_list.insert("end", row[2])
         ylevel_list.insert("end", row[3])
         gender_list.insert("end", row[4])
         pcode_list.insert("end", row[5])

   with open(student_path, "r") as f:
      reader = csv.reader(f)
      next(reader)
      sorted_gen = sorted(reader, key=operator.itemgetter(4))
   update(sorted_gen)

def sort_lastname():
   def update(students):
      id_list.delete(0, END)
      fname_list.delete(0, END)
      lname_list.delete(0, END)
      ylevel_list.delete(0, END)
      gender_list.delete(0, END)
      pcode_list.delete(0, END)

      for row in students:
         id_list.insert("end", row[0])
         fname_list.insert("end", row[1])
         lname_list.insert("end", row[2])
         ylevel_list.insert("end", row[3])
         gender_list.insert("end", row[4])
         pcode_list.insert("end", row[5])

   with open(student_path, "r") as f:
      reader = csv.reader(f)
      next(reader)
      sorted_lname = sorted(reader, key=operator.itemgetter(2))
   update(sorted_lname)

def sort_fname():
   def update(students):
      id_list.delete(0, END)
      fname_list.delete(0, END)
      lname_list.delete(0, END)
      ylevel_list.delete(0, END)
      gender_list.delete(0, END)
      pcode_list.delete(0, END)

      for row in students:
         id_list.insert("end", row[0])
         fname_list.insert("end", row[1])
         lname_list.insert("end", row[2])
         ylevel_list.insert("end", row[3])
         gender_list.insert("end", row[4])
         pcode_list.insert("end", row[5])

   with open(student_path, "r") as f:
      reader = csv.reader(f)
      next(reader)
      sorted_fname = sorted(reader, key=operator.itemgetter(1))
   update(sorted_fname)

def sort_program():
   def update(students):
      id_list.delete(0, END)
      fname_list.delete(0, END)
      lname_list.delete(0, END)
      ylevel_list.delete(0, END)
      gender_list.delete(0, END)
      pcode_list.delete(0, END)

      for row in students:
         id_list.insert("end", row[0])
         fname_list.insert("end", row[1])
         lname_list.insert("end", row[2])
         ylevel_list.insert("end", row[3])
         gender_list.insert("end", row[4])
         pcode_list.insert("end", row[5])

   with open(student_path, "r") as f:
      reader = csv.reader(f)
      next(reader)
      sorted_prog = sorted(reader, key=operator.itemgetter(5))
   update(sorted_prog)

def sort_id():
   def update(students):
      id_list.delete(0, END)
      fname_list.delete(0, END)
      lname_list.delete(0, END)
      ylevel_list.delete(0, END)
      gender_list.delete(0, END)
      pcode_list.delete(0, END)

      for row in students:
         id_list.insert("end", row[0])
         fname_list.insert("end", row[1])
         lname_list.insert("end", row[2])
         ylevel_list.insert("end", row[3])
         gender_list.insert("end", row[4])
         pcode_list.insert("end", row[5])

   with open(student_path, "r") as f:
      reader = csv.reader(f)
      next(reader)
      sorted_i = sorted(reader, key=operator.itemgetter(0))
   update(sorted_i)

def search(event):

   def update(students):
      id_list.delete(0, END)
      fname_list.delete(0, END)
      lname_list.delete(0, END)
      ylevel_list.delete(0, END)
      gender_list.delete(0, END)
      pcode_list.delete(0, END)

      for row in students:
         id_list.insert("end", row[0])
         fname_list.insert("end", row[1])
         lname_list.insert("end", row[2])
         ylevel_list.insert("end", row[3])
         gender_list.insert("end", row[4])
         pcode_list.insert("end", row[5])

   searched = search_box.get()

   with open(student_path, "r") as f:
      reader = csv.reader(f)
      if search_by.get() == "ID#":
         if searched == "":   #ID# Search
            show_students()
         else:
            student = []
            for row in reader:
               if searched in row[0]:
                  student.append(row)
            update(student)

      elif search_by.get() == "Any":   
         if searched == "":   #ANY Search
            show_students()
         else:
            student = []
            for row in reader:
               if searched in row[0] or searched in row[1] or searched in row[2] or searched in row [3] or searched in row[4] or searched in row[5]:
                  student.append(row)
            update(student)

      elif search_by.get() == "First Name":
         if searched == "":   #FN Search
            show_students()
         else:
            student = []
            for row in reader:
               if searched in row[1]:
                  student.append(row)
            update(student)

      elif search_by.get() == "Last Name":
         if searched == "":   #LN Search
            show_students()
         else:
            student = []
            for row in reader:
               if searched in row[2]:
                  student.append(row)
            update(student)
      elif search_by.get() == "Year Level":
         if searched == "":   #YL Search
            show_students()
         else:
            student = []
            for row in reader:
               if searched in row[3]:
                  student.append(row)
            update(student)

      elif search_by.get() == "Gender":
         if searched == "":   #G Search
            show_students()
         else:
            student = []
            for row in reader:
               if searched in row[4]:
                  student.append(row)
            update(student)

      elif search_by.get() == "Program Code":
         if searched == "":   #PCode Search
            show_students()
         else:
            student = []
            for row in reader:
               if searched in row[5]:
                  student.append(row)
            update(student)


def show_students():
  id_list.delete(0, END)
  fname_list.delete(0, END)
  lname_list.delete(0, END)
  ylevel_list.delete(0, END)
  gender_list.delete(0, END)
  pcode_list.delete(0, END)

  with open(student_path, "r") as f:
    reader = csv.reader(f) 
    next(reader)
    for row in reader:
      id_list.insert("end", row[0])
      fname_list.insert("end", row[1])
      lname_list.insert("end", row[2]) 
      ylevel_list.insert("end", row[3])
      gender_list.insert("end", row[4])
      pcode_list.insert("end", row[5])

#College
def show_colleges():

   def col_exists(code,colname):
      colcode = []
      col_name = []
      with open(college_path, "r") as f:
         reader = csv.reader(f)
         for row in reader:
            colcode.append(row[0])
            col_name.append(row[1])
      if code in colcode or colname in col_name:
         return True
      else:
         return False
   
   #For delete check code
   def code_exists(code):
      colcode = []
      with open(college_path, "r") as f:
         reader = csv.reader(f)
         for row in reader:
            colcode.append(row[0])
      if code in colcode:
         return True
      else:
         return False

   def used(code):
      using = []
      with open(program_path,"r") as f:
         reader = csv.reader(f)
         for row in reader:
            using.append(row[2].strip())
      if code in using:
         return True
      else:
         return False

   def show_college():
      college_code_list.delete(0,END)
      college_name_list.delete(0,END)
         #Entering data
      with open(college_path, "r") as f:  
         reader = csv.reader(f)
         next(reader)
         for row in reader:
            college_code_list.insert("end", row[0])
            college_name_list.insert("end", row[1])

   def add_college():

      def filled_in():
         info = []
         info.append(code_entry.get())
         info.append(colname_entry.get())
         if "" in info:
            return False
         else:
            return True
      
      def submit():
         if filled_in() == False:
            messagebox.showerror("Fields must be Filled", "All fields must be Filled")
         elif col_exists(code_entry.get(),colname_entry.get()) == True:
            messagebox.showerror("College Already Exists", "College Already Exists")
         else:
            college_new.append(code_entry.get())
            college_new.append(colname_entry.get())

            with open(college_path, "a", newline="") as f:  #adding
               writer = csv.writer(f)
               writer.writerow(college_new)

            college_new.clear()  #Clearing
            show_college()

         

      add_window = Toplevel()
      add_window.title("Adding College")

      add_frame = Frame(add_window)
      add_frame.grid(row=0, column=0,)

      Label(add_frame, text="College Code:", font=('Helvetica', 15)).grid(row=1, column=0, padx=10, pady=5)
      code_entry = Entry(add_frame, font=('Helvetica', 15),width=40)
      code_entry.grid(row=1, column=1, padx=10, pady=5, columnspan=2)

      Label(add_frame, text="College name:", font=('Helvetica', 15)).grid(row=2, column=0, padx=10, pady=5)
      colname_entry = Entry(add_frame, font=('Helvetica', 15),width=40)
      colname_entry.grid(row=2, column=1, padx=10, pady=5, columnspan=2)

      submit_button = Button(add_frame, text="Add College", font=('Helvetica', 15), command=submit)
      submit_button.grid(row=14, column=0, columnspan=3, pady=10)

   def delete_college():

      def deleting():
         if delcol.get() == "":
            messagebox.showerror("Field must be filled", "Field must be filled")
         elif code_exists(delcol.get()) == False:
            messagebox.showerror("College does not Exist", "College does not exist")
         elif used(delcol.get()) == True:
            messagebox.showerror("College is currently used", "A Program is currently registered to this College. To delete this college the program must be edited or deleted")
         else:
            with open(college_path, "r") as f:
               reader = csv.reader(f)
               for row in reader:
                  if row[0] != delcol.get():
                     college_keep.append(row)
            
            with open(college_path, "w", newline="") as f:
               writer = csv.writer(f)
               for row in college_keep:
                  writer.writerow(row)
            
            college_keep.clear()
            show_college()
            

      delete_window = Toplevel()
      delete_window.title("Delete College")
      delete_window.resizable(FALSE,FALSE)
      del_frame = Frame(delete_window)
      del_frame.grid(row=0,column=0, pady=10, padx=10)

      Label(del_frame, text="Delete Student", font=('Helvetica', 20)).grid(row=0, column=0, columnspan=3, padx=10, pady=10)
      Label(del_frame, text="Student ID#", font=('Helvetica', 15)).grid(row=1, column=0,pady=10)
      delcol = Entry(del_frame, font=("Helvetica", 15))
      delcol.grid(row=1, column=2)
      delete_button = Button(del_frame, text="Delete College", font=('Helvetica', 15), pady=10, padx=10, command=deleting)
      delete_button.grid(row=2, columnspan=3)

   def edit_college(): 

      def editing():

         def submit():
            if code_entry.get() == "" or cname_entry.get() == "":
               messagebox.showerror("Fields must be Filled", "Fields must be filled")
            elif col_exists(code_entry.get(), cname_entry.get()) == True and code_entry.get() != college:
               messagebox.showerror("College Already Exists", "College Already Exists")
            else:
               college_e = []
               college_e.append(code_entry.get())
               college_e.append(cname_entry.get())

               college_edit = []
               with open(college_path, "r") as f:  #read first
                  reader = csv.reader(f)
                  for row in reader:
                     if row[0] == college:
                        college_edit.append(college_e)
                     else:
                        college_edit.append(row)
               
               with open(college_path, "w", newline="") as f:
                  writer = csv.writer(f)
                  for row in college_edit:
                     writer.writerow(row)

               editing_window.destroy()
               show_college()


         if editcol.get() == "":
            messagebox.showerror("Field must be filled", "Field must be filled")
         elif code_exists(editcol.get()) == False:
            messagebox.showerror("College does not Exist", "College does not exist")
         else: 
            college = editcol.get()
            edit_window.destroy()
            college_edit = []
            #Read first
            with open(college_path, "r") as f:
               reader = csv.reader(f)
               for row in reader:
                  if row[0] == college:
                     college_edit.append(row)
            
            editing_window = Toplevel()
            editing_window.title("Editing College")
            editing_window.resizable(FALSE,FALSE)
            edit_frame = Frame(editing_window)
            edit_frame.grid(row=0, column=0)

            Label(edit_frame, text="College", font=('Helvetica', 20)).grid(row=0, column=0, columnspan=3, padx=10, pady=10)
            
            Label(edit_frame, text="Code:", font=('Helvetica', 15)).grid(row=1, column=0, padx=10)
            code_entry = Entry(edit_frame, font=('Helvetica', 15), width=40)
            code_entry.grid(row=1, column=1, padx=10, columnspan=2, pady=5)
            code_entry.insert(0, college_edit[0][0])

            Label(edit_frame, text="College name:", font=('Helvetica', 15)).grid(row=2, column=0, padx=10)
            cname_entry = Entry(edit_frame, font=('Helvetica', 15), width=40)
            cname_entry.grid(row=2, column=1, padx=10, columnspan=2, pady=5)
            cname_entry.insert(0, college_edit[0][1])

            submit_button = Button(edit_frame, text="Submit", font=('Helvetica', 15), pady=10, padx=10, command=submit)
            submit_button.grid(row=3, columnspan=3)

         
      edit_window = Toplevel()
      edit_window.title("Edit College")
      edit_window.resizable(FALSE,FALSE)
      edit_frame = Frame(edit_window)
      edit_frame.grid(row=0,column=0, pady=10, padx=10)

      Label(edit_frame, text="Edit College", font=('Helvetica', 20)).grid(row=0, column=0, columnspan=3, padx=10, pady=10)
      Label(edit_frame, text="Code:", font=('Helvetica', 15)).grid(row=1, column=0,pady=10)
      editcol = Entry(edit_frame, font=("Helvetica", 15))
      editcol.grid(row=1, column=2)
      edit_button = Button(edit_frame, text="Edit College", font=('Helvetica', 15), pady=10, padx=10, command=editing)
      edit_button.grid(row=2, columnspan=3)

   def sync_scroll_college(*args):
      college_code_list.yview(*args)
      college_name_list.yview(*args)

   def search_college(event):

      def updatecol(colleges):
         college_code_list.delete(0,END)
         college_name_list.delete(0,END)
         for row in colleges:
            college_code_list.insert("end", row[0])
            college_name_list.insert("end", row[1])


      searched = search_col.get()

      with open(college_path, "r") as f:
         reader = csv.reader(f)
         if searchcol_by.get() == "Any":
            if searched == "":
               show_college()
            else:
               college = []
               for row in reader:
                  if searched in row[0] or searched in row[1]:
                     college.append(row)
               updatecol(college)
         
         elif searchcol_by.get() == "College Code":
            if searched == "":
               show_college()
            else:
               college = []
               for row in reader:
                  if searched in row[0]:
                     college.append(row)
               updatecol(college)
         
         elif searchcol_by.get() == "College Name":
            if searched == "":
               show_college()
            else:
               college = []
               for row in reader:
                  if searched in row[1]:
                     college.append(row)
               updatecol(college)
   
   def sort_colcode():

      def update(colleges):
         college_code_list.delete(0,END)
         college_name_list.delete(0,END)

         for row in colleges:
            college_code_list.insert("end",row[0])
            college_name_list.insert("end",row[1])


      with open(college_path, "r") as f:
         reader = csv.reader(f)
         next(reader)
         sorted_code = sorted(reader, key=operator.itemgetter(0))
      update(sorted_code)
   
   def sort_colname():

      def update(colleges):
         college_code_list.delete(0,END)
         college_name_list.delete(0,END)

         for row in colleges:
            college_code_list.insert("end",row[0])
            college_name_list.insert("end",row[1])


      with open(college_path, "r") as f:
         reader = csv.reader(f)
         next(reader)
         sorted_code = sorted(reader, key=operator.itemgetter(1))
      update(sorted_code)

   college_window = Toplevel()
   college_window.title("Colleges")
   college_window.resizable(False,False)
   college_window.geometry("850x500")

   menubar = Menu(college_window)
   college_window.config(menu=menubar)

   manage_menu = Menu(menubar, tearoff=0, font=("Helvetica", 11))
   menubar.add_cascade(label="Manage College", menu=manage_menu)
   manage_menu.add_command(label="Add College", command=add_college)
   manage_menu.add_command(label="Delete College", command=delete_college)
   manage_menu.add_command(label="Edit College", command=edit_college)

   sort_menu = Menu(menubar, tearoff=0, font=("Helvetica", 11))
   menubar.add_cascade(label="Sort College", menu=sort_menu)
   sort_menu.add_command(label="None", command=show_college)
   sort_menu.add_command(label="Code", command=sort_colcode)
   sort_menu.add_command(label="Name", command=sort_colname)



   college_frame = Frame(college_window)
   college_frame.pack(side=LEFT,padx=10)

   college_button_frame = Frame(college_frame)
   college_button_frame.pack(side=LEFT,padx=10)

   search_frame = Frame(college_frame)
   search_frame.pack(side=TOP)

   Label(search_frame, text="Search by: ").pack(side=LEFT, padx=10)
   choice = ["College Code", "College Name", "Any"]
   searchcol_by = ttk.Combobox(search_frame,font=("Helvetica", 15), width=15, values=choice, state="readonly")
   searchcol_by.pack(side=LEFT,padx=5)
   search_col = Entry(search_frame, font=('Helvetica', 15), width=40)
   search_col.pack(side=LEFT,padx=5)
   search_col.bind("<KeyRelease>",search_college)

   scroll_college = Scrollbar(college_frame, orient=VERTICAL)

   college_code_frame = Frame(college_frame)
   college_code_frame.pack(side=LEFT, padx=10)
   Label(college_code_frame,text="Code").pack(side=TOP)
   college_code_list = Listbox(college_code_frame, width=10, height=15, font=("Helvetica", 15), yscrollcommand=scroll_college.set)
   college_code_list.pack(side=TOP)

   college_name_frame = Frame(college_frame)
   college_name_frame.pack(side=LEFT)
   Label(college_name_frame,text="College Name").pack(side=TOP)
   college_name_list = Listbox(college_name_frame, width=50, height=15, font=("Helvetica", 15), yscrollcommand=scroll_college.set)
   college_name_list.pack(side=LEFT,anchor=NW)

   scroll_college.config(command=sync_scroll_college)
   scroll_college.pack(side=LEFT,anchor=NE, fill=Y)

   show_college()

#program
def show_programs():

   def prog_exists(code):
      pcode = []
      with open(program_path, "r") as f:
         reader = csv.reader(f)
         for row in reader:
            pcode.append(row[0])
      if code in pcode:
         return True
      else:
         return False
   
   def prog_codename_exists(code,colname):
      progcode = []
      prog_name = []
      with open(college_path, "r") as f:
         reader = csv.reader(f)
         for row in reader:
            progcode.append(row[0])
            prog_name.append(row[1])
      if code in progcode or colname in prog_name:
         return True
      else:
         return False
   
   def add_program():
      def prog_exists(progcode,progname):
         code = []
         name = []
         with open(program_path, "r") as f:
            reader = csv.reader(f)
            for row in reader:
               code.append(row[0])
               name.append(row[1])
         if progcode in code:
            return True
         elif progname in name:
            return True
         else:
            return False
      
      def filled():
         info = []
         info.append(code_entry.get())
         info.append(pname_entry.get())
         info.append(ccode_entry.get())

         if "" in info:
            return False
         else:
            return True
      
      def submit():
         if filled() == False:
            messagebox.showerror("Fields must be filled", "Fields must be filled")
         elif prog_exists(code_entry.get(),pname_entry.get()) == True:
            messagebox.showerror("Program already exists", "Program Already exists")
         else:
            program_new.append(code_entry.get())
            program_new.append(pname_entry.get())
            program_new.append(ccode_entry.get())

            with open(program_path, "a", newline="") as f:
               writer = csv.writer(f)
               writer.writerow(program_new)

            student_new.clear()
            show_program()
            
         
      add_window = Toplevel()
      add_window.title("Add Program")
      add_window.resizable(FALSE,FALSE)

      add_frame = Frame(add_window)
      add_frame.grid(row=0, column=0,)


      Label(add_frame, text="Program", font=('Helvetica', 20)).grid(row=0, column=0, columnspan=3, padx=10, pady=10)
   
      Label(add_frame, text="Code:", font=('Helvetica', 15)).grid(row=1, column=0, padx=10, pady=5)
      code_entry = Entry(add_frame, font=('Helvetica', 15),width=40)
      code_entry.grid(row=1, column=1, padx=10, pady=5, columnspan=2)

      Label(add_frame, text="Program name:", font=('Helvetica', 15)).grid(row=2, column=0, padx=10, pady=5)
      pname_entry = Entry(add_frame, font=('Helvetica', 15),width=40)
      pname_entry.grid(row=2, column=1, padx=10, pady=5, columnspan=2)

      Label(add_frame, text="College Code:", font=('Helvetica', 15)).grid(row=3, column=0, padx=10, pady=5)
      ccode_entry = Entry(add_frame, font=('Helvetica', 15),width=40)
      ccode_entry.grid(row=3, column=1, padx=10, pady=5, columnspan=2)

      submit_button = Button(add_frame, text="Add Student", font=('Helvetica', 15),command=submit)
      submit_button.grid(row=14, column=0, columnspan=3, pady=10)
      
   def used(code):
      using = []
      with open(student_path,"r") as f:
         reader = csv.reader(f)
         for row in reader:
            using.append(row[5].strip())
      if code in using:
         return True
      else:
         return False
      
   def delete_program():

      def deleting():
         if delprogram.get() == "":
            messagebox.showerror("Field must be filled", "Field must be filled")
         elif prog_exists(delprogram.get()) == False:
            messagebox.showerror("Program does not Exist", "Program does not exist")
         elif used(delprogram.get()) == True:
            messagebox.showerror("Program is Currently Used", "A student is currently enrolled to this program. To delete this program the student enrolled must be edited or deleted")
         else:
            with open(program_path, "r") as f:  #Read
               reader = csv.reader(f)
               for row in reader:
                  if row[0] != delprogram.get():
                     program_keep.append(row)
            
            with open(program_path, "w",newline="") as f:
               writer = csv.writer(f)
               for row in program_keep:
                  writer.writerow(row)
            
            program_keep.clear() #Clear
            show_program() #relist

          

      delete_window = Toplevel()
      delete_window.title("Delete Student")
      delete_window.resizable(FALSE,FALSE)
      del_frame = Frame(delete_window)
      del_frame.grid(row=0,column=0, pady=10, padx=10)

      Label(del_frame, text="Delete Program", font=('Helvetica', 20)).grid(row=0, column=0, columnspan=3, padx=10, pady=10)
      Label(del_frame, text="Program Code: ", font=('Helvetica', 15)).grid(row=1, column=0,pady=10)
      delprogram = Entry(del_frame, font=("Helvetica", 15))
      delprogram.grid(row=1, column=2)
      delete_button = Button(del_frame, text="Delete Program", font=('Helvetica', 15), pady=10, padx=10, command=deleting)
      delete_button.grid(row=2, columnspan=3)

   def edit_program():

      def editing():

         def submit(): 
            if code_entry.get() == "" or pname_entry.get() == "" or ccode_entry.get() == "":
               messagebox.showerror("Fields must be Filled", "Fields must be filled")
            elif prog_codename_exists(code_entry.get(), pname_entry.get()) == True and code_entry.get() != program:
               messagebox.showerror("College Already Exists", "College Already Exists")
            else:
               program_e = []
               program_e.append(code_entry.get())
               program_e.append(pname_entry.get())
               program_e.append(ccode_entry.get())

               program_edit = []
               with open(program_path, "r") as f:  #read first
                  reader = csv.reader(f)
                  for row in reader:
                     if row[0] == program:
                        program_edit.append(program_e)
                     else:
                        program_edit.append(row)
               
               with open(program_path, "w", newline="") as f:
                  writer = csv.writer(f)
                  for row in program_edit:
                     writer.writerow(row)

               editing_window.destroy()
               show_program()
            
         if editprog.get() == "":
            messagebox.showerror("Field must be filled", "Field must be filled")
         elif prog_exists(editprog.get()) == False:
            messagebox.showerror("College does not Exist", "College does not exist")
         else: 
            program = editprog.get()
            edit_window.destroy()
            program_edit = []
            #Read first
            with open(program_path, "r") as f:
               reader = csv.reader(f)
               for row in reader:
                  if row[0] == program:
                     program_edit.append(row)
            
            editing_window = Toplevel()
            editing_window.title("Editing College")
            editing_window.resizable(FALSE,FALSE)
            edit_frame = Frame(editing_window)
            edit_frame.grid(row=0, column=0)

            Label(edit_frame, text="Program", font=('Helvetica', 20)).grid(row=0, column=0, columnspan=3, padx=10, pady=10)
            
            Label(edit_frame, text="Code:", font=('Helvetica', 15)).grid(row=1, column=0, padx=10)
            code_entry = Entry(edit_frame, font=('Helvetica', 15), width=40)
            code_entry.grid(row=1, column=1, padx=10, columnspan=2, pady=5)
            code_entry.insert(0, program_edit[0][0])

            Label(edit_frame, text="Program name:", font=('Helvetica', 15)).grid(row=2, column=0, padx=10)
            pname_entry = Entry(edit_frame, font=('Helvetica', 15), width=40)
            pname_entry.grid(row=2, column=1, padx=10, columnspan=2, pady=5)
            pname_entry.insert(0, program_edit[0][1])

            Label(edit_frame, text="College code:", font=('Helvetica', 15)).grid(row=3, column=0, padx=10)
            ccode_entry = Entry(edit_frame, font=('Helvetica', 15), width=40)
            ccode_entry.grid(row=3, column=1, padx=10, columnspan=2, pady=5)
            ccode_entry.insert(0, program_edit[0][2])

            submit_button = Button(edit_frame, text="Submit", font=('Helvetica', 15), pady=10, padx=10, command=submit)
            submit_button.grid(row=4, columnspan=3)

      edit_window = Toplevel()
      edit_window.title("Edit College")
      edit_window.resizable(FALSE,FALSE)
      edit_frame = Frame(edit_window)
      edit_frame.grid(row=0,column=0, pady=10, padx=10)

      Label(edit_frame, text="Edit Program", font=('Helvetica', 20)).grid(row=0, column=0, columnspan=3, padx=10, pady=10)
      Label(edit_frame, text="Program Code:", font=('Helvetica', 15)).grid(row=1, column=0,pady=10)
      editprog = Entry(edit_frame, font=("Helvetica", 15))
      editprog.grid(row=1, column=2)
      edit_button = Button(edit_frame, text="Edit Program", font=('Helvetica', 15), pady=10, padx=10, command=editing)
      edit_button.grid(row=2, columnspan=3)

   def sync_scroll_programs(*args):
      program_code_list.yview(*args)
      program_name_list.yview(*args)
      pcollege_code_list.yview(*args)
   
   def show_program():
      program_code_list.delete(0,END)
      program_name_list.delete(0,END)
      pcollege_code_list.delete(0,END)
      with open(program_path, "r") as f:
         reader = csv.reader(f)
         next(reader)
         for row in reader:
            program_code_list.insert("end", row[0])
            program_name_list.insert("end", row[1])
            pcollege_code_list.insert("end", row[2])
   
   def search_program(event):

      def updateprog(programs):
         program_code_list.delete(0,END)
         program_name_list.delete(0,END)
         pcollege_code_list.delete(0,END)
         for row in programs:
            program_code_list.insert("end", row[0])
            program_name_list.insert("end", row[1])
            pcollege_code_list.insert("end", row[2])
      
      searched = search_prog.get()
      with open(program_path,"r") as f:
         reader = csv.reader(f)
         if searchprog_by.get() == "Any":
            if searched == "":
               show_program()
            else:
               program = []
               for row in reader:
                  if searched in row[0] or searched in row[1] or searched in row[2]:
                     program.append(row)
               updateprog(program)
         
         elif searchprog_by.get() == "Program Code":
            if searched == "":
               show_program()
            else:
               program = []
               for row in reader:
                  if searched in row[0]:
                     program.append(row)
               updateprog(program)

         elif searchprog_by.get() == "Program Name":
            if searched == "":
               show_program()
            else:
               program = []
               for row in reader:
                  if searched in row[1]:
                     program.append(row)
               updateprog(program)
         
         elif searchprog_by.get() == "College Code":
            if searched == "":
               show_program()
            else:
               program = []
               for row in reader:
                  if searched in row[2]:
                     program.append(row)
               updateprog(program)

   def sort_pcode():

      def update(programs):
         program_code_list.delete(0,END)
         program_name_list.delete(0,END)
         pcollege_code_list.delete(0,END)

         for row in programs:
            program_code_list.insert("end",row[0])
            program_name_list.insert("end",row[1])
            pcollege_code_list.insert("end",row[2])


      with open(program_path, "r") as f:
         reader = csv.reader(f)
         next(reader)
         sorted_code = sorted(reader, key=operator.itemgetter(0))
      update(sorted_code)

   def sort_pname():
      
      def update(programs):
         program_code_list.delete(0,END)
         program_name_list.delete(0,END)
         pcollege_code_list.delete(0,END)

         for row in programs:
            program_code_list.insert("end",row[0])
            program_name_list.insert("end",row[1])
            pcollege_code_list.insert("end",row[2])
      
      with open(program_path,"r") as f:
         reader = csv.reader(f)
         next(reader)
         sorted_names = sorted(reader, key=operator.itemgetter(1))
      update(sorted_names)
         
   def sort_ccode():
      def update(programs):
         program_code_list.delete(0,END)
         program_name_list.delete(0,END)
         pcollege_code_list.delete(0,END)

         for row in programs:
            program_code_list.insert("end",row[0])
            program_name_list.insert("end",row[1])
            pcollege_code_list.insert("end",row[2])
      
      with open(program_path,"r") as f:
         reader = csv.reader(f)
         next(reader)
         sorted_colcode = sorted(reader, key=operator.itemgetter(2))
      update(sorted_colcode)

   program_window = Toplevel()
   program_window.title("Programs")
   program_window.resizable(False,False)
   program_window.geometry("1050x500")

   menubar = Menu(program_window)
   program_window.config(menu=menubar)

   manage_menu = Menu(menubar, tearoff=0, font=("Helvetica", 11))
   menubar.add_cascade(label="Manage Program", menu=manage_menu)
   manage_menu.add_command(label="Add Program", command=add_program)
   manage_menu.add_command(label="Delete Program", command=delete_program)
   manage_menu.add_command(label="Edit Program", command=edit_program)

   sort_menu = Menu(menubar, tearoff=0, font=("Helvetica", 11))
   menubar.add_cascade(label="Sort Program", menu=sort_menu)
   sort_menu.add_command(label="None", command=show_program)
   sort_menu.add_command(label="Code", command=sort_pcode)
   sort_menu.add_command(label="Name", command=sort_pname)
   sort_menu.add_command(label="College", command=sort_ccode)

   program_frame = Frame(program_window)
   program_frame.pack(side=LEFT,padx=10)

   search_frame = Frame(program_frame)
   search_frame.pack(side=TOP)

   Label(search_frame, text="Search by: ").pack(side=LEFT, padx=10)
   choice = ["Program Code", "Program Name","College Code", "Any"]
   searchprog_by = ttk.Combobox(search_frame,font=("Helvetica", 15), width=15, values=choice, state="readonly")
   searchprog_by.pack(side=LEFT,padx=5)
   search_prog = Entry(search_frame, font=('Helvetica', 15), width=40)
   search_prog.pack(side=LEFT)
   search_prog.bind("<KeyRelease>",search_program)

   scroll_program = Scrollbar(program_frame, orient=VERTICAL)

   program_code_frame = Frame(program_frame)
   program_code_frame.pack(side=LEFT, padx=10)
   Label(program_code_frame,text="Code").pack(side=TOP)
   program_code_list = Listbox(program_code_frame, width=10, height=15, font=("Helvetica", 15), yscrollcommand=scroll_program.set)
   program_code_list.pack(side=TOP)

   program_name_frame = Frame(program_frame)
   program_name_frame.pack(side=LEFT)
   Label(program_name_frame,text="Program Name").pack(side=TOP)
   program_name_list = Listbox(program_name_frame, width=50, height=15, font=("Helvetica", 15), yscrollcommand=scroll_program.set)
   program_name_list.pack(side=LEFT,anchor=NW)

   pcollege_code_frame = Frame(program_frame)
   pcollege_code_frame.pack(side=LEFT)
   Label(pcollege_code_frame, text="College Code").pack(side=TOP)
   pcollege_code_list = Listbox(pcollege_code_frame,width=15,height=15, font=("Helvetica",15), yscrollcommand=scroll_program.set)   
   pcollege_code_list.pack(side=LEFT)

   scroll_program.config(command=sync_scroll_programs)
   scroll_program.pack(side=LEFT,anchor=NE, fill=Y)
   
   show_program()

#Main window

main_window = Tk()

main_window.title("Student Information System")
main_window.geometry("1200x768")


menubar = Menu(main_window)
main_window.config(menu=menubar)

#Menu for viewing College and program
view_menu = Menu(menubar, tearoff=0, font=("Helvetica", 11))
menubar.add_cascade(label="View", menu=view_menu)
view_menu.add_command(label="Students", command=show_students)
view_menu.add_command(label="Colleges", command=show_colleges)
view_menu.add_command(label="Programs", command=show_programs)

#Menu for Managing student
manage_menu = Menu(menubar, tearoff=0, font=("Helvetica", 11))
menubar.add_cascade(label="Manage Student", menu=manage_menu)
manage_menu.add_command(label="Add Student", command=add_student)
manage_menu.add_command(label="Delete Student", command=delete_student)
manage_menu.add_command(label="Edit Student", command=edit_student)     

#Menu for Sorting student
sort_menu = Menu(menubar, tearoff=0, font=("Helvetica", 11))
menubar.add_cascade(label="Sort Students", menu=sort_menu)
sort_menu.add_command(label="None", command=show_students)
sort_menu.add_command(label="Year Level", command=sort_year_level)
sort_menu.add_command(label="Gender", command=sort_gender)
sort_menu.add_command(label="Last name", command=sort_lastname)
sort_menu.add_command(label="First name", command=sort_fname)
sort_menu.add_command(label="Program", command=sort_program)
sort_menu.add_command(label="ID", command=sort_id)

#for search box
search_frame = Frame(main_window)
search_frame.pack(side=TOP, padx=20, pady=10)


search_box = Entry(search_frame, font=('Helvetica', 15))
search_box.pack(side=RIGHT)
schoice = ["Any","ID#","First Name", "Last Name", "Gender", "Program Code", "Year Level"]
search_by = ttk.Combobox(search_frame,font=("Helvetica", 15), width=15, values=schoice, state="readonly")
search_by.pack(side=RIGHT,padx=5)

#Label for search box
Label(search_frame, text="Search by: ").pack(side=RIGHT)

#Listing students

main_frame = Frame(main_window)
main_frame.pack(side=TOP, padx=20, pady=20)

id_frame = Frame(main_frame)
fname_frame = Frame(main_frame)
lname_frame = Frame(main_frame)
ylevel_frame = Frame(main_frame)
gender_frame = Frame(main_frame)
pcode_frame = Frame(main_frame)


id_frame.pack(side=LEFT,padx=5)
fname_frame.pack(side=LEFT,padx=5)
lname_frame.pack(side=LEFT,padx=5)
ylevel_frame.pack(side=LEFT,padx=5)
gender_frame.pack(side=LEFT,padx=5)
pcode_frame.pack(side=LEFT,padx=5)


Label(id_frame, text="ID#", font=("Helvetica", 15)).pack(side=TOP)
Label(fname_frame, text="First Name", font=("Helvetica", 15)).pack(side=TOP)
Label(lname_frame, text="Last Name", font=("Helvetica", 15)).pack(side=TOP)
Label(ylevel_frame, text="Year Level", font=("Helvetica", 15)).pack(side=TOP)
Label(gender_frame, text="Gender", font=("Helvetica", 15)).pack(side=TOP)
Label(pcode_frame, text="Program Code", font=("Helvetica", 15)).pack(side=TOP)

scroll = Scrollbar(main_frame, orient=VERTICAL)

id_list = Listbox(id_frame, width=10, height=25,yscrollcommand=scroll.set, font=("Helvetica",15),selectmode=SINGLE)
fname_list = Listbox(fname_frame, width=20, height=25,yscrollcommand=scroll.set, font=("Helvetica",15),selectmode=SINGLE)
lname_list = Listbox(lname_frame, width=20, height=25,yscrollcommand=scroll.set, font=("Helvetica",15),selectmode=SINGLE)
ylevel_list = Listbox(ylevel_frame, width=10, height=25,yscrollcommand=scroll.set, font=("Helvetica",15),selectmode=SINGLE)
gender_list = Listbox(gender_frame, width=20, height=25,yscrollcommand=scroll.set, font=("Helvetica",15),selectmode=SINGLE)
pcode_list = Listbox(pcode_frame, width=15, height=25,yscrollcommand=scroll.set, font=("Helvetica",15),selectmode=SINGLE)

listboxes = [id_list, fname_list, lname_list, ylevel_list, gender_list, pcode_list]

for listbox in listboxes:     #Packing 
   listbox.pack(side=LEFT)

scroll.config(command=sync_scroll_student)
scroll.pack(side=RIGHT, fill=Y)

show_students()

search_box.bind("<KeyRelease>", search)

main_window.resizable(False,False)

main_window.mainloop()