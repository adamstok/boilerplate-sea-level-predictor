import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']

    # Create scatter plot
    plt.plot(x, y, 'o')


    # Create first line of best fit
    res = linregress(x, y)
    newx = []
    for i in range(1880, 2050):
        newx.append(i)
    newy = []
    for i in newx:
        newy.append(res.slope * i + res.intercept)
    
    plt.plot(newx, newy, 'r')


    # Create second line of best fit
    x2 = x[x >= 2000]
    y2 = df[df['Year'] >= 2000]['CSIRO Adjusted Sea Level']
    res2 = linregress(x2, y2)

    newx2 = []
    for i in range(2000, 2050):
        newx2.append(i)
    newy2 = []
    for i in newx2:
        newy2.append(res2.slope * i + res.intercept)

    plt.plot(newx2, newy2, 'r')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
