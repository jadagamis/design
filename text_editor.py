import tkinter.messagebox
from tkinter import *
from tkinter import filedialog

filename = None

def new_file():
    global filename
    filename = "Untitled"
    my_text.delete(0.0, END)


def save_file():
    global filename
    t = my_text.get(0.0, END)
    if my_text.compare("end-1c", "==", "1.0"):
        # tkinter.messagebox.showerror(title="Oops!", message="Unable to save file.")
        tkinter.messagebox.showerror(title="Oops!", message="Your file is empty... and can't be saved.")
    else:
        status_bar = Label(root, text="Saved", anchor=E)
        status_bar.pack(fill=X, side=BOTTOM)


def save_as():
    f = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    t = my_text.get(0.0, END)
    try:
        f.write(t.rstrip())
    except:
        tkinter.messagebox.showerror(title="Oops!", message="Unable to save file.")


def open_file():
    f = filedialog.askopenfile(mode="r")
    t = f.read()
    my_text.delete(0.0, END)
    my_text.insert(0.0, t)


root = Tk()
root.title("Text Editor")
root.geometry("900x520")

# main frame
my_frame = Frame(root)
my_frame.pack(pady=5)

# scrollbar
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

# text box
my_text = Text(my_frame, width=97, height=25, font=("Helvetica", 16), selectforeground="black", undo=True,
               yscrollcommand=text_scroll.set)
my_text.pack()

# configure scrollbar
text_scroll.config(command=my_text.yview)

# menu
my_menu = Menu(root)
root.config(menu=my_menu)

# add file menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_as)
file_menu.add_separator()
file_menu.add_command(label="Quit", command=root.quit)

# edit menu
edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")
edit_menu.add_command(label="Undo")
edit_menu.add_command(label="Redo")

root.mainloop()
