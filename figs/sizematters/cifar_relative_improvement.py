import numpy as np
from matplotlib import pyplot
import matplotlib


matplotlib.rcParams['ps.useafm'] = True
matplotlib.rcParams['pdf.use14corefonts'] = True
matplotlib.rcParams['text.usetex'] = True

codes = [200,400,800,1600,3200]

accu_sel = np.array([ 0.6902  ,  0.70542 ,  0.71184 ,  0.7149  ,  0.714675])*100
accu_sel_std = np.array([ 0.00166975  ,  0.00227104,  0.00163658,  0.00281283,  0.00275806])*100
accu_svd = np.array([ 0.6902 ,  0.71142,  0.72128,  0.72484,  0.72522])*100
accu_svd_std = np.array([ 0.00166975,  0.00170106,  0.00154583,  0.00112889,  0.00069685])*100


line1 = pyplot.semilogx(codes, accu_svd, 'r-.', lw=2)
pyplot.fill_between(codes, accu_svd-accu_svd_std, accu_svd+accu_svd_std, facecolor = "#ff9848", edgecolor = "#ff9848", alpha=0.5)
line2 = pyplot.semilogx(codes, accu_sel, 'b-', lw=2)
pyplot.fill_between(codes, accu_sel-accu_sel_std, accu_sel+accu_sel_std, facecolor = "#38efff", edgecolor = "#38efff", alpha=0.5)
line3 = pyplot.semilogx(codes, [accu_sel[0]] *len(codes), 'k-', lw=2)
pyplot.axis([150,4800,68.5,73])
pyplot.xticks(codes, [str(c) for c in codes])
pyplot.xlabel("Starting dictionary size")
pyplot.ylabel("Testing accuracy")
pyplot.grid(True)

pyplot.legend(('Oracle', 'PADL', 'Coates et al. 2011'), loc='center right', bbox_to_anchor=(1,0.35))

fig = pyplot.gcf()
fig.set_size_inches([6., 4.])

fig.savefig("cifar_improvement.pdf")
pyplot.show()
