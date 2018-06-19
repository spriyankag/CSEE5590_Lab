import numpy as np
import matplotlib.pyplot as plt
#Created 2 arrays with 2 variables
x=np.array([0,1,2,3,4,5,6,7,8,9])
y=np.array([1,3,2,5,7,8,8,9,10,12])
#calculated mean
meanx=np.mean(x)
meany=np.mean(y)

#sum of the means
num=np.sum((x-meanx)*(y-meany))
den=np.sum(pow((x-meanx),2))
m=num/den
#slope calculation
intercept=meany-(m*meanx)
val=(m*x)+intercept
plt.plot(x,y)
plt.plot(x,val)
plt.show()