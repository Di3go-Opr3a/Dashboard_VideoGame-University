import pandas as pd # installare pip pandas (lettura CSV)
import streamlit as st # installare pip streamlit (visual 3D)

# importazione dati da file csv in variabile tabella
# 'CSV/' perchè il file sta in una cartella
table = pd.read_csv('CSV/videogame.csv')

# Creazione Pagina Dashboard
st.set_page_config(page_title="Dashboard Economy | StrealmClix",
                   page_icon=":bar_chart:",
                   layout="wide") # logo che non abbiamo

# per vedere la tabella nella schermata
st.dataframe(table)


# PER APRIRE SCHEDA WEB SCRIVERE COMANDO TERMINALE: streamlit run dashboardEconomy.py