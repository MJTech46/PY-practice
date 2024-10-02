import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Click Counter")

# Initialize the counter variable
counter = 0

# Function to update the counter
def update_counter():
    global counter
    counter += 1
    label.config(text=f"Button clicked: {counter} times")

# Create a frame to hold the widgets
frame = tk.Frame(root)
frame.pack(expand=True, fill='both')

# Create a label to display the counter
label = tk.Label(frame, text="Button clicked: 0 times")
label.pack(padx=20, pady=20)

# Create a button that calls the update_counter function when clicked
button = tk.Button(frame, text="Click Me", command=update_counter)
button.pack(padx=20, pady=20)

# Center the frame in the window
frame.place(relx=0.5, rely=0.5, anchor='center')

# Run the application
root.mainloop()
