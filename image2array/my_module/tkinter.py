import tkinter as tk

from my_module.image import read_image


class TkinterUserFace:
    def __init__(self, parameters):
        # 画像の横幅
        self.image_width = parameters.pop("image_width")
        # 画像の縦幅
        self.image_height = parameters.pop("image_height")
        # ボタン同士の隙間
        if "ui_margin" in parameters:
            self.ui_margin = parameters.pop("ui_margin")
        else:
            self.ui_margin = 20
        # ボタンの横幅
        if "paint_button_width" in parameters:
            self.paint_button_width = parameters.pop("button_margin")
        else:
            self.paint_button_width = 120
        # 選択部分の種類(Yelow, Swamplandなど)を決定
        self.paint_button_labels = parameters.pop("paint_button_labels")
        # [Red, Cyan, Black, 床情報]などの、編集するモード
        self.edit_mode_button_labels = parameters.pop("edit_mode_button_labels")

        # 四角形の選択範囲のクリック座標
        self.start_x = self.start_y = -1
        # 四角形の選択範囲のクリックを外した座標
        self.end_x = self.end_y = -1

    def set_buttons(self, **parameters):
        def set_list_button(button_texts, on_click_function, place_position):
            # ボタンのクラスを作成
            list_button = tk.Listbox(self.root, height=len(button_texts))

            for text in button_texts:
                # ボタンの名前を末尾(tk.END)に追加
                list_button.insert(tk.END, text)

            # 初期状態で選択されているボタンは0番目のもの
            list_button.select_set(0)
            # ボタンが押されたときに呼ばれる関数を設定
            list_button.bind("<ButtonRelease-1>", on_click_function)
            # ボタンを画面上のどこに配置するか
            list_button.place(x=place_position[0], y=place_position[1])

        def set_single_button(button_text, on_click_function, place_position):
            button = tk.Button(self.root, text=button_text)
            button.bind("<Button-1>", on_click_function)
            button.place(x=place_position[0], y=place_position[1])

        on_click_paint_button = parameters.pop("paint")
        on_click_edit_mode_button = parameters.pop("edit_mode")
        on_click_output_button = parameters.pop("output")
        on_click_load_button = parameters.pop("load")

        # どの種類の物体をマップ上に追加するかを選択するボタンの設定
        x = self.image_width + self.ui_margin * 2
        y = self.ui_margin * 1
        set_list_button(self.paint_button_labels, on_click_paint_button, (x, y))

        # 表示・設定のモードを変更するボタンを設定
        # 例:Red,Cyan,Black Objectの設定
        x = self.image_width + self.ui_margin * 2
        y = self.ui_margin * (len(self.paint_button_labels) + 2)
        set_list_button(self.edit_mode_button_labels, on_click_edit_mode_button, (x, y))

        # 出力ボタンの設定
        x = self.image_width + self.ui_margin * 2
        y = self.ui_margin * (len(self.paint_button_labels) + 8)
        set_single_button("出力", on_click_output_button, (x, y))

        # ロードボタンの設定
        x = self.image_width + self.ui_margin * 2
        y = self.ui_margin * (len(self.paint_button_labels) + 10)
        set_single_button("ロード", on_click_load_button, (x, y))

    # 画像の周りに黒い線を表示する
    def add_line_around_image(self):
        line_margin = 2
        self.canvas.create_rectangle(
            self.ui_margin - line_margin / 2,
            self.ui_margin - line_margin / 2,
            self.image_width + self.ui_margin + line_margin / 2,
            self.image_height + self.ui_margin + line_margin / 2,
            outline="black",
            width=line_margin,
        )

    # 画像の任意の点をクリックされたときに呼ばれる関数を設定する
    def set_image_on_click_listener(self, on_click, on_release, on_motion):
        # マウスでクリックをしたときに呼ばれる関数
        def on_click_image(event):
            # クリックされた座標を記録
            self.start_x, self.start_y = event.x, event.y
            # main.py側の関数を呼ぶ
            on_click(self.start_x, self.start_y)

        # マウスのクリック中から、手を離したときに呼ばれる関数
        def on_release_image(event):
            # rectangleというタグのついた画面上に描写された物体を削除する
            # 意訳：範囲選択中に表示される四角形を削除する
            self.canvas.delete("selected_rectangle")
            # アンクリックされたときの座標を記録
            self.end_x, self.end_y = event.x, event.y
            # main.py側の関数を呼ぶ
            on_release(self.start_x, self.start_y, self.end_x, self.end_y)

        # マウスでクリックしたあと、手を話す前のときに、現在のマウスの座標が引数として呼び出される関数
        def on_motion_image(event):
            # rectangle というタグのついた画面上に描写された物体を削除する
            # 意訳：範囲選択中に表示される四角形を削除する
            self.canvas.delete("selected_rectangle")
            # 現在のカーソルの場所を記録
            moving_x, moving_y = event.x, event.y
            # 選択中の範囲をわかりやすくするため、黒色の長方形で囲む
            self.canvas.create_rectangle(
                self.start_x,
                self.start_y,
                moving_x,
                moving_y,
                width=1,
                outline=1,
                tag="selected_rectangle",
            )
            # main.py側の関数を呼ぶ
            on_motion(moving_x, moving_y)

        # クリックされたときに呼ばれる関数を設定
        self.canvas.bind("<Button-1>", on_click_image)
        # クリックし、手を離したときに呼ばれる関数を設定
        self.canvas.bind("<ButtonRelease-1>", on_release_image)
        # クリックしている最中(10msなどの短い時間ごとに)に呼ばれる関数を設定
        self.canvas.bind("<B1-Motion>", on_motion_image)

    # 画像を表示
    def set_image(self):
        self.image = read_image(self.image_width, self.image_height)
        self.canvas.create_image(
            self.ui_margin, self.ui_margin, image=self.image, anchor=tk.NW
        )

    def tkinter_setup(self, title, on_click_functions):
        # ソフト作成
        self.root = tk.Tk()
        # ソフト名
        self.root.title("image 2 array")

        # 画面の大きさの設定
        self.canvas = tk.Canvas(
            self.root,
            width=self.image_width + self.ui_margin * 2 + self.paint_button_width,
            height=self.image_height + self.ui_margin * 2,
            bg="white",
        )
        # コンパイルする
        self.canvas.pack()

        # 画像の設置
        self.set_image()

        # 画像の周りに黒い線を描画する(画像の端が白色の場合、境界線がわからない)
        self.add_line_around_image()

        # ボタンを押されたときに実行する関数を設定
        self.set_buttons(
            paint=on_click_functions["on_click_paint_button"],
            edit_mode=on_click_functions["on_click_edit_mode_button"],
            output=on_click_functions["on_click_output_button"],
            load=on_click_functions["on_click_load_button"],
        )

        # 画像上をクリックされたときに実行する関数を設定
        self.set_image_on_click_listener(
            on_click=on_click_functions["on_click_image"],
            on_release=on_click_functions["on_release_image"],
            on_motion=on_click_functions["on_motion_image"],
        )

        # arduinoでいうloop関数を実行する
        self.root.mainloop()

