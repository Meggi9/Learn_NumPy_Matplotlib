from Task_1 import *
from Task_2 import *
from Task_3 import *
from Task_5 import *

print("Лабораторная работа №3")
print("Изучение библиотеки Numpy и Matplotlib")
while (True):
    print("========================")
    print("Выберите задание: ")
    print("1 - Одномерные массивы Numpy")
    print("2 - Двумерные массивы Numpy")
    print("3 - Построение графика с помощью Matplotlib")
    print("4 - Построение графика с использованием функции subplots")
    print("5 - Построение нескольких графиков на одном рисунке")
    print("6 - Построение графиков разных типов")
    print("7 - Использование библиотек Numpy и Matplotlib для работы с изображениями")
    print("0 - Выход")
    numTask = int(input("==> "))
    print("========================")

    match numTask:
        case 1:
            Task_1()
        case 2:
            Task_2()
        case 3:
            Task_3()
        # case 4:
            # Task_4()
        case 5:
            Task_5()
        # case 6:
            # Task_6()
        # case 7:
        #     Task_7()
        case 0:
            print("Завершение работы программы!")
            print("============================")
            break
