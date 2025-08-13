# MADE BY KAIF TARASAGAR

import tkinter as tk
from tkinter import messagebox
# MADE BY KAIF TARASAGAR
def add_char(ch):
    if ch == "C":
        entry.delete(0, tk.END)
        entry.config(bg="#2d2d2d")
    else:
        entry.insert(tk.END, ch)

def calculate():# MADE BY KAIF TARASAGAR
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
        entry.config(bg="#2d2d2d")
    except:
        entry.config(bg="#8b0000")# MADE BY KAIF TARASAGAR
        messagebox.showerror("Error", "Invalid Expression!")
        entry.delete(0, tk.END)

def hover_in(e): 
    equal_btn.config(bg="#198754")  
def hover_out(e): 
    equal_btn.config(bg="#0d6efd")  

root = tk.Tk()
root.title("Calculator")# MADE BY KAIF TARASAGAR
root.geometry("400x550")
root.config(bg="#1e1e1e")

entry = tk.Entry(root, font=("Arial", 22), bg="#2d2d2d", fg="white",
                 insertbackground="white", justify="right")
entry.pack(fill="x", padx=10, pady=20, ipady=8)
# MADE BY KAIF TARASAGAR
btn_frame = tk.Frame(root, bg="#1e1e1e")
btn_frame.pack(expand=True, fill="both", padx=10, pady=10)

buttons = [["7","8","9","/"], ["4","5","6","*"],
           ["1","2","3","-"], ["0",".","C","+"]]# MADE BY KAIF TARASAGAR

for r,row in enumerate(buttons):
    for c,char in enumerate(row):
        b = tk.Button(btn_frame, text=char, font=("Arial",18,"bold"),
                      bg="#333333", fg="white", activebackground="#555",
                      command=lambda ch=char: add_char(ch))
        b.grid(row=r, column=c, sticky="nsew", padx=5, pady=5)# MADE BY KAIF TARASAGAR

for i in range(4):
    btn_frame.columnconfigure(i, weight=1)
    btn_frame.rowconfigure(i, weight=1)
# MADE BY KAIF TARASAGAR
equal_btn = tk.Button(root, text="=", font=("Arial",20,"bold"),
                      bg="#0d6efd", fg="white", command=calculate)
equal_btn.pack(fill="x", padx=10, pady=10, ipady=10)

equal_btn.bind("<Enter>", hover_in)
equal_btn.bind("<Leave>", hover_out)

root.mainloop()
# MADE BY KAIF TARASAGAR


                                        #-- MADE BY KAIF TARASAGAR 
                                               
                                         # https://www.linkedin.com/in/kaif-tarasgar-0b5425326/
                                              
                                         # https://x.com/Kaif_T_200