import tkinter as tk
import random
import webbrowser
import pygame.mixer
from PIL import Image, ImageTk
import os
import subprocess
from tkinter import messagebox
import ast
import time

# ========== ЦВЕТА ДЛЯ КОНСОЛИ ==========
class Colors:
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    END = '\033[0m'

def color_print(text, color=Colors.WHITE, bold=False):
    if bold:
        print(f"{Colors.BOLD}{color}{text}{Colors.END}")
    else:
        print(f"{color}{text}{Colors.END}")

def highlight_command(cmd):
    cmd_parts = cmd.split("::")
    highlighted = []
    
    for part in cmd_parts:
        if part in ["root", "rename", "color", "msg", "box", "console", "export", "import", "table", "copy", "open", "command", "Gui", "canvas", "get", "time"]:
            highlighted.append(f"{Colors.BLUE}{part}{Colors.END}")
        elif part.isdigit():
            highlighted.append(f"{Colors.GREEN}{part}{Colors.END}")
        elif "." in part or "/" in part or "\\" in part:
            highlighted.append(f"{Colors.YELLOW}{part}{Colors.END}")
        elif part.startswith("#") or part.startswith("/"):
            highlighted.append(f"{Colors.WHITE}{part}{Colors.END}")
        else:
            highlighted.append(f"{Colors.PURPLE}{part}{Colors.END}")
    
    return "::".join(highlighted)

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
    "EXPORT EXE:export::exe::MyApp",
    "IMPORT:import::myproject.pwr",
    "BOX WRITE:box::data.txt::w::Hello World",
    "BOX APPEND:box::data.txt::a::New line",
    "BOX READ:box::data.txt::r",
    "COPY:copy::Hello World",
    "OPEN:open::https://google.com",
    "COMMENT:#::This is a comment",
    "TABLE:table::3::3::my_table::win",
    "RANDOM:console::random::1::10",
    "RANDOMBOX:console::randombox::apple::banana::cherry",
    "TIME:time::5::+::msg::Title::Text"
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

