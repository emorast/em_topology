from network import Network
import json
from queue import Queue

def main():

    network = Network("My network", 'testwgs84.geojson')

    network.write("out")

    return

if __name__ == '__main__':

    main()
