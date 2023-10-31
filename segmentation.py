import pydicom
import nibabel as nib
import os
import matplotlib.pyplot as plt
import numpy as np

# Load the DICOM images, NIfTI segmentation, and get the slice data with non-zero values
dicom_path = 'D:/Documentos/Uni/TFG/tfg_attempt/input/file1'
nifti_path = 'D:/Documentos/Uni/TFG/tfg_attempt/output/brain.nii/brain.nii'

if not os.path.exists(dicom_path):
    print(f"The DICOM directory '{dicom_path}' does not exist.")
    exit(1)

dicom_files = [os.path.join(dicom_path, filename) for filename in os.listdir(dicom_path) if filename.endswith('.dcm')]

if not dicom_files:
    print(f"No DICOM files found in '{dicom_path}'.")
    exit(1)

# Sort the DICOM files to ensure they are in the correct order
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

# Load the DICOM images
nifti_img = nib.load(nifti_path)
nifti_data = nifti_img.get_fdata()


# Create a list of slices with non-zero values from the NIfTI segmentation
valid_slices = [i for i in range(nifti_data.shape[-1]) if nifti_data[:, :, i].max() > 0]

# Display the DICOM images with NIfTI segmentation for the valid slices
for i in valid_slices:
    plt.figure()
    
    # Display the original DICOM image
    show_slice(slice_index)
    
    # Rotate the NIfTI segmentation to match the DICOM orientation
    rotated_nifti_data = np.rot90(nifti_data[:, :, i], k=1)  # Rotate 90 degrees counterclockwise 3 times (270 degrees clockwise)

    # Display the segmentation with transparency
    plt.imshow(rotated_nifti_data, cmap='jet', alpha=0.5)
    
    plt.title(f'Slice {i}')
    plt.colorbar()
    plt.show()
