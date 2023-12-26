# Перевірка роботи бібліотеки
import numpy as np
import matplotlib.pyplot as plt
from scipy import sparse
x= np.array([[1, 2, 3],[4, 5, 6]])
print("x:\n{}".format(x))

# Создаем 2D массив NumPy с единицами по главной диагонали и нулями в остальных ячейках
eye = np.eye(4)
print("массив NumPy:\n{}".format(eye))

# Генерируем последовательность чисел от -10 до 10 с 100 шагами
x = np.linspace(-10, 10, 100)
# Создаем второй массив с помощью синуса
y = np.sin(x)
# Функция создает линейный график на основе двух массивов
plt.plot(x, y, marker="x")
plt.show()
