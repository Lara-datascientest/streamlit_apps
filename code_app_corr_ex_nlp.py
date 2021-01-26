# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 17:37:38 2021

@author: Lara_bis
"""

import streamlit as st
from tensorflow.keras.preprocessing.sequence import pad_sequences 
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.models import load_model
import os

def main():
    
    st.title("Application Streamlit: Réaliser une analyse de sentiment")
    st.header("Choisissez votre modèle de classification")
    chemin=os.path.dirname(os.path.abspath(__file__))
    def file_selector(chemin):
        filenames = os.listdir(chemin)
        filenames=[f for f in filenames if f.endswith('.' + "h5")]
        selected_filename = st.selectbox('Choisissez votre modèle ', filenames)
        return os.path.join(chemin, selected_filename)
    
    chemin=file_selector(chemin)
    model=load_model(chemin)
    
    texte = st.text_area('Ecrivez le texte à analyser:')
    if texte is not None: 
        texte1=texte
   
    instance = Tokenizer().texts_to_sequences(texte1)
    flat_list = []
    for sublist in instance:
        for item in sublist:
            flat_list.append(item)
    
    flat_list = [flat_list]

    instance = pad_sequences(flat_list, padding='post', maxlen=100)

    proba=round(model.predict(instance)[0][0]*100)
    
    if proba < 0:
        st.write("Le modèle prédit que le commentaire est négatif à hauteur de:",abs(proba),"%")
    else:
        st.write("Le modèle prédit que le commentaire est positif à hauteur de:",abs(proba),"%")  
    
if __name__ == "__main__":
    main()                