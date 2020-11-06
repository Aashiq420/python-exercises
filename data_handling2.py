import numpy as np
import matplotlib.pyplot as plt

#Box plot
a = [1.3, 3.4, 2.3, 9.8]
b= [3.5, 4.6, 1.3, 2.2, ]
c= [9.7, 1.5, 4.3, 0.9, 11.2]
data = [a,b,c]

plt.boxplot(data)
plt.xlabel("College")
plt.ylabel("Marks")
plt.show()

#Scatter plots 
x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])
plt.plot(x,y,'o')

m, b = np.polyfit(x, y, 1)

plt.plot(x, m*x + b)

plt.show()

#Pie chart 
labels = ["Conquerers", "Armament","Perception","Ryuo"]
sizes = [100, 88, 85, 90]
explode = [0.1,0,0,0]

figure, ax_1= plt.subplots()

ax_1.pie(sizes, explode=explode, labels=labels,shadow=True)
ax_1.axis("equal")
plt.show()