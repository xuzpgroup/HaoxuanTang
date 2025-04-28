# Low-Temperature Alloy Mechanical Properties Data Construction Project

This project is dedicated to building a dataset for the mechanical properties of low-temperature alloys. The code is divided into five major modules, as outlined below:

## Modules Overview

1. **Document Download**
   - This module compiles search queries based on keywords and retrieves relevant literature from Web of Science. It then downloads the literature in XML/HTML and PDF formats and extracts structured text.

2. **Text Processing**
   - This module processes the downloaded structured text using GPT and GLM to extract the required data from the literature.

3. **Figure Processing**
   - This module extracts images from the literature, segments composite images, and filter the required experimental images. ImageEXtractor software is used to collect data points from the images.

4. **Dataset Processing Scripts**
   - These are post-processing scripts for the dataset. They allow for accessing data, adding entries, importing standard formats, and evaluating data quality.

5. **Data Visualization**
   - This module provides code for visualizing the data, generating statistical plots.

## Usage

For detailed instructions on how to use each module, please refer to the `README.md` files located in the corresponding subdirectories.
