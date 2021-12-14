import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
import seaborn as sns
import warnings
from IPython.display import Markdown, display

# Render correctly Markdown when open for first time
def md_formatter(md, pp, cycle):
    pp.text(md.data)
text_plain = get_ipython().display_formatter.formatters['text/plain']
text_plain.for_type(Markdown, md_formatter)
del text_plain.type_printers[Markdown]


pd.set_option('display.notebook_repr_html', True)
def _repr_latex_(self):
    return self.to_latex()

pd.DataFrame._repr_latex_ = _repr_latex_  # monkey patch pandas DataFrame

# For Display full dataframes column with
pd.set_option('display.max_colwidth', None)
pd.set_option('display.notebook_repr_html', True)

# Suppress Warnings
warnings.filterwarnings('ignore')

# Enconding categorical data of nominal values
sexo_dict = {
    "Hombre":"0",
    "Mujer":"1"
}


nivel_de_estudios_dict = {
    "Carrera técnica con preparatoria terminada":"0",
    "Doctorado":"1",
    "Maestría":"2",
    "Preparatoria / Bachillerato":"3",
    "Profesional":"4"
}

cuatrimestre_dict = {
    "Cuarto":"0",
    "Noveno":"1",
    "Primero":"2",
    "Quinto":"3",
    "Segundo":"4",
    "Tercero":"5"
}

R1_dict = {
    "Escuela":"0",
    "Hogar":"1",
    "Trabajo":"2",
}

R2_dict = {
    "Escuela":"0",
    "Hogar":"1",
    "Trabajo":"2",
}

# List & Dictionary EEP-10 (Type Answers A)
responses_list_A = ['R1', 'R2', 'R3', 'R4', 'R5', 'R8', 'R11', 'R12']
answers_calification_A_dict = {
    "Nunca": 0,
    "Casi nunca": 1,
    "De vez en cuando": 2,
    "A menudo": 3,
    "Muy a menudo": 4
}

# List & Dictionary EEP-10 (Type Answers B) Items: 4, 5, 7, 8
responses_list_B = ['R6', 'R7', 'R9', 'R10']
answers_calification_B_dict = {
    "Nunca": 4,
    "Casi nunca": 3,
    "De vez en cuando": 2,
    "A menudo": 1,
    "Muy a menudo": 0
}

# Encoding table by variable
def display_encoding_table(variable_name):
    if variable_name == 'Sexo':
        display(pd.DataFrame(sexo_dict.items(), columns=['Nominal Value', 'Categorical Value']))
    elif variable_name == 'Nivel de estudios':
        display(pd.DataFrame(nivel_de_estudios_dict.items(), columns=['Nominal Value', 'Categorical Value']))
    elif variable_name == 'Cuatrimestre Cursando':
        display(pd.DataFrame(cuatrimestre_dict.items(), columns=['Nominal Value', 'Categorical Value']))
    elif variable_name == 'R1':
        display(pd.DataFrame(R1_dict.items(), columns=['Nominal Value', 'Categorical Value']))
    elif variable_name == 'R2':
        display(pd.DataFrame(R2_dict.items(), columns=['Nominal Value', 'Categorical Value']))
    elif variable_name in responses_list_A:
        display(pd.DataFrame(answers_calification_A_dict.items(), columns=['Nominal Value', 'Categorical Value']))
    elif variable_name in responses_list_B:
        display(pd.DataFrame(answers_calification_B_dict.items(), columns=['Nominal Value', 'Categorical Value']))

    

# Data Descriotion
response_dict = {
    "R1":"¿Dónde percibes con mayor frecuencia estrés?",
    "R2":"En el ambiente universitario ¿Qué aspecto te provoca más estrés?",
    "R3":"Respecto a las clases de la Licenciatura en Psicología ¿Con qué frecuencia has estado afectado por algo que ha ocurrido inesperadamente?",
    "R4":"¿Con qué frecuencia te has sentido incapaz de controlar las cosas importantes en tu vida?",
    "R5":"¿Con qué frecuencia te has sentido nervioso o estresado?",
    "R6":"¿Con qué frecuencia ha estado seguro sobre su capacidad para manejar sus problemas personales?",
    "R7":"¿Con qué frecuencia has sentido que las cosas te van bien?",
    "R8":"¿Con qué frecuencia has sentido que no podías afrontar todas las cosas que tenías que hacer?",
    "R9":"¿Con qué frecuencia has podido controlar las dificultades en tu vida?",
    "R10":"¿Con qué frecuencia te has sentido que tenía todo bajo control?",
    "R11":"¿Con qué frecuencia has estado enfadado porque las cosas que te han ocurrido estaban fuera de tu control?",
    "R12":"¿Con qué frecuencia has sentido que las dificultades se acumulan tanto que no puedes superarlas?"
}


