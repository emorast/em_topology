import json
import math as m
from geojson import Point, MultiLineString, Feature, FeatureCollection, dump

class Node:

    node_count = 0

    def __init__(self, position):

        self.id = Node.node_count
        self.position = position
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
        self.data = Feature(geometry = MultiLineString(((coordinates)),
                            precision = 15),
                            properties = {"id": self.id,
                                            "cost": self.cost,
                                            "fnode": self.fnode,
                                            "tnode": self.tnode})
        return

class Network:

    def __init__(self, name, file_name):

        self.name = name
        self.nodes = {}
        self.edges = {}

        with open(file_name) as f:
            data = json.load(f)

            i = 0;

            nodes = []

            for feature in data['features']:

                temp_seg = Segment(feature['properties']['gid'],
                                    feature['properties']['shape_leng'],
                                    feature['geometry']['coordinates'])

                seg_nodes = []

                for point in feature['geometry']['coordinates'][0]:

                    temp_node = Node(point)

                    seg_nodes.append(temp_node)

                # TODO: Improve algorithm to calculate longest euclidean distance between any
                # two nodes on the segment """

                max_d = {}
                for a in seg_nodes:
                    for b in seg_nodes:

                        d = m.sqrt((a.position[0] - b.position[0])**2 + (a.position[1] - b.position[1])**2)

                        if len(max_d.keys()) == 0:

                            max_d[d] = [a, b]

                            dmax = d

                        else:

                            if d > dmax:

                                dmax = d

                                max_d[dmax] = [a, b]

                temp_seg.fnode = max_d[dmax][1]
                temp_seg.tnode = max_d[dmax][0]
                nodes.append(max_d[dmax][1])
                nodes.append(max_d[dmax][0])

                Node.node_count += 2

                self.edges[temp_seg.id] = temp_seg

            for node in nodes:

                if node not in self.nodes.values():

                    self.nodes[node.id] = node

                else:

                    Node.node_count -= 1

        print("SUCCESS: Created " + str(Node.node_count) + " nodes")
        return

    # Calculates shortest path between source and target node
    # IN: source node, target node
    # OUT: sequences of edges belonging to shortest_path
    # TODO: Implement one-to-many, many-to-one, many-to-many functionality

    def shortest_path(self, source, target):



        return seq

    # Calculates the shortest path to all nodes in the network from source node
    # IN: soruce node
    # OUT: dictionary with node id as key and distance to said node as value

    def distance_from(self,source):


        return distance_map


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
