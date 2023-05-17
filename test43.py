import streamlit as st # creazione interfaccia web
from PIL import Image # importare immagini come ico per logo
import pandas as pd # usato per creazione di vari DataFrame da CSV
import plotly.express as px # creazione pie chart
from streamlit_echarts import st_echarts # creazione radar
import numpy as np # creazione celle zeros


def rimuovi_clone(lista_default):
    lista = []
    
    for valore in lista_default:
        if valore not in lista: 
            lista.append(valore)

    # elimino celle nulle
    lista = list(filter(esistenza, lista))
    return lista


def esistenza(valore):
        if valore != 'nan':
            return True
        else:
            return False 
        
def estrai_colonna(chiave):
    colonna = file[chiave].values # estraggo collona senza indice
    colonna = colonna.tolist() # conversione numpy -> list
    return colonna

file = pd.read_csv('videogame.csv', index_col=['Rank'])

colonna = estrai_colonna('Year')
colonna = rimuovi_clone(colonna)
colonna = list(map(str, colonna))
cleanedList = [x for x in colonna if x != 'nan']
cleanedList = list(map(float, cleanedList ))
cleanedList = list(map(int, cleanedList ))
print(cleanedList)
