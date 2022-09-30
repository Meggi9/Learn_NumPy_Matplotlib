from matplotlib import pyplot as plt

def Y1(x):
    return 2*(x**2)

def Y2(x):
    return 5*x+4

def Task_4():
    x0=-5
    x1=5
    h=1

    arrX = []
    arrYA = []
    arrYB = []

    for i in range(x0,x1+1,h):
        arrX.append(i)
        arrYA.append(Y1(i))
        arrYB.append(Y2(i))

    fig, axs = plt.subplots(1,2)
    axs[0].plot(arrX, arrYA,'--y')
    axs[0].set_title('y1(x)=a*x^2')
    axs[1].plot(arrX, arrYB,'*')
    axs[1].set_title('y1(x)=b*x+c')
    plt.show()
