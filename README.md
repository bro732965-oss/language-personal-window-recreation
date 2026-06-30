# PWR - Personal Window Recreation

**The simplest programming language for creativity!**

[📄 PWR Code](office.py)
[📜 License](License.txt)

![Table in PWR](Screenshot_2026-06-30-17-18-51-745_iiec.pyramide.python-edit.jpg)
![Mona Lisa in PWR](Screenshot_2026-06-30-10-48-30-341_iiec.pyramide.python-edit.jpg)

---

## 🚀 What is it?

**PWR** is a programming language created for quickly building windows, games, and applications.  
It is written in **Python + Tkinter** and uses a simple syntax with no extra code.

### Features:
- ✅ **Instant results** — one command = one action
- ✅ **Simple syntax** — like an instruction in English
- ✅ **Works everywhere** — where Python runs
- ✅ **Interactivity** — buttons, input fields, dialogs
- ✅ **Graphics** — canvas, shapes, images
- ✅ **Sound** — audio support via pygame
- ✅ **Internet** — open websites
- ✅ **Tables** — for data input
- ✅ **Project saving** — export/import `.pwr`

---

## 📋 All PWR Commands

```pwr
root()                                    # Window
rename::win::MyApp                        # Rename window
geometry::win::400::300                   # Window size
msg::box::win::Hello::50::50              # Text
msg::Hello::World                         # Dialog box
color::win::red                           # Background color
picture::my_image.png::win::50::50        # Image
command::net::google.com                  # Website
command::audio::music.mp3::1              # Sound
Gui::canvas::win::400::300::white         # Canvas
canvas::figure::create_rectangle::100::100::200::200::blue::black::2
canvas::figure::create_oval::150::150::250::250::red::black::2
canvas::figure::create_line::100::100::200::200::green::3
get::text::win::100::100::Hello           # Input field
command::button::text::Hello!::Click::lightblue::100::100   # Text button
command::button::net::google.com::Google::lightgreen::100::100 # Website button
command::button::circle::win::300::200::white::Draw::lightcoral::100::100 # Circle button
command::copy::win::Hello World::Copy::lightblue::100::100  # Copy button
command::open::win::https://google.com::Chrome::lightblue::100::100 # Open button
command::msg::win::Hello::Message::lightblue::100::100      # Message button
copy::Hello World                         # Copy text
open::https://google.com                  # Open program
box::data.txt::w+::Hello World            # File operations
table::3::3::my_table::win                # Table
console::random::1::10                    # Random number
console::randombox::apple::banana::cherry # Random choice
export::myproject                         # Save project
import::myproject.pwr                     # Load project
#::This is a comment                      # Comment