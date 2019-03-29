from random import randint
import matplotlib.pyplot as plt

nbiter = 100
size = 2
buzz = 4
innov = 1

liste = []
urn = {}
for i in range(size):
	urn[i] = 1
	
for n in range(nbiter):
	size = len(urn)
	draw = randint(0, size)
	if draw in liste:
		urn[draw] += buzz
	else:
		liste.append(draw)
		for i in range(size, size+innov):
			urn[i] = 1

print(urn)

keys=[]
values=[]
for key in urn.keys():
    keys.append(key)
    
for value in urn.values():
    values.append(value)
    
plt.plot(keys, values, 'bo',keys, values,'k')
plt.show()

