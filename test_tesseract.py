# tesseract的使用
# 在python代码中操作tesseract需要安装一个库pytesseract
# 读取图片，需要安装PIL库

import pytesseract
from PIL import Image
from urllib import request
import time

# 1、将图片中的英文识别出来
# pytesseract.pytesseract.tesseract_cmd = r'D:\tesseract\Tesseract-OCR\tesseract.exe'  # tesseract.exe的路径
#
# image = Image.open('a.png')  # 打开图片
# text = pytesseract.image_to_string(image)
# print(text)


# 2、识别中文
# pytesseract.pytesseract.tesseract_cmd = r'D:\tesseract\Tesseract-OCR\tesseract.exe'
# image = Image.open('c.png')
# text = pytesseract.image_to_string(image, lang='chi_sim')
# print(text)


# 3、识别图形验证码
def main():
    pytesseract.pytesseract.tesseract_cmd = r'D:\tesseract\Tesseract-OCR\tesseract.exe'
    while True:
        url = 'https://login.zhipin.com/captcha/?randomKey=NmQGUW9COxz8JASN7xItFu4fRP8O7dbn&_r=1535768563732'  # 验证码
        request.urlretrieve(url, 'captcha.png')  # 保存图片
        image = Image.open('captcha.png')  # 打开图片
        text = pytesseract.image_to_string(image)
        print(text)
        time.sleep(2)


if __name__ == '__main__':
    main()


