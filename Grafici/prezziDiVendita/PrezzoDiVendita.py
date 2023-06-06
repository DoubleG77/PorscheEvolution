
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statistics as st

def median(year, df) :
    j = 0
    my = {}
  
    for y in year :
        y
        price_df = df[df['web-scraper-start-url'].str.contains(str(y))]['Price']
        p = []
        for i in range(len(price_df)) :
            s = price_df[j].lstrip('Price:').replace("$", "").replace(",", "").split("-")
            if (len(s) >1 ) :
                p.append((int(s[0]) + int(s[1]))/2)
            else :
                p.append(0)
            j = j+1

        my[y] = st.median(p)

    return my


box = pd.read_csv("boxterPricePerYearPerModelScrape.csv", sep=",")
median_box = median(np.arange(1997, 2018, 1), box)
median_911 = median(np.arange(1966, 2023, 1), pd.read_csv("911PricePerYearPerModel.csv", sep=","))
median_cy = median(np.arange(2003, 2023, 1), pd.read_csv("cayennePricePerYearPerModel.csv", sep=","))
median_pn = median(np.arange(2009, 2023, 1), pd.read_csv("panameraPricePerYearPerModel.csv", sep=","))
median_mc = median(np.arange(2014, 2023, 1), pd.read_csv("macanPricePerYearPerModel.csv", sep=","))
median_ty = median(np.arange(2020, 2023, 1), pd.read_csv("taycanPricePerYearPerModel.csv", sep=","))

fig, ax = plt.subplots(figsize=(17, 8), sharex=True)

x = np.arange(1994, 2023, 1)
ax.xaxis.set_ticks( x)
ax.set_xticklabels(x)
ax.set_xlabel("Anni", fontsize=12, labelpad=20)

x911 =  list(median_911.keys())
y911 = list(median_911.values() )
ax.plot(x911[28:],y911[28:], label="911", linewidth=3, color="#66ccee", marker='o')


ax.plot(median_box.keys(), median_box.values(), label="boxter", linewidth=3, color="#ee6677", marker='o')
ax.plot(median_cy.keys(), median_cy.values(), label="cayanne", linewidth=3, color="#228833", marker='o')
ax.plot(median_pn.keys(), median_pn.values(), label="panamera", linewidth=3, color="#ccbb44", marker='o')
ax.plot(median_mc.keys(), median_mc.values(), label="macan", linewidth=3, color="grey", marker='o') ##color
ax.plot(median_ty.keys(), median_ty.values(), label="taycan", linewidth=3, color="#aa3377", marker='o')
ax.grid(axis= "y", linewidth=0.5)
fig.legend(loc="upper left", bbox_to_anchor=(0,1), bbox_transform=ax.transAxes, fontsize="medium")
ax.set_title("Prezzo di vendita", size=17, pad=20)

color=["#66ccee", "#ee6677", "#228833", "#ccbb44", "#767171", "#aa3377"]

plt.show()