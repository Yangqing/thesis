import os

base_url = 'http://www.icsi.berkeley.edu/~jiayq/ilsvrctest/'


files = [int(line.strip()) for line in open('files.txt')]

for file in files:
    name = 'ILSVRC2010_test_%08d.JPEG' % file
    outname = '%d.JPEG' % file
    if os.path.exists(outname):
        print 'skipped %s' % outname
    else:
        os.system('wget %s%s -O %s' % (base_url, name, outname))

