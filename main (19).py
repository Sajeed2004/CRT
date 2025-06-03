class Graphlist:
    def __init__(self):
        self.graph={}
        
    def add_edge(self,u,v):
        if u not in self.graph:  
            self.graph[u]=[]
             
        if v not in self.graph:
            self.graph[v]=[]     
            
            
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def display(self):
        print("Adjacent list")
        for i in self.graph:
            print(f"{i}--->{self.graph[i]}")
            
    def bfs(self,start):
        visited = set()
        queue=[start]
        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.add(vertex)
                print(vertex, end=' ')
                for i in self.graph[vertex]:
                    if i not in visited:
                        queue.append(i)

g=Graphlist()
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(2,4)
g.add_edge(3,4)
g.add_edge(4,5)
g.add_edge(6,7)
g.display()
g.bfs(1)
adj_matrix=[
[0,1,1,0,0,0,0],
[1,0,0,1,0,0,0],
[1,0,0,1,0,0,0],
[0,1,1,0,0,0,0],
[0,0,0,1,0,1,0],
[0,0,0,0,1,0,1],
[0,0,0,0,0,1,0]
]
            