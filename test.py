import undetected_chromedriver as uc
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = uc.Chrome(headless=False,use_subprocess=False)
#driver.get('https://www.browserscan.net/bot-detection')

# driver.get('https://abrahamjuliot.github.io/creepjs/')
# driver.save_screenshot('nowsecure.png')
#https://skinport.com/rust/market?sort=percent&order=desc
driver.get('https://skinport.com/rust/market?sort=percent&order=desc&pricegt=85')



    # results_container = WebDriverWait(driver, timeout=3).until(
    #     EC.presence_of_element_located((By.ID, "rso"))

wait2 = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME,"ItemPreview-content")))
wait = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME,"CatalogPage-items")))

# items = driver.find_elements(By.CLASS_NAME, "ItemPreview-content")
#driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
i = 0
# print(wait.children)
with open("test.txt", "w") as myfile:
    for items in wait.children("div", recursive=True):
        for item in items.children():
            #print(item.tag_name)
            for grandchild in item.children(recursive=True):
            #    print("\t\t", grandchild.tag_name, "\n\t\t\t", grandchild.text)
                myfile.write(grandchild.text)
        i += 1
        if i == 5:
            break



print(i)
# class ItemPreview-itemInfo



# time.sleep(3)
# for item in wait:
#         item.tag_name
#         # iteminfo = item.find_element((By.CLASS_NAME,"ItemPreview-itemInfo"))
#         # itemprice = iteminfo.find_element((By.CLASS_NAME,"ItemPreview-priceValue"))
#         # itemeuro = itemprice.find_element((By.CLASS_NAME,"Tooltip-link"))
#         # print (f"item price: {itemeuro.text}")

# time.sleep(10)