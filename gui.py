import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import requests

API_URL = "http://127.0.0.1:8000/generate_course"

def generate_course():
    # Grab user input from the text fields and strip whitespace
    topic = topic_entry.get().strip()
    duration = duration_entry.get().strip()

    # Make sure both fields have something in them
    if not topic or not duration:
        messagebox.showwarning("Input error", "Please enter both topic and duration.")
        return

    payload = {"topic": topic, "duration": duration}

    # Call the backend API to generate the course
    try:
        response = requests.post(API_URL, json=payload)
        response.raise_for_status()
    except Exception as e:
        messagebox.showerror("API error", f"Failed to call API:\n{e}")
        return

    data = response.json()
    course_text = data.get("course", "No course content returned.")

    # Show the result in the text box, clearing old text first
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, course_text)

# Set up the main window
root = tk.Tk()
root.title("Course Generator")

# Put everything inside a frame with some padding
frm = ttk.Frame(root, padding=10)
frm.grid(row=0, column=0, sticky="NSEW")

# Label and input for the course topic
ttk.Label(frm, text="Course Topic:").grid(row=0, column=0, sticky="W")
topic_entry = ttk.Entry(frm, width=40)
topic_entry.grid(row=0, column=1, pady=5)

# Label and input for duration (like "5 days")
ttk.Label(frm, text="Duration (e.g. 5 days):").grid(row=1, column=0, sticky="W")
duration_entry = ttk.Entry(frm, width=40)
duration_entry.grid(row=1, column=1, pady=5)

# Button that triggers the course generation
generate_btn = ttk.Button(frm, text="Generate Course", command=generate_course)
generate_btn.grid(row=2, column=0, columnspan=2, pady=10)

# Text box with scrollbar for showing the generated course
result_text = scrolledtext.ScrolledText(frm, width=60, height=20)
result_text.grid(row=3, column=0, columnspan=2)

# Start the GUI event loop
root.mainloop()
