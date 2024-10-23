import matplotlib.pyplot as plt
import numpy as np
X=np.linspace(1,20,5)
y1=X
y2=np.square(X)
y3=np.sqrt(X)
print(y1)
print(y2)
print(y3)
plt.plot(X,y1,'r',X,y2,'g',X,y3,'b')
plt.legend(['x','square-X','sqrt-x'])
plt.xticks(X)
plt.yticks(y3)
plt.title("Linear_Yashaswini TM-1KI23CS187")
plt.show()
