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
list_dict = [
    {'26-35': 0, '36-45': 1, '46-55': 2},
    {'Biparental (los dos padres)': 0, 'Monoparental (madre o padre soltero)': 1},
    {'$11,000-$15,000 pesos': 0, '$16,000-$20,000 pesos': 1, '$21,000-$25,000 pesos': 2, '$5,000-$10,000 pesos': 3, 'Más de 25,000 pesos': 4},
    {'No': 0, 'Sí': 1},
    {'Número de hijos': '', 'Número de hijos': ''},
    {'Carrera técnica': 0, 'Estudios universitarios': 1, 'Maestría': 2, 'Preparatoria o bachillerato': 3, 'Primaria': 4},
    {'No': 0, 'Sí': 1},
    {'Privada': 0, 'Pública': 1},
    {'Desinterés de los hijos por las clases en línea/virtuales': 0, 'Falta de recursos': 1, 'Falta de tiempo para dar seguimiento a las clases virtuales/híbridas/programa en línea': 2, 'Insatisfacción de clases/asesorías en línea': 3, 'Porque la educación es irrelevante en este momento': 4},
    {'Contenido pobre o irrelevante del programa': 0, 'Elevada carga de trabajo': 1, 'Mala actitud de los docentes hacia los alumnos': 2, 'Poco control de grupo por parte de los maestros': 3, 'Prioridad a las evaluaciones por encima del aprendizaje': 4, 'Prisa en cubrir los temas del programa': 5},
    {'<NA>': -1, 'Acompañamiento emocional': 0, 'Atención personalizada': 1, 'Autonomía en la educación': 2, 'Programa personalizado': 3},
    {'1-6 meses': 0, '13-18 meses': 1, '7-12 meses': 2, 'más de 19 meses': 3},
    {'1 a 3 meses': 0, 'Más de 1 año': 1, 'Más de 3 meses': 2, 'Más de 6 meses': 3},
    {'Me informé por mi cuenta': 0, 'Más de una de las opciones anteriores': 1, 'Tomé un curso/taller': 2, 'Una persona me brindó información': 3},
    {'Alternando más de una de las opciones anteriores': 0, 'Comunidad de aprendizaje (Sin registro ante la SEP)': 1, 'Con escuela sombrilla': 2, 'Con un tutor': 3, 'Fuera de la escuela pero con un programa': 4, 'Sin programa, de forma libre': 5},
    {'Mucho': 0, 'Nada': 1, 'Poco': 2, 'Suficiente': 3},
    {'Aprendizaje de calidad': 0, 'Certificado': 1, 'Que mi(s) hijo(s) sigan las tendencias actuales de la educación': 2},
    {'Elegir el contenido a revisar': 0, 'Encontrar forma de validar estudios': 1, 'Encontrar la información y recursos educativos para cubrir los temas': 2, 'Mantener el interés de los niños en el aprendizaje': 3, 'Tener apoyo familiar': 4},
    {'Mucha dificultad': 0, 'Ninguna dificultad': 1, 'Poca dificultad': 2},
    {'Material digital en sitios especializados en educación': 0, 'Material disponible en la red en sitios no especializados': 1, 'Material impresos (libros, revistas, enciclopedias)': 2, 'Otro': 3},
    {'Mejorado': 0, 'Sigue igual': 1},
    {'Sin cambios': 0, 'Sí': 1},
    {'Igual': 0, 'Mayor': 1, 'Menor': 2},
    {'No': 0},
    {'Con compañeros de talleres o clases extracurriculares': 0, 'Con familiares': 1, 'Con personas del vecindario': 2},
    {'Mejor actitud': 0, 'Misma actitud': 1, 'Peor actitud': 2},
    {'Educación en casa con programa (Homeschooling)': 0, 'Educación en casa sin programa (Unschooling)': 1},
    {'No': 0, 'No estoy segura': 1, 'Sí': 2},
    {'Los niños': 0, 'Los padres': 1, 'Más de uno de los anteriores': 2, 'Un programa diferente a la SEP': 3},
    {'No': 0, 'Sí': 1},
    {'Busca a alguien más que pueda impartir el contenido (maestro, tutor, plataforma)': 0, 'Descarta el tema': 1, 'Investiga del tema para poder enseñar a su(s) hijo(s)': 2, 'Investiga y busca apoyo en alguien más experimentado en el tema': 3},
    {'Empeorado': 0, 'Mejorado': 1, 'Se mantienen igual': 2},
    {'Autonomía en el aprendizaje': 0, 'Herramientas de aprendizaje': 1, 'Herramientas de gestión emocional': 2},
    {'Mayor responsabilidad': 0, 'Menor responsabilidad': 1, 'Misma responsabilidad que en la escuela': 2},
    {'Ha disminuído': 0, 'Ha incrementado': 1, 'Ha permanecido igual': 2}
]


