from logging import root
import itertools
import pandas as pd
from os import truncate
from pyvis import network as net
import networkx as nx

#Alliance
star=["Aegean","Air Canada","Air China","Air India","Air New Zealand", "ANA", "ASIANA","Austrian","Lifemiles","Brussels","Copa","CROATIA","EGYPTAIR","Ethiopian","EVA","LOT Polish","Lufthansa","SAS","Shenzhen","Singapore","Swiss","TAP","Thai","Turkish","United"]
one=["Alaska","American","British","CATHAY","FINNAIR","Iberia","JAL","Malaysia","Qantas","Qatar","Royal Air Morac","Royal Jordanian","Srilankan","FIJI","OMAN","XD"]
sky=["AeroArgentina","AeroMexico","AirEuropa","AirFrance","China Airlines","China Eastern","CZECH","DELTA","Garuda","ITA","Kenya","KLM","Korean","MEA","Saudia","TARDM","Vietnam","Virgin Atlantic","XIAMENAIR"]
#hotel=["Hyatt","IHG","Hilton","Choice","Wyndham","Accor"]

#Credit card
AMEX=["M","AirFrance","KLM","Air Canada","ANA","Lifemiles","British","Virgin Atlantic","Aer Lingus","AeroMexico","CATHAY","DELTA","Emirates","Hawaiian","Iberia","JetBlue","Qantas","Qatar","Singapore"]
Citi=["AeroMexico","Lifemiles","CATHAY","Emirates","Etihad","EVA","AirFrance","KLM","JetBlue","Qantas","Qatar","Singapore","Thai","Turkish","Virgin Atlantic"]
Chase=["M","Aer Lingus","Air Canada","British","AirFrance","KLM","Iberia","Singapore","JetBlue","Southwest","United","Virgin Atlantic"]
Bilt=["M","Alaska","American","AirFrance","KLM","Air Canada","United","Virgin Atlantic","Turkish","British","CATHAY","Lifemiles","Iberia","Aer Lingus","Emirates","Hawaiian"]
CO=["AirFrance","KLM","Virgin Atlantic","AeroMexico","Air Canada","CATHAY","Lifemiles","British","Emirates","Etihad","EVA","FINNAIR","Qantas","TAP","Singapore","Turkish","Lifemiles","British","CATHAY",]
Marriott=["Aegean","Aer Lingus","AeroMexico","Air Canada","Air China","AirFrance","KLM","Alaska","American","ANA","ASIANA","China Southern","Copa","DELTA","Emirates","Etihad","FRONTIER","Hainan","Hawaiian","Iberia","InterMiles","JAL","Korean","LATAM","Qantas","Qatar","Saudia","Singapore","Southwest","TAP","Thai","Turkish","United","Virgin Atlantic","Virgin Australia","Vueling"]
W=["Lifemiles","AirFrance","KLM","British","Iberia","Aer Lingus"]

AS=["Aer Lingus","Air Tahiti Nui", "Condor","Israel","Hainan","Icelandair","Korean","LATAM","Ravn Alaska","Singapore","STARLUX"]
VA=["Air New Zealand","ANA","Hawaiian","Indigo","LATAM","SAS","Singapore","South African","Virgin Australia"]
VAs=["Qatar","ANA","Hawaiian","Air Canada","United","Singapore","Virgin Atlantic",'Etihad',"South African",'Hainan',"HongKong","Capital","Tianjin","LINK","PELICAN"]
JB=["Hawaiian","Icelandair","JSX","Qatar","Silver","Singapore","South African"]
JAL=["S7",'Srilankan',"AirFrance","Bangkok",'China Eastern','Emirates',"Hawaiian","Korean","LATAM","Vistara","Jetstar"]
Avios=["Aer Lingus","Vueling","Qatar","Iberia","British","FINNAIR"]
CS=["Vietnam","Korean","XIAMENAIR","AirFrance","DELTA","MEA","CZECH","China Airlines","Saudia","AeroFlot","American","Sichuan"]

