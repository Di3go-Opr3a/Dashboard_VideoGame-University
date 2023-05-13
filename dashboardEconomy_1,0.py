import streamlit as st # creazione interfaccia web
from PIL import Image # importare immagini come ico per logo
import pandas as pd # usato per creazione DataFrame da CSV
import plotly.express as px # create a pie chart
from streamlit_echarts import st_echarts
import numpy as np


def estrai_colonna(chiave):
    colonna = file[chiave].values # estraggo collona senza indice
    colonna = colonna.tolist() # conversione numpy -> list
    return colonna


def ricavoTotale_Area(chiave):
    colonna = estrai_colonna(chiave) # richiamo funzione
    text = str(round(sum(colonna),4)) + " M" # round -> troncamento numeri
    return text


# creo celle con valore nullo quante sono nella riga 0
def creazione_cella(matrice):
    count = len(matrice[0])
    matrice[1] = [None] * count


# assegno valore zero alle celle nulle
def assegnazione_cella0(matrice):
    count = len(matrice[0])

    for valore in range(count):
        matrice[1][valore] = 0


def esistenza(valore):
        if valore != 'nan':
            return True
        else:
            return False 
        

def rimuovi_clone(lista_default):
    lista = []
    
    for valore in lista_default:
        if valore not in lista: 
            lista.append(valore)

    # elimino celle nulle
    lista = list(filter(esistenza, lista))
    return lista


# conteggio elementi tra due liste
def contaElementi_XY(lista, lista_default, memoria):
    for x in range(len(lista)):
        for y in lista_default:
            if y == lista[x]:
                memoria[x] += 1

    return memoria


# somma elementi tra due liste
def sommaElementi_XY(listaFix, listaFix_default, listaValue_default, memoria):
    for x in (listaFix):
        for y in range(len(listaFix_default)):
                if x == listaFix_default[y]:
                    posizione = listaFix.index(x)
                    memoria[posizione] += float(listaValue_default[y])
    return memoria


# HEADER
logo = Image.open("image.ico")

st.set_page_config(
    page_title="StrealClix",
    page_icon= logo,
    layout="wide", # prende tutto lo schermo
    initial_sidebar_state="auto" # menu di lato (aperta o chiusa),
)

# MAIN CONTENT
# Banner
st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown('''
<nav class="navbar fixed-top navbar-expand-lg navbar-dark bannerStrealClix" style="background-color: #fff;">
  <img src="https://shorturl.at/hoHT0" />
</nav>
<style>
.bannerStrealClix img {width: 23%; margin: auto;}
''', unsafe_allow_html=True)

hide_menu_style = '''
<style>
header {visibility:hidden;}
#MainMenu {visibility: hidden;}str
'''
st.markdown(hide_menu_style, unsafe_allow_html=True)


file = pd.read_csv('videogame.csv', index_col=['Rank'])

