from matplotlib import pyplot
import networkx as nx
import cPickle as pickle
import random

def get_subgraph(graph, node):
    """Get the subgraph rooted at node. Note that if there are loops in the
    graph, this function might fall into loops.
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
random.seed(1701)
gray = (0.75,0.75,0.75,1)
graydark = (0.5,0.5,0.5,1)
cmap = pyplot.get_cmap('Paired')
darken = lambda c, r: (c[0]*r, c[1]*r, c[2]*r, c[3])
# draw the graph
graph, prior = pickle.load(open('ilsvrc_graph.pickle'))
root = [n for n in graph.nodes() if graph.predecessors(n) == []]
pos = nx.graphviz_layout(graph, prog='sfdp')
nx.draw_networkx_nodes(graph, pos, with_labels = False, node_size=10, node_color=gray, linewidth=None).set_edgecolor(graydark)
nx.draw_networkx_nodes(graph, pos, nodelist = root, with_labels = False, node_size=40, node_color=gray, linewidth=None).set_edgecolor(graydark)
nx.draw_networkx_edges(graph, pos, arrows=False, edge_color=[gray]*len(graph.edges()))

dog = get_subgraph(graph, 'n02084071')
nx.draw_networkx_nodes(dog, pos, node_size=10, node_color=cmap(0.3)).\
        set_edgecolor(darken(cmap(0.3), 0.75))
nx.draw_networkx_nodes(dog, pos, nodelist = ['n02084071'], \
                       node_size=40, node_color=cmap(0.3)).\
        set_edgecolor(darken(cmap(0.3), 0.75))
nx.draw_networkx_edges(dog, pos, edge_color='k', arrows=False)
feline = get_subgraph(graph, 'n02120997')
nx.draw_networkx_nodes(feline, pos, node_size=10, node_color=cmap(0.45)).\
        set_edgecolor(darken(cmap(0.45), 0.75))
nx.draw_networkx_nodes(feline, pos, nodelist = ['n02120997'], \
                       node_size=40, node_color=cmap(0.45)).\
        set_edgecolor(darken(cmap(0.45), 0.75))
nx.draw_networkx_edges(feline, pos, edge_color='k', arrows=False)
vehicle = get_subgraph(graph, 'n04524313')
nx.draw_networkx_nodes(vehicle, pos, node_size=10, node_color=cmap(0.6)).\
        set_edgecolor(darken(cmap(0.6), 0.75))
nx.draw_networkx_nodes(vehicle, pos, nodelist = ['n04524313'], \
                       node_size=40, node_color=cmap(0.6)).\
        set_edgecolor(darken(cmap(0.6), 0.75))
nx.draw_networkx_edges(vehicle, pos, edge_color='k', arrows=False)
pyplot.axis('equal')
pyplot.axis('off')
pyplot.savefig('ilsvrc_graph.pdf')

# OK, now draw individual graphs
pyplot.figure()
nx.draw_networkx_nodes(dog, pos, node_size=100, node_color=cmap(0.3)).\
        set_edgecolor(darken(cmap(0.3), 0.75))
nx.draw_networkx_nodes(dog, pos, nodelist = ['n02084071'], \
                       node_size=300, node_color=cmap(0.3)).\
        set_edgecolor(darken(cmap(0.3), 0.75))
nx.draw_networkx_edges(dog, pos, edge_color='k', width=2.0, arrows=False)
pyplot.axis('equal')
pyplot.axis('off')
pyplot.savefig('ilsvrc_graph_dog.pdf')

pyplot.figure()
nx.draw_networkx_nodes(feline, pos, node_size=100, node_color=cmap(0.45)).\
        set_edgecolor(darken(cmap(0.45), 0.75))
nx.draw_networkx_nodes(feline, pos, nodelist = ['n02120997'], \
                       node_size=300, node_color=cmap(0.45)).\
        set_edgecolor(darken(cmap(0.45), 0.75))
nx.draw_networkx_edges(feline, pos, edge_color='k', width=2.0, arrows=False)
pyplot.axis('equal')
pyplot.axis('off')
pyplot.savefig('ilsvrc_graph_feline.pdf')

pyplot.figure()
nx.draw_networkx_nodes(vehicle, pos, node_size=100, node_color=cmap(0.6)).\
        set_edgecolor(darken(cmap(0.6), 0.75))
nx.draw_networkx_nodes(vehicle, pos, nodelist = ['n04524313'], \
                       node_size=300, node_color=cmap(0.6)).\
        set_edgecolor(darken(cmap(0.6), 0.75))
nx.draw_networkx_edges(vehicle, pos, edge_color='k', width=2.0, arrows=False)
pyplot.axis('equal')
pyplot.axis('off')
pyplot.savefig('ilsvrc_graph_vehicle.pdf')

pyplot.show()
