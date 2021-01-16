import numpy as np
import matplotlib.pyplot as plt
import math

S = []
def calc(points, total_pts, multiplier):
  if points==1:
    return S
  points = points - 1
  T = (points, (points*multiplier) % (total_pts) )  
  S.append(T)
  return calc(points, total_pts, multiplier)

def draw(sequence, color):
  fig, ax = plt.subplots()
  #bug?
  rad = 1#(len(sequence))/2
  circle = plt.Circle((0, 0), rad, color=color, fill=None, linewidth=0.3)

  # need A points on the circle
  angle = float(360/(len(sequence)))

  # dictionary holding points and marker data
  markers = {}
  for seq in range(len(sequence)):
    x = rad * math.cos(math.radians(seq*angle))
    y = rad * math.sin(math.radians(seq*angle))
    
    #optional: see points
    #point = plt.Circle((x, y), 0.1, color='r', fill=None) ## point on circle.
    #ax.add_artist(point)
    
    # mark the point as the number on the circle for future reference.
    markers.update({seq:[x,y]})
    #print(markers)

  # draw lines mapped sequence (x,y) to marker (z) where 
  for line in sequence:
      x_a = markers.get(line[0], (0,0))
      x_a_o = x_a[0]
      x_b = markers.get(line[1], (0,0))
      x_a_b = x_b[0]

    
      
      y_a = markers.get(line[0], (0,0))
      y_a_o = y_a[1]
      y_b = markers.get(line[1], (0,0))
      y_a_b = y_b[1]


      if (y_a_o) == 0 or (y_a_b) == 0:
          continue
      if (x_a_o) == 0 or (x_a_b) == 0:
          continue
    
      #print([x_a_o,x_a_b], [y_a_o,y_a_b])

      line = plt.Line2D(xdata=[x_a_o,x_a_b], ydata=[y_a_o,y_a_b], linewidth=0.2, color=color)
      ax.add_artist(line)



  # draw circle
  plt.xlim(-1*rad,1*rad)
  plt.ylim(-1*rad,1*rad)
  plt.grid(linestyle='')
  plt.axis('off')
  plt.style.use('dark_background')
  ax.set_aspect(1)
  ax.add_artist(circle)
  

  from datetime import datetime
  #plt.savefig(f"plt_{total_points}_{factor}_{datetime.timestamp(datetime.now())}.png")
  #plt.savefig(f"plt_{total_points}_{factor}.png")
  plt.show()

  #plt.close('all')
  
def run_whaldorf(factor):
  total_points = 200
  color = np.random.rand(3,)
  factor = factor
  A = calc(total_points,total_points,factor)
  draw(A, color)
  print(f'{total_points}, {factor}')
  S.clear()

run_whaldorf(220)

# total_points = 300
# for i in range(2,30):
#   color = np.random.rand(3,)
#   factor = i
#   A = calc(total_points,total_points,factor)
#   draw(A, color)
#   print(f'{total_points}, {factor}')
#   S.clear()