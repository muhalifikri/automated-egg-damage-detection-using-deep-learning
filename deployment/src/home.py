import streamlit as st
import matplotlib.image as mpimg


def run():
    #membuat title
    st.title ('Model for Filtering Duck Egg')

    #input gambar
    data =mpimg.imread ('./src/duck_egg.jpg')
    st.image(data, caption='Duck Egg')




        
if __name__ == '__main__':
    run()