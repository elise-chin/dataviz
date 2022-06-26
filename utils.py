import pandas as pd
import numpy as np
import os
import plotly.express as px
import streamlit as st
import plotly.io as pio
import plotly.express as px
import plotly.graph_objects as go

def plot_map(df_filtered):
    hover_data = df_filtered[["happiness_rank","happiness_score"]]

    fig = px.choropleth(df_filtered,
                        locations=df_filtered["country"],
                        locationmode="country names",
                        projection="natural earth",
                        hover_data=hover_data,
                        hover_name=df_filtered["country"],
                        color="happiness_rank",
                        color_continuous_scale=px.colors.sequential.RdBu[::-1],
                        scope="europe")
    fig.update_layout(height=600, margin={"r":0,"t":0,"l":0,"b":0})
    st.plotly_chart(fig, use_container_width=True)

    
def plot_top(df):
    fig = px.line(df, x='year', y='happiness_rank', color='country')
    fig['layout']['yaxis']['autorange'] = "reversed"
    st.plotly_chart(fig, use_container_width=True)
    
    
def plot_score(df_interest):

    fig = px.box(df_interest,
                 x="happiness_score",
                 y="country",
                 color="country",
                 color_discrete_sequence=px.colors.qualitative.Pastel_r)
    fig.update_traces(boxmean=True,
                      whiskerwidth=0.8,
                      marker_size=2,
                line_width=2.5
                      )
    fig.update_layout(height=600,
                      width=800,
                      showlegend=True,
                      yaxis= dict(showticklabels = False),
                      title="Distribution of happiness score by region")
    
    st.plotly_chart(fig, use_container_width=True)
    
def plot_heat_corr(corr):
    fig = go.Figure(data=go.Heatmap(
        x=corr.columns,
        y=corr.columns,
        z=corr,
        colorscale=px.colors.diverging.Spectral,
        zmin=-1,
        zmax=1
    ))
    st.plotly_chart(fig, use_container_width=True)