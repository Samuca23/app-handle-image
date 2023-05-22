import cv2
import streamlit as st
import numpy as np
from PIL import Image
from skimage import morphology, io, color, feature, filters

def principal():
    layoutPrincipal()

def layoutPrincipal():
    st.title("Tratativa de imagens com OpenCV")
    st.subheader("Aplicativo para integrar processamento de imagem")
    file_img = getUploadImage()

    borrao = st.sidebar.slider("Borrão", min_value=0.2, max_value=3.5)
    brilho = st.sidebar.slider("Brilho", min_value=50, max_value=50, value=0)
    melhoramento = st.sidebar.checkbox("Aplicar melhoramento")
    cinza = st.sidebar.checkbox("Aplicar filtro preto e branco")
    erosao = st.sidebar.checkbox("Aplicar filtro erosao")
    dilatacao = st.sidebar.checkbox("Aplicar filtro dilatacao")
    edge = st.sidebar.checkbox("Aplicar filtro edge")

    if file_img:
        openImageOriginal(file_img)
        file_img = Image.open(file_img)
        file_img = np.array(file_img)
        file_img_processada = borra_img(file_img, borrao)
        file_img_processada = brilho_img(file_img_processada, brilho)

        if melhoramento:
            file_img_processada = melhora_detalhe(file_img_processada)
        
        if cinza:
            file_img_processada = escala_cinza(file_img_processada)
        
        if erosao:
           file_img_processada = filter_erosao(file_img_processada)
        
        if dilatacao:
            file_img_processada = filter_dilatacao(file_img_processada)
        
        if edge:
            file_img_processada = filter_edge(file_img_processada)
        
        openImageHandler(file_img_processada)
       

def getUploadImage():
    return st.file_uploader("Envie sua imagem", type=["jpg", "png", "jpeg"])

def openImageOriginal(img):
    st.text("Imagem Original")
    st.image(img)

def openImageHandler(img):
    st.text("Imagem Processada")
    st.image(img)

def borra_img(img, resultado):
    return cv2.GaussianBlur(img, (7,7), resultado)

def brilho_img(img, resultado):
    return cv2.convertScaleAbs(img, beta=resultado)

def melhora_detalhe(img):
    return cv2.detailEnhance(img, sigma_s=34, sigma_r=0.50)

def escala_cinza(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def filter_erosao(img):
    return morphology.erosion(img)

def filter_dilatacao(img):
    return morphology.dilation(img)

def filter_edge(img):
    return filters.sobel(img)
        

if __name__ == "__main__":
    principal()