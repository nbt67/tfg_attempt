import os
import pydicom
import matplotlib.pyplot as plt
import numpy as np

# Directory containing DICOM files
dicom_dir = "D:/Documentos/Uni/TFG/tfg_attempt/input/file1"

# Get a list of all DICOM files in the directory
dicom_files = [os.path.join(dicom_dir, filename) for filename in os.listdir(dicom_dir) if filename.endswith('.dcm')]

# Sort the DICOM files based on their instance number (slice location)
dicom_files.sort(key=lambda x: pydicom.dcmread(x).InstanceNumber)

# Create an empty list to store the pixel data
pixel_data_list = []

# Load the pixel data from each DICOM file
for dicom_file in dicom_files:
    ds = pydicom.dcmread(dicom_file)
    pixel_data = ds.pixel_array
    pixel_data_list.append(pixel_data)

# Convert the list of pixel data to a NumPy array
pixel_data_array = np.array(pixel_data_list)

# Create a 3D volume from the NumPy array
volume = 255 * (pixel_data_array - pixel_data_array.min()) / (pixel_data_array.max() - pixel_data_array.min())

# Display the 3D volume (you can scroll through slices with the 'slice_index' variable)
slice_index = 56

def show_slice(slice_index):
    plt.imshow(volume[slice_index], cmap=plt.cm.bone)
    plt.title(f"DICOM Slice {slice_index}")
    plt.colorbar()

show_slice(slice_index)
plt.show()
