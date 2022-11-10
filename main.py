import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
import numpy as np

#dependencies:
#pip install streamlit
#pip install streamlit-option-menu
#to run the webapp:
#streamlit main.py

#creating sidebar menu 
with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=['Home','Temp1','Temp2','Temp3'],
        icons=['house','gear','gear','gear'],
        menu_icon="cast",
        default_index=0,
    
    )

def home():
    pass

def temp1():
    #pass
    
    st.markdown(
    """
    # Table of Segment Profits by Year
    
    """
    )
    #display the df 
    dfp = pd.read_pickle('./data/yearly_profit.pkl')
    st.dataframe(dfp,400,200)

    st.markdown('# Visualization')
    #present a chart of that df  
    labels = dfp.index

    cons = dfp['Consumer'] 
    corp = dfp['Corporate']
    home = dfp['Home Office']

    x = np.arange(len(labels))  # the label locations
    width = 0.2  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - 0.2, cons, width, label='Consumer')
    rects2 = ax.bar(x , corp, width, label='Corporate')
    rects3 = ax.bar(x + 0.2, home, width, label='Home Office')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Profit')
    ax.set_title('Profits of Segments from 2017 to 2020')
    ax.set_xticks(x, labels)
    ax.legend()

    #ax.bar_label(rects1, padding=3)
    #ax.bar_label(rects2, padding=3)
    #ax.bar_label(rects3, padding=3)

    #fig.tight_layout()
    #plt.show()

    st.pyplot(fig)

def temp2():
    pass

def temp3():
    pass

if selected == 'Home':
    st.title(f'You have selected {selected}')
if selected == 'Temp1':
   # st.title(f'You have selected {selected}')
    temp1()
if selected == 'Temp2':
    st.title(f'You have selected {selected}')
if selected == 'Temp3':
    st.title(f'You have selected {selected}')


