import spacy_streamlit
from pathlib import Path
import streamlit as st
import srsly
import os
import importlib

from hydralit import HydraHeadApp

class SpacyNLP(HydraHeadApp):

    def __init__(self, title = '', **kwargs):
        self.__dict__.update(kwargs)
        self.title = title
        
    def run(self):
        st.write('Hello')
