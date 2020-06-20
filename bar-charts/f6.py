import matplotlib.pyplot as plt
font = {'family': 'Times New Roman',  'size': 15}
name_list = ['Search Request', 'Product Detail', 'Buy Request', 'Buy Confirm']
num_list = [8, 4, 13, 11]

x = list(range(len(num_list)))
width = 0.5

plt.bar(x, num_list, width=width, tick_label=name_list, fc='darkblue', edgecolor='black')
#plt.legend(prop={'family': 'Times New Roman'})
plt.xticks(fontproperties= 'Times New Roman', size = 15)
plt.yticks(fontproperties= 'Times New Roman', size = 15)
plt.xlabel("Microservice", font)
plt.ylabel("Number of execution traces", font)
plt.ylim(ymax=14, ymin=0)
plt.savefig( 'f6.svg', bbox_inches='tight')
plt.show()