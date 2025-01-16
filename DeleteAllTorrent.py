import os
import glob

def delete_torrent_files(directory):
    # 使用glob模块查找所有.torrent文件，包括子目录中的
    torrent_files = glob.glob(os.path.join(directory, '**', '*.torrent'), recursive=True)
    
    for torrent_file in torrent_files:
        try:
            os.remove(torrent_file)
            print(f"Deleted: {torrent_file}")
        except OSError as e:
            print(f"Error deleting {torrent_file}: {e.strerror}")

if __name__ == "__main__":
    directory_path = "/path"  # 替换为你的目录路径
    delete_torrent_files(directory_path)