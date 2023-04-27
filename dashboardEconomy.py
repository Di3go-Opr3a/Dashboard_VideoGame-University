import pandas as pd # pip install pandas

file = pd.read_csv("videogame.csv") # save date in file

# # Graph bar platform
collumPlatform = file['Platform'] # list date collum 'Platform'
wii, ps4, ds = 0, 0, 0

for x in collumPlatform:
    if x == 'Wii':
        wii += 1
    elif x == 'PS4':
        ps4 += 1

print(wii, ps4)

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