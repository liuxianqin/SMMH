from die import Die
import pygal
die_1=Die()
die_2=Die()
results=[]
for rool_num in range(100000):
	result=die_1.roll()+die_2.roll()
	results.append(result)
frequencies=[]
max_result=die_1.num_sides+die_2.num_sides
for value in range(2,max_result+1):
	frequence=results.count(value)
	frequencies.append(frequence)
print(frequencies)

hist=pygal.Bar()
hist.title="Result of rolling 2 D6 dice 1000 times"
hist.x_labels=['2','3','4','5','6','7','8','9','10','11','12']
hist.x_title="Result"
hist.y_title="Frequence"
hist.add('D6+D6',frequencies)
hist.render_to_file('dice_visual.svg')
