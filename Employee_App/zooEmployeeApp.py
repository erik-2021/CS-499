# The code for changing pages was derived from: http://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
# License: http://creativecommons.org/licenses/by-sa/3.0/	

# Hashing/Salt Reference: https://nitratine.net/blog/post/how-to-hash-passwords-in-python/

# Some of the fake names in  the database were generated with this: https://www.fakenamegenerator.com/gen-random-us-us.php
# Some of the job titles in the database were derived/influenced from here: https://nationalzoo.si.edu/education/wildlife-careers

# The "base code" (how to use multiple frames/change between them) was derived from the 1st reference above.   
# Modifed in accordance with creative commons license for an educational project. 
# Added Complete functionality which includes user login, hashing, and CRUD operations for a sqlite3 database. 

# Important Notes:
# 1. Unhashed password is only stored in the  DB for this educational project. This would not be done in a real life scenario (Major Vulnerability)
#       * This is done so multiple different logins & passwords can be tested and modified without keeping track of every password. 


#from tkinter import *
import tkinter as tk # Used for GUI
import sqlite3 # Used for SQL database  connection
import hashlib # Used for password hashing
import os # Used to generate a salt
import zooEmployeeAppFunctions as eaf # Functions created for the zoo employee app

# Predefined fonts
large_font= ("Verdana", 12)
norm_font = ("Helvetica", 10)
small_font = ("Helvetica", 8)

# Logged in employee info
logged_in_employee_id = 0
logged_in_permission_level = 0

# Call this to open a popup message with one button that destroys the popup
def pop_up_msg(msg, button_label, title):
    popup = tk.Tk()
    popup.wm_title(title)
    label = tk.Label(popup, text=msg, font=norm_font)
    label.pack(side = "top", fill = "x", pady = 10)
    B1 = tk.Button(popup, text=button_label, command = popup.destroy)
    B1.pack()
    popup.mainloop()


# Class for displaying all of the different frames
class Frames(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side = "top", fill = "both", expand = True)

        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {}

        # Loop through all the pages
        for F in (StartPage, HomePage, ChangePassword, AdminPage, AddNewEmployeePage, UpdateEmployeePage):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row = 0, column = 0, sticky="nsew")

        self.show_frame(StartPage)

        # Called to show a specific frame
    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global logged_in_employee_id
        logged_in_employee_id = 0 # Reset to 0 (No One) In case it's used differently in the future
        global logged_in_permission_level
        logged_in_permission_level = 0

        # Check to see if password is correct
        def check_credentials(entered_username, entered_password):
            
            is_login_valid = eaf.check_password(entered_password, entered_username)
            
            # Check to see if password hashes match
            if is_login_valid:
                # Get Permission Level
                permission_level = eaf.get_permission_level(entered_username)

                # Set global employee info
                global logged_in_permission_level
                logged_in_permission_level = permission_level
                global logged_in_employee_id
                logged_in_employee_id = entered_username
                controller.show_frame(HomePage)
            else:
                pop_up_msg("Incorrect Password!", "Acknowledge ", "Error") 


            # Clear the textboxes
            try:
                username.delete(0, len(str(entered_username)))
                password.delete(0, len(str(entered_password)))
            except:
                print("Program Exited")

        # Textboxes, Labels & Buttons
        label_title = tk.Label(self, text="Please Login", font=large_font)
        label_title.grid(row = 0, column = 0)
        
        label_emp_id = tk.Label(self, text="Employee ID: ")
        label_emp_id.grid(row = 1, column = 0)

        username = tk.Entry(self, width = 25)
        username.grid(row = 1, column = 2)

        label_pw = tk.Label(self, text="Password: ")
        label_pw.grid(row = 2, column = 0)

        password = tk.Entry(self, width = 25)
        password.grid(row = 2, column = 2)

        # Check credentials
        button_login = tk.Button(self, text="Login",
                    command = lambda: check_credentials(username.get(), password.get()))
        button_login.grid(row = 3, column = 1, pady = 10)



class HomePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def check_admin_creds():
            global logged_in_permission_level

            if logged_in_permission_level >= 7:
                controller.show_frame(AdminPage)
            else:  
                pop_up_msg("You're not authorized to access this. \n\n Action logged.", "I Understand", "UNAUTHORIZED!") 


        # Textboxes, Labels & Buttons
        label_title = tk.Label(self, text="Successfully Logged In!", font=large_font)
        label_title.pack(pady = 10,padx = 10)

        button_change_pw = tk.Button(self, text="Change Password",
                            command = lambda: controller.show_frame(ChangePassword))
        button_change_pw.pack()

        button_logout = tk.Button(self, text="Logout",
                            command = lambda: controller.show_frame(StartPage))
        button_logout.pack(pady = 5)
        

        button_admin_menu = tk.Button(self, text="Admin Menu",
                            command = lambda: check_admin_creds())
        button_admin_menu.pack()

          
