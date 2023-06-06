import matplotlib.pyplot as plt
import pandas as pd

f = pd.read_csv('coppia-potenza.csv', sep=';')

fig, axP = plt.subplots(figsize=(12, 8))
axC = axP.twinx()

axP.plot(f['giri/min'], f['Ty-potenza'], color="#EE6677", marker='o', label="Potenza")

axP.set_xlabel("giri/min", fontsize=18, labelpad=20, fontstyle="italic")
axP.set_ylabel("Potenza (cv)", color="#EE6677", fontsize=18, rotation=0, loc='top', fontstyle="italic")

axC.plot(f['giri/min'], f['Ty-coppia'], color="#4477AA", marker='o', label="Coppia")
axC.set_ylabel("Coppia (Nm)", color="#4477AA", fontsize=18, rotation=0, loc='top', fontstyle="italic")
axC.yaxis.set_label_coords(1.185, 1.08)
axP.yaxis.set_label_coords(0, 1.05)

fig.subplots_adjust(
    top=0.895,
    bottom=0.125,
    left=0.145,
    right=0.855,
    hspace=0.2,
    wspace=0.2
)

maxP = int(max(f['Ty-potenza']))
maxC = int(max(f['Ty-coppia']))
axP.set_ylim(bottom=0, top=800)
axC.set_ylim(bottom=0, top=1330)

axP.plot([2000, 7500], [maxP, maxP], linestyle='dashed', color="#EE6677", linewidth="1.0")
axC.plot([500, 7500], [maxC, maxC], linestyle='dashed', color="#4477AA", linewidth="1.0")


axP.text(2000, maxP+8, maxP, color="#EE6677", size=13)
axC.text(6600, maxC+10, maxC, color="#4477AA", size=13)


plt.show()