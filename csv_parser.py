

import pandas as pd
import matplotlib.pyplot as plt
#import sys
import click

"""input at console: python csv_parser.py display_columns oktoberfestgesamt19852016.csv """


@click.group()
def cli():
    """can display and plot csv files."""
    pass

@cli.command()
@click.argument('filename')
def display(filename):
    """Displays the column names and their data type"""
    df = pd.read_csv(filename)
    print(df.dtypes)

@cli.command()
@click.argument('filename')
@click.option('--column', default=None, help='Name of column to plot. If not used, all will be plotted.')
def plot(filename, column):
    """Plots histogram"""
    df = pd.read_csv(filename)
    if column is None:
        df.hist()
    else:
        df[column].hist()
    plt.show()
    

if __name__ == '__main__':
    cli() #like a directory of functions
    #display_columns()
    #plot_hist()
    
#if __name__ == '__main__':
 #   command = sys.argv[1]
  #  filename = sys.argv[2]
   # if command == 'display':
    #    display_columns(filename) 
    #elif command == 'plot':
     #   plot_hist(filename)
    #else:
     #   raise IOError("csv_parser requires 'plot' or 'display' commands")

        
#print(df.head())

#df.bier_konsum.hist()
#plt.gcf()
#plt.title('Bier Konsum')
#plt.show()

#df.hendl_konsum.hist(color='red')
#plt.gcf()
#plt.title('Hendl Konsum')
#plt.show()


#df.hist()

#print(df['besucher_tag'].hist())
#plt.show()

#print(df.dtypes)