interpretation_dict = {
    "Sexo":"From genre data, there is more women (75%) than men (%25).",
    "Edad":"From age data, mean and median have approximately the same value however the mode is skewed. We can observe from histogram that ages were concentrated in 20-35 years range and we have an outlier that correspond from someone of 62 years, that causes to have the skewness and the mean and median distanced from mode.",
    "Nivel de estudios":"From studies level data, mean and mode have the same value however the mean is slightly skewed. We can observe from histogram that the studies level is concentrated in ‘Preparatoria’ and ‘Profesional’ level. However, the reason why we don’t have a normal is distribution is due that we have two outliers that corresponds to ‘Carrera técnica con preparatoria terminada’ and ‘Doctorado’.",
    "Escolaridad":"From years of accumulated study data, mean and median have the same value approximately the same value however the mode is skewed, data is concentrated around the 17-10 years of study. However, the reason why we don’t have a normal is distribution is due that we have two outliers that corresponds to lowest value 9 years and the highest value 28.",
    "Cuatrimestre Cursando":"From quarter studying data, mean, median, mode have the same value approximately the same value, that corresponds from people that are in first quarter. However, the reason why we don’t have a normal is distribution is due that we have five outliers that corresponds to people that are in other quarters, the dispersion of the data is high, just a slight concentration of people that is on the first quarter.",
    "(n) de materias cursando":"From (n) of coursing subjects, the mean, median and mode have approximately the same value. Most of the data concentrate in the third value, that means, most of the subjects of the sample were coursing 3 subjects",
    "R1":"From R1, mean and mode have the same value however the mean is skewed. Mean and mode corresponds to ‘Trabajo’. From data, percentages correspond to: 11.4% - ‘Hogar’, 36%.4 - ‘Escuela’ and 52.3% - ‘Trabajo’, half of the sample perceived in the work the stress.",
    "R2":"From R2, median and mode have the same value however the mean is skewed. Mean and mode corresponds to ‘Profesores’. From the data ‘Trabajo en Equipo’ and ‘Profesores’ have the same percentage 9.1%. From the shape of the boxplot and distribution curve, we can observe that the data has a high dispersion among the responses, and we don’t have a normal distribution due to the four outliers that appear in the data.",
    "R3":"From R3, median and mode have the same value however the mean is skewed. Mean and mode corresponds to ‘De vez en cuando’. Median corresponds to 75% percentile, ‘De vez en cuando’ percentage corresponds to 43.2%, there is an outlier that corresponds to ‘Nunca’.",
    "R4":"From R4, we have two Modes that correspond to ‘Casi nunca’ and ‘De vez en cuando’, both percentage values corresponds to 38.6%, that is the reason why we have a Leptokurtic shape due to the data concentration in ‘Casi nunca’ and ‘De vez en cuando response’. There is an outlier that corresponds to ‘Nunca’.",
    "R5":"From R5, mean, median and mode have approximately the same value. The mean corresponds to 25% percentile that is the ‘De vez en cuando’ value and it has the 43.2% percentage from the data. However, from the other responses there is a high dispersion. From this reactive, there wasn’t responses from the sample for ‘Nunca’ option.",
    "R6":"From R6, mean, median and mode have approximately the same value that corresponds to ‘Casi nunca’. Observation from distribution shows that data are skewed and concentrated in the ‘A menudo’ – 45.5% percentage, half of the data, that is the reason why box blot is skewed to the first half, the boxplot starts in the first whisker.",
    "R7":"From R7, mean, median and mode have approximately the same value that corresponds to ‘Casi nunca’ that has 47.7%, mean and median corresponds to the 25% percentile that is the ‘Casi nunca’ value. From the other responses there is a high dispersion from the data.",
    "R8":"From R8, mean, median and mode have approximately the same value that corresponds to ‘De vez en cuando’. Observation from distribution shows that data are skewed and concentrated in the ‘De vez en cuando’ – 38.6% percentage, approximately one third from the data, that is the reason why box blot is skewed to the first half, the boxplot starts in the first whisker.",
    "R9":"From R8, mean, median and mode have approximately the same value that corresponds to ‘De vez en cuando’ that corresponds to 63.6% percentage, that means two thirds from the data. The boxplot seams to be inexistent due to that the data is highly concentrated in ‘De vez en cuando’ value and the remaining data corresponds to the outliers.",
    "R10":"From R10, mean, median and mode have approximately the same value that corresponds to ‘De vez en cuando’. Data is concentrated in ‘De vez en cuando’ – 45.5% and ‘A menudo’ – 38.6%. Median and mode corresponds to the 75% percentile and approximately match with the sum of the 45.5% and 38.6% values percentages.",
    "R11":"From R11, mean, median and mode have approximately the same value that corresponds to ‘De vez en cuando’. The measures of central tendency corresponds with the 50% percentile. The shape of the data shows that most of the values have approximately the same percentage of occurrence and concentrate to the ≈28.78%.",
    "R12":"From R12, mean, median and mode have different values, mode corresponds to ‘Casi nunca’ value – 47.7% of occurrence percentage and median and mode are more near to the ‘De vez en cuando’ value – 25% of occurrence percentage. Distribution is skewed to ‘Casi nunca’ value that is approximately half of the data.",
    "TOTAL":"From total, mean, median and mode have different values, however mean concentrate in the 18 score, lowest score was 6 and highest 32, but most the data in the 10 to 25 score range, that means that comparing with the lowest and highest value most of data is on the center and the assumption is that the perceived stress is in a normal parameter.",
}

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
    f, (ax_box, ax_hist) = plt.subplots(2, sharex=True, figsize=(16,9), gridspec_kw={'height_ratios': [1, 2]})
    
    #Get variable name if is a response, from R1-R12
    variable_name = ""
    if variable in response_dict.keys():
        variable_name = variable + " : " + response_dict[variable]
    else:
        variable_name = variable

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
    ax_hist.axvline(mean, color='g', linestyle='-')
    ax_hist.axvline(median, color='r', linestyle='--')
    ax_hist.axvline(mode, color='b', linestyle='-')

    # add description to plot
    ax_box.set(title="Measures of central tendency: ")
    ax_hist.set(ylabel="Probability of occurrence")
    ax_hist.set(xlabel=variable)
    
    # display measure of central tendency legend
    plt.legend({'Mean':mean,'median':median,'moda':mode})
    
    # Saphiro-Wilk test
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
    display(Markdown('### ' + variable_name))

    # Display categorical encoding table
    display_encoding_table(variable)

    # Show plot
    plt.show()
    
    # Show statistics data
    display(Markdown('**Mean:** ' + str(mean)))
    display(Markdown('**Median:** ' + str(median)))
    display(Markdown('**Mode:** ' + str(mode)))
    display(Markdown('**Analysis:**'))
    display(Markdown('&nbsp;&nbsp;&nbsp;&nbsp;**Kursotis:** ' + str(round(kurtosis_analysis[0], 4)) + ', ' + str(kurtosis_analysis[1])))
    display(Markdown('&nbsp;&nbsp;&nbsp;&nbsp;**Skewness:** ' + str(round(skewness_analysis[0], 4)) + ', ' + str(skewness_analysis[1])))
    display(Markdown('&nbsp;&nbsp;&nbsp;&nbsp;**Normality Test:**'))
    print('\t Saphiro-Wilk Test: ', 'W = ', W, ' p-value = ', p)
    display(Markdown('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**' + normality_test + '**'))
    display(Markdown('**Interpretation of Data:**'))
    print(interpretation_dict[variable])
    display(Markdown('---'))

