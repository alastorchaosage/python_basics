"""
Задание 2.

Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.

Пример:
Введите время в секундах: 3600
Время в формате ч:м:с - 1.0 : 60.0 : 3600
"""

sec_into = int(input('Введите время в секундах: '))
sec = sec_into % (24 * 3600)
hou_res = str(sec // 3600)
min_res = str(sec % 3600 // 60)
sec_res = str(sec_into % 60)
time_res = (hou_res + ':' + min_res + ':' + sec_res)
print(f"Время в формате чч:мм:сс - ", time_res.format('%HH:%MM:%SS'))







