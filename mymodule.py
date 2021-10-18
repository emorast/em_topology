import json

class Node:

    __amount = 0

    id = None
    next = None
    prev = None

    def __init__(self):

        return

class Segment:

    id = None
    cost = None
    start = None
    stop = None
    fnode = None
    tnode = None


    def __init__(self, id, cost):

        self.id = id
        self.cost = cost

        return

class Network:

    head = None
    name = None
    segments = None

    def __init__(self, name, file_name):

        self.name = name

        with open(file_name) as f:
            data = json.load(f)

            i = 0; # Counter

            print("Initiating network")
            for feature in data['features']:

                id = feature['properties']['gid']
                cost = feature['properties']['shape_leng']

                seg = Segment(id, cost)

                i += 1

                if i%10 == 0:
                    print(i)

        return

    def print_network_name(self):

        print(self.name)
