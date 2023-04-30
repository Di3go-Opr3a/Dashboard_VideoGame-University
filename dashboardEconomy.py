import pandas as pd # pip install pandas
import streamlit as st # pip install streamlit
import matplotlib.pyplot as plt # pip install matplotlib


def checkPlatform(colonna):
    def myFunc(x):
        if x == "N/A":
            return True
        else:
            return False  
    
    lista = [] # salvataggio piattaforme
    for x in colonna:
        if x not in lista: # controllo se la piattaforma non esiste
            lista.append(x) # salvo la piattaforma in list
    lista = list(filter(myFunc, lista))

    print(lista)


# creo celle quante sono gli elementi riga 0, nella riga 1 di platform 
# assegno 0
def create0Value(platform):
    count = len(platform[0])
    platform[1] = [None] * count
    
    for x in range(count):
        platform[1][x] = 0
    
    return platform

# conto quanti sono i valori nel DataFrame per ogni elemento riga 0
def countPlatform(platform):
    global collumPlatform
    
    for row in range(len(platform[0])):
        for element in collumPlatform:
            if element == platform[0][row]:
                platform[1][row] += 1

    return platform

def piechart(platform):
    # Distanza tra elementi
    fig1, ax1 = plt.subplots()

    explode = (0, 0, 0, 0.1, 0 , 0, 0, 0.1, 0, 0, 0)

    # autopct = Numero percentuale mostrato
    # startangle = parte da 90 gradi
    ax1.pie(platform[1], labels=platform[0], autopct='%1.1f%%', startangle=90, explode=explode)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    
    return st.pyplot(fig1)



file = pd.read_csv("videogame.csv") # salvo dati in 'file'

# DATAFRAME in vista
st.dataframe(file)

# GRAPH BAR CON 'PIATTAFORME'
collumPlatform = file['Platform'] # lista dati con colonna 'Platform'

# checkPlatform()
platform = [['PC', 'PS4', 'PS3', 'PS2', 'PSP', 'X360', 'XOne', 'DS', 'WiiU', 'Wii', '3DS'],
            []]
create0Value(platform)
countPlatform(platform)
# print(platform)

piechart(platform)

#GRAFICO A LINEE
colonna_anni = file['Year']
checkPlatform(colonna_anni)

# st.line_chart(chart_data) 


