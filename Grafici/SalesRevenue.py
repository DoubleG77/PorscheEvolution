#meglio etichette orizzontali
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
f = pd.read_csv('1994-2022.csv', sep=';', decimal='.', index_col=0)
fig, axS = plt.subplots(figsize=(17, 8))

fig.subplots_adjust(
top=0.88,
bottom=0.11,
left=0.125,
right=0.84,
hspace=0.2,
wspace=0.2
)
x = np.arange(1994, 2022, 5)
index_pos = [0, 5, 10, 15, 20, 25]

df=pd.DataFrame({'911':f.iloc[17].values,
                 'Boxter': f.iloc[20].values,
                 'Cayenne': f.iloc[25].values,
                 #'Carrera GT': f.iloc[21].values,
                 'Panamera': f.iloc[22].values,
                 'Macan' : f.iloc[24].values,
                 'Taycan' : f.iloc[26].values},
                #'Spyder': f.iloc[23].values},
                index=[np.arange(1994,2023, 1)])

#911 66ccee
#box 767171
#cy 228833
#mc ccbb44
#pn ee6677
#ty aa3377


df.plot.bar(stacked=True, ax=axS, color=["#66ccee", "#ee6677", "#228833", "#ccbb44", "#767171", "#aa3377"], legend=False)


plt.xticks(np.arange(0, 29,1), np.arange(1994, 2023, 1), rotation=0)
axS.set_ylabel("Unità vendute", fontsize=12, loc="top", rotation=0)
axS.set_xlabel("Anni", fontsize=12, labelpad=20)
axR = axS.twinx()
revenue = f.iloc[0]
axR.plot(revenue, lw=3, color="black", label='Ricavi (€ milioni)', marker="o")
axR.set_ylabel("Ricavi (€ milioni)", fontsize=12, loc="top", rotation=0)
axR.yaxis.set_label_coords(1.16, 1)
axS.yaxis.set_label_coords(-0.03,0.97)
fig.legend(loc="upper left", bbox_to_anchor=(0,1), bbox_transform=axS.transAxes, fontsize="medium")


plt.show()
