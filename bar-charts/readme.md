#Some common functions and instances in bar-charts drawing.

#to limit the range of y-axis from 0 to 100

plt.ylim(ymax=100, ymin=0)

#to limit the range of x-axis from 0 to 100

plt.xlim(xmax=100, xmin=0)

#a function used for generating a legend and set the format

plt.legend(prop={'family': 'Times New Roman', 'size': 34})

#a function used for drawing bars

#fc means the color of the bar, label is used to generate legend.

plt.bar(x, num_list, width=width, label='Precision', fc='darkblue', edgecolor='black')

#the two functions in the following are used for setting format for the ticks

plt.xticks(fontproperties='Times New Roman', size=34)

plt.yticks(fontproperties='Times New Roman', size=34)
