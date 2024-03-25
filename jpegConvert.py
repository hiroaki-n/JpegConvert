import os
from tkinter import filedialog
from tkinter import Tk
from PIL import Image
import pillow_avif
from PIL import Image


#pip install pillow-avif-plugin
#でavifファイルをフォローできるようにする

# フォローしてるファイルの拡張子
IMAGE_EXTENSIONS = ['.png', '.bmp', '.gif', '.avif', '.tiff', '.tif']

# 指定されたフォルダ内のJPEG以外の画像ファイルをJPEGに変換し、
# 変換後に元のファイルを削除する関数。Pillowを使用。
def process_folder(folder_path):
    print(f"フォルダ処理開始: {folder_path}")
    for filename in os.listdir(folder_path):
        file_ext = os.path.splitext(filename)[1].lower()
        if file_ext in IMAGE_EXTENSIONS or file_ext != '.jpg':
            input_file = os.path.join(folder_path, filename)
            output_file = os.path.join(folder_path, os.path.splitext(filename)[0] + ".jpg")
            
            if input_file != output_file and convert_to_jpeg(input_file, output_file):  # 変換成功時にのみ削除
                delete_file(input_file)
    print("フォルダ処理完了")

# 画像ファイルをJPEGに変換し、変換後に元のファイルを削除
def convert_to_jpeg(input_file, output_file):
    try:
        print(f"変換を開始します: {input_file}")
        with Image.open(input_file) as img:
            img.convert('RGB').save(output_file, 'JPEG')
        print(f"変換完了: {input_file} -> {output_file}")
        return True
    except Exception as e:
        print(f"変換エラー: {input_file}, エラー: {e}")
        return False

# 変換後のファイルを削除
def delete_file(file_path):
    try:
        os.remove(file_path)
        print(f"削除完了: {file_path}")
    except Exception as e:
        print(f"削除エラー: {file_path}, エラー: {e}")



# tkinterのルートウィンドウを作成して非表示にする
if __name__ == "__main__":    
    root = Tk()
    root.withdraw()
    
    # ダイアログを表示
    folder_path = filedialog.askdirectory(title="フォルダを選択してください")
    
    if folder_path:
        print(f"選択されたフォルダ: {folder_path}")
        process_folder(folder_path)
    else:
        print("フォルダが選択されませんでした。")
