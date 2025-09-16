import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df_1 = pd.read_csv(r'C:\Users\Пользователь\Desktop\Аналитик данных 1\[SW.BAND] 2 МОДУЛЬ PYTHON\[SW.BAND] Данные для Минипроектов\3_user_data.csv', encoding='windows-1251')
df_2 = pd.read_csv(r'C:\Users\Пользователь\Desktop\Аналитик данных 1\[SW.BAND] 2 МОДУЛЬ PYTHON\[SW.BAND] Данные для Минипроектов\3_logs.csv', encoding='windows-1251')

platform_unique = df_2['platform'].unique() #узнали сколько уникальных значений принимает стобец platform (3 значения)
#print(platform_unique)

successful = df_2[df_2['success'] == True] # фильтруем успешные операции
client_counts = (successful.groupby('client')
                 .size()) # считаем количество успешных операций по клиентам
max_count = client_counts.max() # находим максимум
top_clients = (client_counts[client_counts == max_count]
               .index) # выбираем всех клиентов с этим максимумом
result = ', '.join(map(str, sorted(top_clients))) # делаем строку с ID клиентов
#print("Клиент(ы) с наибольшим числом успешных операций:", result)

platform_counts = (successful.groupby('platform')
                   .size()) # группируем по платформе и считаем количество
top_platform = platform_counts.idxmax() # находим платформу с максимумом
max_ops = platform_counts.max()
#print(f"Больше всего успешных операций на платформе {top_platform} ({max_ops} операций).")

merged = df_2.merge(df_1[['client', 'premium']], on='client', how='left') # объединим данные по клиенту
premium_logs = merged[merged['premium'] == True] # оставим только премиум-клиентов
platform_countss = premium_logs.groupby('platform').size() # посчитаем количество операций по платформам
max_platform = platform_countss.idxmax()
max_countt = platform_countss.max()
print(f"Самая популярная платформа среди премиум-клиентов: {max_platform} ({max_countt} операций)")

# Гистограмма распределения возраста по типу клиента
sns.histplot(data=df_1, x='age', hue='premium', multiple='stack')
plt.title("Распределение возраста клиентов по типу")
plt.xlabel("Возраст")
plt.ylabel("Количество клиентов")
plt.show()



