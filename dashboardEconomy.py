import pandas as pd # pip install pandas
import streamlit as st # pip install streamlit
import matplotlib.pyplot as plt # pip install matplotlib

def estrai_colonna(key):
    file[key] = file[key].astype(str)
    colonna = file[key].values # estraggo collona con titolo 'Platform' senza indice
    colonna = colonna.tolist() # conversione numpy -> list

    return colonna

def esistenza(valore):
        if valore != 'nan':
            return True
        else:
            return False 
        
def rimuovi_clone(lista_default):
    # salva solo elementi con valore
    
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
    



file = pd.read_csv('videogame.csv', index_col=['Rank'])
print(file)

### TOTALE VENDITE
colonna_file2 = estrai_colonna('Global_Sales')
colonna_file2 = [float(x) for x in colonna_file2]
ricavo = sum(colonna_file2)
text = str(round(ricavo,4)) + " Milion"

colonna_file2 = estrai_colonna('NA_Sales')
colonna_file2 = [float(x) for x in colonna_file2]
ricavo = sum(colonna_file2)
text2 = str(round(ricavo,4)) + " Milion"

colonna_file2 = estrai_colonna('EU_Sales')
colonna_file2 = [float(x) for x in colonna_file2]
ricavo = sum(colonna_file2)
text3 = str(round(ricavo,4)) + " Milion"

colonna_file2 = estrai_colonna('JP_Sales')
colonna_file2 = [float(x) for x in colonna_file2]
ricavo = sum(colonna_file2)
text4 = str(round(ricavo,4)) + " Milion"

colonna_file2 = estrai_colonna('Other_Sales')
colonna_file2 = [float(x) for x in colonna_file2]
ricavo = sum(colonna_file2)
text5 = str(round(ricavo,4)) + " Milion"

col1, col2, col3 = st.columns(3)

col4, col5 = st.columns(2)

col1.metric("Ricavo Totale", text)
col2.metric("America", text2)
col3.metric("Europa", text3)

col4.metric("Giappone", text4)
col5.metric("Altri Continenti", text5)


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
    for y in range(len(colonna_file)):
        if x == colonna_file[y]:
            posizione = anno_profitto[0].index(x)
            anno_profitto[1][posizione] += float(colonna_file2[y])

df = pd.DataFrame({
  'date': anno_profitto[0],
  'second column': anno_profitto[1]
})

df = df.rename(columns={'date':'index'}).set_index('index')

st.line_chart(df)


# GRAFICO A BARRE con Publisher
colonna_file = estrai_colonna('Publisher')
colonna_file = list(filter(esistenza, colonna_file)) # possibili spazi vuoti

publicazione = [[],[]]
publicazione[0] = rimuovi_clone(colonna_file)
creazione_cella(publicazione)
assegnazione_cella0(publicazione)

for valore in range(len(publicazione[0])):
        for valore_default in range(len(colonna_file)):
            if publicazione[0][valore] == colonna_file[valore_default]:
                publicazione[1][valore] += 1

list = []
list2 = []

for x in range(len(publicazione[1])):
    if publicazione[1][x] > 25:
        list2.append(publicazione[0][x])
        list.append(publicazione[1][x])

publicazione[0] = list2
publicazione[1] = list

df = pd.DataFrame({
  'date': publicazione[0],
  'second column': publicazione[1]
})

df = df.rename(columns={'date':'index'}).set_index('index')

st.bar_chart(df)
