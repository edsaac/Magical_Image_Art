import cv2
import numpy as np
from PIL import Image
import streamlit as st
from streamlit_image_comparison import image_comparison as img_compare
from image_process import *

# Set page title and favicon.
st.set_page_config(
    page_title="Magical Image Art", page_icon='🌟',
)

st.write('## Magical Art Effects on Image using OpenCV 🧙‍♂️✨')
with st.sidebar:
    bg = Image.open('bg_show.png')
    st.image(bg, width=327)

"""
[![Star](https://img.shields.io/github/stars/ShruAgarwal/Magical_Image_Art.svg?logo=github&style=social)](https://github.com/ShruAgarwal/Magical_Image_Art)
[![Follow](https://img.shields.io/twitter/follow/Shru_explores?style=social)](https://www.twitter.com/Shru_explores)
"""

with st.expander("⭐ HIGHLIGHTS OF THE APP"):
    st.write("""This app can convert & apply three different effects on an Image,
             i.e, `pop/dotted art`, `water color art` & `cartoon style art`.
             \nAll the above effects are given using two python libraries -- *OPENCV & NUMPY* 🤯
             \n 👈 *Sidebar (in left) is an illustration of effects applied onto images*
             \nHope you'll like it! 🙌

                 """)

file_up = st.file_uploader("UPLOAD AN IMAGE",key="file_up")
st.button('See the Magic! 🎉',key="btn_go")

##################################################################################

if st.session_state.file_up and st.session_state.btn_go:
    tab1, tab2, tab3 = st.tabs(["CARTOON 😲", "POP ART 👀", "WATERCOLOR 🎨"])
    
    display_image = Image.open(file_up)

    with tab1:
        st.write('### CARTOON STYLED IMAGE')

        cartoon_img = cartoon_style(display_image)

        # Using image-comparison
        img_compare(
            img1 = display_image,
            img2 = cartoon_img,
            label1 = "original",
            label2 = "new",
            width = 800,
            show_labels = True,
        )
        
    with tab2:
        st.write('### POP ART IMAGE')
        pop_image = pop_art(display_image)
        st.image(pop_image)

    with tab3:
        st.write('### WATERCOLOR STYLED IMAGE')
        water_image = waterColor_style(display_image)
        st.image(water_image)
        
        
