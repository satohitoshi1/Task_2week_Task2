from PIL import Image, ImageDraw, ImageFont

img = Image.open("konjikido_01.jpg")
resize_kjkd_img = img.resize((1400, 730))  # ただのリサイズ
# print(resize_kjkd_img)
text = "平泉 最高"  # 画像に追加する文字列を指定
font_color = (0, 255, 255)  # 水色RGB
font_path = "C:\Windows\Fonts\MEIRYO.TTC"  # windowsのフォントを呼び出す
font = ImageFont.truetype(font_path, 250)  # フォントを指定、サイズ
(font_w, font_h), (offset_x, offset_y) = font.font.getsize(text)
img_w, img_h = img.size  # フォントの縦横幅を取得
pos = ((img_w - font_w) / 2, (img_h - font_h) / 2)  # 中央に調整
draw = ImageDraw.Draw(img)
draw.text(pos, text, font=font, fill=font_color)  # 描写

img.show()

# アスペクト比を維持したままリサイズ いったんボツ
# def scale_to_width(img, width):  
#     height = round(img.height * img.width / img.width)
#     return img.resize((width, height))
# resize_kjkd = scale_to_width(img, 1400)
# print(f"{img.size} -> {resize_kjkd.size}")
# resize_kjkd.show()
