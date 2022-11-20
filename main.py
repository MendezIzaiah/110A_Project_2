import streamlit as st
from streamlit_option_menu import option_menu
import helper

#creating sidebar menu 
with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=['Home','Segment Profits','Sub-Category Profits','Consumer Sub-Category'],
        icons=['house','box-arrow-in-up-right','box-arrow-in-up-right','box-arrow-in-up-right'],
        menu_icon="cast",
        default_index=0,
    
    )

if selected == 'Home':
    helper.pagez.home()
if selected == 'Segment Profits':
    helper.pagez.segment_profits()
if selected == 'Sub-Category Profits':
    helper.pagez.sub_cat_profit()
if selected == 'Consumer Sub-Category':
    helper.pagez.con_sub()

