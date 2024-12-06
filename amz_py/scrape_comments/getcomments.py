from playwright.sync_api import sync_playwright

pw = sync_playwright().start()

browser = pw.chromium.launch(headless=False)

page  = browser.new_page()

page.goto("https://www.amazon.com/ref=nav_logo")

print(page.title())
page.locator("#twotabsearchtextbox").fill("B0CP1TSMST")

page.locator("#nav-search-submit-button").click()

print(page.locator(".a-declarative").all())