import datetime
import io
from hydralit import HydraHeadApp

import astropy.units as u
import pandas as pd
import streamlit as st
from astropy.coordinates import SkyCoord
from sunpy.coordinates import frames

from apps.extras.backmapping import *
import hydralit_components as hc


class SolarMach(HydraHeadApp):

    def __init__(self, title = '', **kwargs):
        self.__dict__.update(kwargs)
        self.title = title

    def run(self):
        
        st.write('AI v2')