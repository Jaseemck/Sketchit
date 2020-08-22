import streamlit as st
import cv2
from PIL import Image
import numpy as np

def dodgeV2(x, y):
    return cv2.divide(x, 255 - y, scale=256)

def sketchit(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_invert = cv2.bitwise_not(img_gray)
    img_smoothing = cv2.GaussianBlur(img_invert, (21, 21),sigmaX=0, sigmaY=0)
    final_img = dodgeV2(img_gray, img_smoothing)
    return final_img

def download():
    return f'<a href="{final.jpg}" download="Image.jpeg">Download Img</a>'

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
        Image.fromarray(final).show()
