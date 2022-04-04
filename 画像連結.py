# 画像結合  comb.py
import cv2
import glob
import numpy as np
from PIL import Image
from natsort import natsorted

# 所定のフォルダ内にある jpg ファイルを連続で読み込んでリスト化する
for s in [200]:
    files = glob.glob(f"{s}/*.jpg")

    # 空のリストを準備
    d = []

    # natsortedで自然順（ファイル番号の小さい順）に1個づつ読み込む
    for i in natsorted(files):
        img = Image.open(i)    # img は'JpegImageFile' object
        img = np.asarray(img)  # np.asarrayで img を ndarray に変換
        d.append(img)          # d にappend で img を追加

    # 画像の高さ方向と幅方向を結合
    img_x = np.vstack((np.hstack(d[0:4]),
                    np.hstack(d[4:8]),
                    np.hstack(d[8:12]),
                    np.hstack(d[12:16])
                    ))

    # 色をBGR から RGB に変更
    img_x = cv2.cvtColor(img_x, cv2.COLOR_BGR2RGB)
    cv2.imwrite(f'.result_{s}.jpg', img_x)

    cv2.waitKey(0)
    cv2.destroyAllWindows()