import matplotlib.pyplot as plt
font = {'family': 'Times New Roman', 'weight': 'normal', 'size': 15}
def drawChart(x, y):
    for i in range(len(x)):
        plt.plot(x[i], y[i], 'black', linewidth=0.5, marker='o', mew=1, ms=4,mfc='white', label='fault(1)')
    plt.xlabel("Number of components", font)
    plt.ylabel("Ratio of the principle components(%)", font)
    plt.ylim(ymax=70)
    plt.xlim(xmax=60)
    plt.savefig('f10.svg', dpi=400, bbox_inches='tight')
    plt.show()
    plt.close()
    return


x = [[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59]]
y = [[65,26,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
#marker = ['o']


drawChart(x, y)