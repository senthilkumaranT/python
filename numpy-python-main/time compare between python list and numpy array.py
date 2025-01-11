import numpy as np 
import time 


SIZE=100000

b1=range(SIZE)
b2=range(SIZE)


a1=np.arange(SIZE)
a2=np.arange(SIZE)


#checking list timing 
start=time.time()
result=[x+y for x,y in zip(b1,b2)]
print("time of python list ",(time.time()-start)*1000 )


start=time.time()
result=a1+a2
print("time of numpy ",(time.time()-start)*1000 )