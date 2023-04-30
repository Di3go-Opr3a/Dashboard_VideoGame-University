import pandas as pd # pip install pandas
import streamlit as st
import matplotlib.pyplot as plt

# def checkPlatform():
#     global collumPlatform

#     list = [] # save platform
#     for x in collumPlatform:
#         if x not in list: # check if the variable isn't in list
#             list.append(x) # save variable in list

#     print(list)

def create0Value(platform):
    count = len(platform[0])
    platform[1] = [None] * count
    
    for x in range(count):
        platform[1][x] = 0
    
    return platform

def countPlatform(platform):
    global collumPlatform

    for row in range(len(platform[0])):
        for element in collumPlatform:
            if element == platform[0][row]:
                platform[1][row] += 1

    return platform
            
            
file = pd.read_csv("videogame.csv") # save date in file

# GRAPH BAR WITH PLATFORM
collumPlatform = file['Platform'] # list with date collum 'Platform'

# checkPlatform()
platform = [['PC', 'PS4', 'PS3', 'PS2', 'PSP', 'X360', 'XOne', 'DS', '3DS', 'Wii', 'WiiU'],
            []]
create0Value(platform)
countPlatform(platform)

print(platform  )


# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]

fig1, ax1 = plt.subplots()
ax1.pie(platform[1], labels=platform[0], autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

st.pyplot(fig1)





