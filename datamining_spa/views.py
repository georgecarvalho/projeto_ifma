from django.shortcuts import render
import numpy as np
import pandas as pd
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

from matplotlib import pyplot as plt

import seaborn as sns
""" import missingno as msno """

def index(request):
    return render(request, 'index.html')


def dashboard(request):
    url = 'https://dadosjuventude.ibict.br/dataset/5e28ed5a-bae5-4653-9a78-4b229daf1f8f/resource/12edf31d-0d53-4b6b-941c-396ee353807a/download/eixo4_distribuicaoracacor_2010.csv'
    df = pd.read_csv(url)
    df.head()

    sns.kdeplot(df.Branca,shade=True)

    x = [6, 7, 4]  # Base
    y = [2, 6, 2]  # Altura

    titulo = "dado aluno"
    eixox = "Eixo X"
    eixoy = "Eixo Y"

    print("hello")

    grafico = plt.title(titulo)
    grafico = plt.xlabel(eixox)
    grafico = plt.ylabel(eixoy)
    grafico = plt.plot(x, y)
    grafico = plt.savefig('media/grafico/graficos.png', dpi=72)
    return render(request, 'index.html', {'grafico': grafico})
