import tkinter as tk
import random
import webbrowser
import pygame.mixer
from PIL import Image, ImageTk

boxGui=["COLOR:color.window.color|color.click.window.color","FIGURE:command.figure()","AUDIO:command.audio","TEXT:command.text()","PICTURE:picture"]

print("""
personal window recreation
    ####  ###   #
    #### ##### ###
    ####  ### #####
""")

win=tk.Tk()
windows = {"win": win}  
canvases = {}

while True:
    try:
        a=input("*")
        b=a.split("::")
        
        if a=="root()":
            root=tk.Toplevel(win)
            windows["root"] = root
            
        elif b[0] == "rename":
            parent = windows.get(b[1], win)
            parent.title(b[2])
            
        elif b[0]=="picture":
            try:
                parent = windows.get(b[2], win)
                image = Image.open(b[1])
                photo = ImageTk.PhotoImage(image)
                label = tk.Label(parent, image=photo)
                label.place(x=int(b[3]), y=int(b[4]))
                label.image = photo
            except Exception as e:
                print(f"Ошибка картинки: {e}")
            
        elif b[0]=="Gui" and b[1]=="canvas":
            parent = windows.get(b[2], win)
            canvas = tk.Canvas(parent, width=int(b[3]), height=int(b[4]), bg=b[5])
            canvas.pack()
            canvases["canvas"] = canvas
            
        elif b[0]=="canvas" and b[1]=="figure":
            canvas = canvases.get("canvas")
            if canvas:
                if b[2] == "create_rectangle":
                    canvas.create_rectangle(int(b[3]), int(b[4]), int(b[5]), int(b[6]), fill=b[7], outline=b[8], width=int(b[9]))
                elif b[2] == "create_oval":
                    canvas.create_oval(int(b[3]), int(b[4]), int(b[5]), int(b[6]), fill=b[7], outline=b[8], width=int(b[9]))
                elif b[2] == "create_line":
                    canvas.create_line(int(b[3]), int(b[4]), int(b[5]), int(b[6]), fill=b[7], width=int(b[8]))
                
        elif b[0]=="msg" and b[1]=="box":
            parent = windows.get(b[2], win)
            label = tk.Label(parent, text=b[3])
            label.place(x=int(b[4]), y=int(b[5]))
            
        elif b[0]=="command" and b[1]=="audio":
            try:
                pygame.mixer.init()
                pygame.mixer.music.load(b[2])
                pygame.mixer.music.play(int(b[3]))
            except Exception as e:
                print(f"Ошибка аудио: {e}")
            
        elif b[0]=="command" and b[1]=="net":
            webbrowser.open(b[2])
            
        elif b[0]=="get" and b[1]=="text":
            parent = windows.get(b[2], win)
            entry = tk.Entry(parent)
            entry.place(x=int(b[3]), y=int(b[4]))
            
            def git(ent=entry, text=b[5], par=parent, x=b[3], y=b[4]):
                if ent.get() == text:
                    label = tk.Label(par, text="Correct")
                    label.place(x=int(x), y=int(y)+30)
            
        elif b[0]=="color":
            parent = windows.get(b[1], win)
            parent.configure(bg=b[2])
            
        elif b[0]=="export":
            try:
                with open(b[1]+".pwr", "w") as f:
                    f.write(a + "\n")
                print(f"Файл {b[1]}.pwr сохранен!")
            except Exception as e:
                print(f"Ошибка экспорта: {e}")
                
        elif b[0]=="import":
            try:
                with open(b[1],"r") as f:
                    commands = f.readlines()
                    for cmd in commands:
                        cmd = cmd.strip()
                        if cmd:
                            b2 = cmd.split(".")
                            if cmd == "root()":
                                root=tk.Toplevel(win)
                                windows["root"] = root
                            elif b2[0] == "rename":
                                parent = windows.get(b2[1], win)
                                parent.title(b2[2])
                            elif b2[0] == "picture":
                                try:
                                    parent = windows.get(b2[2], win)
                                    image = Image.open(b2[1])
                                    photo = ImageTk.PhotoImage(image)
                                    label = tk.Label(parent, image=photo)
                                    label.place(x=int(b2[3]), y=int(b2[4]))
                                    label.image = photo
                                except Exception as e:
                                    print(f"Ошибка картинки: {e}")
                            elif b2[0] == "Gui" and b2[1] == "canvas":
                                parent = windows.get(b2[2], win)
                                canvas = tk.Canvas(parent, width=int(b2[3]), height=int(b2[4]), bg=b2[5])
                                canvas.pack()
                                canvases["canvas"] = canvas
                            elif b2[0] == "canvas" and b2[1] == "figure":
                                canvas = canvases.get("canvas")
                                if canvas:
                                    if b2[2] == "create_rectangle":
                                        canvas.create_rectangle(int(b2[3]), int(b2[4]), int(b2[5]), int(b2[6]), fill=b2[7], outline=b2[8], width=int(b2[9]))
                                    elif b2[2] == "create_oval":
                                        canvas.create_oval(int(b2[3]), int(b2[4]), int(b2[5]), int(b2[6]), fill=b2[7], outline=b2[8], width=int(b2[9]))
                                    elif b2[2] == "create_line":
                                        canvas.create_line(int(b2[3]), int(b2[4]), int(b2[5]), int(b2[6]), fill=b2[7], width=int(b2[8]))
                            elif b2[0] == "msg" and b2[1] == "box":
                                parent = windows.get(b2[2], win)
                                label = tk.Label(parent, text=b2[3])
                                label.place(x=int(b2[4]), y=int(b2[5]))
                            elif b2[0] == "command" and b2[1] == "audio":
                                try:
                                    pygame.mixer.init()
                                    pygame.mixer.music.load(b2[2])
                                    pygame.mixer.music.play(int(b2[3]))
                                except Exception as e:
                                    print(f"Ошибка аудио: {e}")
                            elif b2[0] == "command" and b2[1] == "net":
                                webbrowser.open(b2[2])
                            elif b2[0] == "get" and b2[1] == "text":
                                parent = windows.get(b2[2], win)
                                entry = tk.Entry(parent)
                                entry.place(x=int(b2[3]), y=int(b2[4]))
                                def git(ent=entry, text=b2[5], par=parent, x=b2[3], y=b2[4]):
                                    if ent.get() == text:
                                        label = tk.Label(par, text="Correct")
                                        label.place(x=int(x), y=int(y)+30)
                            elif b2[0] == "color":
                                parent = windows.get(b2[1], win)
                                parent.configure(bg=b2[2])
            except FileNotFoundError:
                print(f"Файл {b[1]} не найден!")
            except Exception as e:
                print(f"Ошибка импорта: {e}")
    except Exception as e:
        print(f"Ошибка: {e}")
    else:
        if b[0] not in ["root", "rename", "picture", "Gui", "canvas", "msg", "command", "get", "color", "export", "import"]:
            print(b, "error !", "did you mean>>", random.choice(boxGui))

tk.mainloop()