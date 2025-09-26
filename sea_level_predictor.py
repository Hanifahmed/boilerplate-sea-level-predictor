import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # scatter plot
    plt.figure(figsize=(10,6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue')

    # first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # prediction up to 2050
    years_all = pd.Series(range(df['Year'].min(), 2051))
    plt.plot(years_all, intercept + slope * years_all, 'r', label='Best Fit: All Data')

    # second line of best fit (from year 2000)
    df_recent = df[df['Year'] >= 2000]
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent = pd.Series(range(2000, 2051))
    plt.plot(years_recent, intercept2 + slope2 * years_recent, 'green', label='Best Fit: 2000-Present')

    # labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # plot and return data for testing
    plt.savefig('sea_level_plot.png')
    return plt.gca()
