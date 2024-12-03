from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


chrome_options = Options()
chrome_options.add_argument("--headless")  # 无头模式，不显示浏览器界面
chrome_options.add_argument("--no-sandbox")  # 解决DevToolsActivePort文件不存在的报错
chrome_options.add_argument("--disable-dev-shm-usage")  # 禁用共享内存

# 伪装 User-Agent
chrome_options.add_argument("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")



driver = webdriver.Chrome(options=chrome_options)




driver.get("https://www.amazon.com/ref=nav_logo")