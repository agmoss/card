import scipy.special
import matplotlib.pyplot as plt
import pylab
import numpy as np
import matplotlib.cm as cm

if __name__ == "__main__":

    fig, ax = plt.subplots()
    fig.set_size_inches(3.5, 2, forward=True)

    # Remove the plot frame lines
    ax.spines["top"].set_visible(False)    
    ax.spines["bottom"].set_visible(True)    
    ax.spines["right"].set_visible(False)    
    ax.spines["left"].set_visible(True)  

    # Text
    ax.text(45,0.7, 'Andrew Moss',fontsize=12,style = 'oblique',horizontalalignment='right')
    ax.text(45,0.45, 'W: m0ss.dev',fontsize=8,horizontalalignment='right')
    ax.text(45,0.35, 'E: andrew@m0ss.dev',fontsize=8,horizontalalignment='right')
    ax.text(45,0.2, 'P: 403 690 2015',fontsize=8,horizontalalignment='right')

    # Plot Chi square survival function
    color=iter(cm.winter(np.linspace(0,1,10)))
    x = np.linspace(0,50,500)
    for i in range(10):
        c=next(color) 
        ax.plot(x,scipy.special.chdtrc(i,x),c=c)

    fig.tight_layout()
    plt.show()
