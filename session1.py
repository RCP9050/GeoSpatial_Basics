!pip install matplotlib osgeo numpy
import streamlit as st
import matplotlib.pyplot as plt
from osgeo import gdal
import numpy as np

# App Title
st.title("Satellite Image Viewer")

# Uploading file
uploaded_file = st.file_uploader("Choose a JP2 file", type=["jp2"])

if uploaded_file is not None:
    # Save the uploaded file temporarily
    with open("temp_image.jp2", "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Open the JP2 file using GDAL
    dataset = gdal.Open("temp_image.jp2")
    
    # Read the first band (assuming a single band image, modify for multi-band images)
    band = dataset.GetRasterBand(1)
    image_data = band.ReadAsArray()

    # Show image data information
    st.write(f"Image size: {image_data.shape}")
    st.write(f"Data type: {image_data.dtype}")

    # Plot the image using Matplotlib
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.imshow(image_data, cmap="gray")
    ax.set_title("Satellite Image")
    ax.axis('off')

    # Display the plot in Streamlit
    st.pyplot(fig)

