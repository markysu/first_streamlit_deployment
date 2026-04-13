import streamlit as st
import pandas as pd
import plotly.express as px

if "form_submitted" not in st.session_state or not st.session_state["form_submitted"]:
    st.warning("Please submit the form on the Home page first.")
    st.page_link("home.py")
    st.stop()

anun = st.session_state.get("anun", "")
st.markdown(f"## Analyzing data...{anun}")

@st.cache_data
def read_data():
    data = pd.read_parquet("shnik_mini.parquet")
    return data


def get_statistics(data, anun, azganun=None, haeranun=None):
    new_data = data[data["anun"] == anun]
    if azganun:
        new_data = new_data[new_data["azganun"] == azganun]
    if haeranun:
        new_data = new_data[new_data["haeranun"] == haeranun]

    return new_data


def get_plots(new_data):
    d = new_data.groupby(["marz"])["anun"].count().reset_index()
    d=d.sort_values(by="anun",ascending=True)
    plot_bar = px.bar(y=d["marz"].tolist(),x=d["anun"].tolist(),orientation='h')
    plot_bar=plot_bar.update_layout(xaxis_title="count",yaxis_title="marz")

    d=new_data.groupby(["tari"])["anun"].count()
    plot_bar2 = px.bar(x=d.index,y=d.values)
    plot_bar2 = plot_bar2.update_layout(xaxis_title="Year born",yaxis_title="count")

    return plot_bar, plot_bar2


data = read_data()

anun = st.session_state["anun"]
azganun = st.session_state["azganun"]
haeranun = st.session_state["haeranun"]

new_data = get_statistics(data, anun, azganun, haeranun)

if new_data.empty:
    st.write("No data found for the given criteria.")
    st.page_link("home.py", label="Go back to Home")
else:
    st.write(new_data.head(10))
    plot_bar, plot_bar2 = get_plots(new_data)
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(plot_bar)
    with col2:
        st.plotly_chart(plot_bar2)