from mymodule import Network
import json

def main():

    network = Network("My network", 'testwgs84.geojson')

    network.write("out")

    return

if __name__ == '__main__':

    main()
