import os
import subprocess
import csv
import re

# Directory containing the .bin files
bin_dir = "/mnt/PublicDatasets/semantic-kitti/dataset/sequences/20/velodyne"
# Output CSV file
output_csv = "output.csv"

# Command template
cmd_template = "python infer.py --model_file /home/GPU/wxu/local_storage/point-cloud-dreamteam/paddlerecog_voxelrcnn_output/voxel_rcnn.pdmodel --params_file /home/GPU/wxu/local_storage/point-cloud-dreamteam/paddlerecog_voxelrcnn_output/voxel_rcnn.pdiparams --lidar_file {} --num_point_dim 4 --point_cloud_range 0 -40 -3 70.4 40 1"

# Regular expression to match the desired output format
pattern = r"Score: ([0-9.]+) Label: (\d+) Box\(x_c, y_c, z_c, w, l, h, -rot\): ([\d\s.-]+)"

# Open the CSV file for writing
with open(output_csv, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Filename', 'Score', 'Label', 'Box Coordinates'])

    # Process each .bin file in the directory
    for filename in os.listdir(bin_dir):
        if filename.endswith(".bin"):
            # Construct the full file path
            file_path = os.path.join(bin_dir, filename)
            # Construct the command
            cmd = cmd_template.format(file_path)
            # Execute the command
            output = subprocess.check_output(cmd, shell=True, text=True)

            # Extract the relevant lines from the output
            for match in re.finditer(pattern, output):
                score, label, box_coords = match.groups()
                writer.writerow([filename, score, label, box_coords])
