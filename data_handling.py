import matplotlib.pyplot as plt
import numpy as np

#******************************************************************
# cities=['East London', 'Cape Town', 'Kimberley', 'Durban']
# rainfall= [140,  200, 120, 157]
# x_pos = [i for i, _ in enumerate(cities)] #labels on the x-axis
# #labeling and visuals
# plt.bar(x_pos, rainfall, color='green')
# plt.xlabel("Cities")
# plt.ylabel("Rainfall in (mm)")
# plt.title("Rainfall for the 4 main cities in SA")
# plt.xticks(x_pos, cities)
# plt.show()
#******************************************************************

from scipy import stats
test_scores = [12,99,65,85,42]
test_names = ["Andy", "Martin", "Zahara", "Vuyo","Ziyaad" ]
x_pos = [i for i, _ in enumerate(test_names)]

plt.bar(x_pos, test_scores, color='blue')
plt.xlabel("Names")
plt.ylabel("Marks (%)")
plt.title("Marks for 5 students")
plt.xticks(x_pos, test_names)
plt.show()

Testmarks = [98,78, 68, 73, 72, 97, 88, 60, 94, 95, 80, 73, 82, 80, 99, 91, 74, 88, 70, 94, 86, 81, 100, 99, 84, 93, 94, 79]
meanmarks= np.mean(Testmarks) #calculating mean
medianmark=np.median(Testmarks) # calculating median
modemarks=stats.mode(Testmarks) #calculating mode (value with highest frequencies)

print(meanmarks,medianmark,modemarks)