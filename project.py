__author__ = 'DELL'
import networkx as nx
import random
def dem(G):
    g=G.copy()
    g.remove_edge('4','7')
    g.remove_edge('3','7')
    g.remove_edge('3','8')
    g.remove_edge('5','8')
    g.remove_edge('4','8')
    g.add_edge('0','7')
    g.add_edge('0','8')
    return(g)
G = nx.Graph()
print("\n ****** nodes *****")
ch=1
while True:
    n1 = input(" \n enter the node...")
    G.add_node(n1)
    ch = input("do you want to add more nodes..(press y if yes)" )
    if ch =='n':
        break
    else:
        continue
ch=1
print("\n ***** edges ****")
while True:
    n1 = input(" enter the node 1...")
    n2 = input(" enter the node 2...")
    G.add_edge(n1,n2)
    rand =random.random()
    print(round(rand,3))
    G[n1][n2]['weight']=rand
    ch = input("do you want to add more edges..(press y if yes)")
    if ch =='n':
        break
    else:
        continue

print("\n ****display****")
print("\n ----nodes are----\n")
print(G.nodes())
print("\n ----edges are----\n")
print(G.edges())
a=[]
flag=0
for n,nbrs in G.adjacency_iter():
    a.append(n)
    for nbr,eattr in nbrs.items():
        data=eattr['weight']
        for x in a:
            if x==nbr:
                flag=1
        if flag==0:
         print( n,nbr,round(data,3))
        else:
            flag=0

iset=[]
ch=1
while True:
    n1=input("\n enter the infected node...")
    iset.append(n1)
    ch = input("do you want to add more nodes..(press y if yes)" )
    if ch =='n':
        break
    else:
        continue
print("\n ***** infected nodes****")
for x in iset:
    print(x)
I=0
G.add_node(I)
for node in iset:
    for nbr in nx.all_neighbors(G, node):
        w=G[node][nbr]['weight']
        if G.has_edge(I,nbr)==False:
            G.add_edge(I,nbr,weight=w)
        else:
            temp=G[I][nbr]['weight']
            G[I][nbr]['weight']=temp+(1-temp)*w


for node in iset:
    if node in G:
        G.remove_node(node)
print("\n ****display****")
print("\n ----nodes are----\n")
print(G.nodes())
print("\n ----edges are----\n")
print(G.edges())
a=[]
flag=0
for n,nbrs in G.adjacency_iter():
    a.append(n)
    for nbr,eattr in nbrs.items():
        data=eattr['weight']
        for x in a:
            if x==nbr:
                flag=1
        if flag==0:
         print(n,nbr,round(data,3))
        else:
            flag=0
g1=nx.Graph()
g2=nx.Graph()
b=[]
print("\n \n iteration 1: ")
print("\n dominator tree...")
g1=dem(G)
print(g1.nodes())
print(g1.edges())
def rem(G):
    m=G.copy()
    #m.remove_edge('0','3')
    m.remove_edge('3','6')
    m.remove_edge('3','7')
    m.remove_edge('3','8')
    m.remove_node('3')
    m.remove_node('6')

    return m
infected='0'
max=0
for x in g1.nodes():
    if x!=0:
        b.append(x)
for n in b:
    deg=g1.degree(n)
    if max< deg:
        max=deg
        nod=n
print("\n node ")
print(nod)
print(" with highest degree ")
print("\n required graph: ")
g2=rem(G)
print(g2.nodes())
print(g2.edges())













