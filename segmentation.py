import pydicom
import nibabel as nib
import os
import matplotlib.pyplot as plt

# Load the DICOM images, NIfTI segmentation, and get the slice data with non-zero values
dicom_path = 'D:/Documentos/Uni/TFG/totalSegmentatorAttempt/input/file1'
nifti_path = 'D:/Documentos/Uni/TFG/totalSegmentatorAttempt/output/brain.nii/brain.nii'

if not os.path.exists(dicom_path):
    print(f"The DICOM directory '{dicom_path}' does not exist.")
    exit(1)

dicom_files = [file for file in os.listdir(dicom_path) if file.endswith('.dcm')]

if not dicom_files:
    print(f"No DICOM files found in '{dicom_path}'.")
    exit(1)

# Sort the DICOM files to ensure they are in the correct order
sorted_dicom_files = sorted(dicom_files, key=lambda x: int(x.split('.')[0][2:]))  # Assumes a pattern like 'CT000000.dcm'

# Load the DICOM images
dicom_images = [pydicom.dcmread(os.path.join(dicom_path, dicom_file)) for dicom_file in sorted_dicom_files]
nifti_img = nib.load(nifti_path)
nifti_data = nifti_img.get_fdata()


# Create a list of slices with non-zero values from the NIfTI segmentation
valid_slices = [i for i in range(nifti_data.shape[-1]) if nifti_data[:, :, i].max() > 0]

# Display the DICOM images with NIfTI segmentation for the valid slices
for i in valid_slices:
    plt.figure()
    
    # Display the original DICOM image
    plt.imshow(dicom_images[i].pixel_array, cmap='gray')
    
    # Display the segmentation with transparency
    plt.imshow(nifti_data[:, :, i], cmap='jet', alpha=0.5)
    
    plt.title(f'Slice {i}')
    plt.colorbar()
    plt.show()
