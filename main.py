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
        options=['Home','Segment Profits','Sub-Category Profits','Consumer Sub-Category'],
        icons=['house','box-arrow-in-up-right','box-arrow-in-up-right','box-arrow-in-up-right'],
        menu_icon="cast",
        default_index=0,
    
    )

def home():
    st.markdown(
        """
        # Plan to increase Profits by 10%

        ## Approaches that can increase profits by 10%:
        - Reduce unprofitable products and subcategories to provide the top 50% most frequent accounts with requested products
        - Provide a concentrated marketing segment recommendation in support of Natasha's goal of increasing profit by 10%

        """
    )

def segment_profits():
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
    # Total Sub-Category profits and sales

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
        List of products from sub-category table

        """
    )
    df_tbs = SalesData[['Product Name','Profit']].loc[SalesData["Sub-Category"].isin(['Tables','Bookcases','Supplies'])].groupby("Product Name").sum().round().sort_values("Profit")
    st.dataframe(df_tbs.style.format('${:,.2f}'))

    #display for chart if needed

def con_sub():
    st.markdown(
        """
        # Consumer Sub-Category Profits 
        We can see that the consmer sub-categories perform well
        """
        
    )
    only_consumer = SalesData[SalesData['Segment'] == 'Consumer']
    consumer_subcat_profit = only_consumer[['Sub-Category','Profit']].groupby('Sub-Category').sum().round().sort_values('Profit',ascending= False)

    st.dataframe(consumer_subcat_profit.style.format('${:,.2f}'))

    st.markdown(
        """
        # All Consumer products 
        Though there are few underperforming sub-categories, we can see there are several underperforming products
        """
    )

    only_consumer = SalesData[SalesData['Segment'] == 'Consumer']
    only_consumer_prod_prof = only_consumer[['Product Name','Profit']].groupby('Product Name').sum().round().sort_values('Profit',ascending = False)
    only_consumer_prod_prof = only_consumer_prod_prof.reset_index()

    fig, ax = plt.subplots()
    plt.scatter(data = only_consumer_prod_prof, x = "Product Name", y = "Profit")

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Profit')
    ax.set_xlabel('Products')
    ax.set_title('Profits of all Consumer Products')
    ax.set_xticks([''])
    #ax.legend() 

    st.pyplot(fig)

if selected == 'Home':
    home()
if selected == 'Segment Profits':
    segment_profits()
if selected == 'Sub-Category Profits':
    sub_cat_profit()
if selected == 'Consumer Sub-Category':
    con_sub()

