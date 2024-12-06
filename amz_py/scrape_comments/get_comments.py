from playwright.sync_api import sync_playwright

# 启动 playwright driver进程
p = sync_playwright().start()

browser = p.chromium.launch(headless=False)

page = browser.new_page()

