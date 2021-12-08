import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
import seaborn as sns
import warnings
from IPython.display import Markdown, display

# Suppress Warnings
warnings.filterwarnings('ignore')

# Saphiro-Wilk test
def saphiro_test(data):
    stat, p = stats.shapiro(data)
    
    return (stat, p)

# Kurtosis and curve distribution
def kurtosis(data):
    distribution_type = ""
    k = stats.kurtosis(data)
    if k > 0:
        distribution_type = "Leptokurtic"
    elif k == 0:
        distribution_type = "Mesokurtic"
    elif k < 0:
        distribution_type = "Platikurtic"
        
    return (k, distribution_type)

# Skewness 
def skewness(data):
    assymetry_type = ""
    s = stats.skew(data)
    if s > 0:
        assymetry_type = "Right Assymetry (+)"
    elif s == 0:
        assymetry_type = "Symmetric"
    elif s < 0:
        assymetry_type = "Left Assymetry (+)"
        
    return (s, assymetry_type)
        

# Function to get the measures of the center of the data (mode, median and mean)
def measures_of_center(df, variable):
    # creating a figure composed of a boxplot and histogram
    f, (ax_box, ax_hist) = plt.subplots(2, sharex=True, gridspec_kw= {"height_ratios": (.15, .85)})
    
    # calculate measures of central tendency
    mean=round(df[variable].mean(), 4)
    median=round(df[variable].median(), 4)
    mode=round(df[variable].mode().tolist()[0], 4)
    
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
    ax_box.set(title="Measures of central tendency: ")
    ax_hist.set(ylabel="Probability of occurrence")
    ax_hist.set(xlabel=variable)
    
    # display measure of central tendency legend
    plt.legend({'Mean':mean,'median':median,'moda':mode})
    
    # Saphito-Wilk test
    saphiro_stats = saphiro_test(df[variable])
    W = round(saphiro_stats[0], 4)
    p = saphiro_stats[1]
    if p > 0.05:
        normality_test = "H0: Variable has a normal distribution"
    else:
        normality_test = "H1: Variable has a non-normal distribution"
    
    # Kurtosis Analysis
    kurtosis_analysis = kurtosis(df[variable])
    
    # Skewness Analysis
    skewness_analysis = skewness(df[variable])
    
    # Display Tittle
    display(Markdown('### ' + variable))
        
    # Show plot
    plt.show()
    
    # Show statistics data
    display(Markdown('**Mean:** ' + str(mean)))
    display(Markdown('**Median:** ' + str(median)))
    display(Markdown('**Mode:** ' + str(mode)))
    display(Markdown('**Interpretation**'))
    display(Markdown('&nbsp;&nbsp;&nbsp;&nbsp;**Kursotis:** ' + str(round(kurtosis_analysis[0], 4)) + ', ' + str(kurtosis_analysis[1])))
    display(Markdown('&nbsp;&nbsp;&nbsp;&nbsp;**Skewness:** ' + str(round(skewness_analysis[0], 4)) + ', ' + str(skewness_analysis[1])))
    display(Markdown('&nbsp;&nbsp;&nbsp;&nbsp;**Normality Test:**'))
    print('\t Saphiro-Wilk Test: ', 'W = ', W, ' p-value = ', p)
    display(Markdown('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**' + normality_test + '**'))
    display(Markdown('---'))

# Function to get the measures of dispersion
def measures_of_dispersion(df, variable):
    std = df[variable].std()
    var = df[variable].var()
    display(Markdown('**' + variable + '**'))
    print("\tStandard Deviation: " + str(std))
    print("\tVariance: " + str(var) + '\n')

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