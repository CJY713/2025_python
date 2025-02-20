# 參考網址: https://github.com/sml2h3/ddddocr

import ddddocr

ocr = ddddocr.DdddOcr()

def get_captcha_code():
    image = open("captcha.png", "rb").read()
    result = ocr.classification(image)
    print("Get captcha code: ", result)
    return result

if __name__ == '__main__':
    get_captcha_code()
