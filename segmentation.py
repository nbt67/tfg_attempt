import pydicom
import nibabel as nib
import os
import matplotlib.pyplot as plt
import numpy as np
import utils 


def load_dicom(dicom_path):
    if dicom_path:
        if utils.is_zip_file(dicom_path):
            print(f"The provided path '{dicom_path}' is a zip file. The input must be a folder with DICOM files.")
            exit(1)
             
        if not os.path.exists(dicom_path):
            print(f"The DICOM directory '{dicom_path}' does not exist.")
            exit(1)
        
        #Creates a list with all the dicom files 
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
        dicom_volume = 255 * (pixel_data_array - pixel_data_array.min()) / (pixel_data_array.max() - pixel_data_array.min())

    else:
        dicom_volume = None

    return dicom_volume


def load_nifti(nifti_path):
    if nifti_path:
        if utils.is_zip_file(nifti_path):
            print(f"The provided path '{nifti_path}' is a zip file. The input must be a nifti file.")
            exit(1)
             
        if not os.path.exists(nifti_path):
            print(f"The nifti directory '{nifti_path}' does not exist.")
            exit(1)        

        if not utils.is_nifti_file(nifti_path):
            print(f"The file is not a nifti file '{nifti_path}'. It must end with nii.gz or nii.")
            exit(1)        

        if os.path.isdir(nifti_path):
            print(f"It can't be a directory, it must be a nifti file. '{nifti_path}'")
            exit(1)

        # Load the nifti images
        nifti_img = nib.load(nifti_path)
        nifti_data = nifti_img.get_fdata()

    else:
        nifti_data = None

    return nifti_data


def show_slice(slice_index, volume):

    #For the specified slice we plot it from the dicom volume
    slice_index = int(slice_index)
    plt.imshow(volume[slice_index], cmap=plt.cm.bone)
    plt.title(f"DICOM Slice {slice_index}")
    plt.colorbar()


def check_valid_slices(nifti_data):        
        # Create a list of slices with non-zero values from the NIfTI segmentation
        valid_slices = [i for i in range(nifti_data.shape[-1]) if nifti_data[:, :, i].max() > 0]
        return valid_slices


def plot_dicom_nifti(volume, nifti_data, valid_slices=True, slice_index=None):

    if valid_slices:
        nifti_slices = check_valid_slices(nifti_data)

    # Display the DICOM images with NIfTI segmentation for the valid slices
    for i in nifti_slices:
        plt.figure()
        
        # Display the original DICOM image
        if slice_index:
            show_slice(slice_index, volume)

        show_slice(i, volume)
        
        # Rotate the NIfTI segmentation to match the DICOM orientation
        rotated_nifti_data = np.rot90(nifti_data[:, :, i], k=1)  # Rotate 90 degrees counterclockwise 3 times (270 degrees clockwise)

        # Display the segmentation with transparency
        plt.imshow(rotated_nifti_data, cmap='jet', alpha=0.5)
        
        plt.title(f'Slice {i}')
        plt.colorbar()
        plt.show()
