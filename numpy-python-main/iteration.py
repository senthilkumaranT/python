import numpy as np

num = np.array([[6, 7, 8], [1, 2, 3], [9, 3, 2]])

# to print the row 
for row in num:
    print(row)


#flat
for cell in num.flat:
    print(cell)
    

a=np.arange(6).reshape(3,2)
b=np.arange(6,12).reshape(3,2)

print(np.vstack((a,b)))


print(np.hstack((a,b)))
