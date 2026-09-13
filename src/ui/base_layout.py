import streamlit as st
def style_background_home():
    st.markdown(
        """
        <style>    
        }
        .stApp {
            background-color: #586F2 !important;
        }
        
        .stApp div[data-testid="stColumn"] {
            background-color: #E0E3FF !important;
            padding: 2.5rem !important;
            border-radius: 5rem !important;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
    
def style_background_dashboard():
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #5865f2 !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
def style_base_layout():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979..2050&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');
        
            #Mainmenu, header, footer{
            visibility: hidden;
            }
            .block-container {
            padding-top: 1rem !imortant; 
            }
            h2{
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 2rem !important;
                line-height: 0.9 !important;
                margin-bottom: 0 !important;
                color: #140f0f !important;
            }
            h1{
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 3.5rem !important;
                line-height: 0.9 !important;
                margin-bottom: 0 !important;
                color: #E0E3FF !important;
            }
            h3,h5,h6,p{
                font-family: 'Outfit', sans-serif !important;
                
            }
            button[kind="primary"]{
                border-radius: 1.5rem !important;
                background-color: #5865F2 !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.3s ease-in-out !important;
            }
            button[kind="secondary"]{
                border-radius: 1.5rem !important;
                background-color: #e8459e !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.3s ease-in-out !important;
            }
            button[kind="tertiary"]{
                border-radius: 1.5rem !important;
                background-color: black !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.3s ease-in-out !important;
            }
            button:hover{
                transform: scale(1.05) !important;
                }
        </style>
        """,
        unsafe_allow_html=True
    )