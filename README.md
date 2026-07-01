# PWR - Personal Window Recreation

**The simplest programming language for creativity!**

[📄 PWR Code](office.py)
[📜 License](License.txt)

![Table in PWR](Screenshot_2026-06-30-17-18-51-745_iiec.pyramide.python-edit.jpg)
![Mona Lisa in PWR](Screenshot_2026-06-30-10-48-30-341_iiec.pyramide.python-edit.jpg)

---

## 🚀 What is it?

**PWR** is a programming language for creating windows, games, and applications.  
Written in **Python + Tkinter**. One command = one action.

**Features:**
- ✅ Instant results
- ✅ Simple syntax
- ✅ Free & portable
- ✅ Graphics, sound, internet
- ✅ Tables, variables, loops
- ✅ Animation & EXE export

---

## 📋 ALL PWR COMMANDS

```pwr
root()                                    # Window
rename::win::MyApp                        # Rename window
geometry::win::400::300                   # Window size
color::win::red                           # Background color
msg::box::win::Hello::50::50              # Text
msg::Hello::World                         # Dialog box
picture::my_image.png::win::50::50        # Image
Gui::canvas::win::400::300::white         # Canvas
canvas::figure::create_rectangle::100::100::200::200::blue::black::2
canvas::figure::create_oval::150::150::250::250::red::black::2
canvas::figure::create_line::100::100::200::200::green::3
get::text::win::100::100::Hello           # Input field
command::button::text::Hello!::Click::lightblue::100::100
command::button::net::google.com::Google::lightgreen::100::100
command::button::circle::win::300::200::white::Draw::lightcoral::100::100
command::button::audio::music.mp3::1::Play::lightcoral::100::100
command::move::player::0::-10::0::0::Up::lightblue::350::530
button::move::0::0::10::10::Hello::100::100
button::movefigure::0::0::10::10::cube::100::100
time::5::move::cube::10::0
time::5::+::msg::Title::Text
time+::5::+::label::win::0::0::Hello::10::10
time-::10::-::5::label::win::0::0::Hello::10::10
set::x::10
get::x
for::i::1::10::msg::box::win::Hello::50::50
foreach::row::my_table::msg::box::win::Hi::50::50
while::x>5::msg::box::win::Big::50::50
command::net::google.com
command::audio::music.mp3::1
copy::Hello World
open::https://google.com
box::data.txt::w::Hello World
box::data.txt::r
box::data.txt::a::New line
table::3::3::my_table::win
console::random::1::10
console::randombox::apple::banana::cherry
export::myproject
export::exe::MyApp
import::myproject.pwr
#::This is a comment