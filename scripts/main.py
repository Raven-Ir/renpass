import tkinter as tk
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

root = tk.Tk()

#iconbar
root.iconbitmap("C:\\Users\\Irene\\Documents\\GitHub\\renpass\\assets\\key.ico")
root.title('RenPass') #title change

#window
canvas = tk.Canvas(root, width = 800, height = 600, bg = "#242424")
canvas.grid(columnspan=6, rowspan=6)

#buutons
new_pswrd_text = tk.StringVar()
new_pswrd_btn = tk.Button(root, textvariable= new_pswrd_text, font="Consolas")
new_pswrd_text.set("new password")
new_pswrd_btn.grid(column=2, row=3)

saved_pswrd_text = tk.StringVar()
saved_pswrd_btn = tk.Button(root, textvariable=saved_pswrd_text, font="Consolas")
saved_pswrd_text.set("saved passwords")
saved_pswrd_btn.grid(column=3, row=3)

#logo
logo = Image.open("C:\\Users\\Irene\\Documents\\GitHub\\renpass\\assets\\renpass_logo.png")
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo #this line is necessary
logo_label.grid(column=0, row = 0)





root.mainloop()