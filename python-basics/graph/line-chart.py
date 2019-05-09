import matplotlib.pyplot as plt
import matplotlib.style as style

# For adding style in graph
style.use('ggplot')

x1 = [5,8,9,10]
y1 = [2,5,7,5]
x2 = [4,6,8,10]
y2 = [3,5,7,9]

plt.plot(x1, y1, 'g', label='Open Line', linewidth=2, color='B')
# If you wish to add multiple line in graph
plt.plot(x2, y2, 'g', label='Close Line', linewidth=2, color='R')

plt.ylabel('Open')
plt.xlabel('Close')
plt.title('Stock Movement')

plt.legend()
plt.grid(True, color='K')

plt.show()