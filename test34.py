import streamlit as st # creazione interfaccia web
from PIL import Image # importare immagini come ico per logo
import pandas as pd # usato per creazione DataFrame da CSV



def estrai_colonna(chiave):
    colonna = file[chiave].values # estraggo collona senza indice
    colonna = colonna.tolist() # conversione numpy -> list
    return colonna

def ricavoTotale_Area(chiave):
    colonna = estrai_colonna(chiave)
    ricavo = sum(colonna)
    text = str(round(ricavo,4)) + " Milion" # round -> troncamento numeri
    return text

file = pd.read_csv('videogame.csv', index_col=['Rank'])
ricavoTotale_Area('Global_Sales')