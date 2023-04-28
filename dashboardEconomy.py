import pandas as pd # pip install pandas

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


# import plotly.express as px
# import pandas as pd
# import plotly

# df = pd.read_excel('Book.xlsx')
# ages = df["Platform"]
# print(ages)

# values = df['Result']
# names = df['Platform']

# fig = px.pie(df, 
#             values=values,
#             names = names,
#             title = "ciccio brllo")
   
# fig.update_traces(
#     textposition = 'inside',
#     textinfo='percent+label'
# )

# fig.update_layout(
#     title_font_size = 10
# )

# plotly.offline.plot(fig,filename='Piechart.html')




