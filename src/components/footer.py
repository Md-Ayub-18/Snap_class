import streamlit as st


def footer_home():
    logo_url = "https://i.ibb.co/C5gwHGXC/mdayublogo1-2.png"

    st.markdown(f"""
<div style="position:fixed; bottom:20px; left:0; width:100%; display:flex; justify-content:center; align-items:center; gap:6px; z-index:9999;">
<p style="font-weight:bold; color:white; font-size:20px; margin:0;">Created with ❤️ by</p>
<img src="{logo_url}" style="height:25px; width:auto; display:block;">
</div>
""", unsafe_allow_html=True)


def footer_dashboard():
    logo_url = "https://i.ibb.co/C5gwHGXC/mdayublogo1-2.png"

    st.markdown(f"""
    <div style="
        position: fixed;
        bottom: 20px;
        left: 0;
        width: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 6px;
    ">
        <span style="
            font-weight: bold;
            color: black;
            font-size: 20px;
        ">Created with ❤️ by</span><img src="{logo_url}" style="height: 30px; width: auto;">
    </div>
    """, unsafe_allow_html=True)