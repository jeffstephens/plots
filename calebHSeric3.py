import math
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random



fig, ax = plt.subplots()

def circle(radius, points, centerx, centery, transparency, theta = 0, color = 'c', lw = 2):
	r = radius
	t = transparency
	steptheta = 360.0/points
	stepsize = (2.0 * r) / points
	x0 = centerx
	y0 = centery
	vy = [1]
	vx = [1]
	pointsrange = points
	for i in range(pointsrange):
		y = math.sin(math.radians(theta))
		vy.append(r*y+y0)
		x = math.cos(math.radians(theta))
		vx.append(r*x+x0)
		theta = theta + steptheta
	vxf = (vx[1]+vx[-1])/2
	vyf = (vy[1]+vy[-1])/2
	vx.append(vxf)
	vy.append(vyf)
	vx[0] = vxf
	vy[0] = vyf



	plt.plot(vx,vy, c=color, alpha=t, linewidth=lw)

def pentagon(radius, centerx, centery, transparency, theta, color='#800080', lw=5.5):
	r = radius
	t = transparency
	x0 = centerx
	y0 = centery
	circle(r, 5, x0, y0, transparency, theta, color, lw)

def triangle(radius, centerx, centery, transparency, theta, color='#800080', lw=2):
	r = radius
	t = transparency
	x0 = centerx
	y0 = centery
	circle(r, 3, x0, y0, transparency, theta, color, lw)

def circlesq(r, radius2, points, points2, centerx, centery, transparency, theta = 0, color = 'c', lw = 2):
	t = transparency
	steptheta = 360.0/points
	stepsize = (2.0 * r) / points
	x0 = centerx
	y0 = centery
	pointsrange = points + 1
	for i in range(pointsrange):
		y = math.sin(math.radians(theta))
		x = math.cos(math.radians(theta))
		circle(radius2, points2, r*x+x0, r*y+y0, 1.0, theta-180, color, lw)
		theta = theta + steptheta




def drawing(r_):
	r=0.5
	delta=0.025
	for i in range(9):
		circle(r - 9 * delta / 2.0 + i * delta, 200, 0.0, 0.0, 1, lw=0.5)


	r=r_
	delta=0.025
	for i in range(9):
		circle(r - 9 * delta / 2.0 + i * delta, 200, 0.0, 0.0, 1, lw=0.5)


	circlesq(0.4, 0.4, 6, 60, 0, 0, 0.8, 270, '#800080', 2)
	circlesq(1, 0.2, 24, 60, 0, 0, 0.8, 270, '#00529F', 2)

drawing(1.5)





# fig1 = plt.figure(frameon=False)
# ims = []

# for i in range(20):
# 	im = drawing(i * 0.05)
# 	ims.append([im])
# 	plt.clf()
# reversed_arr = ims[::-1]
# imsf = ims + reversed_arr

# im_ani = animation.ArtistAnimation(fig1, imsf, interval=500, repeat_delay=3000,
#     blit=True)
# im_ani.save('eric1.gif', writer='imagemagick')


# import os
# os.system("open -a 'Google Chrome' eric1.gif")










# circle(0.05, 40, 0.0, 0.0, 1, lw=0.5)
# circle(0.055, 40, 0.0, 0.0, 1, lw=0.5)
# circle(0.06, 40, 0.0, 0.0, 1, lw=0.5)
# circle(0.045, 40, 0.0, 0.0, 1, lw=0.5)
# circle(0.04, 40, 0.0, 0.0, 1, lw=0.5)


# circle(0.1, 40, 0.0, 0.0, 1, lw=0.5)
# circle(0.11, 40, 0.0, 0.0, 1, lw=0.5)
# circle(0.105, 40, 0.0, 0.0, 1, lw=0.5)
# circle(0.09, 40, 0.0, 0.0, 1, lw=0.5)
# circle(0.095, 40, 0.0, 0.0, 1, lw=0.5)



# circle(0.3, 120, 0.0, 0.0, 1, lw=1)
# circle(0.4, 120, 0.0, 0.0, 1, lw=1)

# circle(0.9, 120, 0.0, 0.0, 1, lw=1)
# circle(0.8, 120, 0.0, 0.0, 1, lw=1)

# circle(1.3, 120, 0.0, 0.0, 1, lw=1)
# circle(1.4, 120, 0.0, 0.0, 1, lw=1)


# circle(0.6, 40, 0.0, 0.0, 1, lw=5)
# circlesq(0.8, 0.1, 10, 30, 0, 0, 0.8, 270, '#800080', 2)
# circlesq(0.9, 0.1, 10, 3, 0, 0, 0.8, 270, '#FFB6C1', 2)

# circle(1.1, 70, 0.0, 0.0, 1, lw=5)
# circlesq(1.3, 0.1, 20, 30, 0, 0, 0.8, 270, '#800080', 2)
# circlesq(1.4, 0.1, 20, 3, 0, 0, 0.8, 270, '#000033', 2)

# circle(1.6, 90, 0.0, 0.0, 1, lw=5)

