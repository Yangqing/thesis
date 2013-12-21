import numpy as np
from matplotlib import pyplot
import matplotlib

matplotlib.rcParams['ps.useafm'] = True
matplotlib.rcParams['pdf.use14corefonts'] = True

all_dims = [100,200,400,800,1600,3200,6400]
N = 7
line_formats = ['b-', 'ro-.', 'gv--', 'm^:']

pyplot.ion()

"""
#filename = 'cifar/cifar_from_to_accuracy.txt'
filename = 'stl/stl_from_to_accuracy.txt'

all_accu = np.zeros((N, N))
all_accu_std = np.zeros((N, N))

stat = np.loadtxt(filename)
fromdim = stat[:,0].astype(int)
todim = stat[:,1].astype(int)
accu = stat[:,2]

for j in range(N):
    for i in range(j, N):
        all_accu[i,j] = np.mean(accu[(fromdim == all_dims[i]) & (todim == all_dims[j])])
        all_accu_std[i,j] = np.std(accu[(fromdim == all_dims[i]) & (todim == all_dims[j])])
        print all_dims[i], all_dims[j], all_accu[i,j]
print all_accu
"""

all_accu = np.array(\
[[ 0.65185     , 0.          , 0.          , 0.          , 0.          , 0.          , 0.        ],
 [ 0.66805     , 0.69018333  , 0.          , 0.          , 0.          , 0.          , 0.        ],
 [ 0.67412     , 0.70542     , 0.72208     , 0.          , 0.          , 0.          , 0.        ],
 [ 0.67646     , 0.71184     , 0.7384      , 0.75262     , 0.          , 0.          , 0.        ],
 [ 0.67594     , 0.7149      , 0.74356     , 0.76692     , 0.77962     , 0.          , 0.        ],
 [ 0.675975    , 0.714675    , 0.74212     , 0.76764     , 0.78714     , 0.79908     , 0.        ],
 [ 0.6797      , 0.7134      , 0.7449      , 0.7672      , 0.7873      , 0.8037      , 0.8137    ]]) * 100

pyplot.figure()
pyplot.semilogx(all_dims[:-1], np.diag(all_accu)[:-1], line_formats[0], lw = 2)
for i in range(1, 4):
    pyplot.semilogx(all_dims[:-i], np.diag(all_accu,-i), line_formats[i], lw=2)
pyplot.xticks(all_dims, [str(c) for c in all_dims])
pyplot.grid(True)
pyplot.axis([70, 4800, 65, 81])
pyplot.xlabel('Final Dictionary Size')
pyplot.ylabel('Accuracy')
pyplot.legend(('K-means', '2x PADL', '4x PADL', '8x PADL'), loc = 'lower right')
fig = pyplot.gcf()
fig.set_size_inches([6., 4.])
fig.savefig('cifar_accuracy.pdf')

speed_up = np.zeros_like(all_accu)
speed_up.flat[:] = np.exp(np.interp(all_accu.flat, np.diag(all_accu), np.log(all_dims), np.nan, np.nan))
#speed_up /= np.array(all_dims)
speed_up = np.array(all_dims) / speed_up
pyplot.figure()
pyplot.plot(np.diag(all_accu), [1] * np.diag(all_accu).size, line_formats[0], lw = 2)
for i in range(1, 4):
    pyplot.plot(np.diag(all_accu,-i), np.diag(speed_up, -i), line_formats[i], lw=2)
pyplot.xlabel('Accuracy')
pyplot.ylabel('Relative Computation Time')
pyplot.legend(('Baseline', '2x PADL', '4x PADL', '8x PADL'), loc = 'lower right')
pyplot.axis([65, 81, 0.4, 1.05])
pyplot.grid(True)
fig = pyplot.gcf()
fig.set_size_inches([6., 4.])
fig.savefig('cifar_speedup.pdf')

all_accu = np.array(\
[[ 0.5056    , 0.        , 0.        , 0.        , 0.        , 0.        , 0.      ],
 [ 0.523475  , 0.532225  , 0.        , 0.        , 0.        , 0.        , 0.      ],
 [ 0.5287    , 0.5457    , 0.552425  , 0.        , 0.        , 0.        , 0.      ],
 [ 0.53115   , 0.55525   , 0.5635    , 0.569575  , 0.        , 0.        , 0.      ],
 [ 0.527     , 0.555225  , 0.56935   , 0.578675  , 0.581625  , 0.        , 0.      ],
 [ 0.5243    , 0.5476    , 0.563775  , 0.574625  , 0.582825  , 0.584375  , 0.      ],
 [     np.nan,     np.nan,     np.nan,     np.nan,     np.nan,     np.nan,   np.nan]]) * 100

pyplot.figure()
pyplot.semilogx(all_dims[:-1], np.diag(all_accu)[:-1], line_formats[0], lw = 2)
for i in range(1, 4):
    pyplot.semilogx(all_dims[:-i], np.diag(all_accu,-i), line_formats[i], lw=2)
