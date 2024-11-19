import requests

# Отправляем GET-запрос на сайт
response = requests.get('https://api.github.com')

# Проверяем статус ответа
if response.status_code == 200:
    print("Ответ получен успешно!")
    # Выводим содержимое ответа
    print(response.text)
else:
    print(f"Произошла ошибка: {response.status_code}")


    
import pandas as pd

# Чтение данных из CSV-файла
data = pd.read_csv('example_data.csv')

# Вывод первых пяти строк таблицы
print(data.head())

# Вычисление среднего значения столбца 'age'
mean_age = data['age'].mean()
print(f"Средний возраст: {mean_age:.2f}")

# Группировка данных по значению столбца 'gender' и вычисление количества записей в каждой группе
grouped = data.groupby('gender').size().reset_index(name='count')
print(grouped)



import matplotlib.pyplot as plt

# Создание списка значений для оси X и Y
x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

# Построение линейного графика
plt.plot(x, y, marker='o', linestyle='--', color='b')

# Добавление подписей осей
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

# Добавление названия графика
plt.title('Simple Line Graph')

# Отображение графика
plt.show()