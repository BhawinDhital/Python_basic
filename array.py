#matrix multiplication using np.array
import numpy as np
import math
from math import acos

#p_l = 55,p_h = 455,p_l/p_h = 0.120879121, p_h/p_l = 8.27272727
#M_ler = [- 0.0956692(M11),- 6.59303601(M12), 0.17944340(M21), 1.91364372(M22): x, x']
#M_her = [ 0.03643061(M11), 6.27719597(M12), - 0.17017192(M21), -1.87211828(M22): x, x']
#These values are given by elegant

M_ler = A = np.array([[- 0.09566924955456843,- 6.593036012965720],\\
[0.179443409212927,1.913643726511682]])
M_phase = z = np.array([[- 1.90669118353,- 6.55612783643],\\
[0.1777336225,0.0866655623848]])
Mcav_acc = B = np.array([[1,0],[0,0.120879121]])
M_her = C = np.array([[0.03643061257738980,6.277195977004854],\\
[- 0.1701719079712370,-1.872118289842428]])
Mcav_dec = D = np.array([[1,0],[0,8.27272727]])
a = np.dot(z, A)
b = np.dot(B, a)
c = np.dot(C, b)
X = np.dot(D,c)

#a = B.dot(A)
#b = C.dot(a)
#X = D.dot(b)
print"One loop-transfer map:\n",(X)
print"Determinant:",(np.linalg.det(X))
Y =np.trace(X)
print"Diagonal_sum(Trace):",Y
y = Y/2
print"Trace divide by 2:",y
