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


obstacle=[(4,4),(3,4),(3,13),(13,13),(13,5),(6,5),(6,6),(12,6),(12,12),(4,12)]

fig = plt.figure()
ax=fig.add_subplot(111)

plt.scatter(q_s[0],q_s[1],s=100)
plt.scatter(q_g[0],q_g[1],s=100)

rect_1=matplotlib.patches.Polygon(obstacle,color='green')

ax.add_patch(rect_1)

plt.grid(True)
plt.show()