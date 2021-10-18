from mymodule import Network
import json

def main():

    network = Network("My network", 'testdata.geojson')

    network.print_network_name()

    return

if __name__ == '__main__':

    main()
