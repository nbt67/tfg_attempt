from totalsegmentator.python_api import totalsegmentator
import zipfile
import os
import segmentation
import nifti_viewer
import dicom_viewer

# Load the DICOM images, NIfTI segmentation, and get the slice data with non-zero values
dicom_path = 'D:/Documentos/Uni/TFG/tfg_attempt/input/file1'
nifti_path = 'D:/Documentos/Uni/TFG/tfg_attempt/output/brain.nii.gz'

dicom_volume = segmentation.load_dicom(dicom_path)
nifti_data = segmentation.load_nifti(nifti_path)

#nifti_viewer.nifti_viewer(nifti_data, None)

#dicom_viewer.dicom_viewer(dicom_volume, None)

#segmentation.plot_dicom_nifti(dicom_volume, nifti_data)