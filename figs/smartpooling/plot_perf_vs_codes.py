from matplotlib import pyplot

x = [200,400,800,1600,4000]
baseline = [69.86,73.45,75.70,77.90,79.60]
ours = [73.42,76.03,78.30,80.17,82.04]
ours_best = [76.81,78.07,79.06,80.36,82.09]

pyplot.semilogx(x,baseline,'o-',lw=2)
pyplot.semilogx(x,ours,'d-',lw=2)
pyplot.semilogx(x,ours_best,'^-',lw=2)
pyplot.xticks(x,x)
pyplot.axis([150,6000,68,84])
pyplot.gcf().set_size_inches([6,4.5])
pyplot.legend(('Baseline','Ours, equal-dim','Ours, optimum-dim'),loc='lower right')
pyplot.xlabel('Codebook Size')
pyplot.ylabel('Accuracy')
pyplot.grid(True)
pyplot.title('Performance on CIFAR-10')
pyplot.savefig('perf_vs_codes.eps')
pyplot.savefig('perf_vs_codes.pdf')
pyplot.show()

