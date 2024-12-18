# co2-level-data-visualizer-project
 This project is a simple Python-based tool for visualizing global monthly mean CO₂ levels over time. The tool reads a CSV dataset containing atmospheric CO₂ measurements, processes the data, and generates a line plot to visualize trends.
The script reads CO₂ data from a CSV file, cleans and processes the dataset by renaming columns and checking for missing data, and visualizes the data using a line plot. The plot includes the Average CO₂ (ppm) represented as a green line and the Trend represented as a blue dashed line. The visualization displays the relationship between CO₂ levels and time, showing trends from 1980 to the present. The following Python libraries are required to run the script: pandas for reading and processing the CSV file and matplotlib for visualizing the data. You can install the required libraries using pip:
pip install pandas matplotlib
To use this project, place the co2_mm_gl.csv file in the same directory as the script. Ensure the CSV file starts with 57 rows of metadata (which the script skips). Run the Python script using the command:
python main.py
The script will produce a plot
This project is open-source and available under the MIT License. The dataset used in this project is publicly available and sourced from reputable environmental monitoring organizations.
