import networkx as nx
import cPickle as pickle
from matplotlib import pyplot

graph, prior = pickle.load(open('ilsvrc_graph.pickle'))

LEAF = 'n11901977' # poppy
#LEAF = 'n02110341' # dalmatian
#LEAF = 'n07774719' # pecan
#LEAF = 'n02951585' # can opener
#LEAF = 'n02123394' # persian cat

GAMMA = 0.1
OFFSET = -0.0025

def get_parents(node):
    parents = [node]
    while len(graph.predecessors(parents[-1])) != 0:
        parents.append(graph.predecessors(parents[-1])[0])
    return parents

def rotate_coordinate(xy, theta):
    # note we simply assume that things are in the first quadrant
    x, y = xy
    return 

parents = get_parents(LEAF)
subgraph = nx.subgraph(graph, parents)
pos = nx.graphviz_layout(subgraph, prog='dot')

node_color = [prior[n] for n in subgraph.nodes()]
maxval = max(node_color)
node_color = [n / maxval for n in node_color]
nx.draw_networkx_edges(subgraph, pos, arrows = False)
labels = [graph.node[n]['word'] for n in parents]
nx.draw_networkx_nodes(subgraph, pos, node_size=200, node_color=[n**GAMMA for n in node_color], cmap = pyplot.get_cmap('hot_r'))

# create a dummy label graph
labelgraph = nx.DiGraph()
labelgraph.add_nodes_from([graph.node[n]['word'].split(',')[0] for n in parents])
labelpos = dict([(graph.node[n]['word'].split(',')[0], (pos[n][0] + OFFSET, pos[n][1])) for n in parents])
nx.draw_networkx_labels(labelgraph, labelpos, font_size = 15)

print [graph.node[n]['word'] for n in parents]
pyplot.axis('off')
pyplot.savefig('prior_path.pdf')
pyplot.show()
