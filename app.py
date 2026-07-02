import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.title("Nassau Candy Distributor Data Analysis")

df = pd.read_csv("Nassau Candy Distributor.csv")

st.header("First 5 Rows")
st.dataframe(df.head())

st.header("Dataset Information")
st.write(df.describe(include='all'))

st.header("Missing Values")
st.write(df.isnull().sum())

df = df.drop_duplicates()

first_col = df.columns[0]

st.header(f"Top 10 {first_col}")

fig, ax = plt.subplots(figsize=(8, 5))
df[first_col].value_counts().head(10).plot(kind="bar", ax=ax)
plt.xticks(rotation=45)
st.pyplot(fig)

st.success("Data Analysis Completed Successfully!")