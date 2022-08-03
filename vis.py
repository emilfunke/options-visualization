import pandas as pd
import yfinance as yf
import datetime
from datetime import date
from pandas_datareader import data as pdr
import matplotlib.pyplot as plt
from matplotlib import style

options = pd.read_excel("options.xlsx").to_numpy()


# first zeile, second spalte
# 4 spalte strike time of options, 3 spalte Art der Option
def convert_date_strike(string):
    day = int(string[0:2])
    month = string[2:5]
    year = int(string[5:])
    if month == 'JAN':
        month = 1
    elif month == 'FEB':
        month = 2
    elif month == 'MAR':
        month = 3
    elif month == 'APR':
        month = 4
    elif month == 'MAY':
        month = 5
    elif month == 'JUN':
        month = 6
    elif month == 'JUL':
        month = 7
    elif month == 'AUG':
        month = 8
    elif month == 'SEP':
        month = 9
    elif month == 'OKT':
        month = 10
    elif month == 'NOV':
        month = 11
    elif month == 'DEC':
        month = 12
    else:
        month == 'ERROR'

    return day, month, year


# month = convert_date(options[5][4])[1]
yf.pdr_override()
today = datetime.date.today().strftime("%B %d, %Y")
dax_data = pdr.get_data_yahoo("^GDAXI", start="2018-09-01", end=date.today(), period='1d')


# ((dax_data['High']+dax_data['Low'])/2).plot()

def find_boundary(string):
    state = 0
    if string[0] == 'P':
        state = -1
    elif string[0] == 'C':
        state = 1
    position = int(string[1:])
    return state, position


def convert_date(string):
    day = string[0:2]
    month = string[3:5]
    year = string[6:]
    return str(year + "-" + month + "-" + day)


def plot_data(dax_data, options):
    plt.figure(figsize=(10, 5))
    plt.plot((dax_data['High'] + dax_data['Low']) / 2, label="DAX")
    date_open, date_close = "", ""
    state = 0
    position = 0
    color = ''
    current = 18100
    end = 0
    for i in range(60):
        # find all the lines for the same month and year
        # current_list = []
        # current_line = options[i][4]
        # next_line = options[i+1][4]
        # if current_line == next_line:

        date_open = options[i][0]
        date_close = options[i][8]
        delta = (options[i][8] - options[i][0]).days
        end = current + delta
        state = find_boundary(options[i][3])[0]
        position = find_boundary(options[i][3])[1]
        if state == -1:
            color = 'r'
        elif state == 1:
            color = 'g'
        plt.hlines(y=position, xmin=current, xmax=end, color=color, linestyle='-')
        current = end
    plt.legend()
    plt.show()


plot_data(dax_data, options)
print(options[12][4])
