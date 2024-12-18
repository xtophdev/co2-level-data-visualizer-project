import pandas as pd

# Load the CSV file
data = pd.read_csv("co2_mm_gl.csv", skiprows=57)  # Skip the first 57 rows of metadata
print(data.head())  # Display the first few rows
# Rename columns
data.columns = ["Year", "Month", "Decimal_Date", "Average_CO2", "Average_CO2_Uncertainty", "Trend", "Trend_Uncertainty"]
print(data.head())  # Display updated column names
# Check for missing data
print(data.isnull().sum())
import matplotlib.pyplot as plt

# Create a line plot for CO₂ levels
plt.figure(figsize=(10, 6))
plt.plot(data["Decimal_Date"], data["Average_CO2"], label="Average CO₂ (ppm)", color="green")
plt.plot(data["Decimal_Date"], data["Trend"], label="Trend", color="blue", linestyle="--")

# Add labels and title
plt.title("Global Monthly Mean CO₂ Levels (1980 - Present)", fontsize=16)
plt.xlabel("Year", fontsize=14)
plt.ylabel("CO₂ (ppm)", fontsize=14)
plt.legend(fontsize=12)
plt.grid(True)
plt.show()
