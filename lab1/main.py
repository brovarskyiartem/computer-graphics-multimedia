from PIL import Image, ImageDraw
import math

# Створення пустого списку для зберігання даних
datapoints = []

# Зчитування даних з файлу 'DS0.txt' та додавання їх до списку datapoints
with open('DS0.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        # Розділіть рядок на координати, використовуючи пробіл як роздільник
        parts = line.strip().split()
        x, y = map(int, parts)
        datapoints.append((x, y))

# Визначення кута обертання в радіанах
alpha = math.radians(10)

# Визначення матриці обертання
rotation_matrix = [
    [math.cos(alpha), -math.sin(alpha), 0],
    [math.sin(alpha), math.cos(alpha), 0],
    [0, 0, 1]
]

# Виконання афінного перетворення
transformed_datapoints = []
for point in datapoints:
    x, y = point
    # Додавання третьої координати (1) для виконання матричного множення
    point_matrix = [[x], [y], [1]]
    result_matrix = [[0], [0], [0]]

    # Матричне множення
    for i in range(len(rotation_matrix)):
        for j in range(len(point_matrix[0])):
            for k in range(len(point_matrix)):
                result_matrix[i][j] += rotation_matrix[i][k] * point_matrix[k][j]

    # Зберігання трансформованих точок
    transformed_datapoints.append((result_matrix[0][0], result_matrix[1][0]))

# Створення зображення та області малювання
image = Image.new("RGB", [960, 960], color="white")
draw = ImageDraw.Draw(image)

point_radius = 0.1  # Розмір точок
point_color = 'blue'  # Колір точок після трансформації

# Виведення трансформованих точок
for point in transformed_datapoints:
    x, y = point
    x, y = int(y), int(520 - x)  # Обертання координат на 90 градусів
    x, y = x - point_radius, y - point_radius  # Центруємо точки
    x1, y1 = x + 2 * point_radius, y + 2 * point_radius  # Розраховуємо прямокутник, який включає точку
    draw.ellipse([x, y, x1, y1], fill=point_color, outline=point_color)
transformed_filename = "dataset.txt"  # Новий файл для збереження трансформованих точок

with open(transformed_filename, 'w') as file:
    for point in transformed_datapoints:
        x, y = point
        x, y = int(y), int(520 - x)  # Обертання координат на 90 градусів
        x, y = x - point_radius, y - point_radius  # Центруємо точки
        x1, y1 = x + 2 * point_radius, y + 2 * point_radius  # Розраховуємо прямокутник, який включає точку
        draw.ellipse([x, y, x1, y1], fill=point_color, outline=point_color)
        
        # Запис точок у новий файл
        file.write(f"int({x}) int({y})\n")
# Збереження результатів у файл
image.save("transformed_result.png")
image.show()  # Покажемо на екрані
