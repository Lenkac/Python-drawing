import matplotlib.pyplot as plt
font = {'family': 'Times New Roman', 'weight': 'normal', 'size': 15}
def drawChart(x, y, z, h, a, b, c, d):
    for i in range(len(x)):
        plt.plot(x[i], y[i], '--', color='blue',  linewidth=0.5, marker='x', mew=1, ms=4, label='Product Detail')
    for i in range(len(z)):
        plt.plot(z[i], h[i], '-.',  color='black', linewidth=0.5, marker='D', mew=1, ms=4,mfc='white', label='Buy Request')
    for i in range(len(a)):
        plt.plot(a[i], b[i], color='black', linewidth=0.5, marker='*', mew=1, ms=4,mfc='red', label='Search Request')
    for i in range(len(c)):
        plt.plot(c[i], d[i], ':', color='black',linewidth=0.5, marker='o', mew=1, ms=4,mfc='white', label='Buy Confirm')
    plt.ylim(ymax=1.01, ymin=0.2)
    plt.xlim(xmax=13, xmin=0.99)
    plt.legend(prop={'family': 'Times New Roman', 'size': 15}, loc=4)
    plt.xlabel("Number of execution traces", font)
    plt.ylabel("Cumulative proportion", font)
    plt.savefig('f12.svg', dpi=400, bbox_inches='tight')
    plt.show()
    plt.close()
    return


x = [[1,2,3,4]]
y = [[0.72,0.89,0.95,1]]
z = [[1,2,3,4,5,6,7,8,9,10,11]]
h = [[0.44,0.74,0.84,0.9,0.94,0.95,0.97,0.98,0.99,1,1]]
a = [[1,2,3,4,5,6,7,8]]
b = [[0.41,0.67,0.83,0.86,0.9,0.98,0.99,1]]
c = [[1,2,3,4,5,6,7,8,9,10,11,12,13]]
d = [[0.3,0.54,0.72,0.78,0.83,0.88,0.9,0.92,0.95,0.97,0.98,1,1]]
#marker = ['o']


drawChart(x, y, z, h, a, b, c, d)
#drawChart(x, y, z, h)
