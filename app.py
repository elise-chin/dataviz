import os
import pandas as pd
import streamlit as st
from utils import *
from ast import literal_eval
import plotly.express as px

st.set_option('deprecation.showPyplotGlobalUse', False)
st.set_page_config(layout="wide")

##### IMPORT DES DONNEES #####
#dataset complet réharmonisé + pop
happiness_df = pd.read_pickle('happiness_df_pop')
#happiness + pop + city + sunshine hour ds capitale en EU en 2021
sunshine_df = pd.read_pickle('sunshine_df')


countries_of_interest = ['Finland', 'Denmark', 'Norway', 'Sweden', 'France']

europe = ['Central and Eastern Europe','Western Europe']

europe_countries = happiness_df[happiness_df['region'].isin(europe)].country.unique()

europe_df = happiness_df[happiness_df['country'].isin(europe_countries)]

interest_df = happiness_df[happiness_df['country'].isin(countries_of_interest)]
##############################

with st.container():  # Logo et Titre
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image(  # Logo
            os.path.join(os.getcwd() + "/whr.jpg"), width=250)
    with col2:
        st.title('Why are Scandinavians always happier than us?')
st.write("_" * 34) 
#############################
st.header('Have you ever heard something like ...')
with st.container():
    col1, col2 = st.columns([1,1])
    with col1:
        st.image(os.path.join(os.getcwd() + "/img1.jpg"), width=500)
    with col2:
        st.image(os.path.join(os.getcwd() + "/img2.jpg"), width=500)
   
st.write("_" * 34) 
##################################

st.header('But where does this "common knowledge" comes from ?')

col1, col2, col3, col4 = st.columns(4)
col1.metric("Number of countries", "155")
col2.metric("Year of creation", "2012")
col3.metric("Lowest score", "2.40", "-(Afghanistan - 2022)")
col4.metric("Highest score", "7.84", "(Finland - 2021)")
    
        
with st.container():  # Information
    col1, col2, col3 = st.columns([5,3,1])
    with col1:
        plot_map(happiness_df, scope='world')
    with col2:
        world = happiness_df.groupby('year').mean().reset_index()

        world['country']='world'

        world = world[['year', 'happiness_score', 'country']]

        interest_df = interest_df[['year', 'happiness_score', 'country']]

        df_plot = pd.concat([interest_df,world])
        
        plot_score(df_plot)
    with col3:
        evol(df_plot)
        
st.write("_" * 34) 
###################################


st.header('What could explain the happiness score at a global scale ?') 

america = ['North America','Latin America and Caribbean', 'North America and ANZ']
american_countries = list(happiness_df[happiness_df['region'].isin(america)].country.unique())


oceania = ['Australia and New Zealand']
oceanian_countries = list(happiness_df[happiness_df['region'].isin(oceania)].country.unique())


asia = ['Southeastern Asia','Eastern Asia', 'Southern Asia', 'East Asia', 'Southeast Asia', 'South Asia']
asian_countries = list(happiness_df[happiness_df['region'].isin(asia)].country.unique())


africa = ['Middle East and Northern Africa','Sub-Saharan Africa', 'Middle East and North Africa']
african_countries = list(happiness_df[happiness_df['region'].isin(africa)].country.unique())

european_countries = list(happiness_df[happiness_df['region'].isin(europe)].country.unique())

with st.container():  # Information
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        regions = st.multiselect('REGION', ['America', 'Oceania', 'Asia', 'Africa', 'Europe'])
    with col2:
        year = st.slider('Year', 2015, 2022)
    with col3:
        x_axis = st.selectbox('X axis', ['economy', 'social_support', 'health', 'freedom', 'trust', 'generosity'])
    with col4:
        y_axis = st.selectbox('Y axis', ['health', 'social_support', 'economy', 'freedom', 'trust', 'generosity'])
        
country_list = []
if 'America' in regions:
    country_list += american_countries
if 'Oceania' in regions:
    country_list += oceanian_countries
if 'Asia' in regions:
    country_list += asian_countries
if 'Africa' in regions:
    country_list += african_countries
if 'Europe' in regions:
    country_list += european_countries
        
with st.container():
    col1, col2 = st.columns([2,7])
    with col1:
        plot_heat_corr(happiness_df, country_list)
    with col2:
        
        df_bub = happiness_df[happiness_df['year']==year]
        bubble(df_bub, country_list, x_axis, y_axis)
        
st.write("_" * 34) 

##################################

st.header('What are the differences between France and Nordic countries, in practice ?')          
        
with st.container():  # Information
    col1, col2 = st.columns(2)
    with col1:
        sunshine(sunshine_df)         
    with col2:
        criteria_list = ['economy', 'social_support', 'health', 'freedom', 'trust', 'generosity']

        plot_bar_criteria(happiness_df, ['France', 'Sweden'], criteria_list, title="Contribution of criterias to the happiness score in France and Finland")











