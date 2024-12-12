import re
import requests
from playwright.sync_api import Playwright, sync_playwright, expect
import ddddocr


def get_code(url):
    response = requests.get(url)

    ocr = ddddocr.DdddOcr()

    code = ocr.classification(response.content)

    return code



def run(playwright: Playwright,catogaryurl,asin_list) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # 伪装
    page.set_extra_http_headers({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9"
    })

    # 进入主页
    page.goto("https://www.amazon.com/")


    #三种情况 1.被识别为机器人  2.没有被识别为机器人直接登录 3.没有被识别为机器人并且不需要登录
    while page.title() == "Amazon.com":

        print("1.被识别为机器人,或识别错误")
        # 获取图片地址pip
        loc = page.locator(".a-box-inner")
        url = loc.locator("img").get_attribute("src")
        # 解析为验证码

        response = requests.get(url)

        ocr = ddddocr.DdddOcr()

        code = ocr.classification(response.content)

        print(code)
        # 输入code进入目标页面
        page.locator("#captchacharacters").fill(code)

        # 提交
        page.locator(".a-button-text").click()
        


    page.locator("#nav-tools > a:nth-child(2)").click()

    page.get_by_label("Email or mobile phone number").fill("liuwannianliu@gmail.com")

    page.get_by_label("Continue").click()

    page.get_by_label("Password").fill("liu2391042097")

    page.get_by_label("Sign in").click()

    page.wait_for_timeout(10000)

    # 遍历读取数据

    for asin in asin_list:
        #目标路径
        fullurl = catogaryurl + asin

        page.goto(fullurl)

        #查看所有评论
        page.locator("#cr-pagination-footer-0").get_by_role("link", name="See more reviews").click()

        page.locator("#a-autoid-5-announce").click()

        # 根据消极评论分类
        page.get_by_label("Critical reviews").get_by_text("Critical reviews").click()


        # 翻页读取评论
        # 当下一页标签可以点击的时候持续循环  while 条件有没有a标签   html: li a  3个span（有下一页）     li   3个span（没有下一页）
        while page.query_selector('ul.a-pagination li.a-last').query_selector('a'):
            # 如果有下一页持续循环获取文本 .a-size-base review-text review-text-content  > span标签里面装文本
            print("还有评论")

            loclist = page.locator("div#cm_cr-review_list > div.a-section.review.aok-relative")

            #遍历所有的 评论div
            for i in range(loclist.count()):
                loc = loclist.nth(i)

                loc.locator()





    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    catogaryurl = "https://www.amazon.com/dp/"
    asin_list = ["B09DKG2MJ9","B08V4LDPSL","B089QCKGJF"]

    run(playwright,catogaryurl,asin_list)