import pandas as pd
import streamlit as st
from hydralit import HydraHeadApp
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from hotstepper import Steps,Step
import hotstepper as hs
from itertools import chain
from hotstepper import Sequency


SIG_FIGURE_FMT = '{:,.2f}'

class WalshApp(HydraHeadApp):


    def __init__(self, title = '', **kwargs):
        self.__dict__.update(kwargs)
        self.title = title


    def run(self):

        try:
           st.title('hello')

        except Exception as e:
            st.image("./resources/failure.png",width=100,)
            st.error('An error has occurred, someone will be punished for your inconvenience, we humbly request you try again.')
            st.error('Error details: {}'.format(e))

