from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

#Create 3 dice
die_1, die_2 = Die(), Die()


#Make some rolls, and store result in a list
results = [die_1.roll() + die_2.roll() for roll_num in range(1_000)]

#Analyse the results
max_results = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range (2, max_results+1)]

#Visualise the results
x_values = list(range(2, max_results+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title':'Result', 'dtick':1}
y_axis_config = {'title':'Frequency of Result'}
my_layout = Layout(title = 'Results of rolling two D6 dice 1_000 times',
		xaxis = x_axis_config, yaxis = y_axis_config)
offline.plot({'data':data, 'layout':my_layout}, filename='d6_d6.html')