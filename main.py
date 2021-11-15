
import API
import time
import webbrowser
from PIL import Image
import streamlit as st
from utils import SIGNS
from datetime import date

st.set_page_config(page_title="Forex Currency Predicter By Nasr Akram",
                       layout="wide",initial_sidebar_state='collapsed')

def engine():

    def is_authenticated(password):
        return password == "admin"

    def generate_login_block():
        block1 = st.empty()
        block2 = st.empty()

        return block1, block2

    def clean_blocks(blocks):
        for block in blocks:
            block.empty()


    def login(blocks):
        blocks[0].markdown("""
                    <style>
                        input {
                            -webkit-text-security: disc;      
                        }
                    </style>
                """, unsafe_allow_html=True)
        image = Image.open('logo.png')
        st.sidebar.image(image, caption=None, width=100, use_column_width=None, clamp=False, channels="RGB", output_format="centered")
        return blocks[1].text_input('Password')

    def main():
        st.balloons()
        my_bar = st.progress(0)

        for percent_complete in range(100):
            time.sleep(0.005)
            my_bar.progress(percent_complete + 1)
        st.header('Welcome')

        from predictions import predictions
        from utils import divide_currencies, DAYS_OF_PREDICTION, SIGNS_DESCRIPTIONS

        TODAY = date.today()
        st.title("Forex Currency Multitool Predicter")
        st.subheader("By Nasr Akram")
        st.write("""""")
        st.write("""""")
        st.sidebar.info(
            f" NOTE ! : Easy menu to manipulate data"
        )
        if st.sidebar.button('Logout'):
            generate_login_block()




        BASE = st.sidebar.selectbox("Pick a base currency", SIGNS)
        st.write("""""")
        AMOUNT = st.sidebar.number_input("Amount to be converted:", step=1.0, min_value=1.00)
        st.write("""""")

        st.success(
            f" Some easy tools to get a quick access"
        )

        START_DATE = st.sidebar.date_input("Pick Data Pool", max_value=TODAY)

        st.write(
            f'<iframe width="100%" height="750px" src="https://www.forex.com/en/market-analysis/latest-research/"></iframe>',
            unsafe_allow_html=True,
        )

        # Definitions of requests
        st.write("""""")
        st.write("""""")
        st.subheader("Live Market Currency Chart")
        url1 = 'https://www.tradingview.com/chart/AOECoZZ9/'
        if st.button('Advanced online tool'):
            webbrowser.open_new_tab(url1)
        st.write(
                f'<iframe width="100%" height="600px" src="https://s.tradingview.com/dailyfx/widgetembed/?frameElementId=tradingview_8ef6b&symbol=FX_IDC%3AEURUSD&interval=D&hidesidetoolbar=0&symboledit=1&saveimage=1&toolbarbg=EEEFF0&studies=%5B%5D&hideideas=1&theme=Light&timezone=exchange&studies_overrides=%7B%7D&overrides=%7B%7D&enabled_features=%5B%5D&disabled_features=%5B%5D&locale=en&utm_source=www.dailyfx.com&utm_medium=widget&utm_campaign=chart&utm_term=FX_IDC%3AEURUSD"></iframe>',
                unsafe_allow_html=True,
            )
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
        col1, col2 = st.columns(2)
        col1.metric("Buy", "70", "1.2 %")
        col2.metric("Sell", "9", "-5%")
        # st.write(history_data)
        # this part is for future data output as a candle graph
        time_series_conversion_df = API.request_time_series_conversion(BASE,
                                                                                AMOUNT, str(START_DATE),
                                                                                      str(TODAY))
        st.write(time_series_conversion_df)

        st.write("""""")
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
                st.subheader(
                    f"Value of {BASE}'s to {SIGNS_DESCRIPTIONS[k]}")
                colx, coly = st.columns([3, 1])
                with colx:
                    st.line_chart(forecast['currency'])
                with coly:
                    forecast['currency']

        except ValueError as e:
            st.success(
                f" Feed the AI data to get accurate predictions"
            )

    login_blocks = generate_login_block()
    password = login(login_blocks)

    if is_authenticated(password):
        clean_blocks(login_blocks)
        main()
    elif password:
        st.info("Please enter a valid password")
engine()