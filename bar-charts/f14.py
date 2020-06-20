#
import matplotlib.pyplot as plt
font = {'family': 'Times New Roman',  'size': 34}
name_list = ['CPU hog', 'Network congestion', 'Memory leak', 'Service failure']
num_list = [89, 93, 82, 97]
num_list1 = [94, 83, 75, 98]

x = list(range(len(num_list)))
#y = range(70, 105, 5)
total_width, n = 0.8, 2
width = total_width / n

plt.bar(x, num_list, width=width, label='Precision', fc='darkblue', edgecolor='black')
for i in range(len(x)):
    x[i] = x[i] + width
plt.bar(x, num_list1, width=width, label='Recall', tick_label=name_list, fc='yellow', edgecolor='black')
plt.legend(prop={'family': 'Times New Roman', 'size': 34})
plt.xticks(fontproperties='Times New Roman', size=34)
plt.yticks(fontproperties='Times New Roman', size=34)
#plt.yticks(y)
plt.ylim(ymax=100, ymin=0)
plt.xlabel("Fault type", font)
plt.ylabel("Precision & recall(%)", font)
plt.savefig('f14.svg', dpi=400, bbox_inches='tight')
plt.show()