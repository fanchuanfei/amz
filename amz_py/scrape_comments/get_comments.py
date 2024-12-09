from playwright.sync_api import sync_playwright
import ddddocr
# 启动 playwright driver进程
p = sync_playwright().start()

# 启动浏览器
browser = p.chromium.launch(headless=False,executable_path=r'C:\Program Files\Google\Chrome\Application\chrome.exe')

# 创建page页面
page = browser.new_page()

# 设置默认超时时间
page.set_default_timeout(500000)

#爬取的网址 https://www.amazon.com/Microwave-Replacement-KW3AT-16-1x-KW3A-16/dp/B09DKG2MJ9
category_url = "https://www.amazon.com/Microwave-Replacement-KW3AT-16-1x-KW3A-16/dp/"
asin_list = ["B09DKG2MJ9"]
full_path = category_url+asin_list.pop()


# 进入网站
page.goto(full_path)

# page.wait_for_timeout(500000)
# 判断是否遇到了图片验证码
if page.title()=="Amazon.com":

    # 获取图片地址
    imagurl = page.locator(".a-row a-text-center img").get_attribute("src")

    print(imagurl)
    # 打开图片 二进制形式
    f = open(imagurl,'rb')

    img = f.read()

    ocr = ddddocr.DdddOcr()

    # ddddocr是一个开源库 识别验证码
    code = ocr.classification(img)

    # 输入code进入目标页面
    page.locator("#captchacharacters").fill(code)

    # 提交
    page.locator(".a-button-text").click()



# 定位与操作
page.locator(".a-link-emphasis a-text-bold").click()

page.locator(".cr-filter-secondary-view-link").click()

page.locator(".star-option-critical").click()

page.locator(".a-button-input").click()

content = page.locator("#cm_cr-review_list").all()

print(content)
# 关闭浏览器哦


browser.stop_tracing()

