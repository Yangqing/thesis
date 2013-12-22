from matplotlib import pyplot
import networkx as nx
import cPickle as pickle

def get_subgraph(graph, node):
    """Get the subgraph rooted at node. Note that if there are loops in the
    graph, this function might not work.
    """
    queue = [node]
    idx = 0
    visited = set()
    nodes = set(queue)
    while idx < len(queue):
        # expand the current node in queue
        children = graph.successors(queue[idx])
        visited.add(queue[idx])
        nodes.update(children)
        queue.extend(c for c in children if c not in visited)
        idx += 1
    return graph.subgraph(nodes)

###script begins
gray = (0.75,0.75,0.75,1)
graydark = (0.5,0.5,0.5,1)
cmap = pyplot.get_cmap('Paired')

# draw the graph
graph, prior = pickle.load(open('ilsvrc_graph.pickle'))

# get positions
pos = nx.graphviz_layout(graph, prog='sfdp')
#pos = nx.graphviz_layout(graph, prog='dot')

# draw nodes
nx.draw_networkx_nodes(graph, pos, \
        with_labels = False, node_size=10, \
        node_color=gray, linewidth=None).set_edgecolor(graydark)
# draw a larger root
root = [n for n in graph.nodes() if graph.predecessors(n) == []]
nx.draw_networkx_nodes(graph, pos, \
        nodelist = root, with_labels = False, \
        node_size=40, node_color=gray, \
        linewidth=None).set_edgecolor(graydark)
# edges
nx.draw_networkx_edges(graph, pos, \
        arrows=False, edge_color=[gray]*len(graph.edges()))

# get the dog subgraph
dog = get_subgraph(graph, 'n02084071')
# just a cute function to darken a color
darken = lambda c, r: (c[0]*r, c[1]*r, c[2]*r, c[3])
# draw the dog subgraph
nx.draw_networkx_nodes(dog, pos, node_size=10, node_color=cmap(0.3)).\
        set_edgecolor(darken(cmap(0.3), 0.75))
# draw the dog root
nx.draw_networkx_nodes(dog, pos, nodelist = ['n02084071'], \
                       node_size=40, node_color=cmap(0.3)).\
        set_edgecolor(darken(cmap(0.3), 0.75))
# draw edges
nx.draw_networkx_edges(dog, pos, edge_color='k', arrows=False)
pyplot.axis('equal')
pyplot.axis('off')
pyplot.savefig(__file__[:-2] + 'pdf')
