import matplotlib.pyplot as plt
font = {'family': 'Times New Roman', 'weight': 'normal', 'size': 15}
def drawChart(x, y):
    for i in range(len(x)):
        plt.plot(x[i], y[i], 'darkblue', linewidth=0.5, label='fault(1)')
    plt.xlim(xmax=90, xmin=0)
    plt.xlabel("Time(second)", font)
    plt.ylabel("Response time(millisecond)", font)
    plt.savefig('f9.svg', dpi=400, bbox_inches='tight')
    plt.show()
    plt.close()
    return


x = [[1,2,3,4,5,6,7,9,10,11,12,13,15,16,17,19,20,21,22,23,24,25,26,27,30,32,33,35,37,38,39,40,41,42,44,45,46,48,49,50,51,52,53,54,55,57,58,60,61,62,63,64,66,68,69,70,71,72,73,74,75,76,77,78,80,81,82,83,85,86,87,88,89,90]]
y = [[200,1600,80,60,100,80,800,90,800,750,100,60,50,45,800,45,60,45,250,44,43,50,49,48,50,60,55,780,50,55,799,56,70,43,1300,50,50,100,80,690,70,870,100,90,1500,70,1450,70,60,1000,70,100,60,990,75,1360,75,80,1500,80,780,100,960,100,800,90,95,100,1490,100,1400,120,950,1230]]



drawChart(x, y)