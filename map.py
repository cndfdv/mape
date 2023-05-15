import folium as fo
import numpy as np
import tkinter as tk
from folium.plugins import MarkerCluster

xs =[]
ys = []
zs = []
adresses=[]

file = open("Points.txt", encoding='utf-8')

for line in file:
    els = line.split(";")
    num = float(els[0])
    num1 = float(els[1])
    num2 = els[2]
    xs = np.append(xs, num)
    ys = np.append(ys, num1)
    zs = np.append(zs, num2)

map = fo.Map(location=[55.75, 37.6], zoom_start=10)

marker_cluster = MarkerCluster().add_to(map)

for j in range(len(zs)-1):
    adress = "<i>" + str(zs[j]) + "</i>"
    adresses= np.append(adresses, adress)

color = 'green'

def clickY():
    color = 'red'

def clickX():
    color = 'green' 


app = tk.Tk()
buttonУ = tk.Button(app, text="Increase", command=clickY, width=30)
buttonX = tk.Button(app, text="Increase", command=clickX, width=50)

def marker(x,y, z):
    iframe = fo.IFrame(z+'<br><button>Пункт заполнен</button>' + '<br><button>Пункт не заполнен</button>')
    popup1 = fo.Popup(iframe,
                        min_width=250,
                        max_width=250)
    return fo.Marker(location=[x,y], popup=popup1, icon = fo.Icon(icon = "fa-recycle", prefix='fa', color = color)).add_to(marker_cluster)

for i in range(len(xs)-1):
    marker(xs[i],ys[i], adresses[i])



map.save("mape.html")
file.close()

