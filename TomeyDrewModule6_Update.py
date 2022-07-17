#Final Project: Drew's Photo Prints
#Drew Tomey
#SDEV140
#Professor Carver
import tkinter as tk
from PIL import Image, ImageTk
root=tk.Tk()
root.title("Drew's Photo Prints")
width = 600
height = 600
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) /2, (screenheight - height) /2)
root.geometry(alignstr)
root.resizable(width=False, height=False)
root.configure(bg = 'lightblue')
photo1 = ImageTk.PhotoImage(Image.open('one.jpg'))
photo2 = ImageTk.PhotoImage(Image.open('two.jpg'))
photo3 = ImageTk.PhotoImage(Image.open('three.jpg'))
photo4 = ImageTk.PhotoImage(Image.open('four.jpg'))
Label(root, text ="     Drew's Photo Prints", font = "none 25 bold", bg = 'lightblue').grid(row = 0, column = 8)

Label(root, image = photo1, height = 80, width = 80).grid(row = 5, column = 4)
Label(root, text = "4x3 Images", font = 'none 11 bold', bg = 'lightblue').grid(row = 6, column = 4)
Label(root, image = photo2, height = 80, width = 80).grid(row = 8, column = 4)
current_value1 = tk.StringVar(value = 0)
spin_box1 = ttk.Spinbox(root, from_=0, to=100, textvariable = current_value1, wrap=True).grid(row = 5, column = 8)
Label(root, text = "$5 Each", font = 'none 11 bold', bg = 'lightblue').grid(row = 5, column = 15)
Label(root, text = "4x6 Images", font = 'none 11 bold', bg = 'lightblue').grid(row = 9, column = 4)
Label(root, image = photo3, height = 80, width = 80).grid(row = 11, column = 4)
current_value2 = tk.StringVar(value = 0)
spin_box2 = ttk.Spinbox(root, from_=0, to=100, textvariable = current_value2, wrap=True).grid(row = 8, column = 8)
Label(root, text = "$5 Each", font = 'none 11 bold', bg = 'lightblue').grid(row = 8, column = 15)
Label(root, text = "5x7 Images", font = 'none 11 bold', bg = 'lightblue').grid(row = 12, column = 4)
Label(root, image = photo4, height = 80, width = 80).grid(row = 14, column = 4)
current_value3 = tk.StringVar(value = 0)
spin_box3 = ttk.Spinbox(root, from_=0, to=100, textvariable = current_value3, wrap=True).grid(row = 11, column = 8)
Label(root, text = "$5 Each", font = 'none 11 bold', bg = 'lightblue').grid(row = 11, column = 15)
Label(root, text = "6x9 Images", font = 'none 11 bold', bg = 'lightblue').grid(row = 15, column = 4)
current_value4 = tk.StringVar(value = 0)
spin_box4 = ttk.Spinbox(root, from_=0, to=100, textvariable = current_value3, wrap=True).grid(row = 14, column = 8)
Label(root, text = "$5 Each", font = 'none 11 bold', bg = 'lightblue').grid(row = 14, column = 15)