# Function to get the measures of dispersion
def measures_of_dispersion(df, variable):
    std = df[variable].std()
    var = df[variable].var()
    print(variable + ':')
    print("Standard Deviation: " + str(std))
    print("Variance: " + str(var) + '\n')

# Function to create boxplot
def data_boxplot(df, title_name, x_label_name, y_label_name):
    # set boxplot colors
    sns.set_palette(sns.color_palette(["#ff1493"]))

    # set size and create boxplotfigure
    f, (ax_box) = plt.subplots(figsize=(16, 9))

    # assigning a graph to each ax and set graph text
    sns.boxplot(data=df, ax=ax_box, dodge=False)
    ax_box.set_title(title_name, fontsize=20)
    ax_box.set_xlabel(x_label_name, fontsize=10)
    ax_box.set_ylabel(y_label_name, fontsize=10)

    # show plot
    plt.show()

# Function to create boxplot for two variables
def data_variable_boxplot(df, x_variable, y_variable, title_name, x_label_name, y_label_name):
       # Display categorical encoding table
    display_encoding_table(x_variable)
    
    # set boxplot colors
    sns.set_palette(sns.color_palette(["#ff1493"]))

    # set size and create boxplotfigure
    f, (ax_box) = plt.subplots(figsize=(16, 9))

    # assigning a graph to each ax and set graph text
    sns.boxplot(x = x_variable, y = y_variable, data=df , ax=ax_box, dodge=False)
    ax_box.set_title(title_name, fontsize=20)
    ax_box.set_xlabel(x_label_name, fontsize=10)
    ax_box.set_ylabel(y_label_name, fontsize=10)

    # show plot
    plt.show()

# Boxplot for EEP-10 Instrument Responses
def boxplot_instrument_responses(df, group):
    if group == 'A':
        responses_values_A = [response_dict[x] for x in responses_list_A if x in response_dict]
        responses_A = {'Key': responses_list_A, 'Value': responses_values_A}
        display(pd.DataFrame(responses_A))
        display(pd.DataFrame(answers_calification_A_dict.items(), columns=['Nominal Value', 'Categorical Value']))
        df_responses_A = df.filter(responses_list_A, axis=1)
        data_boxplot(df_responses_A, "EEP-10, Group A", "Questions", "Answers")
    elif group == 'B':
        responses_values_B = [response_dict[x] for x in responses_list_B if x in response_dict]
        responses_B = {'Key': responses_list_B, 'Value': responses_values_B}
        display(pd.DataFrame(responses_B))
        display(pd.DataFrame(answers_calification_B_dict.items(), columns=['Nominal Value', 'Categorical Value']))
        df_responses_B = df.filter(responses_list_B, axis=1)
        data_boxplot(df_responses_B, "EEP-10, Group B", "Questions", "Answers")







    

        
        