def create_icon():
    try:
        from PIL import Image, ImageDraw
        
        img = Image.new('RGB', (256, 256), '#F5F5DC')
        draw = ImageDraw.Draw(img)
        
        colors = ['#FF4444', '#4488FF', '#44CC44', '#FFCC00', '#AA44FF', '#FF8800', '#FF66AA', '#00CCFF', '#CC3366']
        x_positions = [0, 85, 170]
        y_positions = [0, 85, 170]
        size = 85
        
        for i, color in enumerate(colors):
            x = x_positions[i % 3]
            y = y_positions[i // 3]
            draw.rectangle([x, y, x+size, y+size], fill=color, outline='#333333', width=3)
        
        draw.line([0, 85, 256, 85], fill='#333333', width=3)
        draw.line([0, 170, 256, 170], fill='#333333', width=3)
        draw.line([85, 0, 85, 170], fill='#333333', width=3)
        draw.line([170, 0, 170, 170], fill='#333333', width=3)
        draw.line([85, 85, 85, 256], fill='#333333', width=3)
        draw.line([170, 85, 170, 256], fill='#333333', width=3)
        
        img.save('icon.ico', format='ICO', sizes=[(256, 256)])
        color_print("Icon created: icon.ico", Colors.GREEN)
        return True
    except Exception as e:
        color_print(f"Icon error: {e}", Colors.RED)
        return False

while True:
    try:
        a = input("* ")
        b = a.split("::")
        
        color_print(f"-> {highlight_command(a)}", Colors.CYAN)

        if a == "root()":
            root = tk.Toplevel(win)
            windows["root"] = root
            
        # ========== ТАЙМЕР ==========
        elif b[0] == "time" and len(b) >= 6:
            try:
                if b[3] == "+":
                    seconds = int(b[1]) + int(b[2])
                    if seconds > 0:
                        color_print(f"Waiting {seconds} seconds...", Colors.YELLOW)
                        time.sleep(seconds)
                        messagebox.showinfo(b[5], b[6])
                        color_print("Message shown", Colors.GREEN)
                    else:
                        color_print("Time must be positive", Colors.RED)
                elif b[3] == "-":
                    seconds = int(b[1]) - int(b[2])
                    if seconds > 0:
                        color_print(f"Waiting {seconds} seconds...", Colors.YELLOW)
                        time.sleep(seconds)
                        messagebox.showinfo(b[5], b[6])
                        color_print("Message shown", Colors.GREEN)
                    else:
                        color_print("Time must be positive", Colors.RED)
                else:
                    color_print("Use + or - for time operation", Colors.RED)
            except ValueError:
                color_print("Time values must be numbers", Colors.RED)
            except Exception as e:
                color_print(f"Time error: {e}", Colors.RED)
        
        elif b[0] == "console" and b[1] == "random":
            try:
                num = random.randint(int(b[2]), int(b[3]))
                color_print(f"Random number: {num}", Colors.GREEN)
            except Exception as e:
                color_print(f"Random error: {e}", Colors.RED)
                
        elif b[0] == "console" and b[1] == "randombox":
            try:
                items = b[2:]
                choice = random.choice(items)
                color_print(f"Random choice: {choice}", Colors.GREEN)
            except Exception as e:
                color_print(f"Randombox error: {e}", Colors.RED)
            
        elif b[0] == "copy":
            os.system('echo ' + b[1] + ' | termux-clipboard-set')
            color_print(f"Copied: {b[1]}", Colors.GREEN)
            
        elif b[0] == "/":
            color_print(f"Comment: {b[1]}", Colors.WHITE)
            
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
                color_print(f"Table '{table_name}' created: {rows}x{cols}", Colors.GREEN)
            except Exception as e:
                color_print(f"Table error: {e}", Colors.RED)
            
        elif b[0] == "box":
            try:
                mode = b[2]
                filename = b[1]
                content = b[3] if len(b) > 3 else ""
                
                if mode == "r":
                    with open(filename, "r", encoding="utf-8") as f:
                        color_print(f.read(), Colors.GREEN)
                elif mode == "w":
                    with open(filename, "w", encoding="utf-8") as f:
                        f.write(content)
                    color_print(f"File '{filename}' written", Colors.GREEN)
                elif mode == "a":
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(content + "\n")
                    color_print(f"File '{filename}' appended", Colors.GREEN)
                elif mode == "w+":
                    with open(filename, "w+", encoding="utf-8") as f:
                        f.write(content)
                        f.seek(0)
                        color_print(f.read(), Colors.GREEN)
                else:
                    color_print(f"Unknown mode '{mode}'", Colors.RED)
            except FileNotFoundError:
                color_print(f"File '{b[1]}' not found", Colors.RED)
            except Exception as e:
                color_print(f"File error: {e}", Colors.RED)
            
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
            color_print(f"Opening: {b[1]}", Colors.GREEN)
            
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
                color_print(f"Picture error: {e}", Colors.RED)

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
                color_print(f"Audio error: {e}", Colors.RED)

        elif b[0] == "command" and b[1] == "net":
            webbrowser.open(b[2])

        elif b[0] == "command" and b[1] == "button" and b[2] == "audio":
            def audio():
                try:
                    pygame.mixer.init()
                    pygame.mixer.music.load(b[3])
                    pygame.mixer.music.play(int(b[4]))
                except Exception as e:
                    color_print(f"Audio error: {e}", Colors.RED)
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
                    label = tk.Label(par, text=b[5])
                    label.place(x=int(x), y=int(y) )

            btn = tk.Button(parent, text="Check", command=git,width=10, height=0)
            btn.place(x=int(b[3])+505, y=int(b[4]) )

        elif b[0] == "color":
            parent = windows.get(b[1], win)
            parent.configure(bg=b[2])

        elif b[0] == "export" and b[1] == "exe":
            try:
                name = b[2] if len(b) > 2 else "PWR_App"
                color_print(f"Building {name}.exe...", Colors.YELLOW)
                
                create_icon()
                
                with open("_build.py", "w") as f:
                    f.write(f'''
import os
import sys
import subprocess

try:
    import PyInstaller
except ImportError:
    subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller"])

if not os.path.exists("icon.ico"):
    print("ERROR: icon.ico not found!")
    sys.exit(1)

cmd = [sys.executable, "-m", "PyInstaller", 
       "--onefile", 
       "--name", "{name}", 
       "--icon", "icon.ico",
       "--console", 
       "--clean", 
       "--noconfirm", 
       "pwr.py"]

for file in ["logo.png", "music.mp3"]:
    if os.path.exists(file):
        cmd.extend(["--add-data", f"{{file}};."])

subprocess.run(cmd, check=True)

if os.path.exists(f"dist/{{name}}.exe"):
    import shutil
    shutil.copy(f"dist/{{name}}.exe", f"{{name}}.exe")
    print(f"Done: {name}.exe with icon")
''')
                
                subprocess.run(["python", "_build.py"])
                os.remove("_build.py")
                color_print(f"{name}.exe built successfully", Colors.GREEN)
                
            except Exception as e:
                color_print(f"Error: {e}", Colors.RED)

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
                color_print(f"File {b[1]}.pwr saved", Colors.GREEN)
            except Exception as e:
                color_print(f"Export error: {e}", Colors.RED)

        elif b[0] == "import":
            try:
                with open(b[1], "r", encoding="utf-8") as f:
                    lines = f.readlines()
                    
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
                                    color_print(f"Table '{table_name}' created: {rows}x{cols}", Colors.GREEN)
                                except Exception as e:
                                    color_print(f"Table error: {e}", Colors.RED)
                            elif b2[0] == "time" and len(b2) >= 6:
                                try:
                                    if b2[3] == "+":
                                        seconds = int(b2[1]) + int(b2[2])
                                        if seconds > 0:
                                            time.sleep(seconds)
                                            messagebox.showinfo(b2[5], b2[6])
                                    elif b2[3] == "-":
                                        seconds = int(b2[1]) - int(b2[2])
                                        if seconds > 0:
                                            time.sleep(seconds)
                                            messagebox.showinfo(b2[5], b2[6])
                                except:
                                    pass
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
                                    color_print(f"Picture error: {e}", Colors.RED)
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
                                    color_print(f"Audio error: {e}", Colors.RED)
                            elif b2[0] == "command" and b2[1] == "net":
                                webbrowser.open(b2[2])
                            elif b2[0] == "command" and b2[1] == "button" and b2[2] == "audio":
                                def audio():
                                    try:
                                        pygame.mixer.init()
                                        pygame.mixer.music.load(b2[3])
                                        pygame.mixer.music.play(int(b2[4]))
                                    except Exception as e:
                                        color_print(f"Audio error: {e}", Colors.RED)
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
                                        label = tk.Label(par, text=b2[5])
                                        label.place(x=int(x), y=int(y) + 30)
                                btn = tk.Button(parent, text="Check", command=git)
                                btn.place(x=int(b2[3]), y=int(b2[4]) + 30)
                            elif b2[0] == "box":
                                try:
                                    mode = b2[2]
                                    filename = b2[1]
                                    content = b2[3] if len(b2) > 3 else ""
                                    
                                    if mode == "r":
                                        with open(filename, "r", encoding="utf-8") as f:
                                            color_print(f.read(), Colors.GREEN)
                                    elif mode == "w":
                                        with open(filename, "w", encoding="utf-8") as f:
                                            f.write(content)
                                        color_print(f"File '{filename}' written", Colors.GREEN)
                                    elif mode == "a":
                                        with open(filename, "a", encoding="utf-8") as f:
                                            f.write(content + "\n")
                                        color_print(f"File '{filename}' appended", Colors.GREEN)
                                    elif mode == "w+":
                                        with open(filename, "w+", encoding="utf-8") as f:
                                            f.write(content)
                                            f.seek(0)
                                            color_print(f.read(), Colors.GREEN)
                                    else:
                                        color_print(f"Unknown mode '{mode}'", Colors.RED)
                                except FileNotFoundError:
                                    color_print(f"File '{b2[1]}' not found", Colors.RED)
                                except Exception as e:
                                    color_print(f"File error: {e}", Colors.RED)
                            elif b2[0] == "color":
                                parent = windows.get(b2[1], win)
                                parent.configure(bg=b2[2])
                            
                            elif b2[0] == "console" and b2[1] == "random":
                                try:
                                    num = random.randint(int(b2[2]), int(b2[3]))
                                    color_print(f"Random number: {num}", Colors.GREEN)
                                except Exception as e:
                                    color_print(f"Random error: {e}", Colors.RED)
                            elif b2[0] == "console" and b2[1] == "randombox":
                                try:
                                    items = b2[2:]
                                    choice = random.choice(items)
                                    color_print(f"Random choice: {choice}", Colors.GREEN)
                                except Exception as e:
                                    color_print(f"Randombox error: {e}", Colors.RED)
                    
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
                            color_print("Tables restored", Colors.GREEN)
                            
            except FileNotFoundError:
                color_print(f"File {b[1]} not found", Colors.RED)
            except Exception as e:
                color_print(f"Import error: {e}", Colors.RED)

        if b[0] not in ["export", "import"]:
            history.append(a)

    except Exception as e:
        color_print(f"Error: {e}", Colors.RED)
    else:
        if b[0] not in ["root", "rename", "geometry", "picture", "Gui", "canvas", "msg", "command", "get", "color", "export", "import", "copy", "open", "box", "table", "console", "#", "time"]:
            error_msg = f"{b} error ! did you mean>> {random.choice(boxGui)}"
            color_print(error_msg, Colors.RED)

tk.mainloop()