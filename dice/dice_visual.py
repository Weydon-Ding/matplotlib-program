import pygal

from dice import Dice

dice_1 = Dice()
dice_2 = Dice()

results = []
for roll_num in range(1000):
	result = dice_1.roll() + dice_2.roll()
	results.append(result)

frequencies = []
max_result = dice_1.num_sides + dice_2.num_sides
for value in range(2,max_result+1):
	frequency = results.count(value)
	frequencies.append(frequency)

hist = pygal.Bar()

hist.title = "Result of rolling two D6 1000 times."
hist.x_labels = ['2','3','4','5','6','7','8','9','10','11','12']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6',frequencies)
hist.render_to_file('dice_visual.svg')
