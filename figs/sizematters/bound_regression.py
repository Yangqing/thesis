from matplotlib import pyplot
import matplotlib
import numpy as np

matplotlib.rcParams['ps.useafm'] = True
matplotlib.rcParams['pdf.use14corefonts'] = True

def regress(size, val, n = 3):
    # perform regression
    scale = (1. / size) ** 0.25
    coeff = np.hstack((scale[:n][:, np.newaxis], np.ones((n,1))))
    param = np.dot(np.linalg.inv(np.dot(coeff.T, coeff)), np.dot(coeff.T, val[:n]))
    return param[0] * scale + param[1]

def draw_figure(size, train, test, name, legend = False):
    pyplot.figure()
    pyplot.plot(size, train, 'r-', lw=3)
    pyplot.plot(size, regress(size, train), 'r-.', lw=3)
    pyplot.plot(size, test, 'b-', lw=2, alpha = 0.4)
    pyplot.plot(size, regress(size, test), 'b-.', lw=2, alpha = 0.4)
    if legend:
        pyplot.legend(('tr', 'tr_predict', 'te', 'te_predict'), loc = 'lower right')
    pyplot.title(name)
    pyplot.ylabel('Accuracy')
    pyplot.grid(True)
    fig = pyplot.gcf()
    #fig.set_size_inches([7, 2.8])
    fig.set_size_inches([6,4])
    pyplot.savefig('bound_' + name + '.pdf')

#mnist
size = np.array([100,200,400,800,1600,6000])
train = np.array([98.76, 99.16, 99.45, 99.67, 99.87, 99.99])
test = np.array([98.60, 98.76, 98.93, 98.99, 99.04, 99.01])
draw_figure(size, train, test, 'MNIST')

# stl
size = np.array([100, 200, 400, 800, 1600, 3200])
train = np.array([58.86, 64.50, 70.68, 77.22, 84.64, 91.42])
test = np.array([50.50, 53.26, 55.07, 57.00, 58.17, 58.45])
draw_figure(size, train, test, 'STL')

#cifar
size = np.array([100, 200, 500, 800, 1600, 6000])
train = np.array([70.6, 75.6, 81.9, 87.5, 91.6, 97.0])
test = np.array([68.5, 71.6, 75.5, 78.4, 79.5, 81.7])
draw_figure(size, train, test, 'CIFAR', True)

# wsj
size = np.array([100,200,400,800,1600, 6000])
train = np.array([47.1, 52.2, 57.2, 61.5, 65.5, 71.7])
test = np.array([47.8, 52.8, 57.8, 62.0, 65.7, 71.3])
draw_figure(size, train, test, 'WSJ')

# TIMIT
size = np.array([100,200,400,800,1600,6000])
train = np.array([36, 41.4, 46.2, 50.5, 54.7, 62.7])
test = np.array([35.4, 40.3, 44.1, 47.1, 49.4, 52.8])
draw_figure(size, train, test, 'TIMIT')
