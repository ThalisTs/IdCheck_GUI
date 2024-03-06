import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def check_name(event=None):
    input_name = name_entry.get()
    input_birthday = f"{day_var.get()}-{month_var.get()}-{year_var.get()}"
    variations = ["eleni", "helen", "helena", "elaine", "eleanor", "ellen", "ella",]
    if input_name.lower() in variations:
        if check_birthday(input_birthday):
            messagebox.showinfo("Success", "nice")  # Display message
            root.destroy()
        else:
            result_label.config(text="Incorrect birthday. Exiting")
            messagebox.showinfo("Wrong Date of Birth", "The input date was wrong")
            root.destroy()
    else:
        result_label.config(text="Invalid name. Exiting")
        messagebox.showinfo("Λάθος Όνομα", f"ΔΕΝ ΕΙΣΑΙ ΔΕΚΤΟΣ {input_name} ")
        root.destroy()

def check_birthday(birthday_str):
    try:
        # Convert the input string to a datetime object
        birthday = datetime.strptime(birthday_str, "%d-%m-%Y")
        
        # Check if the birthday matches the required date
        if birthday.date() == datetime(2000, 1, 1).date():
            return True
        else:
            return False
    except ValueError:
        return False

# Create the main window
root = tk.Tk()
root.title("Name and Birthday Verification")
root.geometry("1200x800")

# Create and pack widgets
name_label = tk.Label(root, text="Enter your name:", font=("Helvetica", 18))
name_label.pack()

name_entry = tk.Entry(root, font=("Helvetica", 12), bd=2, relief=tk.GROOVE)
name_entry.pack()

# Birthday dropdowns
day_label = tk.Label(root, text="Day:", font=("Helvetica", 12))
day_label.pack()

day_var = tk.StringVar(root)
day_dropdown = tk.OptionMenu(root, day_var, *range(1, 32))
day_dropdown.pack()

month_label = tk.Label(root, text="Month:", font=("Helvetica", 12))
month_label.pack()

month_var = tk.StringVar(root)
month_dropdown = tk.OptionMenu(root, month_var, *range(1, 13))
month_dropdown.pack()

year_label = tk.Label(root, text="Year:", font=("Helvetica", 12))
year_label.pack()

year_var = tk.StringVar(root)
year_dropdown = tk.OptionMenu(root, year_var, *range(1980, 2023))
year_dropdown.pack()

verify_button = tk.Button(root, text="Verify Name and Birthday", command=check_name, bg="Pink", fg="white")
verify_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Run the application
root.mainloop()