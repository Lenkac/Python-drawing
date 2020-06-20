#
import matplotlib.pyplot as plt
font = {'family': 'Times New Roman', 'size': 15}
name_list = ['Search Request', 'Product Detail', 'Buy Request', 'Buy Confirm']
num_list = [9, 8, 48, 80]
num_list1 = [9, 8, 50, 85]

x = list(range(len(num_list)))
total_width, n = 0.4, 2
width = total_width / n

plt.bar(x, num_list, width=width, label='Before instrumentation', fc='darkblue', edgecolor='black')
for i in range(len(x)):
    x[i] = x[i] + width + 0.1
plt.bar(x, num_list1, width=width, label='After instrumentation', tick_label=name_list, fc='yellow', edgecolor='black')
plt.legend(prop={'family': 'Times New Roman', 'size': 15})
plt.yticks(fontproperties='Times New Roman', size=15)
plt.xticks(fontproperties='Times New Roman', size=15)
plt.ylim(ymax=90, ymin=0)
plt.xlabel("Microservice", font)
plt.ylabel("Average respond time(millisecond)", font)
plt.savefig( 'f.svg', bbox_inches='tight')
plt.show()