# pentagon(5, 0, 0, 0.8, 270, '#FFB6C1')
# pentagon(5.5, 0, 0, 1, 270, '#FFB6C1')
# pentagon(4.5, 0, 0, 0.6, 270, '#FFB6C1')
# pentagon(4, 0, 0, 0.5, 270, '#FFB6C1')
# pentagon(3.5, 0, 0, 0.4, 270, '#FFB6C1')
# pentagon(3, 0, 0, 0.35, 270, '#FFB6C1')
# pentagon(2.5, 0, 0, 0.3, 270, '#FFB6C1')
# pentagon(2, 0, 0, 0.25, 270, '#FFB6C1')
# pentagon(1.5, 0, 0, 0.2, 270, '#FFB6C1')
# pentagon(1, 0, 0, 0.15, 270, '#FFB6C1')

# pentagon(5, 0, 0, 0.2, 90)
# pentagon(5.5, 0, 0, 0.15, 90)
# pentagon(4.5, 0, 0, 0.25, 90)
# pentagon(4, 0, 0, 0.3, 90)
# pentagon(3.5, 0, 0, 0.35, 90)
# pentagon(3, 0, 0, 0.4, 90)
# pentagon(2.5, 0, 0, 0.5, 90)
# pentagon(2, 0, 0, 0.6, 90)
# pentagon(1.5, 0, 0, 0.8, 90)
# pentagon(1, 0, 0, 1, 90)

# triangle(5, 0, 0, 0.2, 0, "#000033", 4)
# triangle(5.5, 0, 0, 0.15, 0, "#000033", 4)
# triangle(4.5, 0, 0, 0.25, 0, "#000033", 4)
# triangle(4, 0, 0, 0.3, 0, "#000033", 4)
# triangle(3.5, 0, 0, 0.35, 0, "#000033", 4)
# triangle(3, 0, 0, 0.4, 0, "#000033", 4)
# triangle(2.5, 0, 0, 0.5, 0, "#000033", 4)
# triangle(2, 0, 0, 0.6, 0, "#000033", 4)
# triangle(1.5, 0, 0, 0.8, 0, "#000033", 4)
# triangle(1, 0, 0, 1, 0, "#000033", 4)


# circle(1.0, 40, 0.0, 0.0, 1)
# circle(0.5, 60, 0.2, 0.3, 1)
# circle(1.5, 90, 0.1, -1.0, 1)



# circle(0.2, 90, -0.1, 2.0, 1)
# circle(0.1, 90, -0.6, 1.5, 1)
# circle(0.15, 90, 0.8, 1.4, 1)
# circle(0.2, 90, -0.5, 1.0, 1)
# circle(0.1, 90, 0.69, 1.2, 1)
# circle(0.15, 90, 0.1, 1.5, 1)
# circle(0.2, 90, -1.1, 3.0, 1)
# circle(0.1, 90, -1.6, 2.5, 1)
# circle(0.15, 90, 0.3, 2.4, 1)
# circle(0.2, 90, -1.5, 3.2, 1)
# circle(0.1, 90, 0.49, 2.2, 1)
# circle(0.15, 90, 0.2, 2.5, 1)



# circle(0.1, 90, -0.6, 2.0, 1)
# circle(0.08, 90, 0.49, 2.2, 1)
# circle(0.06, 90, 0.1, 2.5, 1)
# circle(0.09, 90, -0.7, 2.8, 1)
# circle(0.08, 90, -0.39, 2.7, 1)
# circle(0.06, 90, 0.5, 2.9, 1)

# for i in range(10):
# 	circle(0.07 -random.randint(0,10)/500.0, 90, 
# 		0.7-random.randint(0,10)/10.0, 2.8 + i/2.0 -random.randint(0,10)/10.0, 1)
# 	circle(0.08 -random.randint(0,10)/500.0, 90, 
# 		0.39-random.randint(0,10)/10.0 - (i/5.0)*(i/10.0)*math.sqrt(i/10.0), 2.7 + i/2.0 -random.randint(0,10)/10.0, 1)
# 	circle(0.09 -random.randint(0,10)/500.0, 90, 
# 		0.5-random.randint(0,10)/5.0 - (i/5.0)*(i/10.0)*math.sqrt(i/10.0), 2.9 + i/2.0 -random.randint(0,10)/10.0, 1)
	
# 	circle(0.08 -random.randint(0,10)/500.0, 90, 
# 		0.39-random.randint(0,10)/5.0 - (i/5.0)*math.sqrt(i/10.0), 2.7 + i/2.0 -random.randint(0,10)/10.0, 1)
# 	circle(0.09 -random.randint(0,10)/500.0, 90, 
# 		0.5-random.randint(0,10)/5.0 - (i/5.0)*math.sqrt(i/10.0), 2.9 + i/2.0 -random.randint(0,10)/10.0, 1)
	
# 	circle(0.08 -random.randint(0,10)/500.0, 90, 
# 		0.39-random.randint(0,10)/10.0 - math.sqrt(i/10.0), 2.7 + i/2.0 -random.randint(0,10)/10.0, 1)
# 	circle(0.09 -random.randint(0,10)/500.0, 90, 
# 		0.5-random.randint(0,10)/10.0 + math.sqrt(i/10.0), 2.9 + i/2.0 -random.randint(0,10)/10.0, 1)









#-----------------------------
#NOTES
#-----------------------------


# to comment out a highlighted selection:
# press "command + ?" 







ax.axis('off')

fig.gca().set_aspect('equal', adjustable='box')
fig.savefig("Pattern7.pdf")


import os
os.system("open Pattern7.pdf")