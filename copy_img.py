'''
Author: SimonHanYANG SimonCK666@mail.163.com
Date: 2024-05-21 14:26:12
LastEditors: SimonHanYANG SimonCK666@mail.163.com
LastEditTime: 2024-05-21 14:26:23
FilePath: \PseudoDataset\move.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import os
import shutil
from pathlib import Path

def copy_images_to_root(root_path):
    # 获取所有的子文件夹
    subfolders = [f.path for f in os.scandir(root_path) if f.is_dir()]
    
    # 支持的图片格式
    image_extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')
    
    for subfolder in subfolders:
        for root, dirs, files in os.walk(subfolder):
            for file in files:
                if file.lower().endswith(image_extensions):
                    source_file = os.path.join(root, file)
                    destination_file = os.path.join(root_path, file)
                    
                    # 确保不覆盖已存在的文件
                    counter = 1
                    while os.path.exists(destination_file):
                        file_name, file_extension = os.path.splitext(file)
                        destination_file = os.path.join(root_path, f"{file_name}_{counter}{file_extension}")
                        counter += 1
                    
                    shutil.copy2(source_file, destination_file)
                    print(f"Copied {source_file} to {destination_file}")

if __name__ == "__main__":
    root_path = input("请输入根目录路径: ")
    copy_images_to_root(root_path)
