import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings

# Suppress Warnings
warnings.filterwarnings('ignore')

# Function to get the measures of the center of the data (mode, median and mean)

def measures_of_center(df, variable):
    # creating a figure composed of a boxplot and histogram
    f, (ax_box, ax_hist) = plt.subplots(2, sharex=True, gridspec_kw= {"height_ratios": (.15, .85)})
    
    # calculate measures of central tendency
    mean=df[variable].mean()
    median=df[variable].median()
    mode=df[variable].mode().tolist()[0]
    
    # show measure of central tendency in boxplot
    sns.boxplot(df[variable], ax=ax_box)
    ax_box.axvline(mean, color='r', linestyle='--')
    ax_box.axvline(median, color='g', linestyle='-')
    ax_box.axvline(mode, color='b', linestyle='-')

    # show measure of central tendency in histogram
    sns.distplot(df[variable], ax=ax_hist)
    ax_hist.axvline(mean, color='r', linestyle='--')
    ax_hist.axvline(median, color='g', linestyle='-')
    ax_hist.axvline(mode, color='b', linestyle='-')

    # add description to plot
    ax_box.set(title="Measures of central tendency: " + variable)
    ax_hist.set(ylabel="Probability of occurrence")
    ax_hist.set(xlabel=variable)
    
    # display measure of central tendency legend
    plt.legend({'Mean':mean,'median':median,'moda':mode})
    
    # Show plot
    plt.show()
    print('Mean=', str(mean))
    print('Median=', str(median))
    print('Mode=', str(mode) + '\n')


# Function to get the measures of dispersion

def measures_of_dispersion(df, variable):
    std = df[variable].std()
    var = df[variable].var()
    print(variable + ':')
    print("Standard Deviation: " + str(std))
    print("Variance: " + str(var) + '\n')

# Function to create boxplot

def data_boxplot(df):
    # set boxplot colors
    sns.set_palette(sns.color_palette(["#ff1493"]))

    # set size and create boxplotfigure
    f, (ax_box) = plt.subplots(figsize=(25, 15))

    # assigning a graph to each ax and set graph text
    sns.boxplot(data=df, ax=ax_box, dodge=False)
    ax_box.set_title('Variables Boxplot', fontsize=40)
    ax_box.set_xlabel('Variables', fontsize=20)
    ax_box.set_ylabel('Probability of occurrence', fontsize=20)

    # show plot
    plt.show()