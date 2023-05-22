import cv2
import streamlit as st
import numpy as np
from PIL import Image
from skimage import morphology, io, color, feature, filters

def layout():
    st.title("Tratativa de imagens com OpenCV")
    st.subheader("Aplicativo para integrar processamento de imagem")

def principal():
    layout()

if __name__ == "__main__":
    principal()