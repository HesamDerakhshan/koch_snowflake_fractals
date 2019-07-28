import math 
import numpy as np
import matplotlib.pyplot as plt

p0=[1,0]
p1=[0,0]

limit=3

x=[]
y=[]

def koch(p0,p1,limit):
	dx=p1[0]-p0[0]

	dy=p1[1]-p0[1]

	dist=np.sqrt(dx*dx+dy*dy)

	unit=dist/3

	angle=math.atan2(dy,dx)

	pA=[p0[0]+dx/3,p0[1]+dy/3]

	pC=[p1[0]-dx/3,p1[1]-dy/3]

	pB=[pA[0]+np.cos(angle-(math.pi)/3)*unit,pA[1]+np.sin(angle-(math.pi)/3)*unit]

	#print (x)
	
	if(limit>0):
		koch(p0,pA,limit-1)
		koch(pA,pB,limit-1) 
		koch(pB,pC,limit-1)
		koch(pC,p1,limit-1)
	else:
		x.append(p0[0])
		y.append(p0[1])
		x.append(pA[0])
		y.append(pA[1])
		x.append(pB[0])
		y.append(pB[1])
		x.append(pC[0])
		y.append(pC[1])
		x.append(p1[0])
		y.append(p1[1])
	
koch(p0,p1,limit)


plt.plot(x,y)

plt.axis('equal')
plt.show()
