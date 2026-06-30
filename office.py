import tkinter as tk
import random
import webbrowser
import pygame.mixer
from PIL import Image, ImageTk
import os
import subprocess
from tkinter import messagebox
import ast

boxGui = [
    "ROOT:root()",
    "RENAME:rename::win::MyApp",
    "GEOMETRY:geometry::win::400::300",
    "COLOR:color::win::lightblue",
    "MSG BOX:msg::box::win::Hello::50::50",
    "MSG DIALOG:msg::Hello::World",
    "PICTURE:picture::logo.png::win::50::50",
    "GUI CANVAS:Gui::canvas::win::400::300::white",
    "FIGURE RECTANGLE:canvas::figure::create_rectangle::50::50::150::100::blue::black::2",
    "FIGURE OVAL:canvas::figure::create_oval::50::50::150::100::red::black::2",
    "FIGURE LINE:canvas::figure::create_line::50::50::150::100::green::3",
    "BUTTON TEXT:command::button::text::Hello!::Click::lightblue::100::100",
    "BUTTON NET:command::button::net::google.com::Google::lightgreen::100::100",
    "BUTTON AUDIO:command::button::audio::music.mp3::1::Play::lightcoral::100::100",
    "BUTTON CIRCLE:command::button::circle::win::300::200::white::Draw Circle::lightgreen::100::100",
    "BUTTON COPY:command::copy::win::Hello World::Copy::lightblue::100::100",
    "BUTTON OPEN:command::open::win::https://google.com::Open Chrome::lightblue::100::100",
    "BUTTON MSG:command::msg::win::Hello::Message::lightblue::100::100",
    "GET TEXT:get::text::win::100::100::Hello",
    "CANVAS:command::canvas::win::300::200::white::Create::lightblue::100::100",
    "EXPORT:export::myproject",
    "IMPORT:import::myproject.pwr",
    "BOX:box::data.txt::w+::Hello World",
    "COPY:copy::Hello World",
    "OPEN:open::https://google.com",
    "COMMENT:#::This is a comment",
    "TABLE:table::3::3::my_table::win",
    "RANDOM:console::random::1::10",
    "RANDOMBOX:console::randombox::apple::banana::cherry"
]

print("""
PWR - Personal Window Recreation
    ####  ###   #
    #### ##### ###
    ####  ### #####
""")

win = tk.Tk()
windows = {"win": win}
canvases = {}
tables = {}
history = []

