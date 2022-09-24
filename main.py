import tkinter as tk
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

root = tk.Tk()

#iconbar
root.iconbitmap("./assets/key.ico")
root.title('pswrd') #title change

#window
canvas = tk.Canvas(root, width = 800, height = 600, bg = "#242424", bd=0, highlightthickness=0)
canvas.grid(columnspan=20, rowspan=20)

#logo
logo = Image.open("./assets/renpass_logo.png")
logo = logo.resize((200,100), Image.Resampling.LANCZOS)
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo, borderwidth=0, highlightthickness=0)
logo_label.image = logo #this line is necessary
logo_label.grid(columnspan=4, row = 0)

#buutons
new_pswrd_text = tk.StringVar()
new_pswrd_btn = tk.Button(root, textvariable= new_pswrd_text, font="Consolas")
new_pswrd_text.set("new password")
new_pswrd_btn.grid(column=4, row=8)

saved_pswrd_text = tk.StringVar()
saved_pswrd_btn = tk.Button(root, textvariable=saved_pswrd_text, font="Consolas")
saved_pswrd_text.set("saved passwords")
saved_pswrd_btn.grid(column=5, row=8)






root.mainloop()