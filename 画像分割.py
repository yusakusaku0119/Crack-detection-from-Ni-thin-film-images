from pathlib import Path
from PIL import Image
import cv2
import numpy as np

def get_paths(input_dir, exts=None):
    paths = sorted([x for x in input_dir.iterdir()])
    if exts:
        paths = list(filter(lambda x: x.suffix in exts, paths))

    return paths


# ディレクトリ内の指定した拡張子のファイルをすべて取得する。
input_dir = Path(r"train/masks")

# 出力先のディレクトリを作成する。
output_dir = Path(r"m")
output_dir.mkdir(exist_ok=True)

for path in get_paths(input_dir, exts=[".jpg", ".jpeg", ".png",".bmp"]):
    # 画像を読み込む。
    img = cv2.imread(str(path))
    #print(img)
    size = (256, 256)  # 分割後の大きさ
    rows = int(np.ceil(img.shape[0] / size[0]))  # 行数
    cols = int(np.ceil(img.shape[1] / size[1]))  # 列数

    chunks = []
    for row_img in np.array_split(img, rows, axis=0):
        for chunk in np.array_split(row_img, cols, axis=1):
            chunks.append(chunk)
            #print(type(chunk))
    print(len(chunks))

    # 保存する。

    for i, chunk in enumerate(chunks):
        #save_path = output_dir / f"chunk_{i:02d}.png"
        #save_path = output_dir / f"{file_name}chunk_{i:02d}.png"
        #cv2.imwrite(str(save_path), chunk)

        # 結果を保存する。
        save_path = output_dir.name + "/" + str(i) + "_" + path.name
        cv2.imwrite(str(save_path), chunk)