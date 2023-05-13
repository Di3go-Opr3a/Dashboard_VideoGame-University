import streamlit as st # creazione interfaccia web
from PIL import Image # importare immagini come ico per logo
import pandas as pd # usato per creazione DataFrame da CSV
import plotly.express as px # create a pie chart
from streamlit_echarts import st_echarts
import numpy as np

df=pd.DataFrame({'platform':['PC', 'PS3', 'PS2'],
                       'genre':['Sport', 'Racing', 'Moda'], 
                       'value':[0,0,0]})

df = df.set_index('platform')
print(df)
