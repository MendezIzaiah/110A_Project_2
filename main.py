import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

xl=pd.ExcelFile("./data/TableauSalesData.xlsx") 
SalesData = xl.parse("Orders") 

#creating sidebar menu 
with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=['Home','Segment Profits','Sub-Category Profits','Temp3'],
        icons=['house','box-arrow-in-up-right','gear','gear'],
        menu_icon="cast",
        default_index=0,
    
    )

def home():
    pass

def segment_Profits():
    st.markdown(
    """
    # Table of Segment Profits by Year
    
    """
    )
    #display the df 
    dfp = pd.read_pickle('./data/yearly_profit.pkl')
    #adding style format while passing in df
    st.dataframe(dfp.style.format('${:,.2f}'),400,200)

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

def sub_cat_profit():
    st.markdown(
    """
    # Total Sub-Category profits

    """
    )
    #display the df
    df = SalesData[["Sub-Category", "Profit", "Sales"]].groupby(by="Sub-Category").sum().sort_values(by="Profit")
    #adding formatting
    st.dataframe(df.style.format('${:,.2f}'),400,400)
    
    #digging deeper into the underperforming sub-categories
    st.markdown(
        """
        ## Investigating the underperforming sub-categories
        partial list of products from sub-category table

        """
    )
    df_tbs = SalesData[['Product Name','Profit']].loc[SalesData["Sub-Category"].isin(['Tables','Bookcases','Supplies'])].groupby("Product Name").sum().round().sort_values("Profit")
    st.dataframe(df_tbs.style.format('${:,.2f}'))

    #display for chart if needed

def temp3():
    pass

if selected == 'Home':
    st.title(f'You have selected {selected}')
if selected == 'Segment Profits':
    segment_Profits()
if selected == 'Sub-Category Profits':
    sub_cat_profit()
if selected == 'Temp3':
    st.title(f'You have selected {selected}')


