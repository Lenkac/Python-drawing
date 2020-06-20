import matplotlib.pyplot as plt
font = {'family': 'Times New Roman',  'size': 15}
name_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']
num_list = [0.5, 0.7, 0.55, 1.05, 1.3, 0.65, 0.86, 0.3, 0.9, 0.32, 0.22, 0.5, 0.32]

x = list(range(len(num_list)))
width = 0.7

plt.bar(x, num_list, width=width, tick_label=name_list, fc='darkblue', edgecolor='black')
#plt.legend(prop={'family': 'Times New Roman'})
plt.xticks(fontproperties= 'Times New Roman', size = 15)
plt.xlabel("Execution traces of Buy Confirm", font)
plt.ylabel("Anomaly Degree", font)
plt.ylim(ymax=1.4, ymin=0)
plt.savefig('f8.svg', dpi=400, bbox_inches='tight')
plt.show()