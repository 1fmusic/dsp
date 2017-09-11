# Matrix Algebra


# Do not change these variables
import numpy as np
from numpy import linalg as la

A = np.array([[1,2,3],[2,7,4]])
B = np.array([[1,-1],[0,1]])
C = np.array([[5,-1],[9,1],[6,0]])
D = np.array([[3,-2,-1],[1,2,3]])

u = np.array([6,2,-3,5])
v = np.array([3,5,-1,4])

AT =np.transpose(A)
E = np.transpose(C)
DT = np.transpose(D)


# Q1: record the dimensions of A, B, C, D, u, v respectively in the dict below. 
#     Do not type the answers, make python do the work



dimensions = { 
        'A': A.shape,
        'B': B.shape,
        'C': C.shape,
        'D': D.shape,
        'u': u.shape,
        'v': v.shape
        }


# Q2: vector operations
#     assign `None` if the operation is not defined
#     do not type the answers, make python do the work
alpha = 6

u_plus_v =   u + v          # u+v [9, 7, -4, 9]
u_minus_v =  u - v          # u-v  [3, -3, -2, 1]
alpha_times_u = alpha * u  # alpha * u,[36, 12, -18, 30]
u_dot_v =  np.dot(u, v)            # [51]  u . v
norm_u = la.norm(u)            # 8.60   ||u|| 


# Q3: compute the following and assign to variables below:
#     assign `None` if the operation is not defined
#     do not type the answers, make python do the work

A_plus_C =     None         # A + C
A_minus_Ctranspose = A.__sub__(E)  # {[-4	-7	-3},[3	6	4}}
Ctranspose_plus_3D = E.__add__(3*D) #([[14,3,3],[2,7,9]]) C.T + 3*D
B_times_A = B.__matmul__(A)  # ([[-1,-5,-1],[2,7,4]]) B*A
B_times_Atranspose =  None  # B*A.T

# Q4: (bonus)

B_times_C = None # B*C
C_times_B = C.__matmul__(B)     # ([[5, -6],[9,-8],[6,-6]]) C*B
B_exp_4 =  B_exp_4 =  la.matrix_power(B,4)    # ([[1,-4],[0,1]])  B^4
A_times_Atranspose = A.__matmul__(AT)   # ([[14,28],[28, 69]])  A*A.T
Dtranspose_times_D = DT.__matmul__(D)   #([[10,-4,0],[-4,8,8],[0,8,10]]) D.T*D


