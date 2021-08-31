# create a graph and initialize it
# call dijkstra algorithm to apply on this graph
import heapq
from queue import PriorityQueue

class Graph:
    def __init__(self, n):
        self.vertices = n
        self.adj_list = [None]*n
        for i in range(0,n):
            self.adj_list[i] = []
    
    def add_edges(self, _from, _to, wt):
        self.adj_list[_from].append((_to, wt))
        self.adj_list[_to].append((_from, wt))
    
    def print_edges(self):
        for i in range(0, len(self.adj_list)):
            for j in range(0, len(self.adj_list[i])):
                print("edge start from {} and end at {}".format(i,self.adj_list[i]), end=" ")
            print()
    
    def dijkstra(self):
        # start with some max weight from inital node
        # run modified bfs to update the 1->2, 1->3, 1->4
        weight = [999999] * self.vertices
        queue = PriorityQueue()
        weight[0] = 0
        queue.put((0,0))
        while not queue.empty():
            tup = queue.get()
            vt = tup[0]
            wt = tup[1]
            if(weight[vt] > wt):
                weight[vt] = wt
            for j in range(0, len(self.adj_list[vt])):
                currV = self.adj_list[vt][j][0]
                currW = self.adj_list[vt][j][1]
                if wt + currW < weight[currV]:
                    weight[currV] =  wt + self.adj_list[vt][j][1]
                    queue.put((self.adj_list[vt][j][0], weight[self.adj_list[vt][j][0]]))
        return weight







if __name__ == "__main__":
    graph = Graph(4)
    graph.add_edges(0,2, 1)
    graph.add_edges(0,3, 4)
    graph.add_edges(1,3, 5)
    graph.add_edges(2,3,2)
    graph.print_edges()
    p = graph.dijkstra()
    for i in range(0,4):
        print(p[i] , end=" ")
    # print(graph.dijkstra())