
import numpy as np 

#one dimension array 
a=np.array([1,2,3])
print(a)

# two dimension array 
b=np.array([[1,2],[3,4]])
print(b[0][0])


#to find which dimension 
print(b.ndim)

# data type 

print(b.dtype)

# represent the dimension
print(b.shape)

#reshape
print(b.reshape(4,1))

#flaten your array 
print(b.ravel())

#min max sum 
print(b.max(),b.max(),b.sum())

#linear space 
print(np.linspace(1,5,10))