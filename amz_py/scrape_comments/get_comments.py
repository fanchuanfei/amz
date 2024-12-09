from playwright.sync_api import sync_playwright
import ddddocr
# 启动 playwright driver进程
p = sync_playwright().start()

# 启动浏览器
browser = p.chromium.launch(headless=False,executable_path=r'C:\Program Files\Google\Chrome\Application\chrome.exe')

context = browser.new_context()
context.tracing.start(snapshots=True,sources=True,screenshots=True)
context.new_page()
# 创建page页面
page = browser.new_page()

page.set_default_timeout(500000)
category_url = "https://www.amazon.com/Microwave-Replacement-KW3AT-16-1x-KW3A-16/dp/"
asin_list = ["B09DKG2MJ9"]
full_path = category_url+asin_list.pop()

# 进入网站
page.goto(full_path)
print(page.title())
# 如果遇到了图片验证码
if page.title()=="Amazon.com":
    # 获取图片地址

    # 打开图片 二进制形式
    f = open('url','rb')

    img = f.read()

    ocr = ddddocr.DdddOcr()

    # ddddocr是一个开源库 识别验证码
    code = ocr.classification(img)

    # 输入code进入目标页面


# 定位与操作
page.locator(".a-link-emphasis a-text-bold").click()

page.locator(".cr-filter-secondary-view-link").click()

page.locator(".star-option-critical").click()

page.locator(".a-button-input").click()

content = page.locator("#cm_cr-review_list").all()

print(content)
# 关闭浏览器哦

# 保存跟踪文件地址，就是录制代码的点击流程
context.tracing.stop(path="trace.zip")

browser.stop_tracing()

