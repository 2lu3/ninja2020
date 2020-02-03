import os
import sys
import tkinter as tk

import cv2
import numpy as np

from my_module.tkinter import TkinterUserFace

# 処理したい最小単位(最終的に36x27にする場合でも、360x270の解像度で操作したいとき)
image_width, image_height = 360, 270
# 出力したい配列の大きさ(image_widthの約数でなければならない)
output_width, output_height = 36, 27


button_labels = [
    "White",
    "Yellow",
    "Wall",
    "Swampland",
    "Deposit",
    "SuperArea",
    "Red",
    "Cyan",
    "Black",
]
button_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
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


def on_click_load_button():
    pass


def on_click_output_button():
    pass


def on_click_paint_button():
    pass


def on_click_edit_mode_button():
    pass


def on_click_image():
    pass


def on_release_image():
    pass


def on_motion_image():
    pass


def main():
    paint_button_labels = [
        "White",
        "Yellow",
        "Wall",
        "Swampland",
        "Deposit",
        "SuperArea",
        "Red",
        "Cyan",
        "Black",
    ]
    edit_mode_button_labels = ["床情報", "Red", "Cyan", "Black"]

    prms = {
        "image_width": 360,
        "image_height": 270,
        "paint_button_labels": paint_button_labels,
        "edit_mode_button_labels": edit_mode_button_labels,
    }
    tkinter_user_face = TkinterUserFace(prms)

    tkinter_user_face.tkinter_setup("image 2 array",)


if __name__ == "__main__":
    main()
