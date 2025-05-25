import numpy as np
import matplotlib.pyplot as plt


def f(x):  # def 를 이용하여 함수 정의
    return x ** 2


x = np.arange(0.0, 10, 0.5)
y = f(x)

plt.plot(x, y)
plt.show()