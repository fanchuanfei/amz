import re
from playwright.sync_api import Playwright, sync_playwright, expect
import ddddocr

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.set_extra_http_headers({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9"
    })


    page.goto("https://www.amazon.com/")


    #三种情况 1.被识别为机器人  2.没有被识别为机器人直接登录 3.没有被识别为机器人并且不需要登录
    if page.title() == "Amazon.com":

        print("1.被识别为机器人")
        # 获取图片地址
        loc = page.locator(".a-box-inner")

        print(loc)
        imagurl = loc.locator("img").get_attribute("src")


        print(imagurl)
        # 打开图片 二进制形式
        f = open(imagurl, 'rb')

        img = f.read()

        ocr = ddddocr.DdddOcr()

        # ddddocr是一个开源库 识别验证码
        code = ocr.classification(img)

        # 输入code进入目标页面
        page.locator("#captchacharacters").fill(code)

        # 提交
        page.locator(".a-button-text").click()

    page.get_by_role("link", name="Sign in", exact=True).click()
    page.get_by_label("Email or mobile phone number").click()
    page.get_by_label("Email or mobile phone number").fill("liuwannianliu@gmail.com")
    page.get_by_label("Continue").click()
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill("liu2391042097")
    page.get_by_label("Sign in").click()
    page.goto("https://www.amazon.com/Microwave-Replacement-KW3AT-16-1x-KW3A-16/dp/B09DKG2MJ9?th=1")
    page.locator("#cr-pagination-footer-0").get_by_role("link", name="See more reviews").click()
    page.locator("#a-autoid-5-announce").click()
    page.get_by_label("Critical reviews").get_by_text("Critical reviews").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)