pyplot.xticks(all_dims, [str(c) for c in all_dims])
pyplot.grid(True)
pyplot.axis([70, 4800, 50, 59])
pyplot.xlabel('Final Dictionary Size')
pyplot.ylabel('Accuracy')
pyplot.legend(('K-means', '2x PADL', '4x PADL', '8x PADL'), loc = 'lower right')
fig = pyplot.gcf()
fig.set_size_inches([6., 4.])
fig.savefig('stl_accuracy.pdf')

speed_up = np.zeros_like(all_accu)
speed_up.flat[:] = np.exp(np.interp(all_accu.flat, np.diag(all_accu), np.log(all_dims), np.nan, np.nan))
#speed_up /= np.array(all_dims)
speed_up = np.array(all_dims) / speed_up
pyplot.figure()
pyplot.plot(np.diag(all_accu), [1] * np.diag(all_accu).size, line_formats[0], lw = 2)
for i in range(1, 4):
    pyplot.plot(np.diag(all_accu,-i), np.diag(speed_up, -i), line_formats[i], lw=2)
pyplot.xlabel('Accuracy')
pyplot.ylabel('Relative computation time')
pyplot.legend(('Baseline', '2x PADL', '4x PADL', '8x PADL'), loc = 'upper left')
pyplot.axis([52, 59, 0.4, 1.05])
pyplot.grid(True)
fig = pyplot.gcf()
fig.set_size_inches([6., 4.])
fig.savefig('stl_speedup.pdf')


all_accu = np.array(\
[[ 0.65468     ,0.          ,0.          ,0.          ,0.          ,0.          ,0.        ],
 [ 0.67198     ,0.69112     ,0.          ,0.          ,0.          ,0.          ,0.        ],
 [ 0.68025     ,0.71091667  ,0.72353333  ,0.          ,0.          ,0.          ,0.        ],
 [ 0.6838      ,0.72115     ,0.74558333  ,0.75313333  ,0.          ,0.          ,0.        ],
 [ 0.68271667  ,0.72513333  ,0.75711667  ,0.77416667  ,0.77905     ,0.          ,0.        ],
 [ 0.68396667  ,0.72526667  ,0.7611      ,0.78438333  ,0.79675     ,0.8003      ,0.        ],
 [     np.nan,     np.nan,     np.nan,    0.7881,      0.8045,       0.8130,   np.nan]]) * 100

pyplot.figure()
pyplot.semilogx(all_dims[:-1], np.diag(all_accu)[:-1], line_formats[0], lw = 2)
for i in range(1, 4):
    pyplot.semilogx(all_dims[:-i], np.diag(all_accu,-i), line_formats[i], lw=2)
pyplot.xticks(all_dims, [str(c) for c in all_dims])
pyplot.grid(True)
pyplot.axis([70, 4800, 65, 81])
pyplot.xlabel('Final Dictionary Size')
pyplot.ylabel('Accuracy')
pyplot.legend(('K-means', '2x SVD', '4x SVD', '8x SVD'), loc = 'lower right')
fig = pyplot.gcf()
fig.set_size_inches([6., 4.])
fig.savefig('cifar_svd_accuracy.pdf')

all_accu = np.array(\
[[ 0.504225  ,0.        ,0.        ,0.        ,0.        ,0.        ,0.      ],
 [ 0.52775   ,0.5309    ,0.        ,0.        ,0.        ,0.        ,0.      ],
 [ 0.54045   ,0.55085   ,0.553025  ,0.        ,0.        ,0.        ,0.      ],
 [ 0.547875  ,0.5637    ,0.569525  ,0.570725  ,0.        ,0.        ,0.      ],
 [ 0.552275  ,0.567825  ,0.576575  ,0.57935   ,0.58025   ,0.        ,0.      ],
 [ 0.551475  ,0.5666    ,0.578     ,0.5825    ,0.5845    ,0.585075  ,0.      ],
 [     np.nan,     np.nan,     np.nan,     np.nan,     np.nan,     np.nan,   np.nan]]) * 100

pyplot.figure()
pyplot.semilogx(all_dims[:-1], np.diag(all_accu)[:-1], line_formats[0], lw = 2)
for i in range(1, 4):
    pyplot.semilogx(all_dims[:-i], np.diag(all_accu,-i), line_formats[i], lw=2)
pyplot.xticks(all_dims, [str(c) for c in all_dims])
pyplot.grid(True)
pyplot.axis([70, 4800, 50, 59])
pyplot.xlabel('Final Dictionary Size')
pyplot.ylabel('Accuracy')
pyplot.legend(('K-means', '2x SVD', '4x SVD', '8x SVD'), loc = 'lower right')
fig = pyplot.gcf()
fig.set_size_inches([6., 4.])
fig.savefig('stl_svd_accuracy.pdf')


