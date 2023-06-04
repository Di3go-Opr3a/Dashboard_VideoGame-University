import streamlit as st # creazione interfaccia web
from PIL import Image # importazione immagini come ico per logo
import pandas as pd # usato per creazione di vari DataFrame da CSV
import plotly.express as px # creazione pie chart
from streamlit_echarts import st_echarts # creazione radar
import numpy as np # creazione celle zeros
import altair as alt # inserire nomi agli assi


def estrai_colonna(chiave):
    colonna = file[chiave].values # estrazione colonna senza indice
    colonna = colonna.tolist() # conversione numpy -> list
    return colonna


def ricavoTotale_Area(chiave):
    colonna = estrai_colonna(chiave) # richiamo alla funzione
    text = str(round(sum(colonna),4)) + " M" # round -> troncamento numeri
    return text


# creazione di tante celle con valore nullo quante sono nella riga 0
def creazione_cella(matrice):
    count = len(matrice[0])
    matrice[1] = [None] * count


# assegnazione del valore zero alle celle nulle
def assegnazione_cella0(matrice):
    matrice[1] = np.zeros(len(matrice[0]), dtype=int) # crea array di zero
    matrice[1] = matrice[1].tolist() # convertire da array a lista


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

    # eliminazione di celle nulle
    lista = list(filter(esistenza, lista))
    return lista


def matrixRadar(matrice):
    for x in cicloGenre:
        matrice[0].append(x)

    creazione_cella(matrice)
    assegnazione_cella0(matrice)

    return matrice


def multychart_value(text, colonna, anni):
    listValue = [0] * len(anni)
    colonna2 = estrai_colonna(text)

    for x in range(len(colonna)):
        for y in range(len(anni)):
            if colonna[x] == anni[y]:
                listValue[y] = listValue[y] + colonna2[x]

    return listValue


# HEADER
icon = Image.open("image.ico")

st.set_page_config(
    page_title="StrealmClix",
    page_icon= icon,
    layout="wide", # prende tutto lo schermo
    initial_sidebar_state="auto"  # menu di lato (aperta o chiusa)
)

hide_menu_style = '''
<style>
header {visibility:hidden;}
#MainMenu {visibility: hidden;}str
'''
st.markdown(hide_menu_style, unsafe_allow_html=True)


# MAIN CONTENT
# Banner
st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown('''
<nav class="navbar navbar-expand-lg navbar-dark bannerStrealClix" style="background-color: #fff;">
    <iframe src="https://embed.lottiefiles.com/animation/143963"></iframe>
    <img src="https://drive.google.com/uc?export=view&id=19JI8HlQ-4BvQRzpTgZvrUcaXTALn70Uf">
</nav>
<style>
.bannerStrealClix img {width: 23%; margin: auto;}
.css-z5fcl4 {padding: 0 5rem 0 5rem}
.bannerStrealClix iframe {position: absolute; width: 10%; height: auto; margin-left: 2rem}
''', unsafe_allow_html=True)


file = pd.read_csv('videogame.csv', index_col=['Rank'])