while True:
    try:
        a = input("*")
        b = a.split("::")

        if a == "root()":
            root = tk.Toplevel(win)
            windows["root"] = root
            
        elif b[0] == "console" and b[1] == "random":
            try:
                num = random.randint(int(b[2]), int(b[3]))
                print(f"Random number: {num}")
            except Exception as e:
                print(f"Random error: {e}")
                
        elif b[0] == "console" and b[1] == "randombox":
            try:
                items = b[2:]
                choice = random.choice(items)
                print(f"Random choice: {choice}")
            except Exception as e:
                print(f"Randombox error: {e}")
            
        elif b[0] == "copy":
            os.system('echo ' + b[1] + ' | termux-clipboard-set')
            
        elif b[0] == "#":
            print(b[1])
            
        elif b[0] == "table":
            try:
                parent = windows.get(b[4], win)
                rows = int(b[1])
                cols = int(b[2])
                table_name = b[3]
                
                entries = []
                for i in range(rows):
                    row_entries = []
                    for j in range(cols):
                        entry = tk.Entry(parent, width=12)
                        entry.place(x=50 + j*200, y=50 + i*50)
                        row_entries.append(entry)
                    entries.append(row_entries)
                
                tables[table_name] = entries
                print(f"Table '{table_name}' created: {rows}x{cols}")
            except Exception as e:
                print(f"Table error: {e}")
            
        elif b[0] == "box":
            try:
                with open(b[1], b[2]) as f:
                    if b[2] == "r":
                        content = f.read()
                        print(content)
                    else:
                        f.write(b[3])
            except Exception as e:
                print(f"File error: {e}")
            
        elif b[0] == "msg":
            messagebox.showinfo(b[1], b[2])
            
        elif b[0] == "command" and b[1] == "msg":
            def msg1():
                messagebox.showinfo(b[3], b[4])
            btners = tk.Button(win, text=b[5], command=msg1, bg=b[6])
            btners.place(x=int(b[7]), y=int(b[8]))
            
        elif b[0] == "open":
            path = r"C:\Program Files\Google\Chrome\Application\chrome.exe " + b[1]
            subprocess.Popen([path])
            
        elif b[0] == "command" and b[1] == "open":
            def opens():
                path = r"C:\Program Files\Google\Chrome\Application\chrome.exe " + b[3]
                subprocess.Popen([path])
            btner = tk.Button(win, text=b[4], command=opens, bg=b[5])
            btner.place(x=int(b[6]), y=int(b[7]))
            
        elif b[0] == "geometry" and b[1] == "win":
            win.geometry(b[2] + "x" + b[3])
            
        elif b[0] == "geometry" and b[1] == "root":
            root.geometry(b[2] + "x" + b[3])
            
        elif b[0] == "rename":
            parent = windows.get(b[1], win)
            parent.title(b[2])

        elif b[0] == "picture":
            try:
                parent = windows.get(b[2], win)
                image = Image.open(b[1])
                photo = ImageTk.PhotoImage(image)
                label = tk.Label(parent, image=photo)
                label.place(x=int(b[3]), y=int(b[4]))
                label.image = photo
            except Exception as e:
                print(f"Picture error: {e}")

        elif b[0] == "Gui" and b[1] == "canvas":
            parent = windows.get(b[2], win)
            canvas = tk.Canvas(parent, width=int(b[3]), height=int(b[4]), bg=b[5])
            canvas.pack()
            canvases["canvas"] = canvas

        elif b[0] == "canvas" and b[1] == "figure":
            canvas = canvases.get("canvas")
            if canvas:
                if b[2] == "create_rectangle":
                    canvas.create_rectangle(int(b[3]), int(b[4]), int(b[5]), int(b[6]), fill=b[7], outline=b[8], width=int(b[9]))
                elif b[2] == "create_oval":
                    canvas.create_oval(int(b[3]), int(b[4]), int(b[5]), int(b[6]), fill=b[7], outline=b[8], width=int(b[9]))
                elif b[2] == "create_line":
                    canvas.create_line(int(b[3]), int(b[4]), int(b[5]), int(b[6]), fill=b[7], width=int(b[8]))

        elif b[0] == "command" and b[1] == "canvas":
            def part():
                parent = windows.get(b[2], win)
                canvas = tk.Canvas(parent, width=int(b[3]), height=int(b[4]), bg=b[5])
                canvas.pack()
                canvases["canvas"] = canvas
            btn = tk.Button(win, text=b[6], command=part, bg=b[7])
            btn.place(x=int(b[8]), y=int(b[9]))

        elif b[0] == "command" and b[1] == "button" and b[2] == "circle":
            def draw_circle():
                parent = windows.get(b[3], win)
                canvas = tk.Canvas(parent, width=int(b[4]), height=int(b[5]), bg=b[6])
                canvas.pack()
                canvases["canvas"] = canvas
                canvas.create_oval(50, 50, 150, 150, fill="red", outline="black", width=2)
            btn = tk.Button(win, text=b[7], command=draw_circle, bg=b[8])
            btn.place(x=int(b[9]), y=int(b[10]))

        elif b[0] == "command" and b[1] == "copy":
            def os_copy():
                os.system('echo ' + b[3] + ' | termux-clipboard-set')
            btnse = tk.Button(win, text=b[4], command=os_copy, bg=b[5])
            btnse.place(x=int(b[6]), y=int(b[7]))

        elif b[0] == "msg" and b[1] == "box":
            parent = windows.get(b[2], win)
            label = tk.Label(parent, text=b[3])
            label.place(x=int(b[4]), y=int(b[5]))

        elif b[0] == "command" and b[1] == "audio":
            try:
                pygame.mixer.init()
                pygame.mixer.music.load(b[2])
                pygame.mixer.music.play(int(b[3]))
            except Exception as e:
                print(f"Audio error: {e}")

        elif b[0] == "command" and b[1] == "net":
            webbrowser.open(b[2])

        elif b[0] == "command" and b[1] == "button" and b[2] == "audio":
            def audio():
                try:
                    pygame.mixer.init()
                    pygame.mixer.music.load(b[3])
                    pygame.mixer.music.play(int(b[4]))
                except Exception as e:
                    print(f"Audio error: {e}")
            btn = tk.Button(win, text=b[5], command=audio, bg=b[4])
            btn.place(x=int(b[6]), y=int(b[7]))

        elif b[0] == "command" and b[1] == "button" and b[2] == "text":
            def text():
                label = tk.Label(win, text=b[3], font=("Arial", 12), fg="black")
                label.place(x=int(b[6]), y=int(b[7]) + 40)
            btn = tk.Button(win, text=b[4], command=text, bg=b[5], width=15)
            btn.place(x=int(b[6]), y=int(b[7]))

        elif b[0] == "command" and b[1] == "button" and b[2] == "net":
            def nets():
                webbrowser.open(b[3])
            btn = tk.Button(win, text=b[4], command=nets, bg=b[5])
            btn.place(x=int(b[6]), y=int(b[7]))

        elif b[0] == "get" and b[1] == "text":
            parent = windows.get(b[2], win)
            entry = tk.Entry(parent)
            entry.place(x=int(b[3]), y=int(b[4]))

            def git(ent=entry, text=b[5], par=parent, x=b[3], y=b[4]):
                if ent.get() == text:
                    label = tk.Label(par, text="Correct")
                    label.place(x=int(x), y=int(y) )

            btn = tk.Button(parent, text="Check", command=git,width=10, height=0)
            btn.place(x=int(b[3])+505, y=int(b[4]) )

        elif b[0] == "color":
            parent = windows.get(b[1], win)
            parent.configure(bg=b[2])

        elif b[0] == "export":
            try:
                table_data = {}
                for name, entries in tables.items():
                    data = []
                    for row in entries:
                        row_data = [entry.get() for entry in row]
                        data.append(row_data)
                    table_data[name] = data
                
                with open(b[1] + ".pwr", "w", encoding="utf-8") as f:
                    f.write("TABLES:" + str(table_data) + "\n")
                    for cmd in history:
                        f.write(cmd + "\n")
                print(f"File {b[1]}.pwr saved!")
            except Exception as e:
                print(f"Export error: {e}")

        elif b[0] == "import":
            try:
                with open(b[1], "r", encoding="utf-8") as f:
                    lines = f.readlines()
                    
                    # Сначала выполняем все команды
                    for cmd in lines:
                        cmd = cmd.strip()
                        if cmd and not cmd.startswith("TABLES:"):
                            b2 = cmd.split("::")
                            if cmd == "root()":
                                root = tk.Toplevel(win)
                                windows["root"] = root
                            elif b2[0] == "table" and len(b2) >= 3:
                                try:
                                    parent = windows.get(b2[4], win)
                                    rows = int(b2[1])
                                    cols = int(b2[2])
                                    table_name = b2[3]
                                    
                                    entries = []
                                    for i in range(rows):
                                        row_entries = []
                                        for j in range(cols):
                                            entry = tk.Entry(parent, width=12)
                                            entry.place(x=50 + j*200, y=50 + i*50)
                                            row_entries.append(entry)
                                        entries.append(row_entries)
                                    
                                    tables[table_name] = entries
                                    print(f"Table '{table_name}' created: {rows}x{cols}")
                                except Exception as e:
                                    print(f"Table error: {e}")
                            elif b2[0] == "rename":
                                parent = windows.get(b2[1], win)
                                parent.title(b2[2])
                            elif b2[0] == "geometry" and b2[1] == "win":
                                win.geometry(b2[2] + "x" + b2[3])
                            elif b2[0] == "geometry" and b2[1] == "root":
                                root.geometry(b2[2] + "x" + b2[3])
                            elif b2[0] == "picture":
                                try:
                                    parent = windows.get(b2[2], win)
                                    image = Image.open(b2[1])
                                    photo = ImageTk.PhotoImage(image)
                                    label = tk.Label(parent, image=photo)
                                    label.place(x=int(b2[3]), y=int(b2[4]))
                                    label.image = photo
                                except Exception as e:
                                    print(f"Picture error: {e}")
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
                            elif b2[0] == "command" and b2[1] == "canvas":
                                def part():
                                    parent = windows.get(b2[2], win)
                                    canvas = tk.Canvas(parent, width=int(b2[3]), height=int(b2[4]), bg=b2[5])
                                    canvas.pack()
                                    canvases["canvas"] = canvas
                                btn = tk.Button(win, text=b2[6], command=part, bg=b2[7])
                                btn.place(x=int(b2[8]), y=int(b2[9]))
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
                                    print(f"Audio error: {e}")
                            elif b2[0] == "command" and b2[1] == "net":
                                webbrowser.open(b2[2])
                            elif b2[0] == "command" and b2[1] == "button" and b2[2] == "audio":
                                def audio():
                                    try:
                                        pygame.mixer.init()
                                        pygame.mixer.music.load(b2[3])
                                        pygame.mixer.music.play(int(b2[4]))
                                    except Exception as e:
                                        print(f"Audio error: {e}")
                                btn = tk.Button(win, text=b2[5], command=audio, bg=b2[4])
                                btn.place(x=int(b2[6]), y=int(b2[7]))
                            elif b2[0] == "command" and b2[1] == "button" and b2[2] == "text":
                                def text():
                                    label = tk.Label(win, text=b2[3], font=("Arial", 12), fg="black")
                                    label.place(x=int(b2[6]), y=int(b2[7]) + 40)
                                btn = tk.Button(win, text=b2[4], command=text, bg=b2[5], width=15)
                                btn.place(x=int(b2[6]), y=int(b2[7]))
                            elif b2[0] == "command" and b2[1] == "button" and b2[2] == "net":
                                def nets():
                                    webbrowser.open(b2[3])
                                btn = tk.Button(win, text=b2[4], command=nets, bg=b2[5])
                                btn.place(x=int(b2[6]), y=int(b2[7]))
                            elif b2[0] == "command" and b2[1] == "button" and b2[2] == "circle":
                                def draw_circle():
                                    parent = windows.get(b2[3], win)
                                    canvas = tk.Canvas(parent, width=int(b2[4]), height=int(b2[5]), bg=b2[6])
                                    canvas.pack()
                                    canvases["canvas"] = canvas
                                    canvas.create_oval(50, 50, 150, 150, fill="red", outline="black", width=2)
                                btn = tk.Button(win, text=b2[7], command=draw_circle, bg=b2[8])
                                btn.place(x=int(b2[9]), y=int(b2[10]))
                            elif b2[0] == "command" and b2[1] == "copy":
                                def os_copy():
                                    os.system('echo ' + b2[3] + ' | termux-clipboard-set')
                                btnse = tk.Button(win, text=b2[4], command=os_copy, bg=b2[5])
                                btnse.place(x=int(b2[6]), y=int(b2[7]))
                            elif b2[0] == "command" and b2[1] == "msg":
                                def msg1():
                                    messagebox.showinfo(b2[3], b2[4])
                                btners = tk.Button(win, text=b2[5], command=msg1, bg=b2[6])
                                btners.place(x=int(b2[7]), y=int(b2[8]))
                            elif b2[0] == "command" and b2[1] == "open":
                                def opens():
                                    path = r"C:\Program Files\Google\Chrome\Application\chrome.exe " + b2[3]
                                    subprocess.Popen([path])
                                btner = tk.Button(win, text=b2[4], command=opens, bg=b2[5])
                                btner.place(x=int(b2[6]), y=int(b2[7]))
                            elif b2[0] == "get" and b2[1] == "text":
                                parent = windows.get(b2[2], win)
                                entry = tk.Entry(parent)
                                entry.place(x=int(b2[3]), y=int(b2[4]))
                                def git(ent=entry, text=b2[5], par=parent, x=b2[3], y=b2[4]):
                                    if ent.get() == text:
                                        label = tk.Label(par, text="Correct")
                                        label.place(x=int(x), y=int(y) + 30)
                                btn = tk.Button(parent, text="Check", command=git)
                                btn.place(x=int(b2[3]), y=int(b2[4]) + 30)
                            elif b2[0] == "box":
                                try:
                                    with open(b2[1], b2[2]) as f:
                                        if b2[2] == "r":
                                            print(f.read())
                                        else:
                                            f.write(b2[3])
                                except Exception as e:
                                    print(f"File error: {e}")
                            elif b2[0] == "color":
                                parent = windows.get(b2[1], win)
                                parent.configure(bg=b2[2])
                            
                            # Добавляем console в import
                            elif b2[0] == "console" and b2[1] == "random":
                                try:
                                    num = random.randint(int(b2[2]), int(b2[3]))
                                    print(f"Random number: {num}")
                                except Exception as e:
                                    print(f"Random error: {e}")
                            elif b2[0] == "console" and b2[1] == "randombox":
                                try:
                                    items = b2[2:]
                                    choice = random.choice(items)
                                    print(f"Random choice: {choice}")
                                except Exception as e:
                                    print(f"Randombox error: {e}")
                    
                    # Потом восстанавливаем данные таблиц
                    for line in lines:
                        if line.startswith("TABLES:"):
                            table_data = ast.literal_eval(line[7:])
                            for name, data in table_data.items():
                                if name in tables:
                                    entries = tables[name]
                                    for i, row in enumerate(data):
                                        if i < len(entries):
                                            for j, value in enumerate(row):
                                                if j < len(entries[i]):
                                                    entries[i][j].delete(0, tk.END)
                                                    entries[i][j].insert(0, str(value))
                            print("Tables restored!")
                            
            except FileNotFoundError:
                print(f"File {b[1]} not found!")
            except Exception as e:
                print(f"Import error: {e}")

        if b[0] not in ["export", "import"]:
            history.append(a)

    except Exception as e:
        print(f"Error: {e}")
    else:
        if b[0] not in ["root", "rename", "geometry", "picture", "Gui", "canvas", "msg", "command", "get", "color", "export", "import"]:
            print(b, "error !", "did you mean>>", random.choice(boxGui))

tk.mainloop()