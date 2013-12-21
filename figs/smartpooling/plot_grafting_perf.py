from matplotlib import pyplot
import numpy as np

steps = 6400
tr = np.loadtxt('tr.txt')
te = np.loadtxt('te.txt')
pyplot.plot(range(steps),tr[:steps],'#CF3000',lw=2)
pyplot.plot(range(steps),te[:steps],'#3C87DC',lw=2)
pyplot.axis([0,6400,0.5,0.9])
pyplot.grid(True)
pyplot.gcf().set_size_inches([5,4])
pyplot.xlabel('Number of Features')
pyplot.ylabel('Accuracy')
pyplot.title('Performance vs. Number of Features')
pyplot.legend(('Training','Testing'),loc='lower right')
pyplot.savefig('grafting_perf.eps')
pyplot.savefig('grafting_perf.pdf')

pyplot.show()
