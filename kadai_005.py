import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(2, 3, tight_layout=True)

# 折れ線
y0 = [1, 2, -5, 2]
axes[0,0].plot(y0)

#sin関数
x = np.linspace(0, 10, 100)
y = 2 + 2 * np.sin(2 * x)

axes[0,1].plot(x, y, linewidth=2.0)

axes[0,1].set(xlim=(0, 10), xticks=np.arange(0, 10),
       ylim=(-1, 5), yticks=np.arange(-1, 6))


# ヒストグラム
x = np.random .normal(15, 5, 2000)
plt.xlim(-10, 40)

axes[0,2].hist(x)


# 散布図
np.random.seed(3)
x = 4 + np.random.normal(0, 2, 60)
y = 4 + np.random.normal(0, 2, len(x))

axes[1,0].scatter(x, y)


plt.show()