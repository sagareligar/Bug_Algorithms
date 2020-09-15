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


obstacle=[(25,1),(24,1),(24,-5),(15,-5),(15,1),(14,1),(14,-5),(5,-5),(5,1),(4,1),(4,-5),(-5,-5),(-5,5),
(9,5),(9,0),(10,0),(10,5),(29,5),(29,0),(30,0),(30,6),(-6,6),(-6,-6),
(25,-6)]

fig = plt.figure()
ax=fig.add_subplot(111)

plt.scatter(q_s[0],q_s[1],s=100)
plt.scatter(q_g[0],q_g[1],s=100)

rect_1=matplotlib.patches.Polygon(obstacle,color='green')

ax.add_patch(rect_1)

point=Point(25,1)

poly=Polygon(obstacle)
print(point.touches(poly))


plt.grid(True)
plt.show()