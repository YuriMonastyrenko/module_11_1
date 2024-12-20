# pandas — это библиотека для анализа данных, которая предоставляет структуры данных и функции для работы с табличными данными.
import pandas as pd
# 1. Чтение данных из файла CSV:
df = pd.read_csv('data.csv')
print(df.head())  # Выводит первые 5 строк DataFrame

# 2. Анализ данных:
filtered_df = df[df['column_name'] > 10]  # Фильтрует строки по условию
print(filtered_df)

# 3. Фильтрация данных:
filtered_df = df[df['column_name'] > 10]  # Фильтрует строки по условию
print(filtered_df)