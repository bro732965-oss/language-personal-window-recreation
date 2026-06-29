# PWR - Personal Window Recreation

**Самый простой язык программирования для творчества!**

![Пример программы: резиновая уточка](screenshots/duck.png)

---

## Что это?

PWR — это язык для создания окон, игр и приложений без сложного синтаксиса. Написан на Python + Tkinter.

---

## 📋 Все команды PWR

```pwr
root()                                    # Окно
rename::win::MyApp                        # Переименовать
msg::box::win::Hello::50::50              # Текст
color::win::red                           # Цвет
picture::my_image.png::win::50::50        # Картинка
command::net::google.com                  # Сайт
command::audio::music.mp3::1              # Звук
Gui::canvas::win::400::300::white         # Холст
canvas::figure::create_rectangle::100::100::200::200::blue::black::2
canvas::figure::create_oval::150::150::250::250::red::black::2
canvas::figure::create_line::100::100::200::200::green::3
get::text::win::100::100::Hello           # Поле ввода
export::myproject                         # Сохранить
import::myproject.pwr                     # Загрузить