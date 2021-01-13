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
    for i in range(1880, 2051):
        newx.append(i)
    newy = []
    for i in range(len(y)):
        newy.append(y[i])
    for i in range(37):
        newy.append(newy[-1]/res.value)
    
    new_df = {'x': newx, 'y':newy}
    new_df_pd = pd.DataFrame(new_df)
    new_res = linregress(new_df_pd['x'], new_df_pd['y'])


    plt.plot(new_df_pd['x'], new_res.intercept + new_res.slope*new_df_pd['x'], 'r')

    # Create second line of best fit


    # Add labels and title

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
