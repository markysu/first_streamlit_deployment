import streamlit as st

st.set_page_config(page_title="Home", page_icon="🏠")

if "form_submitted" not in st.session_state:
    st.session_state["form_submitted"] = False


form = st.form(key="my_form")
anun = form.text_input("anun","")
azganun = form.text_input("azganun","")
haeranun = form.text_input("haeranun","")
submit_button = form.form_submit_button(label="Submit")


if submit_button:
    st.session_state["anun"] = anun
    st.session_state["azganun"] = azganun
    st.session_state["haeranun"] = haeranun
    st.markdown("## Data is being analyzed go to the analyze page to see the results.")
    st.page_link("pages/1_analyze.py")
    st.session_state["form_submitted"] = True



