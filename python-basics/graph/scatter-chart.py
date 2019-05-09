import matplotlib.pyplot as plt
import matplotlib.style as style

# For adding style in graph
style.use('ggplot')

x = [5,7,3,6,9,1]
y = [2,4,5,8,7,3]

plt.ylabel('Y Axis')
plt.xlabel('X Axis')
plt.title('Sample Scatter Chart')
plt.legend()
#plt.grid(True, color='K')

plt.scatter(x, y, label='Scatter Graph', color='k', s=25, marker='o')

plt.show()