import os
import pandas as pd
import streamlit as st
from utils import *
from ast import literal_eval
import plotly.express as px

st.set_option('deprecation.showPyplotGlobalUse', False)
st.set_page_config(layout="wide")

with st.container():  # Logo et Titre
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image(  # Logo
            os.path.join(os.getcwd() + "/whr.jpg"), width=250)

    with col2:
        st.title('Why are Scandinavians always happier than us?')

happiness_df = df = pd.read_pickle('happiness_df')

region = ['Central and Eastern Europe','Western Europe']

country_list = happiness_df[happiness_df['region'].isin(region)].country.unique()

df_europe = happiness_df[happiness_df['country'].isin(country_list)]

countries_of_interest = ['Denmark', 'Norway', 'Sweden', 'Finland', 'France']

df_interest = df_europe[df_europe['country'].isin(countries_of_interest)]

df_interest = df_interest.sort_values('happiness_score', ascending=False)

st.write("_" * 34) 


with st.container():
    col1, col2= st.columns([1, 1])  
    with col1:
        year = st.slider('Year', 2015, 2022)
        df_filtered = df_europe[df_europe['year']==year]
        
     
with st.container():  # Information
    col1, col2 = st.columns(2)
    with col1:
        plot_map(df_filtered)
    with col2:
        plot_score(df_interest)
        
st.write("_" * 34) 

temp = happiness_df[['happiness_score','economy', 'health','social_support','freedom','dystopia_residual','generosity']]

corr = temp.corr()


with st.container():  # Information
    col1, col2 = st.columns(2)
    with col1:
        plot_heat_corr(corr)
    with col2:
        pass











