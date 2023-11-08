from totalsegmentator.python_api import totalsegmentator


def call_total_segmentator(input_path, output_path, fast_mode=False, task_='total'):

    totalsegmentator(input_path, output_path, fast=fast_mode, task=task_)

    return 1

input_path = 'D:/Documentos/Uni/TFG/tfg_attempt/input/file1.zip'
output_path = 'D:/Documentos/Uni/TFG/tfg_attempt/totalSegmentator_output'

call_total_segmentator(input_path, output_path, fast_mode=True, task_='total')