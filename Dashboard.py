# Track number 3 Dashboard Date CSV

import streamlit as st # Create interface
from PIL import Image # Import .ico
import plotly.express as px # pie chart creation
from streamlit_echarts import st_echarts # radar creation
import altair as alt # insert name axis
import pandas as pd
import numpy as np 

def extract_column(key):
    column = file[key].values 
    column = column.tolist() # numpy -> list
    return column


def Profit_Area(key):
    column = extract_column(key)
    text = str(round(sum(column),4)) + " M" # round -> truncation numbers
    return text


# creation of as many cells with null value as there are in row 0
def cell_creation(matrix):
    count = len(matrix[0])
    matrix[1] = [None] * count


def assignment_cell0(matrix):
    matrix[1] = np.zeros(len(matrix[0]), dtype=int)
    matrix[1] = matrix[1].tolist() # numpy -> list


def exist(value):
        if value != 'nan':
            return True
        else:
            return False 
        

def remove_clone(list_default):
    element = []
    
    for value in list_default:
        if value not in element: 
            element.append(value)

    # eliminazione di celle nulle
    element = list(filter(exist, element))
    return element


def matrixRadar(matrix):
    for x in cicleGenre:
        matrix[0].append(x)

    cell_creation(matrix)
    assignment_cell0(matrix)

    return matrix


def multychart_value(text, column, year):
    element = [0] * len(year)
    column2 = extract_column(text)

    for x in range(len(column)):
        for y in range(len(year)):
            if column[x] == year[y]:
                element[y] = element[y] + column2[x]

    return element


# HEADER
icon = Image.open("Image/image.ico")

