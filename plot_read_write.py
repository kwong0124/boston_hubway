from typing import List

import networkx as nx
from hubway_read import get_stations, get_trips, Station
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap as Basemap




def make_graph()->nx.Graph:
    g = nx.Graph()
    stations_list = get_stations()
    g.add_nodes_from([s.id for s in stations_list])
    return g

def add_edges()->nx.Graph:
    graph = make_graph()
    trips = get_trips()
    graph.add_edges_from([(t.start_station, t.end_station) for t in trips])
    return graph

def make_map(stations: List[Station]):
    plt.figure(figsize=(10, 9))
    m = Basemap(projection='merc', llcrnrlon=-180, llcrnrlat=10, urcrnrlon=-50, urcrnrlat=70, lat_ts=0, resolution='l',
                suppress_ticks=True)
    positions = {}


if __name__ == "__main__":
    g = add_edges()
    print(f"Nodes: {g.number_of_nodes()} Edges: {g.number_of_edges()}")

