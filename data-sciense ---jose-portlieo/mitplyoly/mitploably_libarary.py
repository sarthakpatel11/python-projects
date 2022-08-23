import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 5, 11)
y = x**2
# plt.plot(x, y)
# plt.xlabel('X lable')
# plt.ylabel('y lable')
# plt.title('Title')
# plt.show()


plt.subplot(1, 2, 1)
plt.plot(x, y, 'r')
plt.subplot(1, 2, 2)
plt.plot(y, x, 'b')
plt.show()


#    axies (between gape) ///////////
fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes.plot(x, y)
print(axes)
