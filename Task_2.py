import numpy as np

def Task_2():
    Array1 = []
    for i in range(4):
        Array2 = []
        for j in range(4):
            Array2.append(int(1))
            #Array2.append(int(input("Value[{}][{}] = ".format(i, j))))

        Array1.append(Array2)

    a = np.array(Array1)

    b = np.array(np.random.randint(-10,10,(4,4)))

    print("=====================")
    print("Массив а:")
    print(a)
    print("Размер:",a.size)
    print("Форма:",a.shape)
    print("Тип данных:",a.dtype)
    print("Кол-во змерений",a.ndim)
    print("=====================")
    print("Массив b:")
    print(b)
    print("Размер:",b.size)
    print("Форма:",b.shape)
    print("Тип данных:",b.dtype)
    print("Кол-во змерений",b.ndim)
    print("=====================")
    print("Центр. часть массива а:")
    print(a[1:3,1:3])
    print("Прозведение массивов a * b:")
    print(a*b)

    print("Замена 2 строки на сумму элементов 1 и 3 строк:")
    newA = a

    for i in range(newA[1].size):
        newA[1,i] = a[0,i] + a[2,i]

    print(newA)

    print("Вставка столбца")
    print(np.insert(b,2,[0,0,0,0],axis=1))

    c = np.vstack((a,b))

    print("Массив с:")
    print(c)
    print("Массив с (2,16):")
    print(c.reshape(2,16))
    print("Массив с после удаления 3 столбцов")
    print(np.delete(c,[1,2,3],axis=1))
    print("Одномерный массив из 1 и 2 строки массива а:",b[0:2].flatten())
