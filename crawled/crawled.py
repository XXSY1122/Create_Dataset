from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import urllib.request
import os

# 이미지 크롤링 코드
# 'query'에 적혀있는 값을 검색하여 나온 이미지를 저장하는 코드

# Initialize WebDriver
chrome_options = webdriver.ChromeOptions()
chrome_options.binary = 'C://Users/user/Desktop/dataset/crawled/chromedriver.exe'
driver = webdriver.Chrome()

# Search for images
query = '메로나 무료나눔'
driver.get('https://www.google.com/imghp')
search_bar = driver.find_element(By.NAME, "q")
search_bar.send_keys(query)
search_bar.submit()
time.sleep(2)


# 저장할 파일 경로 설정 (만약 바탕화면 crawled 폴더내부로 설정하면 crawled 폴더 내부에 '메로나 무료나눔'이라는 폴더가 따로 생김)
save_path = f'C:/Users/user/Desktop/crawled/{query}'
if not os.path.exists(save_path):
    os.mkdir(save_path)

# 403 방지
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# Scroll down, crawl and save images
# 임의로 변경가능
max_images_per_round = 30
total_images_crawled = 0

while True:  # Keep crawling until you break the loop manually
    # Scroll down to load more images
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # 큰 용량인 사진은 2초로도 부족한 경우 있으니 경우에따라 조절 (10까지 해도 ㄱㅊ)
    
    # Get image elements
    img_elements = driver.find_elements(By.CSS_SELECTOR, ".rg_i")[
        total_images_crawled : total_images_crawled + max_images_per_round
    ]
    
    if not img_elements:
        print("No more images found. Exiting.")
        break
    
    # Fetch image details
    for idx, img in enumerate(img_elements):
        print(f"{total_images_crawled + idx + 1} proceeding...")
        try:
            img.click()
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (
                        By.CSS_SELECTOR,
                        '#Sva75c > div.A8mJGd.NDuZHe.CMiV2d > div.dFMRD > div.pxAole > div.tvh9oe.BIB1wf.hVa2Fd > c-wiz > div > div > div > div.n4hgof > div.MAtCL.PUxBg > a > img.r48jcc.pT0Scc.iPVvYb',
                    )
                )
            )# CSS_SELECTOR뒤에 있는 부분은 계속 바뀔수 있음. 따라서 오류가 뜰시 가장 먼저 바꾸어야 할 부분임.
            # 크롬 > 이미지 검색 > 이미지 클릭 > f12 > 우클로 이미지 클릭한 영역 선택 > HTML 영역 우클 - 복사선택 - 'selector 복사' 하여 그 값을 붙여넣도록 함.
            img_element = driver.find_element(
                By.CSS_SELECTOR,
                '#Sva75c > div.A8mJGd.NDuZHe.CMiV2d > div.dFMRD > div.pxAole > div.tvh9oe.BIB1wf.hVa2Fd > c-wiz > div > div > div > div.n4hgof > div.MAtCL.PUxBg > a > img.r48jcc.pT0Scc.iPVvYb',
            )
            img_src = img_element.get_attribute('src')
            
            # Using Request to add headers and save image
            req = urllib.request.Request(url=img_src, headers=headers)
            with urllib.request.urlopen(req) as response, open(f"{save_path}/{total_images_crawled + idx}.png", 'wb') as out_file:
                data = response.read()
                out_file.write(data)
            print(f"Image {total_images_crawled + idx + 1} saved!")
        except Exception as e:
            print(f'error in {total_images_crawled + idx + 1}: {str(e)}')
    
    total_images_crawled += len(img_elements)
    
# Close WebDriver
driver.close()
print('done')