class ChangePassword(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)



        def change_password(enteredCurrentPass, enteredNewPass):
            global logged_in_employee_id

            # Check to see if existing p/w is correct. 
            isPasswordValid = eaf.check_password(enteredCurrentPass, logged_in_employee_id)

            # Update p/w if valid
            if isPasswordValid:
                eaf.create_password_hash(enteredNewPass, logged_in_employee_id)
                pop_up_msg("Password Changed!", "Acknowledge ", "Success!") 
            else:
                pop_up_msg("Invalid Password \nNo changes made. ", "Acknowledge ", "SQL Error") 


        # Textboxes, Labels & Buttons
        label_title = tk.Label(self, text="Password Change", font=large_font)
        label_title.grid(row = 0, column = 0)

        label_curr_pass = tk.Label(self, text="Current Password: ")
        label_curr_pass.grid(row = 1, column = 0)

        current_password = tk.Entry(self, width = 25)
        current_password.grid(row = 1, column = 2)

        label_new_pass = tk.Label(self, text="New Password: ")
        label_new_pass.grid(row = 3, column = 0)

        new_password = tk.Entry(self, width = 25)
        new_password.grid(row = 3, column = 2)

        button_submit = tk.Button(self, text="Submit", # Change password
                            command = lambda: change_password(current_password.get(), new_password.get()))
        button_submit.grid(row = 4, column = 2, padx = 5)

        button_back = tk.Button(self, text="Go Back", # Return to previous page
                            command = lambda: controller.show_frame(HomePage)) 
        button_back.grid(row = 4, column = 0, padx = 5)


class AdminPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def reset_users_password(reset_id):
             # Connect to database.
            conn = sqlite3.connect('zooEmployeeData.db')
            c = conn.cursor()

            # Gets employees SSN for p/w reset
            #ssn = c.execute("SELECT ssn FROM zooEmployeeData WHERE employee_id = ?", (reset_id,))
            #conn.commit()
            #ssn = c.fetchone() 
            #ssn = ssn[0]

            # Gets employees SSN for p/w reset
            c.execute("SELECT ssn FROM zooEmployeeData WHERE employee_id = ?", (reset_id,))
            conn.commit()
            ssn = c.fetchone()[0]

            # Create a cursor
            c = conn.cursor()

            #Close Connection to DB
            conn.close()

            # Update the password
            eaf.create_password_hash(ssn, reset_id)

            pop_up_msg("Password Reset!", "Acknowledge ", "Success") 


        def delete_user(empIdToDel):
            # Connect to database
            conn = sqlite3.connect('zooEmployeeData.db')

            # isolation level none allows closing connection for error handling below
            conn.isolation_level = None
            c = conn.cursor()

            try: 
                # Delete employee
                c.execute("DELETE FROM zooEmployeeData WHERE employee_id = ?", (empIdToDel,))
                conn.commit()
                pop_up_msg(str(c.rowcount) + " record(s) deleted. ", "Acknowledge ", "SQL Info") 
            except sqlite3.Error as err:
                # Display error message
                pop_up_msg(err, "Acknowledge ", "SQL Error") 
            finally:
                # Close connection \
                conn.close()

        # Textboxes, Labels & Buttons
        label_admin_menu = tk.Label(self, text="Admin Menu", font=large_font)
        label_admin_menu.grid(row = 0, column = 0)

        label_emp_id = tk.Label(self, text="Employee ID: ")
        label_emp_id.grid(row = 2, column = 0)

        employee_id_to_delete = tk.Entry(self, width = 15)
        employee_id_to_delete.grid(row = 2, column = 1)

        button_del_emp = tk.Button(self, text="Delete Employee", # Delete an Employee
                            command = lambda: delete_user(int(employee_id_to_delete.get())))
        button_del_emp.grid(row = 2, column = 2)

        button_emp_id = tk.Label(self, text="Employee ID: ")
        button_emp_id.grid(row = 3, column = 0)

        employee_id_to_reset = tk.Entry(self, width = 15)
        employee_id_to_reset.grid(row = 3, column = 1)

        button_reset_pass = tk.Button(self, text="Reset Employee Pass", # Reset password 
                            command = lambda: reset_users_password(employee_id_to_reset.get()))
        button_reset_pass.grid(row = 3, column = 2, pady = 5)

        # Add new Employee
        buton_add_emp = tk.Button(self, text="Add Employee", 
                            command = lambda: controller.show_frame(AddNewEmployeePage)) 
        buton_add_emp.grid(row = 4, column = 0)

        # Logout
        button_logout = tk.Button(self, text="Logout", 
                            command = lambda: controller.show_frame(StartPage)) 
        button_logout.grid(row = 4, column = 1)

        # Go back
        button_back = tk.Button(self, text="Go Back", 
                            command = lambda: controller.show_frame(HomePage)) 
        button_back.grid(row = 4, column = 2)

        # Update an employee
        update_button = tk.Button(self, text="Update Employee", 
                            command = lambda: controller.show_frame(UpdateEmployeePage)) 
        update_button.grid(row = 5, column = 1)


class AddNewEmployeePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # TODO: Make max permission level for employees through GUI to prevent giving admin perms
        def add_new_employee():

            popup_msg_string = "Employee Added. "

            # Create a random salt for use with hashing
            salt = os.urandom(32)

            # Password Hashing
            key = hashlib.pbkdf2_hmac('sha256', new_employee_pass.get().encode('utf-8'), salt, 100000)

            # Connect to database
            conn = sqlite3.connect('zooEmployeeData.db')

            new_permission_level = int(new_employee_perm_level.get())

            # Set max permission level settable through GUI. (prevent accidential admin perms)
            if  new_permission_level > 7:
                new_permission_level = 7
                popup_msg_string = "Employee Added. \n Max permission level settable here is 7. \n Permission level set to 7. "
            # isolation level none allows closing connection for error handling below
            conn.isolation_level = None
            c = conn.cursor()

            # Insert new employee into DB
            try:
                c.execute("""INSERT INTO zooEmployeeData
                          (first_name, last_name, job_title, employee_id, ssn, password_unhashed, salt, key, permission_level)
                          VALUES
                          (?, ?, ?, ?, ?, ?, ?, ?, ?)
                          """, (str(new_employee_first.get()),str(new_employee_last.get()), str(new_employee_title.get()), int(new_employee_id.get()), new_employee_ssn.get(), new_employee_pass.get(), salt, key, new_permission_level  ))   
            
                pop_up_msg(popup_msg_string, "Acknowledge ", "Success") 
            # Error handling -- most likely a duplicate employee ID (must be unique)
            except sqlite3.Error as err:
                # Display error message
                pop_up_msg(err, "Acknowledge ", "SQL Error") 
            finally:
                # Close connection 
                conn.close()

        # Textboxes, Labels & Buttons
        label_title = tk.Label(self, text="Add Employee to DB", font=large_font)
        label_title.grid(row = 0, column = 0)

        label_first = tk.Label(self, text="First Name: ")
        label_first.grid(row = 1, column = 0)

        new_employee_first = tk.Entry(self, width = 15)
        new_employee_first.grid(row = 1, column = 1)

        label_last = tk.Label(self, text="Last Name: ")
        label_last.grid(row = 2, column = 0)

        new_employee_last = tk.Entry(self, width = 15)
        new_employee_last.grid(row = 2, column = 1)

        label_job_title = tk.Label(self, text="Job Title: ")
        label_job_title.grid(row = 3, column = 0)

        new_employee_title = tk.Entry(self, width = 15)
        new_employee_title.grid(row = 3, column = 1)

        label_emp_id = tk.Label(self, text="Employee ID: ")
        label_emp_id.grid(row = 4, column = 0)

        new_employee_id = tk.Entry(self, width = 15)
        new_employee_id.grid(row = 4, column = 1)

        label_ssn = tk.Label(self, text="SSN: ")
        label_ssn.grid(row = 5, column = 0)

        new_employee_ssn = tk.Entry(self, width = 15)
        new_employee_ssn.grid(row = 5, column = 1)

        label_pass = tk.Label(self, text="Password: ")
        label_pass.grid(row = 6, column = 0)

        new_employee_pass = tk.Entry(self, width = 15)
        new_employee_pass.grid(row = 6, column = 1)

        label_perm_lvl = tk.Label(self, text="Permission Level: ")
        label_perm_lvl.grid(row = 7, column = 0)

        new_employee_perm_level = tk.Entry(self, width = 15)
        new_employee_perm_level.grid(row = 7, column = 1)

        button_add_emp = tk.Button(self, text="Add Employee to DB", 
                            command = lambda: add_new_employee())
        button_add_emp.grid(row = 8, column = 1)

        button_back = tk.Button(self, text="Go Back", 
                            command = lambda: controller.show_frame(AdminPage)) 
        button_back.grid(row = 8, column = 0)

class UpdateEmployeePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        # Load and populate employee data fields
        def load_employee():

            # Error + Return if entered employee id is not an integer 
            try:
                emp_id = int(employee_id_to_update.get())
            except ValueError:
                pop_up_msg("Please enter an employee ID first", "Acknowledge", "ERROR")
                return


            conn = sqlite3.connect('zooEmployeeData.db')
            c = conn.cursor()

            # Loads employee
            c.execute("SELECT * FROM zooEmployeeData WHERE employee_id = ?", (emp_id,))
            conn.commit()
            
            emp_data = c.fetchone() 

            if emp_data is None:
                pop_up_msg("Employee not found.", "Acknowledge", "ERROR")
                return


            # Delete any exisitng data before inserting update data
            update_employee_first.delete(0, len(str(update_employee_first)))
            update_employee_last.delete(0, len(str(update_employee_last)))
            update_employee_title.delete(0, len(str(update_employee_title)))
            update_employee_ssn.delete(0, len(str(update_employee_ssn)))
            update_employee_perm_level.delete(0, len(str(update_employee_perm_level)))

            # Insert loaded employee data
            update_employee_first.insert(len(str(emp_data[0])), emp_data[0]) 
            update_employee_last.insert(len(str(emp_data[1])), emp_data[1])
            update_employee_title.insert(len(str(emp_data[2])), emp_data[2])
            update_employee_ssn.insert(len(str(emp_data[4])), emp_data[4])
            update_employee_perm_level.insert(len(str(emp_data[8])), emp_data[8])
 
            #Close Connection to DB
            conn.close()


        def update_employee():
            
            # Connect to DB
            conn = sqlite3.connect('zooEmployeeData.db')
            c = conn.cursor()

            # Error + Return if entered employee id is not an integer 
            try:
                emp_id = int(employee_id_to_update.get())
            except ValueError:
                pop_up_msg("Please enter an employee ID first", "Acknowledge", "ERROR")
                return

            try: 
                # Update Employee Info
                c.execute("UPDATE zooEmployeeData SET first_name = ?, last_name = ?, job_title = ?, ssn = ?, permission_level = ? WHERE employee_id = ?", (update_employee_first.get(), update_employee_last.get(), update_employee_title.get(), update_employee_ssn.get(), update_employee_perm_level.get(), emp_id,))
                conn.commit()
                pop_up_msg(str(c.rowcount) + " record(s) Updated. ", "Acknowledge ", "SQL Info") 
            except sqlite3.Error as err:
                # Display error message
                pop_up_msg(err, "Acknowledge ", "SQL Error") 
            finally:
                # Close connection to db
                conn.close()

        # Textboxes, Labels & Buttons
        label_title = tk.Label(self, text="Update Employee", font=norm_font)
        label_title.grid(row = 0, column = 1)

        label_emp_id = tk.Label(self, text="Employee ID: ")
        label_emp_id.grid(row = 2, column = 0)

        employee_id_to_update = tk.Entry(self, width = 15)
        employee_id_to_update.grid(row = 2, column = 1)

        button_load_emp = tk.Button(self, text="Load Employee", # Delete an Employee
                            command = lambda: load_employee())
        button_load_emp.grid(row = 2, column = 2)

        # Data to load & update below

        label_title = tk.Label(self, text="*auto-populate below*")
        label_title.grid(row = 3, column = 1, pady = 5)

        label_first = tk.Label(self, text="First Name: ")
        label_first.grid(row = 4, column = 0)

        update_employee_first = tk.Entry(self, width = 15)
        update_employee_first.grid(row = 4, column = 1)

        label_last = tk.Label(self, text="Last Name: ")
        label_last.grid(row = 5, column = 0)

        update_employee_last = tk.Entry(self, width = 15)
        update_employee_last.grid(row = 5, column = 1)

        label_job_title = tk.Label(self, text="Job Title: ")
        label_job_title.grid(row = 6, column = 0)

        update_employee_title = tk.Entry(self, width = 15)
        update_employee_title.grid(row = 6, column = 1)

        label_ssn = tk.Label(self, text="SSN: ")
        label_ssn.grid(row = 8, column = 0)

        update_employee_ssn = tk.Entry(self, width = 15)
        update_employee_ssn.grid(row = 8, column = 1)

        label_perm_lvl = tk.Label(self, text="Permission Level: ")
        label_perm_lvl.grid(row = 9, column = 0)

        update_employee_perm_level = tk.Entry(self, width = 15)
        update_employee_perm_level.grid(row = 9, column = 1)

        save_button = tk.Button(self, text="SAVE CHANGES", 
                            command = lambda: update_employee())
        save_button.grid(row = 10, column = 1)

        back_button = tk.Button(self, text="Go Back", 
                            command = lambda: controller.show_frame(AdminPage)) 
        back_button.grid(row = 10, column = 0, pady = 5)

app = Frames()
app.mainloop()



# TODO - REMOVE BEFORE SUBMITTING IN WEEK 7
# Python Style Guide:

# Reference: https://google.github.io/styleguide/pyguide.html#316-naming
# module_name, package_name, ClassName, method_name, ExceptionName, function_name, GLOBAL_CONSTANT_NAME, global_var_name, 
# instance_var_name, function_parameter_name, local_var_name.