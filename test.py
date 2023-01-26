import matplotlib.pyplot as plt
import math
plt.ion()
x = [0, 1]
y = [0, 1]
print(x)
print(y)
for i in range(1, 100):
    # plt.gca().cla() # optionally clear axes
    plt.plot(x, y)
    plt.title(str(i))
    plt.draw()
    plt.pause(0.1)
    x.append(i)
    y.append(i)

plt.show(block=True) # block=True lets the window stay open at the end of the animation.