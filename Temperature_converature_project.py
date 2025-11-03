

'''
while True:
    try:
        for i in range (10):
            C= float(input("Enter the Temperature Value : "))
            F=(C*(9/5))+32
            print(f"The Farhenhite vale is :{F} ")
    except Exception as e:
        print(f"error occers: {e}  ")
        print("Skipping error and continuing...\n")
'''
import tkinter as tk
from tkinter import messagebox

def calculate():
    results = []  # Moved inside the function

    try:
        value1 = float(entry1.get())
    except Exception as e:
        # Show error in a popup
        messagebox.showerror("Error", f"The error message is: {e}")
        return  # Stop the function so it doesn't continue with invalid input

    try:
        F = (value1 * (9/5)) + 32  # Convert Celsius to Fahrenheit
        results.append(f"Fahrenheit: {F}")
    except Exception as e:
        results.append(f"Calculation Error: {e}")

    # Show the result in the GUI
    result_label.config(text="\n".join(results))


# Create GUI window
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("400x200")

tk.Label(root, text="Enter temperature in Celsius:").pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack(pady=5)

calc_button = tk.Button(root, text="Convert to Fahrenheit", command=calculate)
calc_button.pack(pady=10)

result_label = tk.Label(root, text="", justify="left")
result_label.pack(pady=10)

root.mainloop()
