import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

xl=pd.ExcelFile("./data/TableauSalesData.xlsx") 
SalesData = xl.parse("Orders") 
dfp = pd.read_pickle('./data/yearly_profit.pkl')
st.set_option('deprecation.showPyplotGlobalUse', False)

class data_frames:
    def seg_prof():
       #Made by Izaiah 
        dfp = pd.read_pickle('./data/yearly_profit.pkl')
        #adding style format while passing in df
        st.dataframe(dfp.style.format('${:,.2f}'),400,200)

    def sub_cat_prof():
       #Made by Jonathan 
        df = SalesData[["Sub-Category", "Profit", "Sales"]].groupby(by="Sub-Category").sum().sort_values(by="Profit")
        #adding formatting
        st.dataframe(df.style.format('${:,.2f}'),400,400)
    
    def sub_cat_prod():
       #Made by Jonathan 
        df_tbs = SalesData[['Product Name','Profit']].loc[SalesData["Sub-Category"].isin(['Tables','Bookcases','Supplies'])].groupby("Product Name").sum().round().sort_values("Profit")
        st.dataframe(df_tbs.style.format('${:,.2f}'))

    def con_sub_cat_prof():
       #Made by Izaiah 
        only_consumer = SalesData[SalesData['Segment'] == 'Consumer']
        consumer_subcat_profit = only_consumer[['Sub-Category','Profit']].groupby('Sub-Category').sum().round().sort_values('Profit',ascending= False)

        st.dataframe(consumer_subcat_profit.style.format('${:,.2f}'))

    def bookcase_prof_sales():
        #made by Jonathan
        BookcasesSales = SalesData.loc[SalesData["Sub-Category"]=="Bookcases"]
        BookcasesSalesYear = BookcasesSales.copy()
        BookcasesSalesYear["Year"] = BookcasesSalesYear["Order Date"].dt.year
        BookcasesSalesProf = BookcasesSalesYear[["Year", "Sales", "Profit"]].groupby("Year").sum()

        st.dataframe(BookcasesSalesProf.style.format('${:,.2f}'))

class charts:
    def consumer_scatterplt():
       #Made by Izaiah 
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
        #plt.show() 
        st.pyplot(fig)

    def seg_profits():
       #Made by Izaiah 
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

    def cat_plot():
        #Made by Jonathan
        BookcasesRegion = SalesData.loc[SalesData["Sub-Category"]=="Bookcases"]
        BookcasesSalesRegion = BookcasesRegion.copy()
        BookcasesRegionBar = BookcasesSalesRegion[["Region", "Sales", "Profit"]].groupby("Region").sum()
        BookcasesRegionBar = BookcasesRegionBar.reset_index()
        BookcasesRegionBarGraph = pd.melt (BookcasesRegionBar, id_vars="Region",var_name="Bookcases",value_name= "Regional Numbers")

        CatPlot1 = sns.catplot(x="Region", y="Regional Numbers", hue="Bookcases", data = BookcasesRegionBarGraph, kind = "bar")
        CatPlot1.fig.suptitle("Regional Bookcases Profit and Sales")
        fig = plt.show()

        st.pyplot(fig)

class pagez:
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
        data_frames.seg_prof()

        st.markdown('# Visualization')
        
        charts.seg_profits()

    def sub_cat_profit():
        st.markdown(
        """
        # Total Sub-Category profits and sales

        """
        )
        #display the df
        data_frames.sub_cat_prof()
        
        #digging deeper into the underperforming sub-categories
        st.markdown(
            """
            ## Investigating the underperforming sub-categories
            List of products from sub-category table

            """
        )
        #other df here
        data_frames.sub_cat_prod()

    def con_sub():
        st.markdown(
            """
            # Consumer Sub-Category Profits 
            We can see that the consmer sub-categories perform well
            """
            
        )
        #df here
        data_frames.con_sub_cat_prof()

        st.markdown(
            """
            # All Consumer products 
            Though there are few underperforming sub-categories, we can see there are several underperforming products
            """
        )
        
        charts.consumer_scatterplt()

    def book_prof():
        st.markdown(
           """
           # All bookcase Profit and Sales by year

           """
        )

        #Call the df here
        data_frames.bookcase_prof_sales()

        st.markdown(
          """
          # Visualization
          As we can see high sales does not necessariy correlate to profit
          """
        )
        #call the visualization of df above here
        charts.cat_plot()
        #Call next df here

        #call last visualization here











