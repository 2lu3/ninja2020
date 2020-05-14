import os
import sys
import tkinter as tk

import cv2
import numpy as np

from my_module.tkinter import TkinterUserFace
from tkinter import messagebox

# 画面上で表示したい画像の大きさ
display_width, display_height = 720, 540
# 出力したい配列の大きさ
output_width, output_height = 36, 27

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

tkinter_user_face = TkinterUserFace(parameters)


paint_number = 0
floor_color_num = 6
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


# ロードボタンが押されたとき
# 出力された配列の情報から画像を復元し、編集できるようにする
def on_click_load_button(event):
    messagebox.showinfo("warning", "this function is comming soon")
    pass


# 出力ボタンが押されたとき
def on_click_output_button(event):
    print("output")
    output_array = np.zeros((4, output_height, output_width))
    images = [tkinter_user_face.get_image(image_type) for image_type in [
        "floor", "red", "cyan", "black"]]
    for image_index, image in enumerate(images):
        color_distances = []
        for color in range(floor_color_num):
            image = cv2.resize(cv2.cvtColor(
                image, cv2.COLOR_RGB2BGR), (output_width, output_height))
            color_distances.append(
                np.sum((image - registered_color[color]) ** 2, axis=2))
        for w in range(output_width):
            for h in range(output_height):
                minimum = min([color_distances[i][h, w]
                               for i in range(floor_color_num)])
                for i in range(floor_color_num):
                    if color_distances[i][h, w] == minimum:
                        output_array[image_index][h, w] = i
        np.savetxt("output_array" + str(image_index) +
                   ".txt", output_array[image_index], fmt="%d")


# [White, Yellow, Wall .... RED, CYAN, BLACK]が書かれているボタンが押されたとき
def on_click_paint_button(pushed_button_number):
    global paint_number
    paint_number = pushed_button_number

# 画像のどこかが押されたとき
# 色の範囲選択が始まったとき


def on_click_image(x, y):
    pass


# 画像のどこかを押し、マウスが移動している最中に呼ばれる関数
def on_motion_image(x, y):
    pass


# 画像のどこかを押し、その後マウスのクリックを外したとき
def on_release_image(event, start_x, start_y, end_x, end_y):
    if paint_number < floor_color_num:  # 床情報
        image_type = "floor"
    elif paint_number == floor_color_num:  # red
        image_type = "red"
    elif paint_number == floor_color_num + 1:  # cyan
        image_type = "cyan"
    elif paint_number == floor_color_num + 2:  # black
        image_type = "black"
    image = tkinter_user_face.get_image(image_type)

    cv2.rectangle(image, (start_x, start_y), (end_x, end_y),
                  registered_color[paint_number], thickness=-1)

    tkinter_user_face.replace_image(event, image, image_type)


def main():
    on_click_functions = {
        "on_click_paint_button": on_click_paint_button,
        "on_click_output_button": on_click_output_button,
        "on_click_load_button": on_click_load_button,
        "on_click_image": on_click_image,
        "on_release_image": on_release_image,
        "on_motion_image": on_motion_image,
    }

    tkinter_user_face.start("image 2 array", on_click_functions)


if __name__ == "__main__":
    main()
