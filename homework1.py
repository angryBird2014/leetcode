import numpy as np
import matplotlib.pyplot as plt

def plotshow():
    data = np.array([[2,2],[4,4],[4,0],
                    [0, 0], [2, 0], [0, 2]
                     ])
    label = np.array([1,1,1,-1,-1,-1])

    plt.scatter(data[::,0],data[::,1],c=label)
    plt.show()

if __name__ == '__main__':
    plotshow()