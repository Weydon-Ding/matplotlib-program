import matplotlib.pyplot as plt

input_values = []
squares = []
num = 1

while num <=5:
	input_values.append(num)
	num2 = num ** 2
	squares.append(num2)
	num += 0.1

plt.plot(input_values,squares,linewidth=5)
plt.title("Square Numbers",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)
plt.tick_params(axis='both',labelsize=14)
plt.show()
