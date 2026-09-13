import streamlit as st

def footer_home():
    ftr_url = "https://i.ibb.co/C5gwHGXC/mdayublogo1-2.png"

    st.markdown(f"""
        <div style="
            margin-top: 2rem;
            gap: 6px;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-direction: column;
        ">
            <p style="
                font-weight: bold;
                color: white;
                font-size: 22px;
                margin: 0;
                display: flex;
                align-items: center;
                gap: 8px;
            ">
                Created with ❤️ by
                <img src="{ftr_url}"
                     style="
                        height: 32px;
                        width: auto;
                        display: inline-block;
                        object-fit: contain;
                     ">
            </p>
        </div>
    """, unsafe_allow_html=True)