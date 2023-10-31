import os
import pydicom
import matplotlib.pyplot as plt
import numpy as np

def dicom_viewer(volume, selected_slice=None):

    if not selected_slice:
        # Display multiple slices as an animation
        plt.figure()
        print(len(volume))
        for i in range(len(volume)):
            slice_data = volume[i]

            # Check if the slice contains non-zero values
            plt.imshow(slice_data, cmap='gray')
            plt.title(f'Slice {i}')
            plt.colorbar()
            plt.pause(0.03)  # Pause for a short time between frames
            plt.clf()  # Clear the current plot for the next frame

        # To keep the plot window open after the visualization
        plt.show()

    else:
        plt.imshow(volume[selected_slice], cmap=plt.cm.bone)
        plt.title(f"DICOM Slice {selected_slice}")
        plt.colorbar()

        plt.show()
