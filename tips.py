import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

def display_tips_data():
    file_path = "tips.csv" 
    tips_data = pd.read_csv(file_path)

    st.subheader("Данные о чаевых")
    st.write(tips_data)

    st.subheader("График чаевых по дням")
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='day', y='tip', data=tips_data)
    plt.title("Распределение чаевых по дням")
    st.pyplot(plt)

    st.subheader("Сумма чаевых по полу")
    plt.figure(figsize=(10, 6))
    sns.barplot(x='sex', y='tip', data=tips_data, estimator=sum)
    plt.title("Сумма чаевых по полу")
    st.pyplot(plt)

    st.subheader("Чаевые по размеру группы")
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='size', y='tip', data=tips_data)
    plt.title("Чаевые в зависимости от размера группы")
    st.pyplot(plt)