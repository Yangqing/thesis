import numpy as np
import matplotlib.pyplot as plt

data = np.load('confmats.npz')
# normalize

def show_matrix(mat, start, end, gamma, title):
    mat = mat / mat.sum(1).astype(np.float64)[:, np.newaxis]
    plt.figure()
    plt.imshow(mat[start:end, start:end] ** gamma,
            interpolation = 'nearest',
            cmap = plt.get_cmap('bone_r'))
    plt.xticks(())
    plt.yticks(())
    plt.gcf().set_size_inches([4,4])
    #plt.title(title)
    plt.draw()
    plt.savefig(title + '.pdf')

#for key in data:
#    show_matrix(data[key], -19, -1, 0.4, key)

# draw the bar plot
nonzero_test = float((data['test_conf']>0).sum())
#nonzero_count = [\
#        ((data['train_conf']>0) & (data['test_conf']>0)).sum() / nonzero_test,
#        ((data['val_conf']>0) & (data['test_conf']>0)).sum() / nonzero_test,
#        ((data['approx_conf']>0) & (data['test_conf']>0)).sum() / nonzero_test,
#        ]

block = 4
trainz = (data['train_conf']==0) & (data['test_conf']>0)
valz = (data['val_conf']==0) & (data['test_conf']>0)
unlearnz = (data['approx_conf']==0) & (data['test_conf']>0)
trainz = np.hstack(trainz[:,i:i+4].mean(1)[:, np.newaxis] for i in range(1000/block))
trainz = np.vstack(trainz[i:i+4, :].mean(0) for i in range(1000/block))
valz = np.hstack(valz[:,i:i+4].mean(1)[:, np.newaxis] for i in range(1000/block))
valz = np.vstack(valz[i:i+4, :].mean(0) for i in range(1000/block))
unlearnz = np.hstack(unlearnz[:,i:i+4].mean(1)[:, np.newaxis] for i in range(1000/block))
unlearnz = np.vstack(unlearnz[i:i+4, :].mean(0) for i in range(1000/block))

def show_diff(mat, gamma, title, vmin=-0.75, vmax=0.75):
    plt.figure()
    plt.imshow(mat ** gamma,
            interpolation = 'nearest',
            cmap = plt.get_cmap('RdBu'),
            vmin=vmin, vmax=vmax)
    plt.xticks(())
    plt.yticks(())
    plt.gcf().set_size_inches([4,4])
    #plt.title(title)
    plt.draw()
    plt.savefig(title + '.pdf')

gamma = 0.8
show_diff(trainz, gamma, 'confmat_trainz')
show_diff(valz, gamma, 'confmat_valz')
show_diff(unlearnz, gamma, 'confmat_approxz')

zero_count = [\
        ((data['train_conf']==0) & (data['test_conf']>0)).sum() / nonzero_test,
        ((data['val_conf']==0) & (data['test_conf']>0)).sum() / nonzero_test,
        ((data['approx_conf']==0) & (data['test_conf']>0)).sum() / nonzero_test,
        ]

width = 0.25
step = 0.28
start = 1
space = 1
cmap = plt.get_cmap('Paired')
colors = [cmap(0.65), cmap(0.45), cmap(0.1)]
labels = ['train', 'val', 'unlearn']

#for i in range(3):
#    plt.bar([start+i*step, start+space+i*step], [nonzero_count[i], zero_count[i]], width=width, color=colors[i])

fig = plt.figure()
fig.set_size_inches([3.4, 3.4])
for i in range(3):
    plt.bar([start+i*step], [zero_count[i]], width=width, color=colors[i], label=labels[i])
plt.axis([start + step * 1.5 - space / 2., start + step * 1.5 + space / 2., 0, 1])
plt.xticks([start + step*0.5, start + step * 1.5 - 0.03, start+step*2.5], labels)
plt.yticks([0, 0.5, 1], ['0', '0.5', '1'])
plt.legend(loc='center right')
plt.savefig('confmat_zero_hist.pdf')
plt.show()
