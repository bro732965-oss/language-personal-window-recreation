## 📋 Все команды PWR

### 1. `root()` — Создать окно
```pwr
root()
```

### 2. `rename` — Переименовать окно
```pwr
rename.win.MyApp
```

### 3. `msg box` — Создать текст
```pwr
msg.box.win.Hello.50.50
```

### 4. `color` — Сменить цвет фона
```pwr
color.win.red
```

### 5. `picture` — Показать картинку
```pwr
picture.my_image.png.win.50.50
```

### 6. `command net` — Открыть сайт
```pwr
command.net.google.com
```

### 7. `command audio` — Воспроизвести звук
```pwr
command.audio.music.mp3.1
```

### 8. `Gui canvas` — Создать холст
```pwr
Gui.canvas.win.400.300.white
```

### 9. `canvas figure` — Нарисовать фигуру
```pwr
# Прямоугольник
canvas.figure.create_rectangle.100.100.200.200.blue.black.2

# Круг
canvas.figure.create_oval.150.150.250.250.red.black.2

# Линия
canvas.figure.create_line.100.100.200.200.green.3
```

### 10. `get text` — Поле ввода
```pwr
get.text.win.100.100.Hello
```

### 11. `export` — Сохранить проект
```pwr
export myproject
```

### 12. `import` — Загрузить проект
```pwr
import myproject.pwr
```

## 🦆 Пример программы (Уточка)

```pwr
root()
rename.win.Уточка
Gui.canvas.win.500.400.lightblue
canvas.figure.create_oval.120.180.280.320.yellow.black.2
canvas.figure.create_oval.240.110.330.190.yellow.black.2
canvas.figure.create_oval.290.130.310.150.white.black.1
canvas.figure.create_oval.296.137.304.143.black.black.1
canvas.figure.create_polygon.330.140.370.150.330.160.orange.black.1
canvas.figure.create_oval.160.210.230.270.yellow.black.2
canvas.figure.create_polygon.110.230.70.260.110.280.yellow.black.2
canvas.figure.create_oval.0.330.500.400.blue.black.1
```

---

## 🎯 Краткая шпаргалка

```pwr
root()                                    # Окно
rename.win.Название                       # Переименовать
msg.box.win.Текст.x.y                     # Текст
color.win.цвет                            # Цвет
picture.файл.win.x.y                      # Картинка
command.net.сайт                          # Сайт
command.audio.файл.повторы                # Звук
Gui.canvas.win.ширина.высота.цвет         # Холст
canvas.figure.create_rectangle.x1.y1.x2.y2.цвет.контур.толщина
canvas.figure.create_oval.x1.y1.x2.y2.цвет.контур.толщина
canvas.figure.create_line.x1.y1.x2.y2.цвет.толщина
get.text.win.x.y.ответ                    # Поле ввода
export.имя                                # Сохранить
import.имя.pwr                            # Загрузить
```