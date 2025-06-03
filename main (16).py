class graph:
    def __init__(self):
        self.graph={}
        
    def add_edge(self,u,v):
        if u not in self.graph:  #creating node in u variable
            self.graph[u]=[]
             
        if v not in self.graph:
            self.graph[v]=[]     #creating edge in v variable
            
            
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def display(self):
        print("Adjacent list")
        for i in self.graph:
            print(f"{i}--->{self.graph[i]}")
g=graph()
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(2,4)
g.add_edge(3,4)
g.add_edge(4,5)
g.add_edge(6,7)
g.display()
            