import numpy as np

def Task_1():
    values = []

    for i in range(10):
        values.append(int(input("Value[{}] = ".format(i))))

    a = np.array(values)

    b = np.linspace(20, 40, num=10)

    c = np.random.randint(1,6,10)

    print("Массив а")
    print("-------------------")
    print("Элементы:",a)
    print("Размер:",a.size)
    print("Форма:",a.shape)
    print("Тип данных:",a.dtype)
    print("Кол-во змерений",a.ndim)
    print("Ср. арифметическое:",a.mean())

    print("Массив b")
    print("-------------------")
    print("Элементы:", b)
    print("Размер:", b.size)
    print("Форма:", b.shape)
    print("Тип данных:", b.dtype)
    print("Кол-во змерений", b.ndim)
    print("Ср. арифметическое:",b.mean())

    print("Массив c")
    print("-------------------")
    print("Элементы:", c)
    print("Размер:", c.size)
    print("Форма:", c.shape)
    print("Тип данных:", c.dtype)
    print("Кол-во змерений", c.ndim)
    print("Ср. арифметическое:",c.mean())

    print("=========================")
    print("Result a * b:",a*b)
    print(np.delete(a,a[0:3]))
    newB = np.resize(b[::-1],(2,3))
    print("Новый массив из 6 посл. элементов массива b:",newB)

    d = np.copy(b);
    print(d)

    c_d = np.concatenate((c,d))
    print(c_d.reshape(4,5))

    print(np.append(c,[2,4]))

    print("Сортировка а",np.sort(a))
    print("Сортировка b:",np.flip(b))

