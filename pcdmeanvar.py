import os
import argparse
import numpy as np
import open3d as o3d
from tqdm import tqdm

def process_point_cloud(file_path):
    pcd = o3d.io.read_point_cloud(file_path)
    range_view_image = project_to_range_view(pcd)
    return range_view_image

def project_to_range_view(pcd):
    points = np.asarray(pcd.points)
    range_view_image = np.sqrt(np.sum(points**2, axis=1)).reshape(-1, 1)

    desired_length = 20000  # 可调整的目标长度
    current_length = range_view_image.shape[0]
    if current_length < desired_length:
        range_view_image = np.pad(range_view_image, ((0, desired_length - current_length), (0, 0)), mode='constant')
    elif current_length > desired_length:
        range_view_image = range_view_image[:desired_length]

    return range_view_image

def write_to_file(mean, variance, file_path):
    with open(file_path, 'w') as f:
        f.write("Mean:\n")
        f.write(str(mean))
        f.write("\n\nVariance:\n")
        f.write(str(variance))

def main(folder_path, output_file_path):
    range_view_images = []

    # 使用 tqdm 显示进度
    for file_name in tqdm(os.listdir(folder_path), desc="Processing files"):
        if file_name.endswith('.pcd'):
            file_path = os.path.join(folder_path, file_name)
            range_view_image = process_point_cloud(file_path)
            range_view_images.append(range_view_image)

    range_view_images = np.array(range_view_images)
    mean = np.mean(range_view_images, axis=0)
    variance = np.var(range_view_images, axis=0)

    write_to_file(mean, variance, output_file_path)
    print(f"Results written to {output_file_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process point cloud files and calculate mean and variance.")
    parser.add_argument("folder_path", type=str, help="Path to the folder containing PCD files")
    parser.add_argument("output_file_path", type=str, help="Path to the output text file")

    args = parser.parse_args()
    main(args.folder_path, args.output_file_path)
