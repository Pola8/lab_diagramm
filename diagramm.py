import tkinter as tk
import math

# Количество секторов
NUM_SECTORS = 6


# Функция для построения секторной диаграммы
def draw_pie_chart(canvas, center_x, center_y, radius, sectors, labels):
    total = sum(sectors)
    start_angle = 0

    for i in range(len(sectors)):
        # Проверка наличия элемента в списке labels
        if i < len(labels):
            # Вычисление угла сектора
            angle = 360 * sectors[i] / total

            # Рисование сектора
            canvas.create_arc(
                center_x - radius,
                center_y - radius,
                center_x + radius,
                center_y + radius,
                start=start_angle,
                extent=angle,
                fill="",
                outline="black"
            )

            # Вычисление координат для текста
            text_angle = math.radians(start_angle + angle / 2)
            text_x = center_x + (radius + 20) * math.cos(text_angle)
            text_y = center_y - (radius + 20) * math.sin(text_angle)

            # Добавление наименования сектора
            canvas.create_text(text_x, text_y, text=labels[i], font=("Arial", 10), anchor="w")

            start_angle += angle

    # Добавление процентных значений внутри каждого сектора
    start_angle = 0
    for i in range(len(sectors)):
        if i < len(labels):
            angle = 360 * sectors[i] / total
            text_angle = math.radians(start_angle + angle / 2)
            text_x = center_x + (radius / 2) * math.cos(text_angle)
            text_y = center_y - (radius / 2) * math.sin(text_angle)
            canvas.create_text(text_x, text_y, text=f"{sectors[i]}%", font=("Arial", 10), anchor="center")
            start_angle += angle


# Создание окна
window = tk.Tk()
window.title("Секторная диаграмма")

# Чтение данных из файла
with open("data.txt", "r", encoding="utf-8") as file:
    data = file.readlines()

# Извлечение заголовка, наименований и процентов
title = data[0].strip()
labels = data[1].split()
sectors = list(map(float, data[2].split()))

# Создание холста для диаграммы
canvas = tk.Canvas(window, width=600, height=600)
canvas.pack()

# Построение секторной диаграммы
draw_pie_chart(canvas, 290, 350, 250, sectors, labels)  # Изменено значение center_y на 350

# Добавление заголовка с отступом
canvas.create_text(300, 50, text=title, font=("Arial", 16, "bold"))

# Запуск главного цикла обработки событий
window.mainloop()
