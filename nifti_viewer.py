import nibabel as nib

# Load the NIfTI image
nifti_img = nib.load('D:/Documentos/Uni/TFG/tfg_attempt/output/brain.nii/brain.nii')

import matplotlib.pyplot as plt

# Get the image data from the NIfTI object
img_data = nifti_img.get_fdata()

# Display multiple slices as an animation
plt.figure()

for i in range(img_data.shape[-1]):
    slice_data = img_data[:, :, i]

    # Check if the slice contains non-zero values
    if slice_data.max() > 0:
        plt.imshow(slice_data, cmap='gray')
        plt.title(f'Slice {i}')
        plt.colorbar()
        plt.pause(0.1)  # Pause for a short time between frames
        plt.clf()  # Clear the current plot for the next frame

# To keep the plot window open after the visualization
plt.show()