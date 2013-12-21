from matplotlib import pyplot,cm
from scipy import io
import numpy as np
from jiayq.imageclassify import datasets

mnist = datasets.MNISTDataset()
meandigits = np.zeros((10,28*28))
for i in range(10):
    meandigits[i] = np.mean(mnist.data_tr[mnist.label_tr==i],axis=0)
for i in range(10):
    pyplot.imshow(meandigits[i].reshape(28,28),interpolation='nearest',cmap=cm.gray)
    pyplot.axis('off')
    pyplot.savefig('digit_{}_mean.eps'.format(i))
    pyplot.savefig('digit_{}_mean.pdf'.format(i))


for i in range(10):
    for j in range(i+1,10):
        matdata = io.loadmat('cifar_dumpfinal_{}{}.mat'.format(i,j))
        saliency = np.dot((matdata['weights'][0]**2),matdata['selMetabin'])
        saliency.resize(6,6)
        # dummy reshape
        origSaliency = np.zeros((28,28,3))
        for ii in range(2,26):
            for jj in range(2,26):
                origSaliency[ii,jj,0] = saliency[(ii-2)/4,(jj-2)/4]
                
        origSaliency = origSaliency / origSaliency.max()
        pyplot.imshow(origSaliency,interpolation='nearest',cmap=cm.gray)
        pyplot.axis('off')
        pyplot.savefig('saliency_{}{}.eps'.format(i,j))
        pyplot.savefig('saliency_{}{}.pdf'.format(i,j))
        # draw the two digits with mask
        pyplot.imshow(meandigits[i].reshape(28,28)*origSaliency[:,:,0],interpolation='nearest',cmap=cm.gray)
        pyplot.axis('off')
        pyplot.savefig('difference_{}{}_{}.eps'.format(i,j,i))
        pyplot.savefig('difference_{}{}_{}.pdf'.format(i,j,i))
        pyplot.imshow(meandigits[j].reshape(28,28)*origSaliency[:,:,0],interpolation='nearest',cmap=cm.gray)
        pyplot.axis('off')
        pyplot.savefig('difference_{}{}_{}.eps'.format(i,j,j))
        pyplot.savefig('difference_{}{}_{}.pdf'.format(i,j,j))
        #pyplot.show()
