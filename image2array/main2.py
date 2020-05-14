import os
import sys
import tkinter as tk

import cv2
import numpy as np

from my_module.tkinter import TkinterUserFace

# 画面上で表示したい画像の大きさ
display_width, display_height = 720, 540
# 出力したい配列の大きさ
output_width, output_height = 36, 27

registered_color = [
    [255, 255, 255],  # white
    [255, 255, 0],  # yellow
    [221, 186, 151],  # wall
    [202, 202, 202],  # swampland
    [232, 125, 49],  # deposit
    [0, 176, 240],  # superarea
    [237, 28, 36],  # red
    [63, 72, 204],  # cyan
    [0, 0, 0],  # black
]


def apply_image_changes_to_map(image, registered_color):
    pass


# ロードボタンが押されたとき
# 出力された配列の情報から画像を復元し、編集できるようにする
def on_click_load_button(event):
    pass


# 出力ボタンが押されたとき
def on_click_output_button(event):
    pass


# [White, Yellow, Wall .... RED, CYAN, BLACK]が書かれているボタンが押されたとき
def on_click_paint_button(event):
    pass


# 画像のどこかが押されたとき
# 色の範囲選択が始まったとき
def on_click_image(x, y):
    pass

# 画像のどこかを押し、マウスが移動している最中に呼ばれる関数


def on_motion_image(x, y):
    pass

# 画像のどこかを押し、その後マウスのクリックを外したとき


def on_release_image(start_x, start_y, end_x, end_y):
    pass


def main():
    paint_button_labels = [
        "White",
        "Yellow",
        "Wall",
        "Swampland",
        "DepositArea",
        "SuperArea",
        "Red",
        "Cyan",
        "Black",
    ]

    parameters = {
        "display_width": display_width,
        "display_height": display_height,
        "paint_button_labels": paint_button_labels,
    }

    on_click_functions = {
        "on_click_paint_button": on_click_paint_button,
        "on_click_output_button": on_click_output_button,
        "on_click_load_button": on_click_load_button,
        "on_click_image": on_click_image,
        "on_release_image": on_release_image,
        "on_motion_image": on_motion_image,
    }

    tkinter_user_face = TkinterUserFace(parameters)

    tkinter_user_face.start("image 2 array", on_click_functions)


if __name__ == "__main__":
    main()
