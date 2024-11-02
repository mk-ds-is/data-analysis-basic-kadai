import numpy as np
a = np.array([[0, 1], [2, 3], [4, 5]])
b = np.array([[0, 1, 2, 3], [4, 5, 6, 7]])
c = np.dot(a, b)
d = np.max(c)

print(c)
print("Max", d)