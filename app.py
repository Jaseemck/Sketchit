import streamlit as st
import cv2
from PIL import Image
import numpy as np
import os
import base64

def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Download {file_label}</a>'
    return href

def dodgeV2(x, y):
    return cv2.divide(x, 255 - y, scale=256)

def sketchit(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_invert = cv2.bitwise_not(img_gray)
    img_smoothing = cv2.GaussianBlur(img_invert, (21, 21),sigmaX=0, sigmaY=0)
    final_img = dodgeV2(img_gray, img_smoothing)
    return final_img

st.set_option('deprecation.showfileUploaderEncoding', False)
st.title("SketchIt")
st.success("Now, everyone's an Artist! \U0001f600")
st.sidebar.success("Upload Your Photo :point_down:")
file_img = st.sidebar.file_uploader("", type=['jpeg','jpg','png'])
st.sidebar.info("This is an application that converts the uploaded image into sketch. Feel free to contribute!")
if file_img is None:
    st.warning(":point_left: Upload an Image to Sketch it!")
else:
    img = Image.open(file_img)
    final = sketchit(np.array(img))
    st.write("Input Image")
    st.image(file_img, use_column_width=True)
    st.write("Output Image")
    st.image(final, use_column_width=True)
    if st.button('Download Image'):
        st.success('Good')
        #st.markdown(get_binary_file_downloader_html(bytes(final), 'Picture'), unsafe_allow_html=True)
