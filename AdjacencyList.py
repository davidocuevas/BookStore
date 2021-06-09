"""An implementation of the adjacency list representation of a graph"""
from Interfaces import Graph, List
import numpy as np
import copy
import ArrayList
import ArrayQueue
import ArrayStack

class AdjacencyList(Graph):
    def __init__(self, n : int):
        self.n = n
        self.adj = np.zeros(n, object)
        for i in range(self.n):
            self.adj[i] = ArrayList.ArrayList()

    def new_boolean_matrix(self, n):
        return np.zeros([n,n],np.bool_)

    def new_boolean_array(self, n):
        return np.zeros(n, np.bool_)
            
    def add_edge(self, i : int, j : int):
        # todo
        self.adj[i].append(j)

    def remove_edge(self, i : int, j : int):
        # todo
        for k in range(len(self.adj[i]) - 1):
            if self.adj[i].get(k) == j:
                self.adj[i].remove(k)
                return
                
    def has_edge(self, i : int, j: int) ->bool:
        # todo
        for k in range(self.adj[i].size()):
            if self.adj[i].get(k) == j:
                return True
        return False
        
    def out_edges(self, i) -> List:
        # todo
        return self.adj[i]

    def in_edges(self, i) -> List:
        # todo
        out = ArrayList.ArrayList()
        for j in range(self.n):
            if self.has_edge(j,i):
                out.append(j)
        return out
    
    def bfs(self, r : int):
        # todo
        seen = self.new_boolean_array(self.n)
        q = ArrayQueue.ArrayQueue()
        q.add(r)
        seen[r] = True
        while q.size() > 0:
            i = q.remove()
            print(i, end= '')
            ngh = self.out_edges(i)
            for k in range(ngh.size()):
                j = ngh.get(k)
                if seen[j] == False:
                    q.add(j)
                    seen[j] = True

    def dfs(self, r : int):
        # todo
        seen = self.new_boolean_array(self.n)
        s = ArrayStack.ArrayStack()
        s.push(r)
        while s.size() > 0:
            i = s.pop()
            print(i, end ='')
            seen[i] = True
            ngh = self.out_edges(i)
            for j in range(ngh.size()):
                if seen[ngh.get(j)] == False:
                    s.push(ngh.get(j))
                else:
                    continue

    def bfs2(self, r: int, s : int):
        seen = self.new_boolean_array(self.n)
        q = ArrayQueue.ArrayQueue()
        l = []
        q.add(r)
        l.append(r)
        seen[r] = True
        d = 0
        while q.size() > 0 and d < s:
            i = q.remove()
            ngh = self.out_edges(i)
            for k in range(ngh.size()):
                j = ngh.get(k)
                if seen[j] == False:
                    q.add(j)
                    l.append(j)
                    seen[j] = True
            d += 1
        return l

    def dfs2(self, r1: int, r2: int):
        seen = self.new_boolean_array(self.n)
        d = np.zeros(self.n)
        s = ArrayStack.ArrayStack()
        d[r1] = 0
        s.push(r1)
        while s.size() > 0:
            i = s.pop()
            seen[i] = True
            ngh = self.out_edges(i)
            for k in range(ngh.size()):
                j = ngh.get(k)
                if seen[j] == False:
                    s.push(j)
                    d[j] = d[i] + 1
                if j == r2:
                    return d[j]
        return -1
                    
    def __str__(self):
        s = ""
        for i in range(0, self.n):
            s += "%i,%r\n" % (i, self.adj[i].__str__())
        return s










