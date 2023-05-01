import pandas as pd # pip install pandas
import streamlit as st # pip install streamlit
import matplotlib.pyplot as plt # pip install matplotlib
import numpy as np

def estrai_colonna(key):
    file[key] = file[key].astype(str)
    colonna = file[key].values # estraggo collona con titolo 'Platform' senza indice
    colonna = colonna.tolist() # conversione numpy -> list

    return colonna


def rimuovi_clone(lista_default):
    # salva solo elementi con valore
    def esistenza(valore):
        if valore != 'nan':
            return True
        else:
            return False  
    
    lista = []
    
    for valore in lista_default:
        if valore not in lista: 
            lista.append(valore)

    lista = list(filter(esistenza, lista))
    return lista


 # creo celle con valore nullo quante sono nella riga 0
def creazione_cella(matrice):
    count = len(matrice[0])
    matrice[1] = [None] * count


 # assegno valore zero alle celle nulle
def assegnazione_cella0(matrice):
    count = len(matrice[0])

    for valore in range(count):
        matrice[1][valore] = 0


def piechart(matrice):
    fig1, ax1 = plt.subplots()

    # Distanza tra elementi
    explode = (0, 0, 0, 0.1, 0 , 0, 0, 0.1, 0, 0, 0)

    # autopct = Numero percentuale mostrato
    # startangle = parte da 90 gradi
    ax1.pie(matrice[1], labels=matrice[0], autopct='%1.1f%%', startangle=90, explode=explode)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    
    return st.pyplot(fig1)



file = pd.read_csv('videogame.csv', index_col=['Rank'])

### DATAFRAME in vista
st.dataframe(file)


### GRAFICO PIE CHART con Piattaforme
colonna_file = estrai_colonna('Platform')

# colonna_file = rimuovi_clone(colonna_file)
piattaforme = [['PC', 'PS4', 'PS3', 'PS2', 'PSP', 'X360', 'XOne', 'DS', 'WiiU', 'Wii', '3DS'],
               []]

creazione_cella(piattaforme)
assegnazione_cella0(piattaforme)

# conteggio elementi tra collona e matrice
for valore in range(len(piattaforme[0])):
        for valore_default in colonna_file:
            if valore_default == piattaforme[0][valore]:
                piattaforme[1][valore] += 1

# mando a schermo il grafico
piechart(piattaforme)


### GRAFICO A LINEE con Anni e Profitto
colonna_file = estrai_colonna('Year')
colonna_file2 = estrai_colonna('Global_Sales')

anno_profitto = [[],[]]
anno_profitto[0] = rimuovi_clone(colonna_file)
creazione_cella(anno_profitto)
assegnazione_cella0(anno_profitto)

for x in (anno_profitto[0]):
    for y in colonna_file:
        if x == y:
            posizione = anno_profitto[0].index(x)
            posizione_default = colonna_file.index(y)
            anno_profitto[1][posizione] += float(colonna_file2[posizione_default])

df = pd.DataFrame({
  'date': anno_profitto[0],
  'second column': anno_profitto[1]
})

df = df.rename(columns={'date':'index'}).set_index('index')

st.line_chart(df)