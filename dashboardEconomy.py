import plotly.express as px
import pandas as pd
import plotly

df = pd.read_excel('Book.xlsx')

values = df['Result']
names = df['Platform']

fig = px.pie(df, 
            values=values,
            names = names,
            title = "ciccio brllo")

fig.update_traces(
    textposition = 'inside',
    textinfo='percent+label'
)

# fig.update_layout(
#     title_font_size = 10
# )

plotly.offline.plot(fig,filename='Piechart.html')