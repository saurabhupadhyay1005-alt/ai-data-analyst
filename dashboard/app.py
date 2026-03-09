import streamlit as st
import pandas as pd
import plotly.express as px

from src.ai_query_engine import analyze_question


st.set_page_config(page_title="AI Data Analyst", layout="wide")

st.title("AI Data Analyst (ChatGPT for Datasets)")

st.write("Upload a dataset and ask questions about it.")


uploaded_file = st.file_uploader("Upload CSV dataset", type="csv")


if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")

    st.dataframe(df.head())


    st.subheader("Revenue by Category")

    category = df.groupby("Category")["Revenue"].sum().reset_index()

    fig = px.bar(category, x="Category", y="Revenue", color="Category")

    st.plotly_chart(fig, use_container_width=True)


    st.subheader("Revenue by Region")

    region = df.groupby("Region")["Revenue"].sum().reset_index()

    fig2 = px.pie(region, names="Region", values="Revenue")

    st.plotly_chart(fig2, use_container_width=True)


    st.subheader("Ask AI about your dataset")

    question = st.text_input("Example: Which region has highest revenue?")


    if question:

        answer = analyze_question(df, question)

        st.success(answer)