import glob
import cPickle as pickle
import matplotlib as mpl
from matplotlib import pyplot
import numpy as np
from sklearn import metrics
import os

cmap = pyplot.get_cmap('Paired')
colors = [cmap(0.8), cmap(0.65), cmap(0.3), cmap(0.45), cmap(0.1)]
methods = ['naive', 'proto', 'hist', 'hedge', 'adapt']
markers = ['+', 'x', 'd', '*', 'o']
set_sizes = np.arange(100, dtype=np.int) + 1
upto = 10

def draw_column(colid, title, legend = False):
    fig = pyplot.figure()
    fig.set_size_inches([6.,4.])
    ax = pyplot.subplot(111)
    for i, method in enumerate(methods):
        data = np.maximum(\
                np.loadtxt('soft/'+method + '.txt.mean')[:, colid],
                np.loadtxt('hard/'+method + '.txt.mean')[:, colid])
        pyplot.plot(set_sizes[:upto], data[:upto],
                    color=colors[i],
                    marker=markers[i],
                    lw=2,
                    label=method)
    pyplot.xlabel('Query Index')
    pyplot.ylabel(title)
    pyplot.grid(True)
    box = ax.get_position()
    #ax.set_position([box.x0, box.y0 + box.height*0.05, box.width*0.85, box.height])
    ax.set_position([box.x0, box.y0 + box.height*0.05, box.width, box.height])
    if legend:
        ax.legend(loc='lower right')
    pyplot.savefig('online_'+title+'.pdf')

draw_column(-1, 'accuracy', legend=False)
draw_column(1, 'overlap_score', legend=True)
pyplot.show()
