# Projectile Motion Computer Program
In this project, a projectile motion computer program is built using Python 3. The program requires 3 inputs and it finds the other points of the parabola with a close approximation using the background calculations. For drawing a parabola, 3 points are needed. That’s why, the program asks the user to enter the initial height of the object, the maximum height of the object, and the range. With the input values and the calculated points, the program draws the projectile motion graph of an object and using the kinematic formulas, it finds the unknown parameters.

## Projectile Motion Equations
To find the unknown parameters related to projectile motion, certain equations of motion are used. With knowing at least three points, all the other unknowns can be found using the kinematics formulas. 
These equations are:
*𝑣f=𝑣0+a𝑡
Δx=𝑣0𝑡+1/2a𝑡2
Δy=𝑣0𝑡+1/2a𝑡2
𝑣f2=𝑣02+2aΔx
𝑣f2=𝑣02+2aΔy*


## How?
The program first asks four questions to the user. These questions are:
*“Enter the initial height(in meters):”*
*“Enter the maximum height(in meters):”*
*“Enter the final height(in meters):”*
*“Enter the range(in meters):”*
Next, the program calculates the unknown projectile motion variables using the kinematics formulas. The calculated values are:
*Launch Angle (α0)
Flight Duration (t)
Initial Vertical Velocity (V0y)
Initial Horizontal Velocity (V0x)
Initial Velocity (V0)
Final Vertical Velocity (Vfy)
Final Horizontal Velocity (Vfx)
Final Velocity (Vf)
Time to Reach Max. Height (th)*
The program prints the found values. Meanwhile, the Height vs Range graph is generated. The user can zoom in and out. The graph can be saved as a png file, and as the mouse arrow goes through the graph, each coordinate on the graph is shown. In figure 5/6, an example output can be seen.


## Code.
The code is written in Python.  Functions for calculating the points are defined. When the input is entered, the program calculates the other points on the graph with the function “ap,bp,cp,a1,b1,c1=calc_parabola_vertex(x1, y1, x2, y2, x3, y3)” using the equation y=ax^2+bx+c. After the x and v values are defined, the unknown variables of projectile motion is found with several functions such as: 

*teta=math.atan(bp)*180/pi;
T0Th=math.sqrt((y2-y1)*2/g);
Tfly=T0Th+math.sqrt((y2-y3)*2/g);
Voy=math.sqrt((y2-y1)*2/g)*g;*

Certain values (g and π) are defined beforehand to make the process easier. After the projectile motion variables are calculated, they are printed, so the user can see all the unknown values.

*print("Launch Angle (α0): " + str(teta))
print("Flight Duration (t): " + str(Tfly))
By using the matplot library, the parabola is plotted.
import matplotlib.pyplot as plt
fig = plt.figure()*

The three input coordinates are marked with dots for easier use. 

*plt.scatter(x_pos, y_pos, color='gray') # parabola points
plt.scatter(x1,y1,color='r',marker="D",s=50) # 1st known xy
plt.scatter(x2,y2,color='g',marker="D",s=50) # 2nd known xy
plt.scatter(x3,y3,color='k',marker="D",s=50) # 3rd known xy*


The complete code can be found in the repository.





