from PIL import Image, ImageDraw

# Створення пустого списку для зберігання даних
datapoints = []

# Створення білого зображення розміром 960x540 пікселів
image = Image.new("RGB", [960, 540], color="white")  # Змінено розмір для обернутого зображення
draw = ImageDraw.Draw(image)

# Зчитування даних з файлу 'DS0.txt' та додавання їх до списку datapoints
with open('DS0.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        # Розділіть рядок на координати, використовуючи пробіл як роздільник
        parts = line.strip().split()
        x, y = map(int, parts)
        datapoints.append((x, y))
point_radius = 0.1  # Розмір точок
point_color = 'black'  # Колір точок
# Виведення зчитаних даних у вигляді кортежу та обертання координат
for point in datapoints:
    x, y = point
    x, y = y,520 - x  # Обертання координат на 90 градусів
    x, y = x - point_radius, y - point_radius  # Центруємо точки
    x1, y1 = x + 2 * point_radius, y + 2 * point_radius  # Розраховуємо прямокутник, який включає точку
    draw.ellipse([x, y, x1, y1], fill=point_color, outline=point_color)
image.save("res.png")
image.show()  # Покажемо на екрані