# Saphiro-Wilk test
def saphiro_test(data):
    stat, p = stats.shapiro(data)
    
    return (stat, p)

# Kurtosis and curve distribution
def kurtosis(data):
    distribution_type = ""
    k = stats.kurtosis(data)
    if k > 0:
        distribution_type = "Leptocúrtica"
    elif k == 0:
        distribution_type = "Mesocúrtica"
    elif k < 0:
        distribution_type = "Platicúrtica"
        
    return (k, distribution_type)

# Skewness 
def skewness(data):
    assymetry_type = ""
    s = stats.skew(data)
    if s > 0:
        assymetry_type = "Asimetría Derecha (+)"
    elif s == 0:
        assymetry_type = "Simétrica"
    elif s < 0:
        assymetry_type = "Asimetría Izquierda (-)"
        
    return (s, assymetry_type)

# Function to get the measures of the center of the data (mode, median and mean)
def measures_of_center(df, variable, i):
    # creating a figure composed of a boxplot and histogram
    f, (ax_box, ax_hist) = plt.subplots(2, sharex=True, figsize=(16,9), gridspec_kw={'height_ratios': [1, 2]})
    
    # calculate measures of central tendency
    mean=round(df[variable].mean(), 4)
    median=round(df[variable].median(), 4)
    mode=round(df[variable].mode().tolist()[0], 4)

    # calculate measures of dispersion
    std_deviation = round(df[variable].std(), 4)
    variance = round(df[variable].var(), 4)
    
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
    ax_box.set(title="Medidas de Tendencia Central")
    ax_hist.set(ylabel="Probabilidad de Ocurrencia")
    ax_hist.set(xlabel=variable)
    
    # display measure of central tendency legend
    plt.legend(['moda', 'media', 'mediana'])
    
    # Saphiro-Wilk test
    saphiro_stats = saphiro_test(df[variable])
    W = round(saphiro_stats[0], 4)
    p = saphiro_stats[1]
    if p > 0.05:
        normality_test = "H0: La variable tiene una distribución normal"
    else:
        normality_test = "H1: La variable no tiene una distribución normal"
    
    # Kurtosis Analysis
    kurtosis_analysis = kurtosis(df[variable])
    
    # Skewness Analysis
    skewness_analysis = skewness(df[variable])
    
    # Display Tittle
    display(Markdown('### ' + variable))

    # Display categorical encoding table
    display(pd.DataFrame(list_dict[i].items(), columns=['Valor Nominal', 'Valor Categórico']))

    # Show plot
    plt.show()

    # Pie graph
    plt.figure(figsize = (6,6))
    index = df[variable].value_counts()
    index.plot.pie(
        y=index,
        shadow=False,
        startangle=90,
        autopct='%1.1f%%'
    )

    # fig = plt.figure(figsize = [10, 10])
    plt.axis('equal')
    plt.show()
    
    
    # Show statistics data
    display(Markdown('**Media:** ' + str(mean)))
    display(Markdown('**Mediana:** ' + str(median)))
    display(Markdown('**Moda:** ' + str(mode)))
    display(Markdown('**Análisis de Distribución:**'))
    display(Markdown('&nbsp;&nbsp;&nbsp;&nbsp;**cursotis:** ' + str(round(kurtosis_analysis[0], 4)) + ', ' + str(kurtosis_analysis[1])))
    display(Markdown('&nbsp;&nbsp;&nbsp;&nbsp;**Sesgo:** ' + str(round(skewness_analysis[0], 4)) + ', ' + str(skewness_analysis[1])))
    display(Markdown('&nbsp;&nbsp;&nbsp;&nbsp;**Prueba de Normalidad:**'))
    print('\t Prueba Saphiro-Wilk: ', 'W = ', W, ' p-value = ', p)
    display(Markdown('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**' + normality_test + '**'))
    display(Markdown('**Desviación Estándar:** ' + str(std_deviation)))
    display(Markdown('**Varianza:** ' + str(variance)))
    display(Markdown('---'))

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







    

        
        

