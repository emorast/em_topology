import json
import math as m
from geojson import Point, MultiLineString, Feature, FeatureCollection, dump
from queue import Queue

class Node:

    __node_count = 0

    # TODO: Add next vertice array
    def __init__(self, position):

        Node.__node_count += 1

        self.id = Node.__node_count
        self.position = position
        self.next = {}
        self.connections = {}
        self.data = Feature(geometry = Point((position[0], position[1]), precision = 15),
                            properties = {"id": self.id})

        return

    def __eq__(self, other):

        if abs(self.position[0] - other.position[0]) < 0.00001 and abs(self.position[1] - other.position[1]) < 0.00001:

            return True
        else:

            return False

class Segment:

    def __init__(self, id, cost, coordinates, fnode = None, tnode = None):

        self.id = id
        self.cost = cost
        self.fnode = fnode
        self.tnode = tnode
        self.data = Feature(geometry = MultiLineString(((coordinates)), precision = 15), properties = {"id": self.id, "cost": self.cost})

        return

class Sequence:

    def __init__():

        return



class Network:

    __sum_nodes = 0

    def __init__(self, name, file_name):

        self.name = name
        self.nodes = {}
        self.edges = {}

        with open(file_name) as f:
            data = json.load(f)

            for feature in data['features']:

                seg = Segment(feature['properties']['gid'], feature['properties']['shape_leng'], feature['geometry']['coordinates'])

                seg_nodes = []

                for point in feature['geometry']['coordinates'][0]:

                    new_node = Node(point)

                    seg_nodes.append(new_node)


                first = True

                # Get the end points of the line segment
                for a in seg_nodes:

                    for b in seg_nodes:

                        # Euclidean distance
                        d = m.sqrt((a.position[0] - b.position[0])**2 + (a.position[1] - b.position[1])**2)

                        if first:

                            dmax = d
                            start = a
                            end = b
                            first = False

                        else:
                            if d > dmax:
                                dmax = d
                                start = a
                                end = b

                            else:
                                next

                Network.__sum_nodes += 1

                # Add the start node to the dictionary of nodes if unique
                for nid, node in self.nodes.items():

                    if start == node:

                            Network.__sum_nodes -= 1
                            start = node

                            break

                    else:

                        next

                self.nodes[start.id] = start
                seg.fnode = start
                start.connections.update({seg.id : seg})

                Network.__sum_nodes += 1

                # Add the end node to the dictionary of nodes if unique
                for nid, node in self.nodes.items():

                    if end == node:

                            Network.__sum_nodes -= 1
                            end = node

                            break

                    else:

                        next

                self.nodes[end.id] = end
                seg.tnode = end
                end.connections.update({seg.id : seg})

                # Update geojson
                seg.data['properties'].update({"fnode" : start.id, "tnode" : end.id})
                self.edges[seg.id] = seg

        print("SUCCESS: Created " + str(Network.__sum_nodes) + " nodes")

        return

    # Calculates shortest path between source and target node
    # IN: source node, target node
    # OUT: sequences of edges belonging to shortest_path
    # TODO: Implement one-to-many, many-to-one, many-to-many functionality

    def shortest_path(self, source, target):

        Q = Queue()
        Q.enqueue(self.nodes[source])

        looping = True

        while looping:

            x = Q.dequeue()
            selected_node = x.content

            # Get all segments connecting to the node
            for key, value in selected_node.connections.items():

                if value.fnode == selected_node.id:

                    next_node = self.nodes[value.tnode]

                elif value.tnode == selected_node.id:

                    next_node = self.nodes[value.fnode]


            if Q.isEmpty:

                looping = False

        return

    # Calculates the shortest path to all nodes in the network from source node
    # IN: soruce node
    # OUT: dictionary with node id as key and distance to said node as value

    def distance_from(self, source):


        return


    # Writes the nodes and the edges to separe geojson files
    # IN: name of file to write to
    def write(self, file_name):

        vertices = []

        for n in self.nodes:

            vertices.append(self.nodes[n].data)

        vertices_data = FeatureCollection(vertices)


        with open('em_' + file_name + '_vertices.geojson', 'w+') as outfile:

            dump(vertices_data, outfile, indent = 2)

        edges = []

        for n in self.edges:

            edges.append(self.edges[n].data)

        edges_data = FeatureCollection(edges)


        with open('em_' + file_name + '_edges.geojson', 'w+') as outfile:

            dump(edges_data, outfile, indent = 2)

        return
