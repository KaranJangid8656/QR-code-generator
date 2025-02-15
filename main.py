from tkinter import *
from tkinter import ttk, filedialog, messagebox
import pyqrcode
from PIL import Image, ImageTk

# Color mapping for valid hex values
COLOR_MAP = {
    "black": "#000000",
    "blue": "#0000FF",
    "red": "#FF0000",
    "green": "#008000",
    "white": "#FFFFFF",
    "yellow": "#FFFF00",
    "gray": "#808080",
    "lightblue": "#ADD8E6"
}

def gen_qr():
    data = con.get().strip()
    if data:
        fg_color = COLOR_MAP[color_fg.get()]
        bg_color = COLOR_MAP[color_bg.get()]
        
        qr = pyqrcode.create(data)
        qr.png("temp_qr.png", scale=8, module_color=fg_color, background=bg_color)
        
        image = Image.open("temp_qr.png").resize((200, 200), Image.Resampling.LANCZOS)
        img = ImageTk.PhotoImage(image)
        l4.config(image=img, text='')
        l4.image = img
    else:
        l4.config(text="Enter valid content", image='')

def save():
    data = con.get().strip()
    if not data:
        messagebox.showerror("Error", "Enter content first!")
        return

    file = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png"), ("SVG Files", "*.svg")])
    if file:
        fg_color = COLOR_MAP[color_fg.get()]
        bg_color = COLOR_MAP[color_bg.get()]
        
        qr = pyqrcode.create(data)
        qr.png(file, scale=8, module_color=fg_color, background=bg_color) if file.endswith('.png') else qr.svg(file, scale=8)
        messagebox.showinfo("Success", f"QR Code saved as {file}")

wind = Tk()
wind.title('QR Code Generator')
wind.geometry('500x550')
wind.resizable(0, 0)
wind.config(bg='#F5F5F5')

Label(wind, text="QR Code Generator", font=("Arial", 20, "bold"), bg='#F5F5F5', fg='#333').pack(pady=10)

frame = Frame(wind, bg='#F5F5F5')
frame.pack(pady=5)
Label(frame, text="Enter Content:", font=("Arial", 12), bg='#F5F5F5', fg='#333').grid(row=0, column=0, padx=5, pady=5)
con = StringVar()
e1 = Entry(frame, textvariable=con, width=40, font=("Arial", 12), bg='#FFFFFF', relief=FLAT, bd=5)
e1.grid(row=0, column=1, padx=5, pady=5)

color_fg, color_bg = StringVar(value='black'), StringVar(value='white')

color_frame = Frame(wind, bg='#F5F5F5')
color_frame.pack(pady=5)
Label(color_frame, text="QR Color:", font=("Arial", 11), bg='#F5F5F5', fg='#333').grid(row=0, column=0, padx=5)
ttk.Combobox(color_frame, textvariable=color_fg, values=list(COLOR_MAP.keys()), state="readonly", width=8).grid(row=0, column=1, padx=5)
Label(color_frame, text="BG Color:", font=("Arial", 11), bg='#F5F5F5', fg='#333').grid(row=0, column=2, padx=5)
ttk.Combobox(color_frame, textvariable=color_bg, values=list(COLOR_MAP.keys()), state="readonly", width=8).grid(row=0, column=3, padx=5)

btn_frame = Frame(wind, bg='#F5F5F5')
btn_frame.pack(pady=10)
Button(btn_frame, text='Generate', command=gen_qr, font=("Arial", 12, "bold"), bg='#4CAF50', fg='white', padx=15, pady=5).grid(row=0, column=0, padx=10)
Button(btn_frame, text='Save', command=save, font=("Arial", 12, "bold"), bg='#2196F3', fg='white', padx=15, pady=5).grid(row=0, column=1, padx=10)

l4 = Label(wind, text="QR Code Preview", font=("Arial", 12), bg='#F5F5F5', fg='#666')
l4.pack(pady=20)

wind.mainloop()
