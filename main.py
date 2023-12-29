from tkinter import *

import pyttsx3


def say():
    engine = pyttsx3.init()

    # Set speech properties for clarity
    engine.setProperty('rate', 150)  # You can adjust the rate (words per minute) as needed
    engine.setProperty('volume', 1.0)  # You can adjust the volume (0.0 to 1.0) as needed

    x = textvalue.get()
    engine.say(x)
    engine.runAndWait()


def reset():
    textvalue.set("")


root = Tk()
root.title("Text to Speech")
root.iconbitmap("icon.ico")
root.geometry("350x250")
root.maxsize(350, 250)
root.minsize(350, 250)

# Dark theme colors
bg_color = "#333333"
fg_color = "white"

# Styling
root.configure(bg=bg_color)

# Heading
Label(root, text="RoboSpeaker", font=("Arial", 16, "bold"), bg=bg_color, fg=fg_color, pady=15).grid(row=0, column=3,
                                                                                                    sticky="n")

# Text Label
text = Label(root, text="Please Type your text:", font=("Arial", 12), bg=bg_color, fg=fg_color, pady=10)
text.grid(row=1, column=3, sticky="n")

# Entry for input
textvalue = StringVar(root)
textentry = Entry(root, textvariable=textvalue, font=("Arial", 12), width=30, bg=bg_color, fg=fg_color)
textentry.grid(row=2, column=3, pady=5, sticky="n")

# Buttons with rounded edges
say_button = Button(root, text="Say", command=say, font=("Arial", 12), bg="#4caf50", fg=fg_color, padx=10,
                    borderwidth=0, bd=0, border=0, highlightthickness=0, highlightbackground=bg_color,
                    highlightcolor=bg_color, relief="flat")
say_button.grid(row=3, column=3, pady=10, sticky="n")

reset_button = Button(root, text="Reset", command=reset, font=("Arial", 12), bg="#f44336", fg=fg_color, padx=10,
                      borderwidth=0, bd=0, border=0, highlightthickness=0, highlightbackground=bg_color,
                      highlightcolor=bg_color, relief="flat")
reset_button.grid(row=4, column=3, pady=10, sticky="n")

# Center-align all columns and rows
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
