import matplotlib.pyplot as plt

# Define the specific values of n
n_values = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
x_values = [20 - n for n in n_values]

# Create a stem plot for the specified values
plt.stem(n_values, x_values, linefmt='-', markerfmt='o', basefmt=' ')

# Add labels and title
plt.xlabel('n')
plt.ylabel('x(n)')
plt.title('Stem Plot for x(n) = 20 - n at n=0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24')
plt.savefig('f2.png')
# Display the plot
plt.show()
