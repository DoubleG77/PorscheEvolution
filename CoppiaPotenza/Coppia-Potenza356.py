import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

f = pd.read_csv('coppia-potenza.csv', sep=';')

fig,axP = plt.subplots(figsize=(12,8))
fig.subplots_adjust(
    top=0.895,
    bottom=0.125,
    left=0.145,
    right=0.855,
    hspace=0.2,
    wspace=0.2
)

axC=axP.twinx()

axP.plot(f['giri/min'], f['356-potenza'], color="#EE6677", marker='o')
axC.plot(f['giri/min'], f['356-coppia'] ,color="#4477AA", marker='o')

axP.set_xlabel("giri/min",  fontsize=18, labelpad=20, fontstyle="italic")
axP.set_ylabel("Potenza (cv)", fontsize=18, color="#EE6677", rotation=0, loc='top', fontstyle="italic")

axC.set_ylabel("Coppia (Nm)",fontsize=18, color="#4477AA",rotation=0, loc='top', fontstyle="italic")
axC.yaxis.set_label_coords(1.185, 1.08)
axP.yaxis.set_label_coords(0, 1.05)



maxP = int(max(f['356-potenza']))
maxC = int(max(f['356-coppia']))
axP.set_ylim(bottom=0, top =800)
axC.set_ylim(bottom=0, top =1330)

axP.plot([min(f['giri/min'][f['356-potenza']==maxP]), 5800], [maxP, maxP], linestyle='dashed', color="#EE6677", linewidth="1.0")
axC.plot([2000, max(f['giri/min'][f['356-coppia']==maxC])], [maxC, maxC], linestyle='dashed', color="#4477AA", linewidth="1.0")


axC.text(2000, maxC+10, maxC, color="#4477AA", size=13)
axP.text(5650, maxP+10, maxP, color="#EE6677", size=13)


plt.show()







