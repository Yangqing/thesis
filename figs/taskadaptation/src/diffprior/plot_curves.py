import glob
import cPickle as pickle
import matplotlib as mpl
from matplotlib import pyplot
import numpy as np
from sklearn import metrics
import os

cmap = pyplot.get_cmap('Paired')
colors = [cmap(0.1), cmap(0.65)]
methods = ['erlang', 'flat']
linestyles = ['-', '--']
markers = ['o','*']
set_sizes = [1,2,5,10,20,50,100,200,500]

def draw_column(colid, title, legend = False):
    fig = pyplot.figure()
    fig.set_size_inches([3.5,2.5])
    ax = pyplot.subplot(111)
    for i, method in enumerate(methods):
        data = np.loadtxt('adapt.txt.mean.'+method)[:, colid]
        pyplot.semilogx(set_sizes, data,
                    color=colors[i],
                    marker=markers[i],
                    lw=2,
                    ls=linestyles[i],
                    label=method)
    pyplot.xlabel('set size (log scale)')
    pyplot.ylabel(title)
    pyplot.grid(True)
    pyplot.xticks(set_sizes, [str(s) for s in set_sizes])
    box = ax.get_position()
    ax.set_position([box.x0 + box.width*0.05, box.y0 + box.height*0.15, box.width, box.height*0.9])
    if legend:
        ax.legend(loc='lower right')
    pyplot.savefig('diffprior_'+title+'.pdf')

draw_column(-1, 'accuracy', legend=True)
draw_column(1, 'overlap_score', legend=True)
pyplot.show()
