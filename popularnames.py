#popular names

import pandas as pd
import plotly.express as px
import streamlit as st

st.title('Popular Name Trends')

url = 'https://github.com/esnt/Data/raw/main/Names/popular_names.csv'
df = pd.read_csv(url)

name = st.text_input('Enter a name', value='John')
name_df = df[df['name']==name]

st.header(f'{name} over time')

tab1, tab2 = st.tabs(['Female','Male'])

with tab1:
    plot_df = name_df[name_df['sex']=='F']
    fig_f = px.line(data_frame=plot_df, x='year', y='n', color_discrete_sequence=['#FF0000'])
    st.plotly_chart(fig_f)

with tab2:
    plot_df = name_df[name_df['sex']=='M']
    fig_m = px.line(data_frame=plot_df, x='year', y='n')
    st.plotly_chart(fig_m)


expander = st.expander('About Popular Names')
with expander:
    expander.write("This graphic displays trends in some of the most popular US names from the years 1910 to 2021. Type in a name to get started!")


ssurl = 'https://www.ssa.gov/oact/babynames/decades/century.html'
st.page_link(ssurl, label='Social Security Most Popular Baby Names')


with st.sidebar:
    year = st.slider('Choose a year', 1910, 2021)
    year_df = df[df['year']==year]
    
    girls_names = year_df[year_df.sex=='F'].sort_values('n', ascending=False).head(5)['name']
    boys_names = year_df[year_df.sex=='M'].sort_values('n', ascending=False).head(5)['name']

    top_names = pd.concat([girls_names.reset_index(drop=True), boys_names.reset_index(drop=True)], 
            ignore_index=True, axis=1)
    top_names.columns = ['Girls','Boys']
    st.dataframe(top_names)


#name_df = name_df.groupby('year')['n'].sum().reset_index()

#fig = px.line(data_frame=name_df, x='year', y='n')

#show the plotly in streamlit

#st.plotly_chart(fig)
