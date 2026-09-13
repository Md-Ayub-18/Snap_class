import streamlit as st

def header_home():
    logo_url = "https://i.ibb.co/tMfTLcsh/logo.png"

    st.markdown(f"""
        <div style="
            display: flex;
            align-items: center;
            justify-content: center;
            flex-direction: column;
            margin-top: 0px;
            margin-bottom: 10px;
        ">
            <img src="{logo_url}" style="
                width: 150px;
                display: block;
                margin-top: -50px;
            ">

        </div>
            <h1 style="
                text-align: center;
                color: #E0E3FF;
                margin-top: 5px;
                margin-bottom: 0px;
                line-height: 0.9;
            ">SNAP<br>CLASS</h1>
    """, unsafe_allow_html=True)