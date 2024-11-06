import matplotlib.pyplot as plt
overs=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
runs=[6,12,13,14,17,18,22,24,26,6,8,9,6,22,23,6,7,8,9,12]
plt.plot(overs,runs,marker='X',markerfacecolor='blue',markersize=8,linestyle='dashed',linewidth=2,color='red')
plt.xlabel("overs",color='blue')
plt.ylabel("runs",color='red')
plt.title("Yashaswini TM-1KI23CS187")
plt.show()