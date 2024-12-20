# matplotlib — это библиотека для визуализации данных, позволяющая создавать различные графики и диаграммы.
import matplotlib.pyplot as plt
# 1. Создание линейного графика:

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.plot(x, y)
plt.title('Пример линейного графика')
plt.xlabel('X ось')
plt.ylabel('Y ось')
plt.show()  # Отображает график

# 2. Создание гистограммы:

data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

plt.hist(data, bins=4)
plt.title('Гистограмма')
plt.xlabel('Значения')
plt.ylabel('Частота')
plt.show()

# 3. Сохранение графика в файл:

plt.plot(x, y)
plt.savefig('plot.png')  # Сохраняет график в формате PNG
