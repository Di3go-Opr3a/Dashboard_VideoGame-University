import streamlit as st
import pandas as pd
import time
from streamlit_extras.let_it_rain import rain
from PIL import Image

df = pd.read_csv("videogame.csv")

col = st.sidebar.selectbox("Select any column", df.columns)
  
  
col = st.sidebar.multiselect("Select any column", df.columns)
  
prg = st.progress(0)
  
for i in range(100):
    time.sleep(0.001)
    prg.progress(i+1)
  
img = Image.open('image.png')
# Raining Snowflake.

rain(
    emoji=img,
    
      # the size of each snowflake
    font_size=20,  
    # speed of raining
    falling_speed=3,  
    
    
    # for how much time it will fall
    animation_length="infinite",  
)