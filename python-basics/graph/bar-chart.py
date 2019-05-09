import matplotlib.pyplot as plt
import matplotlib.style as style

# For adding style in graph
style.use('ggplot')

x1 = [5,8,9,10]
y1 = [2,5,7,5]

x1 = [5,8,9,10]
y1 = [2,5,7,5]
x2 = [4,6,8,10]
y2 = [3,5,7,9]

#plt.bar(x1, y1, label='Data 1', color='b')
# If you wish to add multiple bar in graph
plt.bar(x2, y2, label='Data 2', color='g')

plt.ylabel('Bar No')
plt.xlabel('Bar Height')
plt.title('Sample Bar Chart')

plt.legend()
plt.grid(True, color='K')

plt.show()