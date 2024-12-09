import urllib.request
from io import BytesIO
from PIL import Image
import ddddocr
from PIL import Image
import pytesseract
import io
def load_image_as_bytes(url):
    # 使用 urllib 请求获取图片内容
    with urllib.request.urlopen(url) as response:
        # 读取二进制数据
        image_bytes = response.read()

        # 打印响应的内容类型（调试用）
        print(f"Content-Type: {response.getheader('Content-Type')}")



        return image_bytes


url = "https://images-na.ssl-images-amazon.com/captcha/ddwwidnf/Captcha_gvsnwfeghr.jpg"

image_bytes = load_image_as_bytes(url)
print(type(image_bytes))

image = Image.open(io.BytesIO(image_bytes))

code = pytesseract.image_to_string(image, config='--psm 6')
# ocr = ddddocr.DdddOcr()
#
# # ddddocr是一个开源库 识别验证码
# code = ocr.classification(image_bytes)
print(code)