g= nx.Graph()
#Colors={"A":"#6676F5","B":"#F5F46D","Ch":"#64D5D9","Ci":"#E498F5","Co":"#D16F68"}
Colors={"A":"#3EADA5","B":"#7D7D7D","Ch":"#4478BC","Ci":"#E09233","M":"#FFEB98","Co":"#284278","W":"#AA2D35"}
fig="diamond"
g.add_node('A', label='AMEX MR',color=Colors["A"],size=25,shape=fig,image="images/Amex.jpg")
g.add_node("B",label="Bilt",color=Colors["B"],size=25,shape=fig,image="images/Bilt.jpg")
g.add_node('Ci', label='Citi TYP',color=Colors["Ci"],size=25,shape=fig,image="images/Citi.jpg")
g.add_node('Ch', label='Chase UR',color=Colors["Ch"],size=25,shape=fig,image="images/Chase.jpg")
g.add_node("Co",label="Capital One",color=Colors["Co"],size=25,shape=fig,image="images/Capital.jpg")
g.add_node("M",label="Marriott Bonvoy",color=Colors["M"],size=25,shape=fig)
g.add_node("W",label="Wells Fargo",color=Colors["W"],size=25,shape=fig)

g.add_node("Aer Lingus",group="alone")
g.add_nodes_from(star,group=1)
g.add_nodes_from(one,group=2)
g.add_nodes_from(sky,group=5)

#g.add_nodes_from(hotel,group="hotel")

for i in range(len(star)-1):
  for j in range(i+1,len(star)):
    g.add_edge(star[i],star[j],color="lightgray")
for i in range(len(one)-1):
  for j in range(i+1,len(one)):
    g.add_edge(one[i],one[j],color="lightgray")

for i in range(len(sky)-1):
  for j in range(i+1,len(sky)):
    g.add_edge(sky[i],sky[j],color="lightgray")

for i in range(len(Avios)-1):
  for j in range(i+1,len(Avios)):
    g.add_edge(Avios[i],Avios[j],color="lightgray")

for i in range(len(AS)):
  g.add_edge("Alaska",AS[i],color="lightgray")
for i in range(len(VA)):
  g.add_edge("Virgin Atlantic",VA[i],color="lightgray")
for i in range(len(VAs)):
  g.add_edge("Virgin Australia",VAs[i],color="lightgray")
for i in range(len(JB)):
  g.add_edge("JetBlue",JB[i],color="lightgray")
for i in range(len(JAL)):
  g.add_edge("JAL",JAL[i],color="lightgray")
for i in range(len(CS)):
  g.add_edge("China Southern",CS[i],color="lightgray")
#for i in range(len(ET)):
#  g.add_edge("Etihad",ET[i],color="lightgray")
g.add_edge("China Airlines","Qantas",color="lightgray")

for i in AMEX:
  g.add_edge("A",i,color=Colors["A"],title="1:1")
for i in Citi:
  g.add_edge("Ci",i,color=Colors["Ci"],title="1:1")
for i in Bilt:
  g.add_edge("B",i,color=Colors["B"],title="1:1")
for i in Chase:
  g.add_edge("Ch",i,color=Colors["Ch"],title="1:1")
for i in CO:
  g.add_edge("Co",i,color=Colors["Co"],title="1:1")
for i in Marriott:
  g.add_edge("M",i,color=Colors["M"],title="3:1")
for i in W:
  g.add_edge("W",i,color=Colors["W"],title="1:1")
##find "None"
h=dict(g.nodes(data="group"))
k,v=list(h.keys()),list(h.values())

for i in range(12,len(k)):
  if v[i] is None:
    g.nodes[k[i]]["group"]="alone"

## Generate edge title entry
labels=None
#nx.set_edge_attributes(g, labels, "title")
df=nx.to_pandas_edgelist(g)
df.to_csv('out.csv')


pos = nx.circular_layout(g)
vis=net.Network(notebook=True)
#h.toggle_physics(False)
vis.repulsion(node_distance=400, central_gravity=3, spring_length=200, spring_strength=0.185, damping=0.5)
vis.from_nx(g)
vis.show_buttons(filter_=["physics"])
vis.show("flights.html")

de = pd.DataFrame.from_records(vis.edges)
dn=pd.DataFrame.from_records(vis.nodes)
de.to_csv("edges.csv")
dn.to_csv("nodes.csv")
