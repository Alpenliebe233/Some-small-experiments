from random import random
import matplotlib.pyplot as plt

n = 100

def player(estimate, offer, i):
    V1 = 100
    V2 = 1000

    v1 = 0.0
    b1 = 0
    b2 = 0.0
    result = 0.0
    index = 0.0
    sum = 0.0

    v1 = 100.0 + 900 * (random())
    estimate[i] = v1
    for b1 in range(V1, V2):
        y = 0.0
        b2 = b1-(b1-V1) / n
        y = (b1-V1) / (V2-V1)
        result = (pow(y, n-1)) * (v1-b2)
        if result > sum:
            sum = result
            index = b1
    offer[i] = index+400


def auction():
    x_axix = [x for x in range(0, 100+1)]
    estimate = [0 for x in range(0, 100+1)]
    offer = [0 for x in range(0, 100+1)]
    for i in range(1, n+1):
        player(estimate, offer, i)

    plt.title('Estimate and bid for a secondary sealed price auction')
    plt.plot(x_axix, estimate, color='blue', label='Estimate the price')
    plt.plot(x_axix, offer, color='red', label='The actual offer')
    plt.legend(loc='upper right')
    plt.show()


if __name__ == '__main__':
    auction()