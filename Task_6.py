import matplotlib.pyplot as plt
import numpy as np

def Task_6():
    month = ['Январь','Февраль','Март','Апрель','Май','Июнь']
    company_1 = [234, 564, 678, 876, 324, 476]
    company_2 = [675, 345, 743, 432, 436, 463]

    fig, axs = plt.subplots(2,2, figsize=(10,10))
    fig.suptitle('График продаж за полгода', fontsize=16)
    axs[0, 0].plot(month, company_1, label='Предприятие 1')
    axs[0, 0].plot(month, company_2, label='Предприятие 2')
    axs[0, 0].legend()

    x = np.arange(1, len(month)+1)
    width=0.2

    axs[0, 1].bar(x, company_1, width=width, label='Предприятие 1')
    axs[0, 1].bar(x+width, company_2, width=width, label='Предприятие 2')
    axs[0, 1].legend()

    axs[1, 0].pie(company_1, labels=month, autopct='%1.1f%%')
    axs[1, 1].pie(company_2, labels=month, autopct='%1.1f%%')
    plt.show()
