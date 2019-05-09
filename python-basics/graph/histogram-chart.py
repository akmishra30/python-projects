import matplotlib.pyplot as plt
import matplotlib.style as style

# For adding style in graph
style.use('ggplot')

ages = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]
pop_ages = [22, 25, 30, 12, 46, 80, 57, 87, 56, 39, 40, 49, 68, 103, 123, 18, 79]

plt.ylabel('Y Axis')
plt.xlabel('X Axis')
plt.title('Sample Histogram Chart')
plt.legend()
#plt.grid(True, color='K')

plt.hist(pop_ages, ages, histtype='bar', rwidth=0.8, color='B')

plt.show()