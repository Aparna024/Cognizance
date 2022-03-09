import numpy as np
a = np.arange(12)
print('Initial array:')
print(a)
print('3X4 array:')
print(np.reshape(a, (3,4)))
print('4X3  array:')
print(np.reshape(a, (4,3)))
print('6X2  array:')
print(np.reshape(a, (6,2)))
print('2X6 array:')
print(np.reshape(a, (2,6)))
print("-------------------------------------------------------------------")
d = int(input("Enter the dimension of identity matrix: "))
i = np.identity(d, dtype="int")
print("The identity matrix of order",d,"is:")
print(i)


