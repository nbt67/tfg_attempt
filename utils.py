import zipfile
import os
import re

def extract_zip(zip_file, extract_to):
    try:
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
        print(f'Successfully extracted {zip_file} to {extract_to}')

    except Exception as e:
        print(f'Error extracting {zip_file}: {str(e)}')

def is_zip_file(file_path):
    # Get the file extension (excluding the dot)
    file_extension = os.path.splitext(file_path)[1][1:]

    # Check if the file extension is "zip"
    return file_extension.lower() == 'zip'

def is_nifti_file(file_path):
    # Define a regular expression pattern to match "nii" or "nii.gz" file extensions
    pattern = r'\.nii(\.gz)?'

    # Check if the file extension matches the pattern (case-insensitive)
    return bool(re.search(pattern, file_path, re.I))