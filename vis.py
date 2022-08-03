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

plt.figure(figsize=(16, 9))

for i in range(length):
    y = int(option_name[i][1:])
    color = option_name[i][0]
    if color == "C":
        color = "blue"
    else:
        color = "red"
    x1, x2 = sell_date[i], buy_date[i]
    x = [x1, x2]
    y = [y, y]
    if x1 < x2:
        plt.plot(x, y, color)

plt.title("DAX")
dax["Adj Close"].plot(color="black")
plt.savefig("test.jpg")
