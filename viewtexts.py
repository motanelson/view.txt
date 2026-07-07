import os 
import copy
import tkinter as tk
from tkinter import font
import subprocess
class tApp:
    def __init__(self, root,texts,titles):
        self.root = root
        self.root.title(titles)
        self.root.geometry("800x600")
        self.root.configure(bg="white")

        # Frame com barra de scroll
        self.frame = tk.Frame(self.root, bg="white")
        self.frame.pack(fill="both", expand=True)

        # Canvas para desenhar texto
        self.canvas = tk.Canvas(self.frame, bg="white", highlightthickness=0)
        self.canvas.pack(side="left", fill="both", expand=True)

        # Barra de scroll vertical
        self.scrollbar = tk.Scrollbar(self.frame, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Fonte
        self.font = font.Font(family="Courier", size=16)
        ff=texts.split("\n")
        y=20
        for t in ff:
            cursor=0
            cursor2=0
            if len(t)>=50:
                leaves=True
                while(leaves):
                    lll=len(t)-cursor
                    if lll>50:
                        cursor2=cursor + 50
                        ttt=t[cursor:cursor2]
                        tt=self.canvas.create_text(10, y, text=ttt, anchor="nw", font=self.font, fill="red")

                    else:
                        cursor2=lll+cursor
                        ttt=t[cursor:cursor2]
                        tt=self.canvas.create_text(10, y, text=ttt, anchor="nw", font=self.font, fill="red")
                        leaves=False
                    
                    
                    cursor=cursor+50
                    y=y+16 
            else:
                tt=self.canvas.create_text(10, y, text=t, anchor="nw", font=self.font, fill="red")
                y=y+16
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        # Scroll automático para o fim
        self.canvas.yview_moveto(1.0)

print("\033c\033[47;31m\ngive me a text to view ? \n")
a=input().strip()

f1=open(a,"r")
f=f1.read()
f1.close()

root = tk.Tk()

app = tApp(root,f,a)
root.mainloop()