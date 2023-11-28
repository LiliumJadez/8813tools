# 8813tools

## Point Cloud Processor

- [x] pcdmeanvar.py

### Description
This project includes a Python script designed for processing point cloud data (in PCD format). The script reads point cloud files from a specified directory, projects them to range-view images, and calculates the mean and variance across these images. The results are then written to a specified output text file. This tool is particularly useful for analyzing and processing large sets of point cloud data.

### Installation

#### Prerequisites
- Python 3.x
- Open3D
- NumPy

To install the required libraries, run:
```bash
pip install numpy open3d
```
### Usage
To use the script, run it from the command line with the following arguments:

- The path to the directory containing the PCD files.
- The path where the output text file will be saved.


#### Example:
```bash
python point_cloud_processor.py /path/to/pcd/folder /path/to/output/file.txt
```
Replace point_cloud_processor.py with the name of your script, /path/to/pcd/folder with the path to your point cloud file directory, and /path/to/output/file.txt with the desired path for the output file.
