# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 13:32:41 2020

@author: Lara
"""
import streamlit as st
def main():
    st.title("Application Streamlit : Traitement de langage")
    choix = st.selectbox("Que souhaitez-vous faire?", ["Déterminez les rôles grammaticaux des mots dans une phrase", "Effectuer une analyse de sentiments"])
    
    if choix=="Déterminez les rôles grammaticaux des mots dans une phrase":
        
        from spacy_streamlit import visualize_tokens
        from spacy_streamlit import visualize_parser
        from spacy_streamlit import load_model
        st.header("Spacy - Streamlit : Rôles grammaticaux")
        spacy_model = st.selectbox("Nom du modèle que vous souhaitez utiliser", ["fr_core_news_sm", "fr_core_news_md","fr_core_news_lg"])
        
        nlp=load_model(spacy_model)
        
        texte = st.text_area('Ecrivez le texte à analyser:')
        if texte is not None: 
            texte1=nlp(texte)
            visualize_tokens(texte1, attrs=["text", "pos_", "dep_"],title="Rôle de chaque mot dans la phrase:")
            visualize_parser(texte1, title="Visualisation des dépendances entre mots de la phrase:", sidebar_title='Options de visualisation')
        
    elif choix=="Effectuer une analyse de sentiments":
        st.header("Analyse de sentiments")
        from textblob import TextBlob
        from textblob_fr import PatternTagger, PatternAnalyzer
        text = st.text_area('Ecrivez le texte à analyser:')
        blob = TextBlob(text, pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())
        if blob.sentiment[0] <-0.1:
            st.write("Le texte renvoie un sentiment négatif d'une polarité de",round(blob.sentiment[0]*100,2) ,"% avec une subjectivité de",blob.sentiment[1]*100, "%.")
        elif blob.sentiment[0] >0.1:
            st.write("Le texte renvoie un sentiment positif d'une polarité de",round(blob.sentiment[0]*100,2) ,"% avec une subjectivité de",blob.sentiment[1]*100, "%.")
        else:
            st.write("Le texte renvoie un sentiment neutre d'une polarité de",round(blob.sentiment[0]*100,2),"% avec une subjectivité de",blob.sentiment[1]*100, "%.")

if __name__ == '__main__':
	main()
    
