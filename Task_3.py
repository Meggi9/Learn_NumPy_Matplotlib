from matplotlib import pyplot as plt

def Y1(x):
    return 2*(x**2)

def Y2(x):
    return 5*x+4


def Task_3():
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

    print(arrX)
    print(arrYA)
    print(arrYB)

    plt.title("График", color="black", size=16)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid()
    plt.plot(arrX, arrYA,'--y',label="y1(x)=a*x^2")
    plt.plot(arrX, arrYB,'*',label="y1(x)=b*x+c")
    plt.legend()
    plt.figure(figsize=(5,5))
    plt.show()