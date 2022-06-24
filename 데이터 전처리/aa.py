import numpy as np

a = np.array([[0.7, 0.3],
              [0.4, 0.6]])

b = np.array([0, 1])



def solution(a, b):
    return np.matmul(b, a)


for i in range(10000000):
    b = np.matmul(b, a)
    if i < 4:
        print(b)

print(b)