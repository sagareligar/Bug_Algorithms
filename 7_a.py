import matplotlib
import matplotlib.pyplot as plt
#from matplotlib.patches import Rectangle
import math
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import numpy as np


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







#rect_2=matplotlib.patches.Rectangle((3,4),1,8,color='green')
#rect_3=matplotlib.patches.Rectangle((3,12),9,1,color='green')
#rect_4=matplotlib.patches.Rectangle((12,5),1,8,color='green')
#rect_5=matplotlib.patches.Rectangle((6,5),6,1,color='green')


ax.add_patch(rect_1)
ax.add_patch(rect_2)
ax.add_patch(rect_3)
ax.add_patch(rect_4)
ax.add_patch(rect_5)

#g=(1.5,1.5)
#point=Point(g)
#polygon=Polygon(WO_1)
#print(polygon.contains(point))


#m-line
x_values=[q_s[0],q_g[0]]
y_values=[q_s[1],q_g[1]]


slope=(q_g[1]-q_s[1])/(q_g[0]-q_s[0])


c=q_s[1]-(slope*q_s[0])


y_value=0
j=0




while(True):


	y_value=((slope)*(q_s[0]+j))+c
	#print(y_value)
	point_line=(q_s[0]+j,y_value)
	#print(point_line)
	point=Point(point_line)
	polygon=Polygon(WO_1)
	#print(polygon.contains(point))
	if(polygon.contains(point)==True):
		break
	else:
		j=j+0.001


    
	
start=[q_s[0],round(q_s[0]+(j-0.001))]
end=[q_s[1],round(((slope)*(q_s[0]+j-0.001))+c)]
#print(end)

plt.plot(start,end,'m',label='bug-line',linewidth=2)


x_value=round(q_s[0]+(j-0.001))
y_value= round(((slope)*(q_s[0]+j-0.001))+c)

points_min_dist=[]
dist_to_goal=[]
p=0


new_start=(round(q_s[0]+(j-0.001)),round(((slope)*(q_s[0]+j-0.001))+c))
y=new_start[1] 
#folowing boundary
while(y<5):

	
	#x_value = round(q_s[0]+(j-0.001)) 
    y = y +0.001
    min_point=(new_start[0],y)
    #dist=sqrt(((new_start[0]-q_g[0])^2 + ((new_start[1] -q_g[1])^2))
    distance=np.sqrt(np.square(new_start[0]-q_g[0])+np.square(y-q_g[1]) )	
    dist_to_goal.append(distance)
    #np.append(dist_to_goal,distance)
    #distance.append(dist_to_goal)
    points_min_dist.append(tuple(min_point))


start=[x_value,new_start[0]]
end=[y_value,round(y)]

plt.plot(start,end,'m',label='bug-line',linewidth=2)

        
new_start=(start[1],end[1])

x_value=start[1]
y_value=end[1]


x=new_start[0]

while(x<2):

	x=x+0.001
	min_point=(x,y_value)
	distance=np.sqrt(np.square(x-q_g[0])+np.square(y_value-q_g[1]))
	dist_to_goal.append(distance)
	#np.append(dist_to_goal,distance)
	points_min_dist.append(tuple(min_point))  



start=[x_value,round(x)]
end=[y_value,new_start[1]]

plt.plot(start,end,'m',label='bug-line',linewidth=2)


new_start=(start[1],end[1])

x_value=start[1]
y_value=end[1]

y=new_start[1]

while(y>1):
	y=y-0.001
	min_point=(x_value,y)
	distance=np.sqrt(np.square(new_start[0]-q_g[0])+np.square(y-q_g[1]) )
	dist_to_goal.append(distance)
	#np.append(dist_to_goal,distance)
	points_min_dist.append(tuple(min_point)) 


start=[x_value,new_start[0]]
end=[y_value,round(y)]

plt.plot(start,end,'m',label='bug-line',linewidth=2)
     
new_start=(start[1],end[1])

x_value=start[1]
y_value=end[1]

x=new_start[0]



while(x>1):

	x=x-0.001
	min_point=(x,y_value)
	distance=np.sqrt(np.square(x-q_g[0])+np.square(y_value-q_g[1]))
	dist_to_goal.append(distance)
	#np.append(dist_to_goal,distance)
	points_min_dist.append(tuple(min_point))  



start=[x_value,round(x)]
end=[y_value,new_start[1]]

plt.plot(start,end,'m',label='bug-line',linewidth=2)

minpos_index=dist_to_goal.index(min(dist_to_goal))

leave_point=points_min_dist[minpos_index]

print(leave_point)

#while(True):

	#print("hello")
    


#	y_value=(slope)*(q_s[0]+j)+c
#	point_line=(q_s[0]+j,y_value)
    #point=Point(point_line)
#	print(point_line)
		
	
	#
    


    #
    #polygon=Polygon(WO_1)
    #print(polygon.contains(point))
	#if(polygon.contains(point)==True):

	#	break
	#else:
	#	j=j+.001


    
    
    
	
#start=[q_s[0],q_s[0]+(j-0.001)]
#end=[q_s[1],((slope)*(q_s[0]+j-0.001))+c]
#print(end)

#plt.plot(start,end,'m',label='bug-line',linewidth=2)
#plt.lines(x_values,y_values,linestyle="dashed")

plt.grid(True)
plt.show()