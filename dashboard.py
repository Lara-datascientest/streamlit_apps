#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 19 13:16:11 2021

@author: lara
"""

# Import des librairies 

import streamlit as st

st.set_page_config(page_title = "Dashboard technique",
                   layout='wide')

st.markdown("# Chiffres clés ")

indicateur_1, indicateur_2, indicateur_3 = st.beta_columns(3)


with indicateur_1: 
    st.markdown("**Performance du modèle**")
    number1="79%"
    st.markdown(f"<h1 style='text-align: center; color: #EF5350;'>{number1}<h1/>",
                unsafe_allow_html=True)
    

with indicateur_2: 
    st.markdown("** % de clients identifiés à contacter**")
    number2="30%"
    st.markdown(f"<h1 style='text-align: center; color: #EF5350;'>{number2}<h1/>",
                unsafe_allow_html=True)
    
with indicateur_3: 
    st.markdown("**Economie réalisée pour 10 000 clients**")
    number3="40 000€"
    st.markdown(f"<h1 style='text-align: center; color: #EF5350;'>{number3}<h1/>",
                unsafe_allow_html=True)
    
st.markdown("<hr/>", unsafe_allow_html=True)
    
st.markdown("# Caractéristiques des clients identifiés")

indicateur_11, indicateur_22, indicateur_33, indicateur_44, indicateur_55= st.beta_columns(5)

    
with indicateur_11: 
    st.markdown("**% de clients identifiés avec dommages**")
    number11="98%"
    st.markdown(f"<h1 style='text-align: center; color: LightSkyBlue;'>{number11}<h1/>",
                unsafe_allow_html=True)

with indicateur_22: 
    st.markdown("**Moyenne d'âge des clients identifiés**")
    number22="46 ans"
    st.markdown(f"<h1 style='text-align: center; color: LightSkyBlue;'>{number22}<h1/>",
                unsafe_allow_html=True)   
    
with indicateur_33: 
    st.markdown("**Prime moyenne sur les clients identifiés**")
    number33="279€"
    st.markdown(f"<h1 style='text-align: center; color: LightSkyBlue;'>{number33}<h1/>",
                unsafe_allow_html=True)

with indicateur_44: 
    st.markdown("**% d'hommes sur les clients identifiés**")
    number44="61%"
    st.markdown(f"<h1 style='text-align: center; color: LightSkyBlue;'>{number44}<h1/>",
                unsafe_allow_html=True)
    
with indicateur_55: 
    st.markdown("**% de clients non assurés précédemment**")
    number55="99,9%"
    st.markdown(f"<h1 style='text-align: center; color: LightSkyBlue;'>{number55}<h1/>",
                unsafe_allow_html=True)

st.markdown("# Caractéristiques sur tous les clients ")

indicateur_111, indicateur_222, indicateur_333, indicateur_444, indicateur_555 = st.beta_columns(5)

with indicateur_111: 
    st.markdown("**% de clients avec dommages**")
    number111="50%"
    st.markdown(f"<h1 style='text-align: center; color: #80CBC4;'>{number111}<h1/>",
                unsafe_allow_html=True)
    
with indicateur_222: 
    st.markdown("**Moyenne d'âge de tous les clients**")
    number222="39 ans"
    st.markdown(f"<h1 style='text-align: center; color: #80CBC4;'>{number222}<h1/>",
                unsafe_allow_html=True)
      
with indicateur_333: 
    st.markdown("**Prime moyenne sur tous les clients**")
    number333="305€"
    st.markdown(f"<h1 style='text-align: center; color: #80CBC4;'>{number333}<h1/>",
                unsafe_allow_html=True)
    
with indicateur_444: 
    st.markdown("**% d'hommes sur tous les clients**")
    number444="55%"
    st.markdown(f"<h1 style='text-align: center; color: #80CBC4;'>{number444}<h1/>",
                unsafe_allow_html=True)

with indicateur_555: 
    st.markdown("**% de clients non assurés précédemment**")
    number555="54%"
    st.markdown(f"<h1 style='text-align: center; color: #80CBC4;'>{number555}<h1/>",
                unsafe_allow_html=True)

    
st.markdown("<hr/>", unsafe_allow_html=True)































