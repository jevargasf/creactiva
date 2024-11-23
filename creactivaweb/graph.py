import pydot

(graph,) = pydot.graph_from_dot_file('./creactivaweb.dot')
graph.write_png('creactivaweb.png')