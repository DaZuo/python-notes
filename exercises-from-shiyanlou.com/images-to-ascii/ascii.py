"""Python 图片转字符画"""
import argparse
from PIL import Image

def get_args():
    """读取命令行"""
    parser = argparse.ArgumentParser()

    parser.add_argument("file")
    parser.add_argument("-o", "--output")
    parser.add_argument("--width", type=int, default=80)
    parser.add_argument("--height", type=int, default=80)

    return parser.parse_args()

def get_char(rgb_r, rgb_g, rgb_b, rgb_a=256):
    """根据色值获取一个字符"""
    if rgb_a == 0:
        return " "

    ascii_char = list(r"$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
    length = len(ascii_char)
    gray = int(0.2126 * rgb_r + 0.7152 * rgb_g + 0.0722 * rgb_b)

    unit = (256.0 + 1) / length
    return ascii_char[int(gray/unit)]

def main():
    """main执行"""
    args = get_args()
    image = args.file
    width = args.width
    height = args.height
    output = args.output

    image = Image.open(image)
    image = image.resize((width, height), Image.NEAREST)

    txt = ""

    for i in range(height):
        for j in range(width):
            txt += get_char(*image.getpixel((j, i)))
        txt += "\n"

    print(txt)

    if output:
        with open(output, "w") as file:
            file.write(txt)
    else:
        with open("output.txt", "w") as file:
            file.write(txt)

if __name__ == "__main__":
    main()
