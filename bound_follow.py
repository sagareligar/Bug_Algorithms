import matplotlib
import matplotlib.pyplot as plt
#from matplotlib.patches import Rectangle

from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
from shapely.geometry import LineString
from shapely.wkt import loads

#start_point
q_s=(0,0)
#end_point
q_g = (35,0)




fig = plt.figure()
ax=fig.add_subplot(111)

plt.scatter(q_s[0],q_s[1],s=100)
plt.scatter(q_g[0],q_g[1],s=100)


obstacle=[(25,1),(24,1),(24,-5),(15,-5),(15,1),(14,1),(14,-5),(5,-5),(5,1),(4,1),(4,-5),(-5,-5),(-5,5),
(9,5),(9,0),(10,0),(10,5),(29,5),(29,0),(30,0),(30,6),(-6,6),(-6,-6),
(25,-6)]

poly=Polygon(obstacle)

#obstacle co-ordinates
WO_1=[(-6,-6),(25,-6),(25,-5),(-6,-5)]
WO_2=[(-6,5),(30,5),(30,6),(-6,6)]
WO_3=[(-6,-5),(-5,-5),(-5,5),(-6,5)]
WO_4=[(4,-5),(5,-5),(5,1),(4,1)]
WO_5=[(9,0),(10,0),(10,5),(9,5)]
WO_6=[(14,-5),(15,-5),(15,1),(14,1)]
WO_7=[(19,0),(20,0),(20,5),(19,5)]
WO_8=[(24,-5),(25,-5),(25,1),(24,1)]
WO_9=[(29,0),(30,0),(30,5),(29,5)]

#rect_1=matplotlib.patches.Rectangle((1,1),1,4,color='green')
rect_1=matplotlib.patches.Polygon(WO_1,color='green')
rect_2=matplotlib.patches.Polygon(WO_2,color='green')
rect_3=matplotlib.patches.Polygon(WO_3,color='green')
rect_4=matplotlib.patches.Polygon(WO_4,color='green')
rect_5=matplotlib.patches.Polygon(WO_5,color='green')
rect_6=matplotlib.patches.Polygon(WO_6,color='green')
rect_7=matplotlib.patches.Polygon(WO_7,color='green')
rect_8=matplotlib.patches.Polygon(WO_8,color='green')
rect_9=matplotlib.patches.Polygon(WO_9,color='green')



ax.add_patch(rect_1)
ax.add_patch(rect_2)
ax.add_patch(rect_3)
ax.add_patch(rect_4)
ax.add_patch(rect_5)
ax.add_patch(rect_6)
ax.add_patch(rect_7)
ax.add_patch(rect_8)
ax.add_patch(rect_9)




x_values=[q_s[0],q_g[0]]
y_values=[q_s[1],q_g[1]]


slope=(q_g[1]-q_s[1])/(q_g[0]-q_s[0])


c=q_s[1]-(slope*q_s[0])

lin = loads('LineString (0.0 0.0, 35.0 0.0)')
pol=Polygon(obstacle)
polin = LineString(list(pol.exterior.coords))
# intersection 
pt = polin.intersection(lin)
print(pt.wkt)
print(pt.geoms[0].coords[0])
print(pt.geoms[1].coords[0])
print(pt.geoms[2].coords[0])
print(pt.geoms[3].coords[0])
print(pt.geoms[4].coords[0])
print(pt.geoms[5].coords[0])



def towards_goal(q,x,w):#q+x is x xordinate,w is polygon obstacle

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
	if(towards_goal(q_s[0],j,obstacle)==0):
		break
	else:
		obst_point=towards_goal(q_s[0],j,obstacle)



start=(q_s[0],obst_point[0])
end=(q_s[1],obst_point[1])
plt.plot(start,end,'m',label='bug-line',linewidth=2)

x=obst_point[0]
y=obst_point[1]

y_i=1
y_axis=1
y_d=0

x_i=1
x_axis=0
x_d=0

endless=0

while(True):

	#if(y==0 and x==30):
	#	break




	count=0
	if(y_i==1 and y_axis==1):
		x=round(x)
		y=y+0.01
		point=Point(x,y)
		while(point.touches(poly)):
			plt.plot((x,x),(y-0.01,round(y)),'m',label='bug-line',linewidth=2)
			y=y+0.01
			count=count+1
			point=Point(x,y)
			print(point)
			if((y>(obst_point[1]-0.2) and y<obst_point[1]) and (x==obst_point[0])):
				endless=10
				break
		if(endless==10):
			break						
		y=y-0.01
		if(count>1):
			y_d=0
			x_axis=1
			y_axis=0

		else:
			y_axis=1
			y_d=1
	count=0

	if(y_d==1 and y_axis==1):
		x=round(x)
		y=y-0.01
		point=Point(x,y)
		while(point.touches(poly)):
			plt.plot((x,x),(round(y),y+0.01),'m',label='bug-line',linewidth=2)
			y=y-0.01
			count=count+1
			point=Point(x,y)
			print(point)

		y=y+0.01
		if(count>1):
			y_i=0
			x_axis=1
			y_axis=0		
		else:
			y_axis=1
			y_i=1
	count=0
	if(x_axis==1 and x_i==1):
		y=round(y)
		x=x+0.01
		point=Point(x,y)
		while(point.touches(poly)):
			plt.plot((x-0.01,x),(y,y),'m',label='bug-line',linewidth=2)						
			x=x+0.01
			count=count+1
			point=Point(x,y)
			print(point)
		x=x-0.01
		if(count>1):
			x_d=0
			x_axis=0
			y_axis=1
		else:
			x_axis=1
			x_d=1

	count=0
	if(x_axis==1 and x_d==1):
		y=round(y)
		x=x-0.01
		point=Point(x,y)
		while(point.touches(poly)):
			plt.plot((x,x+0.01),(y,y),'m',label='bug-line',linewidth=2)
			x=x-0.01
			count=count+1
			point=Point(x,y)
			print(point)
		x=x+0.01
		if(count>1):
			x_i=0
			x_axis=0
			y_axis=1

		else:
			x_axis=1
			x_i=1



	









plt.grid(True)
plt.show()