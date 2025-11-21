import streamlit as st

pages = [
    st.Page(page="pages/page1.py", titles="Home", icon="🏠"),
    st.Page(page="pages/page2.py", titles="Visualisasi Data", icon="📊"),
    st.Page(page="pages/page3.py", titles="Settings", icon="⚙️")
]

pg = st.navigation(
    pages,
    position="sidenar",
    expanded=True
)

pg.run()