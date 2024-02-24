import tkinter as tk
from tkinter import messagebox

# Function to handle instructor login (replace with actual authentication)
def login_instructor():
    global is_instructor, instructor_frame
    instructor_name = instructor_name_entry.get()

    if instructor_name == "John Doe":  # Replace with secure authentication
        is_instructor = True
        #login_window.destroy()
        instructor_frame.pack_forget()
        instructor_dashboard.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    else:
        messagebox.showerror("Error", "Enter correct Instructor Name")

# Function to handle instructor logout
def logout_instructor():
    global is_instructor, instructor_frame
    is_instructor = False
    instructor_dashboard.pack_forget()
    instructor_frame.pack()


def show_instructor_page():
    student_frame.pack_forget()
    instructor_dashboard.pack_forget()
    instructor_frame.pack()

def show_student_page():
    instructor_frame.pack_forget()
    instructor_dashboard.pack_forget()
    student_frame.pack()


def add_student():
    student_name = student_name_entry.get()
    student_id = student_id_entry.get()
    student_matric = student_matric_entry.get()

    if not (student_name and student_id and student_matric):
        tk.messagebox.showerror("Error", "Please enter all student information.")
    else:
        formatted_info = f"{student_name} - {student_id} - {student_matric}"
        student_list.insert(tk.END, formatted_info)
        clear_student_info()

def clear_student_info():
    student_name_entry.delete(0, tk.END)
    student_id_entry.delete(0, tk.END)
    student_matric_entry.delete(0, tk.END)

def delete_student():
    selected_index = student_list.curselection()
    if selected_index:
        student_list.delete(selected_index[0])


# Create the main window
root = tk.Tk()
root.title("Student-Instructor Platform")
root.geometry("500x500")

# Styling
root.configure(bg="green")

# Student Section
student_frame = tk.LabelFrame(root, text="Student Section", padx=10, pady=10)
student_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

student_name_label = tk.Label(student_frame, text="Student Name:")
student_name_label.grid(row=0, column=0)

student_name_entry = tk.Entry(student_frame, width=20)
student_name_entry.grid(row=0, column=1)

student_id_label = tk.Label(student_frame, text="Student ID:")
student_id_label.grid(row=1, column=0)

student_id_entry = tk.Entry(student_frame, width=20)
student_id_entry.grid(row=1, column=1)

student_matric_label = tk.Label(student_frame, text="Matric Number:")
student_matric_label.grid(row=2, column=0)

student_matric_entry = tk.Entry(student_frame, width=20)
student_matric_entry.grid(row=2, column=1)

submit_button = tk.Button(student_frame, text="Submit Student Info", command=add_student)
submit_button.grid(row=3, column=1)

clear_button = tk.Button(student_frame, text="Clear", command=clear_student_info)
clear_button.grid(row=3, column=0)

student_next_button = tk.Button(student_frame, text="Go to Instructor Login Page", command=show_instructor_page)
student_next_button.grid(row=4, column=0, columnspan=2)

# Instructor Section
instructor_frame =  tk.LabelFrame(root, text="Instructor Login Page", padx=10, pady=10)
instructor_frame.pack_forget()

instructor_name_label = tk.Label(instructor_frame, text="Instructor Name:")
instructor_name_label.grid(row=0, column=0)

instructor_name_entry = tk.Entry(instructor_frame)
instructor_name_entry.grid(row=0, column=1)

instructor_next_button = tk.Button(instructor_frame, text="Go to student page", command=show_student_page)
instructor_next_button.grid(row=4, column=0)

instructor_submit_button = tk.Button(instructor_frame, text="Login", command=login_instructor)
instructor_submit_button.grid(row=2, column=1, pady=4, padx=2)

#instructor Dashboard
instructor_dashboard =  tk.LabelFrame(root, text="Instructor Dashboard", padx=10, pady=10)
instructor_frame.pack_forget()

student_list_label = tk.Label(instructor_dashboard, text="Registered Students:")
student_list_label.pack()

delete_buttn = tk.Button(instructor_dashboard, text="Delete Selected", command=delete_student, bg="blue", fg="white")
delete_buttn.pack(pady=10)

# Logout button in instructor section
logout_button = tk.Button(instructor_dashboard, text="Logout", command=logout_instructor, bg="red", fg="white")
logout_button.pack(pady=10)

student_list = tk.Listbox(instructor_dashboard, font=("Arial", 14))
student_list.pack(fill=tk.BOTH, expand=True)

root.mainloop()