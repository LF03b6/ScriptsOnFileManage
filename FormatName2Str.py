import os

def rename_files_with_prefix(directory, prefix):
    # 获取目录中的所有文件
    files = os.listdir(directory)
    
    # 过滤出只有文件（不包括子目录）
    files = [f for f in files if os.path.isfile(os.path.join(directory, f))]
    
    # 对文件进行排序（如果需要的话，可以根据文件名、修改时间等排序）
    files.sort()
    
    # 按照顺序重命名文件
    for index, filename in enumerate(files, start=1):
        # 获取文件的完整路径
        old_file_path = os.path.join(directory, filename)
        
        # 构建新的文件名，格式为：前缀 + 序号（三位数补零）
        new_filename = f"{prefix}{index:03d}"
        # 如果原文件名有扩展名，则保留扩展名
        if '.' in filename:
            base, ext = os.path.splitext(filename)
            new_filename = f"{new_filename}{ext}"
        
        # 获取新的文件完整路径
        new_file_path = os.path.join(directory, new_filename)
        
        # 重命名文件
        os.rename(old_file_path, new_file_path)
        print(f"Renamed: {old_file_path} -> {new_file_path}")

if __name__ == "__main__":
    directory_path = "/path/[yaer]"  # 替换为你的目录路径
    prefix = "[year]-"  # 指定的前缀
    rename_files_with_prefix(directory_path, prefix)