with st.container():
    # Somma Profitti Totali Aree Geografiche
    RicavoTotale, Europa, America, Giappone, AltriContinenti = st.columns(5)
                
    RicavoTotale.metric("Profitto Totale", ricavoTotale_Area('Global_Sales'))
    Europa.metric("Europa", ricavoTotale_Area('EU_Sales'))
    America.metric("America", ricavoTotale_Area('NA_Sales'))
    Giappone.metric("Asia", ricavoTotale_Area('JP_Sales'))
    AltriContinenti.metric("AltriContinenti", ricavoTotale_Area('Other_Sales'))



    dataframe, radar = st.columns([1.5, 1], gap="medium")
    
    with dataframe:
        st.subheader(':globe_with_meridians: :red[Dataframe StrealmClix]')
        st.dataframe(file)
    
    # Radar di Piattaforme vs Genere
    colonna = estrai_colonna('Platform')
    colonna2 = estrai_colonna('Genre')
    cicloGenre = rimuovi_clone(colonna2)
    cicloGenre = ['Sports', 'Action', 'Role-Playing', 'Misc', 'Shooter', 'Strategy', 'Adventure']

    PC = [[], []]
    PC = matrixRadar(PC)

    Wii = [[], []]
    Wii = matrixRadar(Wii)      

    PSP = [[],[]]
    PSP = matrixRadar(PSP)

    PS4 = [[],[]]
    PS4 = matrixRadar(PS4)

    X360 = [[],[]]
    X360 = matrixRadar(X360)

    list_name = ["PC", "Wii", "PSP", "PS4", "X360"]
    matrix = [[PC], [Wii], [PSP], [PS4], [X360]]
    
    # Contatore - Quanti generi corispondono alle singole piattaforme?
    for x in range(len(colonna)):
        for y in range(len(list_name)):
            if colonna[x] == list_name[y]:
                for b in range(len(matrix[y][0][0])):
                    if colonna2[x] == matrix[y][0][0][b]:
                        matrix[y][0][1][b] = matrix[y][0][1][b] + 1
                        break

    with radar:
        option = {
            "legend": {"data": (list_name)},
            "radar": {
                "indicator": [
                    {"name": cicloGenre[0], "max": 300},
                    {"name": cicloGenre[1], "max": 400},
                    {"name": cicloGenre[2], "max": 300},
                    {"name": cicloGenre[3], "max": 300},
                    {"name": cicloGenre[4], "max": 300},
                    {"name": cicloGenre[5], "max": 300},
                    {"name": cicloGenre[6], "max": 300},
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
                    {
                        "value": matrix[2][0][1],
                        "name": list_name[2],
                    },
                    {
                        "value": matrix[3][0][1],
                        "name": list_name[3],
                    },
                    {
                        "value": matrix[4][0][1],
                        "name": list_name[4],
                    },
                ],
            }],
        }
        st_echarts(option, height="500px")


    pieChart, diagrammaLinee = st.columns([1, 1.5], gap='large')
    # Grafico a Torta con Percentuali Piattaforme
    with pieChart:
        colonna = estrai_colonna('Platform')
        # colonna = rimuovi_clone(colonna_file)
        # piattaforme = [[colonna], []] - essendo troppe, selezioniamo manualmente quelle più interessanti
        piattaforme = [['PC', 'PS4', 'PS3', 'PS2', 'PSP', 'X360', 'XOne', 'DS', 'WiiU', 'Wii', '3DS'],[]]
        creazione_cella(piattaforme)
        assegnazione_cella0(piattaforme)

        # contiamo elementi tra due liste
        for x in range(len(piattaforme[0])):
            for y in colonna:
                if y == piattaforme[0][x]:
                    piattaforme[1][x] += 1

        fig = px.pie(file, values=piattaforme[1], names=piattaforme[0])
        st.subheader("Diagramma a torta % Piattaforme")
        st.write(":blue[Descrizione:] possibilità di vedere quali piattaforme sono state più usate nel corso degli anni")
        st.plotly_chart(fig, use_container_width=True)


    # Diagramma con Anno e Profitto
    with diagrammaLinee:
        st.subheader("Profitto Totale VS Anni")
        st.write(":blue[Descrizione:] Nel corso degli anni il profitto globale coseguito che è possibile vedere nel grafico, ha avuto un picco Max nel 2008")
        st.markdown('''
            <iframe class="animation2" src="https://embed.lottiefiles.com/animation/142251"></iframe>
            <style>
            .animation2 {z-index: 1000; position: absolute; width: 5em; height: 5em}
        ''', unsafe_allow_html=True)
        colonna = estrai_colonna('Year')
        colonna2 = estrai_colonna('Global_Sales')

        anno_profitto = [[],[]]
        anno_profitto[0] = rimuovi_clone(colonna)
        creazione_cella(anno_profitto)
        assegnazione_cella0(anno_profitto)

        # somma di elementi fra due colonne
        for x in (anno_profitto[0]):
            for y in range(len(colonna)):
                if x == colonna[y]:
                    posizione = anno_profitto[0].index(x)
                    anno_profitto[1][posizione] += float(colonna2[y])

        # creazione dataframe momentaneo per definire grafico
        df = pd.DataFrame({
            'date': anno_profitto[0],
            'profitto annuale': anno_profitto[1]
        })

        line_chart = alt.Chart(df).mark_line().encode(
        y=  alt.Y('profitto annuale', title='Profitto($)'),
        x=  alt.X( 'date', title='Anno')
        )
        
        st.altair_chart(line_chart, use_container_width=True)


     # GRAFICO A BARRE - Quante pubblicazioni hanno eseguito le case madri?
    st.subheader("Pubblicazioni numero giochi")
    st.write(":blue[Descrizione:] Grafico a Barre nel quale è possibile vedere le varie aziende quanti giochi hanno pubblicato, ad averne caricate di più è 'Electronics Arts'")
    colonna_file = estrai_colonna('Publisher')
    colonna_file = list(filter(esistenza, colonna_file)) # possibili spazi vuoti

    pubblicazione = [[],[]]
    pubblicazione[0] = rimuovi_clone(colonna_file)
    creazione_cella(pubblicazione)
    assegnazione_cella0(pubblicazione)

    for valore in range(len(pubblicazione[0])):
        for valore_default in range(len(colonna_file)):
            if pubblicazione[0][valore] == colonna_file[valore_default]:
                pubblicazione[1][valore] += 1

    lista = []
    list2 = []

    for x in range(len(pubblicazione[1])):
        if pubblicazione[1][x] > 25:
            list2.append(pubblicazione[0][x])
            lista.append(pubblicazione[1][x])

    pubblicazione[0] = list2
    pubblicazione[1] = lista

    df = pd.DataFrame({
        'date': pubblicazione[0],
        'pubblicazioni': pubblicazione[1]
    })

    line_chart = alt.Chart(df).mark_bar().encode(
        y=  alt.Y('pubblicazioni', title='Pubblicazioni'),
        x=  alt.X('date', title='Aziende Videogame')
        )
        
    st.altair_chart(line_chart, use_container_width=True)



    logo, multychart, avatar = st.columns([0.5, 1.5, 0.5], gap='small')
    
    with logo:
        logoIMG = Image.open("logo.png")
        st.image(logoIMG)

    with multychart:
        st.subheader("Grafico Multi Linee di Profitto VS Continenti")
        st.write(":blue[Descrizione:] Grafico Multi Linee nel quale vengono importati i profitti indicati in cima, come grafici a linee. Durante il corso degli anni ci sono stati degli sovrapossizionamenti")
        colonna = estrai_colonna('Year')
        colonna = list(map(str, colonna))
        anni = rimuovi_clone(list(map(str, colonna)))

        europa = multychart_value("EU_Sales", colonna, anni)
        america = multychart_value("NA_Sales", colonna, anni)
        giappone = multychart_value("JP_Sales", colonna, anni)
        altri = multychart_value("Other_Sales", colonna, anni)

        anni = list(map(float, anni))
        anni = list(map(int, anni))
       
        df = pd.DataFrame({
            'anni': anni,
            'europa': europa,
            'america': america,
            'giappone': giappone,
            'altri': altri})

        line_chart = alt.Chart(df).transform_fold(
            ['europa', 'america', 'giappone','altri']
        ).mark_line().encode(
            x= alt.X('anni:O', title='Anno'),
            y= alt.Y('value:Q', title='Profitto'),
            color='key:N'
        )
        
        st.altair_chart(line_chart, use_container_width=True)
  

    with avatar:
        logoIMG = Image.open("Avatar.png")
        st.image(logoIMG)



# Style Profitti Totali Aree Geografiche
st.markdown('''
<style>
.css-1m02ktg .css-j5r0tf {width: 12%; margin-right: auto;flex: none;}
.css-ocqkz7 {gap:0}
.css-1xarl3l {font-size: 2.00rem;}
.css-t4htji {border: 3px solid #d09f14; padding: 3px; border-radius: 10px 0 10px 0;}
''', unsafe_allow_html=True)

hide_footer_style = '''
<style>
.appview-container .main footer {visibility: hidden;}
'''
st.markdown(hide_footer_style, unsafe_allow_html=True)

st.markdown("""
<style>
p {
    font-size:16px;
}
</style>
""", unsafe_allow_html=True)