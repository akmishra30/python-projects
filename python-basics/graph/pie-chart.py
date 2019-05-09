import matplotlib.pyplot as plt
import matplotlib.style as style

# For adding style in graph
style.use('ggplot')

pie_slices = [15, 8, 23, 2, 35, 16, 19]
pie_cars = ['Tata Motors', 'Suzuki', 'Hundai', 'Honda', 'Toyota', 'Volkswagen', 'Ford']
slices_col = ['b', 'g', 'r', 'c', 'm', 'y', 'w']


plt.title('Sample Pie Chart')
plt.pie(
    pie_slices,
    labels= pie_cars,
    colors= slices_col,
    startangle=90,
    shadow=True,
    explode=None,
    autopct='%1.1f%%'
)

plt.show()