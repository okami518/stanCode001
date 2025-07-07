"""
File: mirror_lake.py
Name:
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def main():
    """
    TODO:
    """
    # original_mt = SimpleImage('images/mt-rainier.jpg')
    # original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


def reflect(filename):
    """
    :param filename: images/mt-rainier.jpg
    :return: img
    """

    img = SimpleImage("images/mt-rainier.jpg")
    b_img = SimpleImage.blank(img.width, img.height*2)  # 製作底圖

    for x in range(img.width):  # 抓出座標
        for y in range(img.height):
            img_p = img.get_pixel(x, y)
            b_img_p = b_img.get_pixel(x, y)

            b_img_p.red = img_p.red  # 在上半部填入一樣的色彩
            b_img_p.green = img_p.green
            b_img_p.blue = img_p.blue

            b_img_p2 = b_img.get_pixel(x, b_img.height-1-y)  # 定義下半部座標的填色邏輯

            b_img_p2.red = img_p.red
            b_img_p2.green = img_p.green
            b_img_p2.blue = img_p.blue

    return b_img


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
