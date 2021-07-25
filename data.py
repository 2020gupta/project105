import csv
import math
with open("data.csv",newline="")as f:
    df=csv.reader(f)
    data=list(df)
data=data[0]
def mean(data):
    n=len(data)
    total=0
    for i in data:
        total+=int(i)
    mean=total/n
    return mean
squareList=[]
for i in data:
    a=int(i)-mean(data)
    a=a**2
    squareList.append(a)
sum=0
for i in squareList:
    sum=sum+i
result=sum/(len(data)-1)
std=math.sqrt(result)
print(std)