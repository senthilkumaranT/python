### Sum of numbers in a given range



starting  = int(input())
ending = int(input())
sum=0

for i in range(starting ,ending+1):
    sum+=i
print(sum)