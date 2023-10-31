import matplotlib.pyplot as plt
import numpy as np


def nifti_viewer(nifti_data, selected_slice):
    if not selected_slice:
        # Display multiple slices as an animation
        plt.figure()

        for i in range(nifti_data.shape[-1]):
            slice_data = np.rot90(nifti_data[:, :, i], k=1)

            # Check if the slice contains non-zero values
            if slice_data.max() > 0:
                plt.imshow(slice_data, cmap='gray')
                plt.title(f'Slice {i}')
                plt.colorbar()
                plt.pause(0.1)  # Pause for a short time between frames
                plt.clf()  # Clear the current plot for the next frame

        # To keep the plot window open after the visualization
        plt.show()

    else:
        # Display the segmentation with transparency
        slice_data = np.rot90(nifti_data[:, :, selected_slice], k=1)  # Rotate 90 degrees counterclockwise 3 times (270 degrees clockwise)

        if slice_data.max() > 0:
            plt.imshow(slice_data, cmap='gray')            
            plt.title(f'Slice {i}')
            plt.colorbar()
            plt.show()
        
        else:
            print('The selected slice has no information.')
