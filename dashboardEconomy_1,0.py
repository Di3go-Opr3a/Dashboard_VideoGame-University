import streamlit as st # creazione interfaccia web
from PIL import Image # importare immagini come ico per logo
import pandas as pd # usato per creazione DataFrame da CSV
import plotly.express as px

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


def sommaElementi_XY(listaFix, listaFix_default, listaValue_default, memoria):
    for x in (listaFix):
        for y in range(len(listaFix_default)):
                if x == listaFix_default[y]:
                    posizione = listaFix.index(x)
                    memoria[posizione] += float(listaValue_default[y])
    return memoria
    

def piechart(matrice):
    fig = px.pie(file, values=matrice[1], names=matrice[0])
    
    return st.plotly_chart(fig, use_container_width=True)


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

        piechart(piattaforme)

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




#     radar = st.columns(1)

#     # Radar di Piattaforme vs Genere
#     with radar:
#         option = {
#             "legend": {"data": piattaforme[0]},
#             "radar": {
#                 "indicator": [
#                     {"name": "Sports", "max": 6500},
#                     {"name": "Platform", "max": 16000},
#                     {"name": "Racing", "max": 30000},
#                     {"name": "Role-Playing", "max": 38000},
#                     {"name": "Puzzle", "max": 52000},
#                     {"name": "Misc", "max": 25000},
#                     {"name": "Shooter", "max": 25000},
#                     {"name": "Simulation", "max": 25000},
#                     {"name": "Action", "max": 25000},
#                     {"name": "Fighting", "max": 25000},
#                     {"name": "Adventure", "max": 25000},
#                     {"name": "Strategy", "max": 25000},
#                 ]
#             },
#             "series": [{   
#                 "type": "radar",
#                 "data": [
#                     {
#                         "value": [4200, 21000, 20000, 3400, 50000, 18000, 28100, 7000, 8000, 21000, 20000, 23050],
#                         "name": "PC",
#                     },
#                     {
#                         "value": [4800, 3000, 20000, 37000, 50000, 18000, 11000, 10000, 9000, 21000, 40000, 23000],
#                         "name": "PS4",
#                     },
#                     {
#                         "value": [4200, 3000, 20000, 35000, 50000, 18000, 12000, 5000, 9000, 21000, 40000, 23000],
#                         "name": "PSP",
#                     },
#                     {
#                         "value": [4200, 3000, 20000, 35000, 50000, 18000, 12000, 5000, 9000, 21000, 40000, 23000],
#                         "name": "X360",
#                     },
#                     {
#                         "value": [4200, 3000, 20000, 35000, 50000, 18000, 12000, 5000, 9000, 21000, 40000, 23000],
#                         "name": "DS",
#                     },
#                     {
#                         "value": [4200, 3000, 20000, 35000, 50000, 18000, 12000, 5000, 9000, 21000, 40000, 23000],
#                         "name": "WiiU",
#                     },
#                     {
#                         "value": [4200, 3000, 20000, 35000, 50000, 18000, 12000, 5000, 9000, 21000, 40000, 23000],
#                         "name": "Wii",
#                     },
#                     {
#                         "value": [4200, 3000, 20000, 35000, 50000, 18000, 12000, 5000, 9000, 21000, 40000, 23000],
#                         "name": "3DS",
#                     },
#                 ],
#             }],
#         }
#         st_echarts(option, height="500px")

# # colonna = estrai_colonna('Genre')
# # colonna = rimuovi_clone(colonna)





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