import webbrowser

from hydralit import HydraHeadApp
from datetime import time, date
import streamlit as st
from pathlib import Path
import base64
import time

# Thanks to streamlitopedia for the following code snippet
import API
from utils import SIGNS


def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded



class CheatApp(HydraHeadApp):

    def __init__(self, title = '', **kwargs):
        self.__dict__.update(kwargs)
        self.title = title
        
    def run(self):

        st.balloons()
        my_bar = st.progress(0)

        for percent_complete in range(100):
            time.sleep(0.005)
            my_bar.progress(percent_complete + 1)

        from predictions import predictions
        from utils import divide_currencies, DAYS_OF_PREDICTION, SIGNS_DESCRIPTIONS

        TODAY = date.today()
        st.write("""""")
        st.write("""""")
        BASE = st.sidebar.selectbox("Pick a base currency", SIGNS)
        st.write("""""")
        AMOUNT = st.sidebar.number_input("Amount to be converted:", step=1.0, min_value=1.00)
        st.write("""""")
        START_DATE = st.sidebar.date_input("Data Pool", max_value=TODAY)

        # Definitions of requests
        st.write("""""")
        st.write("""""")
        st.write("""""")
        st.write("""""")

        i = st.sidebar.selectbox(
            "Interval in minutes",
            ("1m", "5m", "30m", "1h", "1d")
        )

        url2 = 'https://freecurrencyapi.net/dashboard'
        if st.sidebar.button('API STATUS'):
            webbrowser.open_new_tab(url2)
        st.sidebar.header('AI Forex Predicter v2')

        # st.write(history_data)
        # this part is for future data output as a candle graph
        time_series_conversion_df = API.request_time_series_conversion(BASE,
                                                                       AMOUNT, str(START_DATE),
                                                                       str(TODAY))
        st.write("""""")
        st.write(time_series_conversion_df)
        st.subheader(f" AI Predictions : ")
        st.write("""""")
        st.write("""""")
        try:

            st.subheader(f" Predictions for the next {DAYS_OF_PREDICTION} days")
            st.write("""""")
            st.write("""""")
            time_series_dict_to_forecast = divide_currencies(time_series_conversion_df, BASE)
            for k in time_series_dict_to_forecast.keys():
                forecast = predictions(time_series_dict_to_forecast[k])

                m = max((forecast['currency'] - 0.0002) * AMOUNT)
                l = min((forecast['currency'] - 0.0002) * AMOUNT)

                pr = ((m-l)/((m+l)/2))*100
                npr = -1*pr
                col1, col2 = st.columns(2)
                col1.metric("Sell", "{:.5f}".format(m), str("{:.2f}".format(pr)) + "%")
                col2.metric("Buy", "{:.5f}".format(l), str("{:.2f}".format(npr)) + "%")
                st.subheader(
                    f"Value of {BASE}'s to {SIGNS_DESCRIPTIONS[k]}")
                colx, coly = st.columns([3, 1])
                with colx:
                    st.line_chart((forecast['currency']-0.0002)*AMOUNT)
                with coly:
                    st.write((forecast['currency']-0.0002)*AMOUNT)

        except ValueError as e:
            st.success(
                f" Feed the AI data to get accurate predictions"
            )

