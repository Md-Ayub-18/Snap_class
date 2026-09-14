# import streamlit as st

# def header_home():
#     logo_url = "https://i.ibb.co/tMfTLcsh/logo.png"

#     st.markdown(f"""
#         <div style="
#             display: flex;
#             align-items: center;
#             justify-content: center;
#             flex-direction: column;
#             margin-top: 0px;
#             margin-bottom: 10px;
#         ">
#             <img src="{logo_url}" style="
#                 width: 150px;
#                 display: block;
#                 margin-top: -50px;
#             ">

#         </div>
#             <h1 style="
#                 text-align: center;
#                 color: #E0E3FF;
#                 margin-top: 5px;
#                 margin-bottom: 0px;
#                 line-height: 0.9;
#             ">SNAP<br>CLASS</h1>
#     """, unsafe_allow_html=True)

# def header_dashboard():
#     logo_url = "https://i.ibb.co/tMfTLcsh/logo.png"

#     st.markdown(
#         f'<div style="display:flex; align-items:center; justify-content:center; gap:10px; margin:0 0 10px 0;">'
#         f'<img src="{logo_url}" style="width:70px; height:70px; object-fit:contain; display:block;">'
#         f'<h1 style="color:#E0E3FF; margin:0; padding:0; line-height:0.85; text-align:left; font-size:52px; font-weight:900;">SNAP<br>CLASS</h1>'
#         f'</div>',
#         unsafe_allow_html=True
#     )
import streamlit as st


def header_home():

    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"
    
    st.markdown(f"""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:30px; margin-top:30px">
            <img src='{logo_url}' style='height:100px;' />
            <h1 style='text-align:center; color:#E0E3FF'>SNAP<br/>CLASS</h1>
        </div>   
                
                """, unsafe_allow_html=True)


def header_dashboard():

    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"
    
    st.markdown(f"""
        <div style="display:flex; align-items:center; justify-content:center; gap:10px">
            <img src='{logo_url}' style='height:85px;' />
            <h2 style='text-align:left; color:#5865F2'>SNAP<br/>CLASS</h1>
        </div>   
                
                """, unsafe_allow_html=True)
