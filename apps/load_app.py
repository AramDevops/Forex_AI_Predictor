import os
import API
import time
import webbrowser
import streamlit as st
from utils import SIGNS
from datetime import date
import hydralit_components as hc
from hydralit import HydraHeadApp
from predictions import predictions
from utils import divide_currencies, DAYS_OF_PREDICTION, SIGNS_DESCRIPTIONS

class LoaderTestApp(HydraHeadApp):

    def __init__(self, title = 'Forex Tools', delay=0, **kwargs):
        self.__dict__.update(kwargs)
        self.title = title
        self.delay = delay

    def run(self):

        try:
            st.title("Forex Currency Multitool Predicter")
            st.subheader("By Nasr Akram")
            st.write("""""")
            st.write("""""")

            st.write("""""")

            st.success(
                f" Some easy tools to get a quick access"
            )

            st.write(
                f'<iframe width="100%" height="750px" src="https://www.foxnews.com/"></iframe>',
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




        except Exception as e:
            st.image(os.path.join(".","resources","failure.png"),width=100,)
            st.error('An error has occurred, someone will be punished for your inconvenience, we humbly request you try again.')
            st.error('Error details: {}'.format(e))