with st.container():
    # Somma Profitti Totali Aree Geografiche
    RicavoTotale, Europa, America, Giappone, AltriContinenti = st.columns(5)

    RicavoTotale.metric("Profitto Totale", ricavoTotale_Area('Global_Sales'))
    Europa.metric("Europa", ricavoTotale_Area('EU_Sales'))
    America.metric("America", ricavoTotale_Area('NA_Sales'))
    Giappone.metric("Giappone", ricavoTotale_Area('JP_Sales'))
    AltriContinenti.metric("AltriContinenti", ricavoTotale_Area('Other_Sales'))


    st.dataframe(file)


    pieChart, diagrammaLinee = st.columns([1, 1.5], gap='large')
    # Grafico a Torta con Percentuali Piattaforme
    with pieChart:
        colonna = estrai_colonna('Platform')
        # colonna = rimuovi_clone(colonna_file)
        # piattaforme = [[colonna], []] essendo troppe selezioniamo manualmente quelle più interessanti
        piattaforme = [['PC', 'PS4', 'PS3', 'PS2', 'PSP', 'X360', 'XOne', 'DS', 'WiiU', 'Wii', '3DS'],[]]
        creazione_cella(piattaforme)
        assegnazione_cella0(piattaforme)
        piattaforme[1] = contaElementi_XY(piattaforme[0], colonna, piattaforme[1])

        fig = px.pie(file, values=piattaforme[1], names=piattaforme[0])
        st.plotly_chart(fig, use_container_width=True)


    # Diagramma con Anno e Profitto
    with diagrammaLinee:
        colonna = estrai_colonna('Year')
        colonna2 = estrai_colonna('Global_Sales')

        anno_profitto = [[],[]]
        anno_profitto[0] = rimuovi_clone(colonna)
        creazione_cella(anno_profitto)
        assegnazione_cella0(anno_profitto)

        anno_profitto[1] = sommaElementi_XY(anno_profitto[0], colonna, colonna2, anno_profitto[1])
        
        df = pd.DataFrame({
            'date': anno_profitto[0],
            'second column': anno_profitto[1]
        })

        df = df.rename(columns={'date':'index'}).set_index('index')
        st.line_chart(df)


    radar, pubblicazioni = st.columns(2)

    # Radar di Piattaforme vs Genere
    colonna = estrai_colonna('Platform')
    colonna2 = estrai_colonna('Genre')
    cicloGenre = rimuovi_clone(colonna2)
    cicloGenre = cicloGenre[0:(len(cicloGenre)//2)]

    PC = [[], []]
    for x in cicloGenre:
        PC[0].append(x)

    creazione_cella(PC)
    assegnazione_cella0(PC)


    Wii = [[], []]
    for x in cicloGenre:
        Wii[0].append(x)

    creazione_cella(Wii)
    assegnazione_cella0(Wii)      



    list_name = ["PC", "Wii"]
    matrix = [[PC], [Wii]]

    # matrix[0] , matrix[0][0] = PC
    # matrix[1] , matrix[1][0] = Wii
    # matrix[1][1] , matrix[0][1] = ERROR
    # matrix[1][0][0] = ['fagioli', 'fragole'] -> Wii
    # matrix[1][0][0][0] = fagioli

    # matrix[0][0][0] = ['Sport', 'Surf'] -> PC
    # matrix[0][0][0][0] = Sport
    
    for x in range(len(colonna)):
        for y in range(len(list_name)):
            if colonna[x] == list_name[y]:
                for b in range(len(matrix[y][0][0])):
                    if colonna2[x] == matrix[y][0][0][b]:
                        matrix[y][0][1][b] = matrix[y][0][1][b] + 1
                        break
                            
    print(matrix)
    
    with radar:
        option = {
            "legend": {"data": (list_name)}, # divido le piattaforme in quanto troppe
            "radar": {
                "indicator": [
                    {"name": cicloGenre[0], "max": 300},
                    {"name": cicloGenre[1], "max": 300},
                    {"name": cicloGenre[2], "max": 300},
                    {"name": cicloGenre[3], "max": 300},
                    {"name": cicloGenre[4], "max": 300},
                    {"name": cicloGenre[5], "max": 300},
                ]
            },
            "series": [{   
                "type": "radar",
                "data": [
                    {
                        "value": matrix[0][0][1],
                        "name": list_name[0],
                    },
                    {
                        "value": matrix[1][0][1],
                        "name": list_name[1],
                    },
                ],
            }],
        }
        
        st_echarts(option, height="500px")





# Style Profitti Totali Aree Geografiche
st.markdown('''
<style>
.css-1m02ktg .css-j5r0tf {width: 12%; margin-right: auto;flex: none;}
.css-ocqkz7 {gap:0}
.css-1xarl3l {font-size: 2.00rem;}
.css-t4htji {border: 3px solid #d09f14; padding: 3px; border-radius: 10px 0 10px 0;}
''', unsafe_allow_html=True)

# Style DataFrame
st.markdown('''
<style>
.stDataFrame {margin-top: 20px;}
''', unsafe_allow_html=True)


hide_footer_style = '''
<style>
.appview-container .main footer {visibility: hidden;}
'''
st.markdown(hide_footer_style, unsafe_allow_html=True)


















