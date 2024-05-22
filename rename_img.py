'''
Author: SimonHanYANG SimonCK666@mail.163.com
Date: 2024-05-21 14:31:26
LastEditors: SimonHanYANG SimonCK666@mail.163.com
LastEditTime: 2024-05-21 14:31:34
FilePath: \PseudoDataset\rename_img.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import os

def rename_images_in_folder(folder_path):
    # 支持的图片格式
    image_extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')
    
    # 获取文件夹中的所有图片文件
    image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(image_extensions)]
    
    # 按照文件名排序
    image_files.sort()
    
    for index, file_name in enumerate(image_files):
        # 获取文件扩展名
        file_extension = os.path.splitext(file_name)[1]
        
        # 构建新的文件名
        new_file_name = f"{index}{file_extension}"
        
        # 构建完整的文件路径
        old_file_path = os.path.join(folder_path, file_name)
        new_file_path = os.path.join(folder_path, new_file_name)
        
        # 重命名文件
        os.rename(old_file_path, new_file_path)
        print(f"Renamed {old_file_path} to {new_file_path}")

if __name__ == "__main__":
    folder_path = input("请输入文件夹路径: ")
    rename_images_in_folder(folder_path)
