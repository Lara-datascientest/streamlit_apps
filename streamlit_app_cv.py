    # -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 17:11:17 2020

@author: Lara
"""
import streamlit as st
import numpy as np
from PIL import Image 
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
import os


def main():
    st.title("Application Streamlit: Utiliser un modèle de classification d'image")
    st.header("Choisissez votre modèle de classification")
    chemin=os.path.dirname(os.path.abspath(__file__))
    def file_selector(chemin):
        filenames = os.listdir(chemin)
        filenames=[f for f in filenames if f.endswith('.' + "h5")]
        selected_filename = st.selectbox('Choisissez votre modèle ', filenames)
        return os.path.join(chemin, selected_filename)
    chemin=file_selector(chemin)

    st.header("Choisissez une image à classifier")
    image = st.file_uploader("Image:", type=["png", "jpg", "jpeg"])
    
    if image is not None:
        image = Image.open(image)
        st.image(image,caption="Image importée",use_column_width=True)
        image = image.resize((64,64))
        image_redim = img_to_array(image)/255
        image_redim = np.expand_dims(image_redim, axis = 0)
        
        try: 
            model=load_model(chemin)
            proba = round(100*model.predict(image_redim)[0][0], 2)
            if proba < 50:
                proba = round(100-proba, 2)
                st.write("Ce n'est pas le père Noël et on en est sur à:",proba,"%")
            else:
                st.write("C'est le père Noël et on en est sur à:",proba,"%") 
                
        except ValueError:
            model = load_model(chemin)
            image_redim = image_redim[:1, :64, :64, :3]
            proba = round(100*model.predict(test_image)[0][0], 2)
            if proba < 50:
                proba = round(100-proba, 2)
                st.write("Ce n'est pas le père Noël et on en est sur à:",proba,"%")
            else:
                st.write("C'est le père Noël et on en est sur à:",proba,"%") 
            
if __name__ == "__main__":
    main()            



