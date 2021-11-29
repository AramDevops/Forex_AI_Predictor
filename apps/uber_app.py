
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import pydeck as pdk
from hydralit import HydraHeadApp


class UberNYC(HydraHeadApp):

    def __init__(self, title = '', **kwargs):
        self.__dict__.update(kwargs)
        self.title = title

    def run(self):

       st.write('hello')