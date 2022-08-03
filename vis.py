import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

options = pd.read_excel("options_vis.xlsx").to_dict()
length = len(options["Datum Verkauf"])

sell_date = [options["Datum Verkauf"][i].to_pydatetime() for i in range(len(options["Datum Verkauf"]))]
buy_date = [options["Datum Kauf"][i].to_pydatetime() for i in range(len(options["Datum Kauf"]))]

sell_price = [options["Kurs VK"][i] for i in range(len(options["Kurs VK"]))]
buy_price = [options["Kurs EK"][i] for i in range(len(options["Kurs EK"]))]

option_name = [options["Option"][i] for i in range(len(options["Option"]))]

dax = yf.download("^GDAXI", start=sell_date[0], end=sell_date[len(sell_date)-1])
vola = yf.download("^VIX", start=sell_date[0], end=sell_date[len(sell_date)-1])

fig, ax1 = plt.subplots(1, 1, figsize=(16, 9))

ax1.grid()

for i in range(length):
    y = int(option_name[i][1:])
    color = option_name[i][0]
    if color == "C":
        color = "green"
    else:
        color = "red"
    x1, x2 = sell_date[i], buy_date[i]

    if x1 < x2:
        x = [x1, x2]
        y = [y, y]
        ax1.plot(x, y, color)
    elif x2 < x1:
        print("safety")
        x = [x2, x1]
        y = [y, y]
        ax1.plot(x, y, "blue")

plt.title("DAX")
ax1.plot(dax["Adj Close"], color="black")
ax2 = ax1.twinx()
ax2.plot(vola["Adj Close"], color="purple")
plt.savefig("ich.jpg")
