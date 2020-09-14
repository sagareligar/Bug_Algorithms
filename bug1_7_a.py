import matplotlib
import matplotlib.pyplot as plt
#from matplotlib.patches import Rectangle
import math
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import numpy as np
from shapely.wkt import loads
from shapely.geometry import LineString


#start_point
q_s=(0,0)
#end_point
q_g = (10,10)

#obstacle co-ordinates
WO_1=[(1,1),(2,1),(2,5),(1,5)]
WO_2=[(3,4),(4,4),(4,12),(3,12)]
WO_3=[(3,12),(12,12),(12,13),(3,13)]
WO_4=[(12,5),(13,5),(13,13),(12,13)]
WO_5=[(6,5),(12,5),(12,6),(6,6)]

obstacle=[WO_1,WO_2,WO_3,WO_4,WO_5]


fig = plt.figure()
ax=fig.add_subplot(111)

#plt.scatter(0,0,s=100)
#plt.scatter(10,10,s=100)

plt.scatter(q_s[0],q_s[1],s=100)
plt.scatter(q_g[0],q_g[1],s=100)


#rect_1=matplotlib.patches.Rectangle((1,1),1,4,color='green')
rect_1=matplotlib.patches.Polygon(WO_1,color='green')
rect_2=matplotlib.patches.Polygon(WO_2,color='green')
rect_3=matplotlib.patches.Polygon(WO_3,color='green')
rect_4=matplotlib.patches.Polygon(WO_4,color='green')
rect_5=matplotlib.patches.Polygon(WO_5,color='green')






ax.add_patch(rect_1)
ax.add_patch(rect_2)
ax.add_patch(rect_3)
ax.add_patch(rect_4)
ax.add_patch(rect_5)


x_values=[q_s[0],q_g[0]]
y_values=[q_s[1],q_g[1]]


slope=(q_g[1]-q_s[1])/(q_g[0]-q_s[0])


c=q_s[1]-(slope*q_s[0])


def towards_goal(q,x,w,slope,c):#x is x xordinate,w is polygon obstacle

	y=(slope)*(q+x)+c
	follow_point=(q+x,y)
	point=Point(follow_point)
	polygon=Polygon(w)
	if(polygon.contains(point)==True):
		#print("Dont follow")
		return 0
	else:
		#print("continue path")
		return follow_point



	
for j in [float(k)/100 for k in range(0,1000,1)]:
	if(towards_goal(q_s[0],j,WO_1,slope,c)==0):
		break
	else:
		obst_point=towards_goal(q_s[0],j,WO_1,slope,c)

start=(q_s[0],obst_point[0])
end=(q_s[1],obst_point[1])
plt.plot(start,end,'m',label='bug-line',linewidth=2)

disttogoal_W1=[]
mindist_W1=[]



hit_point=(obst_point[0],obst_point[1])

def follow_boundary(x,y):


	if(x==1 and y<5):
		y=y+0.001
		distance=np.sqrt(np.square(x-q_g[0])+np.square(y-q_g[1]))
		disttogoal_W1.append(distance)
		p=(x,y)
		mindist_W1.append(tuple(p))
		return (x,y)

	elif(y>=5 and x<2):
		x=x+0.001
		distance=np.sqrt(np.square(x-q_g[0])+np.square(y-q_g[1]))
		disttogoal_W1.append(distance)
		p=(x,y)
		mindist_W1.append(tuple(p))
		return (x,y)

	elif(x>=2 and y>1):
		y=y-0.001
		distance=np.sqrt(np.square(x-q_g[0])+np.square(y-q_g[1]))
		disttogoal_W1.append(distance)
		p=(x,y)
		mindist_W1.append(tuple(p))
		return (x,y)

	elif(y<=1 and x>1):
		x=x-0.001
		distance=np.sqrt(np.square(x-q_g[0])+np.square(y-q_g[1]))
		disttogoal_W1.append(distance)
		p=(x,y)
		mindist_W1.append(tuple(p))
		return(x,y)





