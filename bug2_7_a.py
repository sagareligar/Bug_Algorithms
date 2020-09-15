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


def towards_goal(q,x,w):# is x xordinate,w is polygon obstacle

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
	if(towards_goal(q_s[0],j,WO_1)==0):
		break
	else:
		obst_point=towards_goal(q_s[0],j,WO_1)

start=(q_s[0],obst_point[0])
end=(q_s[1],obst_point[1])
plt.plot(start,end,'m',label='bug-line',linewidth=2)


#inspired by https://gis.stackexchange.com/questions/339409/find-the-vertices-of-the-edge-of-the-polygon-where-line-intersects-using-shapely

#m-line interesction with the obstable WO_1

lin = loads('LineString (0.0 0.0, 10.0 10.0)')
pol=Polygon(WO_1)
polin = LineString(list(pol.exterior.coords))
# intersection 
pt = polin.intersection(lin)
#print(pt.wkt)
#print(pt.geoms[1].coords[0])

#Hitting the obstacle point
hit_point =pt.geoms[0].coords[0]
#leaving the obstacle
leave_point=pt.geoms[1].coords[0]

#print(hit_point)

#follow boundary after hitting the obstacle


def follow_boundary(x,y):


	if(x==1 and y<5):
		y=y+0.001
		return (x,y)

	elif(y>=5 and x<2):
		x=x+0.001
		return (x,y)

	elif(x>=2 and y>1):
		y=y-0.001
		return (x,y)

	elif(y<=1 and x>1):
		x=x-0.001
		return(x,y)

leave=(0,0)

while(True):

	a=follow_boundary(hit_point[0],hit_point[1])

	#print(a)

	if a:
		if(a[1]<pt.geoms[1].coords[0][1] and a[0]>1.6):
			p=round(a[0])
			q=round(a[1])
			leave=(p,q)

	

    
	if(leave==pt.geoms[1].coords[0]):#on the m line
		break
	else:
		if a:
		    start=(hit_point[0],a[0])
		    end=(hit_point[1],a[1])
		    plt.plot(start,end,'m',label='bug-line',linewidth=2)		
		    hit_point=a
		if not a:
			break

		
#leave_point=pt.geoms[1].coords[0]
for j in [float(k)/100 for k in range(0,1000,1)]:
	if((towards_goal(leave_point[0],j,WO_2)==0) or towards_goal(leave_point[0],j,WO_1)==q_g ):
		break
	else:
		obst_point=towards_goal(leave_point[0],j,WO_1)

start=(leave_point[0],round(obst_point[0]))
end=(leave_point[1],round(obst_point[1]))
plt.plot(start,end,'m',label='bug-line',linewidth=2)


plt.grid(True)
plt.show()