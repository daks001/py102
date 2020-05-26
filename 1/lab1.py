from sympy import *
from sympy.plotting import (plot, plot_parametric, plot3d_parametric_surface, plot3d_parametric_line, plot3d)

#problem 1
F=Matrix([10,18])
P=Matrix([1,3])
Q=Matrix([11,8])
#part (a)
D=Q-P
print("Displacement vector D is:", D)
#part (b) (i)
w=F[0,0]*D[0,0]+F[1,0]*D[1,0]
print("Work done, using component formula is:", w)
#part (b) (ii)
w=F.dot(D)
print("Work done using python's dot command is:", w)

#problem 2
C=Matrix([[-cos (65) , cos (25)] ,
          [sin (65) , sin (25)]])
