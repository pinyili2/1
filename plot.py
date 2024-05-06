from logging import root
import itertools

from os import truncate
from pyvis import network as net
import networkx as nx

#Alliance
star=["Aegean","Air Canada","Air China","Air India","Air New Zealand", "ANA", "ASIANA","Austrian","Lifemiles","Brussels","Copa","CROATIA","EGYPTAIR","Ethiopian","EVA","LOT Polish","Lufthansa","SAS","Shenzhen","Singapore","Swiss","TAP","Thai","Turksih","United"]
one=["Alaska","American","British","CATHAY","FINAIR","Iberia","JAL","Malaysia","Qantas","Qatar","Royal Air Morac","Royal Jordanian","Srilankan","FIJI","OMAN"]
sky=["AeroArgentina","AeroMexico","AirEuropa","AirFrance","China Airlines","China Eastern","CZECH","DELTA","Garuda","ITA","Kenya","KLM","Korean Air","MEA","Saudia","TARDM","Vietnam","Virgin Atlantic","XIAMENAIR"]
#Credit card
AMEX=["AirFrance","KLM","Air Canada","ANA","Lifemiles","British","Virgin Atlantic","Aer Lingus","AeroMexico","CATHAY","DELTA","Emirates","Hawaiian","Iberia","JetBlue","Qantas","Qatar","Singapore"]
Citi=["AeroMexico","Lifemiles","CATHAY","Emirates","Etihad","EVA","AirFrance","KLM","JetBlue","Qantas","Qatar","Singapore","Thai","Turksih","Virgin Atlantic"]
Chase=["Aer Lingus","Air Canada","British","AirFrance","KLM","Iberia","Singapore","JetBlue","Southwest","United","Virgin Atlantic"]
Bilt=["Alaska","American","AirFrance","KLM","Air Canada","United","Virgin Atlantic","Turksih","British","CATHAY","Lifemiles","Iberia","Aer Lingus","Emirates","Hawaiian"]
CO=["AirFrance","KLM","Virgin Atlantic","AeroMexico","Air Canada","CATHAY","Lifemiles","British","Emirates","Etihad","EVA","FINAIR","Qantas","TAP","Singapore","Turksih"]

Airs={}
for i in star:
  Airs[i]="star"
for i in one:
  Airs[i]="one"
for i in sky:
  Airs[i]="sky"

for i in AMEX+Citi+Chase+Bilt+CO:
  if i not in list(Airs.keys()):
    Airs[i]="none"
AS=["Aer Lingus","Air Tahiti Nui", "Condor","Israel","Hainan","Icelandair","Korean Air","LATAM","Ravn Alaska","Singapore","STARLUX"]
VA=["Air New Zealand","ANA","Hawaiian","Indigo","LATAM","SAS","Singapore","South African","Virgin Australia"]

g= nx.Graph()
Colors={"A":"#6676F5","B":"#F5F46D","Ch":"#64D5D9","Ci":"#E498F5","Co":"#D16F68"}
g.add_node('A', label='AMEX MR',color=Colors["A"],size=15,shape="box")
g.add_node("B",label="Bilt",color=Colors["B"],size=15,shape="box")
g.add_node('Ci', label='Citi',color=Colors["Ci"],size=15,shape="box")
g.add_node('Ch', label='Chase',color=Colors["Ch"],size=15,shape="box")
g.add_node("Co",label="Capital One",color=Colors["Co"],size=15,shape="box")


g.add_nodes_from(star,group="star")
g.add_nodes_from(one,group="one")
g.add_nodes_from(sky,group="sky")


for i in range(len(star)-1):
  for j in range(i+1,len(star)):
    g.add_edge(star[i],star[j],color="lightgray")
for i in range(len(one)-1):
  for j in range(i+1,len(one)):
    g.add_edge(one[i],one[j],color="lightgray")

for i in range(len(sky)-1):
  for j in range(i+1,len(sky)):
    g.add_edge(sky[i],sky[j],color="lightgray")

for i in range(len(AS)):
  g.add_edge("Alaska",AS[i],color="lightgray")

for i in range(len(VA)):
  g.add_edge("Virgin Atlantic",VA[i],color="lightgray")

for i in AMEX:
  g.add_edge("A",i,color=Colors["A"])
for i in Citi:
  g.add_edge("Ci",i,color=Colors["Ci"])
for i in Bilt:
  g.add_edge("B",i,color=Colors["B"])
for i in Chase:
  g.add_edge("Ch",i,color=Colors["Ch"])
for i in CO:
  g.add_edge("Co",i,color=Colors["Co"])

##find "None"
h=dict(g.nodes(data="group"))
k,v=list(h.keys()),list(h.values())

for i in range(8,len(k)):
  if v[i] is None:
    g.nodes[k[i]]["group"]="alone"

pos = nx.circular_layout(g)
h=net.Network(notebook=True)
#h.toggle_physics(False)
h.repulsion(node_distance=120, central_gravity=0.0, spring_length=100, spring_strength=0.01, damping=0.09)
h.from_nx(g)
h.show_buttons(filter_=["physics"])
h.show("example.html")
