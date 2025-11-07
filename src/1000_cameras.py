import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("1000_cameras\data\camera_dataset.csv")


# Drops a few columns and renames a few columns
df = df.drop(["Storage included", "Weight (inc. batteries)", "Dimensions"], axis = 1)
df = df.rename(columns={"Max resolution": "Max resolution (pixels)",
                        "Low resolution": "Low resolution (pixels)",
                        "Effective pixels": "Effective pixels (megapixels)",
                        "Normal focus range": "Normal focus range (cm)"
                        })

# Sorts the df by the top 10 cameras with the highest count of megapixels.
sorted_df = df.sort_values(by = "Effective pixels (megapixels)", ascending = False)
sorted_df = sorted_df.head(10)

# Create a dictionary mapping camera models to their sensor sizes
sensor_size = {
    'Canon EOS-1Ds Mark III': '36 x 24 mm',
    'Canon EOS-1Ds Mark II': '36 x 24 mm',
    'Kodak DCS 14n': '24 x 36 mm',
    'Kodak DCS SLR/n': '36 x 24 mm',
    'Kodak DCS SLR/c': '36 x 24 mm',
    'Nikon Coolpix P5100': '7.44 x 5.58 mm',
    'Canon PowerShot A650 IS': '7.53 x 5.64 mm',
    'Nikon D300': '23.6 x 15.8 mm',
    'Nikon D3': '36 x 23.9 mm',
    'Nikon D2Xs': '23.7 x 15.7 mm'
}
def get_sensor_size(model):
    return sensor_size.get(model)

sorted_df['Sensor sizes'] = sorted_df['Model'].apply(get_sensor_size)

# Inputting data into the "Zoom wide (W) column"
zoom_wide = {
    'Canon EOS-1Ds Mark III': '0',
    'Canon EOS-1Ds Mark II': '24',
    'Kodak DCS 14n': '43.27',
    'Kodak DCS SLR/n': '35',
    'Kodak DCS SLR/c': '35',
    'Nikon Coolpix P5100': '35',
    'Canon PowerShot A650 IS': '35',
    'Nikon D300': '28',
    'Nikon D3': '35',
    'Nikon D2Xs': '15.7'
}
def get_focal_length(model):
    return zoom_wide.get(model)

sorted_df['Zoom wide (W)'] = sorted_df['Model'].apply(get_focal_length)

"""Zoom Wide and Zoom Tele is the focal length
Additional information required: pixel size, field of view, or crop factor."""

# First plot
fig, ax1 = plt.subplots(figsize = (10, 10))
ax2 = ax1.twinx()

x = range(len(sorted_df))
width = 0.4

# Bars for Megapixels
bars1 = ax1.bar([i - width/2 for i in x], sorted_df['Effective pixels (megapixels)'], 
                width, color = 'tab:blue', label = 'Megapixels')
ax1.set_xlabel('Camera Models', fontsize = 12)
ax1.set_ylabel('Megapixels (Million Pixels)', color = 'black', fontsize = 12)
ax1.tick_params(axis='y', labelcolor = 'tab:blue')

# Bars for Price
bars2 = ax2.bar([i + width/2 for i in x], sorted_df["Price"], 
                width, color="tab:green", label = 'Price')
ax2.set_ylabel('Price ($)', color='black', fontsize = 12)
ax2.tick_params(axis = 'y', labelcolor='tab:green')

# Sensor size text overtop the bars
for i, (megapixels, sensor_size) in enumerate(zip(sorted_df['Effective pixels (megapixels)'], 
                                                  sorted_df['Sensor sizes'])):
    if pd.notna(sensor_size):
        ax1.text(i - width/2, megapixels - 5, sensor_size, 
                ha='center', va='bottom', rotation=90, fontsize=10, color='black', weight='bold')

# Sets the X and Y labels, the title, annotation, and the legend
ax1.set_xticks(x)
ax1.set_xticklabels(sorted_df["Model"], rotation = 45, ha = 'right')
ax1.legend([bars1[0], bars2[0]], ['Megapixels', 'Price'])
ax1.locator_params(axis='y', nbins = 15)
ax2.annotate('$129', xy=(3.2, 90), xytext = (3.05, 1500), color = 'green', arrowprops=dict(arrowstyle = '->', color = 'tab:red'), fontsize=10)
ax2.locator_params(axis='y', nbins = 20)
plt.title('Megapixels vs Price of The Top 10 Cameras', fontsize = 16)
plt.tight_layout()


# Second plot
sorted_df['Zoom wide (W)'] = pd.to_numeric(sorted_df['Zoom wide (W)'])
sorted_df['Zoom tele (T)'] = pd.to_numeric(sorted_df['Zoom tele (T)'])

fig, (ax1, ax2) = plt.subplots(2, 1, figsize = (12, 12))

sorted_by_zoom = sorted_df.sort_values(by = 'Zoom wide (W)')
x = range(len(sorted_by_zoom))
width = 0.35

# Focal Length Range Bar Graph
bars1 = ax1.bar([i - width/2 for i in x], sorted_by_zoom['Zoom wide (W)'], 
                width, color = 'tab:red', label = 'Wide Zoom')
bars2 = ax1.bar([i + width/2 for i in x], sorted_by_zoom['Zoom tele (T)'], 
                width, color = 'orange', label = 'Telephoto Zoom')

ax1.set_xlabel('Camera Models', fontsize = 12)
ax1.set_ylabel('Focal Length (mm)', fontsize = 12)
ax1.set_title("The Cameras' Focal Length Range", fontsize = 16)
ax1.set_xticks(x)
ax1.set_xticklabels(sorted_by_zoom['Model'], rotation = 45, ha = 'right')
ax1.legend()
ax1.grid(True, axis = 'y', alpha = 0.3, linestyle = '--')
ax1.set_axisbelow(True)
ax1.locator_params(axis = 'y', nbins = 10)

# Camera Prices Bar Graph
bars3 = ax2.bar(x, sorted_by_zoom['Price'], color = 'tab:green', alpha = 0.8, label='Price')

# Sets the X and Y labels, the title, annotation, gridlines, and the legend
ax2.set_xlabel('Camera Models', fontsize = 12)
ax2.set_ylabel('Price ($)', fontsize = 12)
ax2.set_title("Camera Prices", fontsize = 16)
ax2.set_xticks(x)
ax2.set_xticklabels(sorted_by_zoom['Model'], rotation = 45, ha = 'right')
ax2.annotate('$129', xy = (5, 30), xytext=(4.83, 1500), color = 'green', arrowprops = dict(arrowstyle = '->', color = 'tab:red'), fontsize=10)
ax2.grid(True, axis = 'y', alpha = 0.3, linestyle = '--')
ax2.set_axisbelow(True)
ax2.locator_params(axis = 'y', nbins = 15)
plt.tight_layout()
plt.show()