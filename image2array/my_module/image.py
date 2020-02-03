import cv2

from PIL import Image, ImageTk


def read_image(image_width, image_height, path="Background.bmp"):
    # 画像の読み込み(BGRの順番)
    image_bgr = cv2.imread(path)

    # 画像の大きさの変更
    image_bgr = cv2.resize(image_bgr, (image_width, image_height))

    # BGRからRGBに変更 参考: https://note.nkmk.me/python-opencv-bgr-rgb-cvtcolor/
    image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)

    # pil形式に変換
    image_pil = Image.fromarray(image_rgb)

    # tkinter形式に変換
    image_tk = ImageTk.PhotoImage(image_pil)

    return image_tk
