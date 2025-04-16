import streamlit as st
import pandas as pd
import yfinance as yf
from tips import display_tips_data 

st.title("Анализ данных")

page = st.sidebar.selectbox("Выберите страницу", ["Котировки Apple", "Чаевые"])

if page == "Котировки Apple":
    start_date = st.date_input("Выберите дату начала", pd.to_datetime("2024-01-01"))
    end_date = st.date_input("Выберите дату окончания", pd.to_datetime("today"))

    if start_date < end_date:
        data = yf.download("AAPL", start=start_date, end=end_date)
        st.subheader("Данные о котировках Apple")
        st.write(data)

        st.line_chart(data['Close'])
    else:
        st.error("Дата начала должна быть меньше даты окончания.")

elif page == "Чаевые":
    display_tips_data()