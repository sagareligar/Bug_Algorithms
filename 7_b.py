import matplotlib
import matplotlib.pyplot as plt
#from matplotlib.patches import Rectangle

from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

#start_point
q_s=(0,0)
#end_point
q_g = (35,0)




fig = plt.figure()
ax=fig.add_subplot(111)

plt.scatter(q_s[0],q_s[1],s=100)
plt.scatter(q_g[0],q_g[1],s=100)



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


plt.grid(True)
plt.show()