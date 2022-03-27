from Traversals import bfs_path
import heapq
from collections import deque
from Simulator import Simulator
import sys
# This project was worked on by Joseph Maiarana, David Wang, Jameson Reid
class Solution:

    def __init__(self, problem, isp, graph, info):
        self.problem = problem
        self.isp = isp
        self.graph = graph
        self.info = info

    def output_paths(self):
        """
        This method must be filled in by you. You may add other methods and subclasses as you see fit,
        but they must remain within the Solution class.
        """
        n = len(self.graph)
        start = self.isp
        mygraph = self.graph
        #print(self.info)
        #print(mygraph)

        paths, bandwidths, priorities = {}, {}, {}
        # Note: You do not need to modify all of the above. For Problem 1, only the paths variable needs to be modified. If you do modify a variable you are not supposed to, you might notice different revenues outputted by the Driver locally since the autograder will ignore the variables not relevant for the problem.
        # WARNING: DO NOT MODIFY THE LINE BELOW, OR BAD THINGS WILL HAPPEN
        mypaths = {}
        delays = []
        discovered = {}
        queue = []
        queue.append(start)
        mypaths[start].append(start)
        clientpaths = {}
        list_clients = self.info["list_clients"]
        #---- ^Above is the declaration of all of the necessary variables^-----

        self.declarations(n,start,delays,discovered,mypaths)
        # --- ^ The above function formates the delay, discovered and mypath variable^------

        while queue:
            current = queue.pop(0)
            for connection in mygraph[current]:
                if(not discovered[connection]):
                    discovered[connection] = True
                    queue.append(connection)
                    delays[connection] = delays[current] + 1
                    currentpath = mypaths[current] +[connection]
                    mypaths[connection] = currentpath
        #-----^ the above while loop is based on the BFS algorithm from Algorithm page 90 section 3.3
        #-----^ The only difference is this code is the fact that the delay list is the length of the shortest paths and the mypath dictionary stores the shortest path including the node itself as the end node. 
        #-----^ example: the list of the start node will be in the key:value format of: start:[start]. A random node will look like: node:[start,..., node]
        for client in list_clients:
            clientpaths[client] = mypaths[client]
        paths = clientpaths
        #-----^ the above code takes the client list from info  and stores the client and their list inside a dictionary in the format of client:[client_list].
        return (paths, bandwidths, priorities)

    def declarations(self,n, start , dellist, discovereddic, mypathdic):
        for m in range(n):
            if(m == start):
                discovereddic[m] = True
                dellist.append(0)
            else:
                discovereddic[m] = False
                dellist.append(-1)
            mypathdic[m] = []
        
