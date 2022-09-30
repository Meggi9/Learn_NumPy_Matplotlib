import numpy as np
import matplotlib.pyplot as plt

def Task_7():
    arr = np.array(np.random.randint(0,2,(10,10)))
    fig, axs = plt.subplots(2,2, figsize=(10,10))

    axs[0, 0].imshow(arr)
    axs[0, 0].set_title('Исходное изображение')

    newArr = np.array(arr[3:7, 3:7])
    axs[0, 1].imshow(newArr)
    axs[0, 1].set_title('Центр. часть (4х4)')

    invArr = np.array(1 - arr)
    axs[1, 0].imshow(invArr)
    axs[1, 0].set_title('Инвертированное изображение')

    Arr1 = []
    for i in range(len(arr)):
        Arr2 = []
        for j in range(len(arr[i])-1):
            if(j == 0):
                continue
            elif(j == len(arr[i])):
                break
            else:
                Arr2.append((arr[i,j-1]+arr[i,j]+arr[i,j+1])/3)
        Arr1.append(Arr2)

    blurryArr = np.array(Arr1)
    axs[1,1].imshow(blurryArr)
    axs[1, 1].set_title('Размытое изображение')
    plt.show()
    fig.savefig('images_matplotlib.png')