from totalsegmentator.python_api import totalsegmentator
import pydicom as dicom
import matplotlib.pyplot as plt
import zipfile
import os

# Has to be a folder with dicom files
input_path = "./input/file1_2.zip"
output_path = "./output/Segmentation1"

# Input and output paths
input_zip_path = "./input/segmentations.zip"
output_path = "./output/Segmentation1"

"""
# Unzip the DICOM files from the ZIP archive to a temporary directory
temp_dir = "./temp_dicom"
with zipfile.ZipFile(input_zip_path, 'r') as zip_ref:
    zip_ref.extractall(temp_dir)
"""
# Run the segmentation on the unzipped DICOM files
totalsegmentator(input_zip_path, output_path)

"""
# Clean up the temporary directory
for file in os.listdir(temp_dir):
    file_path = os.path.join(temp_dir, file)
    if os.path.isfile(file_path):
        os.remove(file_path)
os.rmdir(temp_dir)
"""