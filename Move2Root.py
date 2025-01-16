import os
import shutil

def rename_and_move_files_recursively(current_dir, root_dir):
    # 获取当前目录中的所有文件和子目录
    entries = os.listdir(current_dir)
    
    for entry in entries:
        entry_path = os.path.join(current_dir, entry)
        
        # 如果是一个目录，则递归调用
        if os.path.isdir(entry_path):
            rename_and_move_files_recursively(entry_path, root_dir)
        # 如果是一个文件，则重命名并移动到根目录
        elif os.path.isfile(entry_path):
            # 获取文件的相对路径（相对于根目录）
            rel_path = os.path.relpath(current_dir, root_dir)
            # 构建新的文件名，格式为：目录路径（用下划线分隔）+ 文件名
            new_filename = '_'.join(os.path.split(rel_path)[0].split(os.sep)) + '_' + entry
            new_file_path = os.path.join(root_dir, new_filename)
            
            # 确保新文件名不会冲突（这里简单地在文件名后加数字直到不冲突为止）
            counter = 1
            while os.path.exists(new_file_path):
                base, ext = os.path.splitext(new_filename)
                new_filename = f"{base}_{counter}{ext}"
                new_file_path = os.path.join(root_dir, new_filename)
                counter += 1
            
            # 移动并重命名文件
            shutil.move(entry_path, new_file_path)
            print(f"Moved and renamed: {entry_path} -> {new_file_path}")

if __name__ == "__main__":
    root_directory = "/root/path"  # 替换为你的根目录路径
    rename_and_move_files_recursively(root_directory, root_directory)