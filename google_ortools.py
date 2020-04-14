# """From Bradley, Hax, and Magnanti, 'Applied Mathematical Programming', figure 8.1."""

from __future__ import print_function
from ortools.graph import pywrapgraph

def main():
  """MinCostFlow simple interface example."""

  # Define four parallel arrays: start_nodes, end_nodes, capacities, and unit costs
  # between each pair. For instance, the arc from node 0 to node 1 has a
  # capacity of 15 and a unit cost of 4.

  #start_nodes = [ 0, 0,  1, 1,  1,  2, 2,  3, 4]
  #end_nodes   = [ 1, 2,  2, 3,  4,  3, 4,  4, 2]
  #capacities  = [15, 8, 20, 4, 10, 15, 4, 20, 5]
  #unit_costs  = [ 4, 4,  2, 2,  6,  1, 3,  2, 3]

  start_nodes = [0, 1, 2, 3, 4, 4, 5, 5, 6, 10, 10, 10]
  end_nodes = [3, 4, 5, 7, 3, 6, 6, 9, 8, 0, 1, 2]
  capacities = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]
  unit_costs = [3, 6, 3, 7, 2, 5, 6, 9, 11, 0, 0, 0]

  # Define an array of supplies at each node.

  #supplies = [20, 0, 0, -5, -15]
  supplies = [0, 0, 0, 0, 0, 0, 0, -10, -25, -15, 50]


  # Instantiate a SimpleMinCostFlow solver.
  min_cost_flow = pywrapgraph.SimpleMinCostFlow()

  # Add each arc.
  for i in range(0, len(start_nodes)):
    min_cost_flow.AddArcWithCapacityAndUnitCost(start_nodes[i], end_nodes[i],
                                                capacities[i], unit_costs[i])

  # Add node supplies.

  for i in range(0, len(supplies)):
    min_cost_flow.SetNodeSupply(i, supplies[i])


  # Find the minimum cost flow between node 0 and node 4.
  if min_cost_flow.Solve() == min_cost_flow.OPTIMAL:
    print('Minimum cost:', min_cost_flow.OptimalCost())
    print('')
    print('  Arc    Flow / Capacity  Cost')
    for i in range(min_cost_flow.NumArcs()):
      cost = min_cost_flow.Flow(i) * min_cost_flow.UnitCost(i)
      print('%1s -> %1s   %3s  / %3s       %3s' % (
          min_cost_flow.Tail(i),
          min_cost_flow.Head(i),
          min_cost_flow.Flow(i),
          min_cost_flow.Capacity(i),
          cost))
  else:
    print('There was an issue with the min cost flow input.')


def net4():
    G = nx.DiGraph()
    G.add_nodes_from([
        ('A',{'ss':np.inf}),
        ('B',{'ss':np.inf}),
        ('C',{'ss':np.inf}),
        ('D',{'ss':None}),
        ('E',{'ss':None}),
        ('F',{'ss':None}),
        ('G',{'ss':None}),
        ('H',{'ss':-10}),
        ('I',{'ss':-25}),
        ('J',{'ss':-15})])

    G.add_edges_from([
        ('A','D',{'z':3}),
        ('D','H',{'z':7}),
        ('B','E',{'z':6}),
        ('E','D',{'z':2}),
        ('E','G',{'z':5}),
        ('G','I',{'z':11}),
        ('F','G',{'z':6}),
        ('C','F',{'z':3}),
        ('F','J',{'z':9}),
        ])
    return G

if __name__ == '__main__':
  main()