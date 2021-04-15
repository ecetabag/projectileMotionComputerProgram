#ecetabag2021

import math
def calc_parabola_vertex(x1, y1, x2, y2, x3, y3):
		'''
http://stackoverflow.com/questions/717762/how-to-calculate-the-vertex-of-a-parabola-given-three-points
		'''

#calculating the points
		a1 = 1;
		b1 =  -(4*y2-4*y1)/x3;
		c1 =  -(4*y2-4*y1)*y1/(x3*x3)+(4*y2-4*y1)*y3/(x3*x3);
		kok1 = (-b1+math.sqrt(((b1*b1)-4*a1*c1)))/(2*a1);
		kok2 =(-b1-math.sqrt(((b1*b1)-4*a1*c1)))/(2*a1);
		ap =(+y3-kok1*x3-y1)/(x3*x3);
		bp = kok1;
		cp =y1;



		return ap,bp,cp, a1,b1,c1
            
	    


#taking input for the known 3 points. 
print('Enter the initial height(in meters):')
input_y1 = input()
input_y1 = int(input_y1)
y1 = input_y1
x1 = 0


print('Enter the maximum height(in meters):')
input_y2 = input()
input_y2 = int(input_y2)
y2 = input_y2
x2 = 15

print('Enter the final height(in meters): ')
input_y3 = input()
input_y3 = int(input_y3)
y3 = input_y3


print('Enter the range(in meters): ')
input_x3 = input()
input_x3 = int(input_x3)
x3 = input_x3



#calculating the unknowns points from the equation y=ax^2+bx+c
ap,bp,cp,a1,b1,c1=calc_parabola_vertex(x1, y1, x2, y2, x3, y3)

#finding the second known point's x coordinate
x2 = -bp/(2*ap)

#defining the x range for the parabola
import numpy as np

x_pos=np.arange(y3,x3,0.01)

y_pos=[]



#calculate y values 
for x in range(len(x_pos)):
    x_val=x_pos[x]
    y=(ap*(x_val**2))+(bp*x_val)+cp
    y_pos.append(y)

#finding the other values
g=9.81
pi = 3.14
#xpeak=-(-b1+math.sqrt((b1*b1-4*a1*c1)))/(2*a1)/(2*ap);
teta=math.atan(bp)*180/pi;
T0Th=math.sqrt((y2-y1)*2/g);
Tfly=T0Th+math.sqrt((y2-y3)*2/g);
Voy=math.sqrt((y2-y1)*2/g)*g;
Vox=(-x1+x3)/Tfly;
Vegik=math.sqrt(Voy*Voy+Vox*Vox);
Vfy = -(math.sqrt((y2-y3)*2/g)*g)
Vfx = (-x1+x3)/Tfly;
Vf = math.sqrt(Vfx*Vfx+Vfy*Vfy);

#printing the found values
print("Launch Angle (α0): " + str(teta))
print("Flight Duration (t): " + str(Tfly))
print("Initial Vertical Velocity (V0y): " + str(Voy))
print("Initial Horizontal Velocity (V0x): " + str(Vox))
print("Initial Velocity (V0): " + str(Vegik))
print("Final Vertical Velocity (Vfy): " + str(Vfy))
print("Final Horizontal Velocity (Vfx): " + str(Vfx))
print("Final Velocity (Vf): " + str(Vf))
print("Time to Reach Max. Height (th): " + str(T0Th))




# plotting the parabola
import matplotlib.pyplot as plt
fig = plt.figure()



ax = fig.add_subplot(111)

ymax = y2
xmax = x2

ax.annotate('max height', xy=(xmax, ymax), xytext=(xmax, ymax+5),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )
plt.ylabel('height')
plt.xlabel('range')

plt.plot(x_pos, y_pos, linestyle='dotted', color='black') # parabola line
plt.scatter(x_pos, y_pos, color='gray') # parabola points
plt.scatter(x1,y1,color='r',marker="D",s=50) # 1st known xy
plt.scatter(x2,y2,color='g',marker="D",s=50) # 2nd known xy
plt.scatter(x3,y3,color='k',marker="D",s=50) # 3rd known xy
plt.gca().set_ylim(bottom=0)
plt.gca().set_xlim(left=0)



plt.show()




