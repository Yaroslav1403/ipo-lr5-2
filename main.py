#Инициализация переменной для подсчета количества совпадающих символов
simvol = 0 
#Просим пользователя ввести первую строку
first_string = input("Введите первую строку: ")
#Заменяем все пробелы на пустую строку
replace_string = first_string.replace(" ","")
#Вычисляем длину первой строки 
first_string_len = len(replace_string)
#Просим пользователя ввести вторую строку
second_string = input("Введите вторую строку: ")
#Создаём цикл для перебора символов второй строки 
for i in second_string:
#Проверяем, содержится ли текущий символ i из второй строки в первой строке без пробелов
    if i in replace_string:
        simvol +=1
#Проверяем, равен ли счетчик simvol длине первой строки без пробелов
if simvol == first_string_len:
#Вывод результатов
    print("Ваши строки являются анограммами")
else:
    print("Ваши строки не являются анограммами")