while(True):

	a=follow_boundary(hit_point[0],hit_point[1])
	print(a)
    
	if a:
		if(a[0]<1 and a[1]<1):
			break
		l=hit_point[0]
		m=hit_point[1]
		x=a[0]
		y=a[1]
		
		if(a[0]<1 or a[0]>2 or a[1]>5 or a[1]<1):
			x=round(a[0])
			y=round(a[1])
		if(hit_point[0]<1 or hit_point[0]>2 or hit_point[1]>5 or hit_point[1]<1):
			l=round(hit_point[0])
			m=round(hit_point[1])

		start=(l,x)
		end=(m,y)
		plt.plot(start,end,'m',label='bug-line',linewidth=2)
		hit_point=a

	



mindist_index=disttogoal_W1.index(min(disttogoal_W1))
leave_point=mindist_W1[mindist_index]
print(leave_point)


start=(round(leave_point[0]),q_g[0])
end=(round(leave_point[1]),q_g[1])

#plt.plot(start,end,'m',label='bug-line',linewidth=2)


slope=(q_g[1]-end[0])/(q_g[0]-start[0])


c=q_g[1]-(slope*q_g[0])



for j in [float(k)/100 for k in range(0,1000,1)]:
	if(towards_goal(round(leave_point[0]),j,WO_2,slope,c)==0):
		break
	else:
		obst_point=towards_goal(round(leave_point[0]),j,WO_2,slope,c)

start=(round(leave_point[0]),obst_point[0])
end=(round(leave_point[1]),obst_point[1])
plt.plot(start,end,'m',label='bug-line',linewidth=2)

print(obst_point)


disttogoal_Wall=[]
mindist_Wall=[]


def follow_bound(x,y):

	if(x==3 and y<13):
		y=y+0.001
		distance=np.sqrt(np.square(x-q_g[0])+np.square(y-q_g[1]))
		disttogoal_Wall.append(distance)
		p=(x,y)
		mindist_Wall.append(tuple(p))
		return (x,y)
	elif(y>=13 and x<13):
		x=x+0.001
		distance=np.sqrt(np.square(x-q_g[0])+np.square(y-q_g[1]))
		disttogoal_Wall.append(distance)
		p=(x,y)
		mindist_Wall.append(tuple(p))
		return (x,y)
	elif(x>=13 and y>5):
		y=y-0.001
		distance=np.sqrt(np.square(x-q_g[0])+np.square(y-q_g[1]))
		disttogoal_Wall.append(distance)
		p=(x,y)
		mindist_Wall.append(tuple(p))
		return (x,y)
	elif(y<=5 and x>6):
		x=x-0.001
		distance=np.sqrt(np.square(x-q_g[0])+np.square(y-q_g[1]))
		disttogoal_Wall.append(distance)
		p=(x,y)
		mindist_Wall.append(tuple(p))
		return (x,y)
	elif(x<=6 and y<6):
		y=y+0.001
		distance=np.sqrt(np.square(x-q_g[0])+np.square(y-q_g[1]))
		disttogoal_Wall.append(distance)
		p=(x,y)
		mindist_Wall.append(tuple(p))
		return (x,y)







while(True):

	a=follow_bound(obst_point[0],obst_point[1])
	print(a)
    
	if a:
		if(a[0]<13 and a[1]<5):
			break
		l=hit_point[0]
		m=hit_point[1]
		x=a[0]
		y=a[1]
		
		if(a[0]<1 or a[0]>2 or a[1]>5 or a[1]<1):
			x=round(a[0])
			y=round(a[1])
		if(hit_point[0]<1 or hit_point[0]>2 or hit_point[1]>5 or hit_point[1]<1):
			l=round(hit_point[0])
			m=round(hit_point[1])

		start=(l,x)
		end=(m,y)
		plt.plot(start,end,'m',label='bug-line',linewidth=2)
		hit_point=a
















plt.grid(True)
plt.show()