import numpy as np
from matplotlib import pyplot as plt
import matplotlib.animation as animation

#Созадние поля (границы дороги) a, b, c, d, e
#Вывод на график
#точка движение влево-вправо
#Вывод на график


a = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
b = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2]
c = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
d = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2]
e = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]

matrix = np.asmatrix((a, b, c, d, e))
shape = matrix.shape

p = np.array((shape[0]//2, shape[1]//2, True))
matrix[p[0], p[1]] = 1

sz = 500

def random_spawn(p):
	if p[1] == shape[1] - 1:
		p[2] = False
	if p[1] == 0:
		p[2] = True
		
	if p[1] < shape[1] and p[2]:
		p[1] += 1
		matrix[p[0], p[1] - 1] = 0
		matrix[p[0], p[1]] = 1
	if not p[2]:
		p[1] -= 1
		matrix[p[0], p[1] + 1] = 0
		matrix[p[0], p[1]] = 1
	print(p[2])

def animate(i):
	random_spawn(p)
	plt.cla()
	for i in range(shape[0]):
		for j in range(shape[1]):
			if matrix[i, j] == 2:
				plt.scatter(j, i, c='red', s=sz)
			elif matrix[i, j] == 0:
				plt.scatter(j, i, c='white', s=sz)
			elif matrix[i, j] == 1:
				plt.scatter(j, i, c='blue', s=sz)




fig = plt.figure()
ani = animation.FuncAnimation(fig, animate, interval=4)	
plt.show()
#ani.save('try_animation.gif', writer='imagemagick')
#exit(0)