st.set_page_config(
    page_title="StrealmClix",
    page_icon= icon,
    layout="wide", # takes the whole screen
    initial_sidebar_state="auto"
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


file = pd.read_csv('University/videogame.csv', index_col=['Rank'])

with st.container():
    # Sum Total Profits Geographic Areas
    Global, Europe, America, Japan, OtherContinents = st.columns(5)
                
    Global.metric("Profit Total", Profit_Area('Global_Sales'))
    Europe.metric("Europe", Profit_Area('EU_Sales'))
    America.metric("America", Profit_Area('NA_Sales'))
    Japan.metric("Asia", Profit_Area('JP_Sales'))
    OtherContinents.metric("Other", Profit_Area('Other_Sales'))



    dataframe, radar = st.columns([1.5, 1], gap="medium")
    
    with dataframe:
        st.subheader(':globe_with_meridians: :red[Dataframe StrealmClix]')
        st.dataframe(file)
    
    # Radar of Platforms vs. Genre
    column = extract_column('Platform')
    column2 = extract_column('Genre')
    cicleGenre = remove_clone(column2)
    cicleGenre = ['Sports', 'Action', 'Role-Playing', 'Misc', 'Shooter', 'Strategy', 'Adventure']

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

    platform = ["PC", "Wii", "PSP", "PS4", "X360"]
    matrix = [[PC], [Wii], [PSP], [PS4], [X360]]
    
    # Counter - How many genres correspond to individual platforms?
    for x in range(len(column)):
        for y in range(len(platform)):
            if column[x] == platform[y]:
                for b in range(len(matrix[y][0][0])):
                    if column2[x] == matrix[y][0][0][b]:
                        matrix[y][0][1][b] = matrix[y][0][1][b] + 1
                        break

    with radar:
        option = {
            "legend": {"data": (platform)},
            "radar": {
                "indicator": [
                    {"name": cicleGenre[0], "max": 300},
                    {"name": cicleGenre[1], "max": 400},
                    {"name": cicleGenre[2], "max": 300},
                    {"name": cicleGenre[3], "max": 300},
                    {"name": cicleGenre[4], "max": 300},
                    {"name": cicleGenre[5], "max": 300},
                    {"name": cicleGenre[6], "max": 300},
                ]
            },
            "series": [{   
                "type": "radar",
                "data": [
                    {
                        "value": matrix[0][0][1],
                        "name": platform[0],
                    },
                    {
                        "value": matrix[1][0][1],
                        "name": platform[1],
                    },
                    {
                        "value": matrix[2][0][1],
                        "name": platform[2],
                    },
                    {
                        "value": matrix[3][0][1],
                        "name": platform[3],
                    },
                    {
                        "value": matrix[4][0][1],
                        "name": platform[4],
                    },
                ],
            }],
        }
        st_echarts(option, height="500px")


    pieChart, diagramLinee = st.columns([1, 1.5], gap='large')
    # Grafico a Torta con Percentuali Piattaforme
    with pieChart:
        column = extract_column('Platform')
        platform = [['PC', 'PS4', 'PS3', 'PS2', 'PSP', 'X360', 'XOne', 'DS', 'WiiU', 'Wii', '3DS'],[]]
        cell_creation(platform)
        assignment_cell0(platform)

        for x in range(len(platform[0])):
            for y in column:
                if y == platform[0][x]:
                    platform[1][x] += 1

        fig = px.pie(file, values=platform[1], names=platform[0])
        st.subheader("Pie chart % Platforms")
        st.write(":blue[Description:] Ability to see which platforms have been most used over the years")
        st.plotly_chart(fig, use_container_width=True)


    # Diagram with Year and Profit
    with diagramLinee:
        st.subheader("Total Profit VS Years")
        st.write(":blue[Description:] Over the years the overall profit achieved which you can see in the graph, had a Max peak in 2008")
        st.markdown('''
            <iframe class="animation2" src="https://embed.lottiefiles.com/animation/142251"></iframe>
            <style>
            .animation2 {z-index: 1000; position: absolute; width: 5em; height: 5em}
        ''', unsafe_allow_html=True)
        column = extract_column('Year')
        column2 = extract_column('Global_Sales')

        profit_year = [[],[]]
        profit_year[0] = remove_clone(column)
        cell_creation(profit_year)
        assignment_cell0(profit_year)

        for x in (profit_year[0]):
            for y in range(len(column)):
                if x == column[y]:
                    position = profit_year[0].index(x)
                    profit_year[1][position] += float(column2[y])

        # momentary dataframe creation to define graph
        df = pd.DataFrame({
            'date': profit_year[0],
            'Profit Annual': profit_year[1]
        })

        line_chart = alt.Chart(df).mark_line().encode(
        y=  alt.Y('Profit Annual', title='Profit($)'),
        x=  alt.X( 'date', title='Year')
        )
        
        st.altair_chart(line_chart, use_container_width=True)


    # GRAPHIC BAR - How many publications did the parent companies run?
    st.subheader("Publications number games")
    st.write(":blue[Description:] Bar graph in which you can see the various companies how many games they have published, to have uploaded the most is 'Electronics Arts'")
    column = extract_column('Publisher')
    column = list(filter(exist, column))

    publication = [[],[]]
    publication[0] = remove_clone(column)
    cell_creation(publication)
    assignment_cell0(publication)

    for value in range(len(publication[0])):
        for value_default in range(len(column)):
            if publication[0][value] == column[value_default]:
                publication[1][value] += 1

    list1 = []
    list2 = []

    for x in range(len(publication[1])):
        if publication[1][x] > 25:
            list2.append(publication[0][x])
            list1.append(publication[1][x])

    publication[0] = list2
    publication[1] = list1

    df = pd.DataFrame({
        'date': publication[0],
        'publications': publication[1]
    })

    line_chart = alt.Chart(df).mark_bar().encode(
        y=  alt.Y('publications', title='Publications'),
        x=  alt.X('date', title='Videogame Companies')
        )
        
    st.altair_chart(line_chart, use_container_width=True)



    logo, multychart, avatar = st.columns([0.5, 1.5, 0.5], gap='small')
    
    with logo:
        logoIMG = Image.open("Image/logo.png")
        st.image(logoIMG)

    with multychart:
        st.subheader("Graph Multi Profit Lines VS Continents")
        st.write(":blue[Description:] Multi Line Graph in which the profits shown at the top are imported as line graphs. Over the years there have been overlaps.")
        column = extract_column('Year')
        column = list(map(str, column))
        year = remove_clone(list(map(str, column)))

        europe = multychart_value("EU_Sales", column, year)
        america = multychart_value("NA_Sales", column, year)
        japan = multychart_value("JP_Sales", column, year)
        other = multychart_value("Other_Sales", column, year)

        year = list(map(float, year))
        year = list(map(int, year))
       
        df = pd.DataFrame({
            'year': year,
            'europe': europe,
            'america': america,
            'japan': japan,
            'other': other})

        line_chart = alt.Chart(df).transform_fold(
            ['europe', 'america', 'japan','other']
        ).mark_line().encode(
            x= alt.X('year:O', title='Year'),
            y= alt.Y('value:Q', title='Profit'),
            color='key:N'
        )
        
        st.altair_chart(line_chart, use_container_width=True)
  

    with avatar:
        logoIMG = Image.open("Image/Avatar.png")
        st.image(logoIMG)



# Style Profit Total Geographic Areas
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