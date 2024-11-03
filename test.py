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
#https://skinport.com/rust/market?sort=percent&order=desc&pricegt=85
driver.get('https://skinport.com/rust/market?sort=percent&order=desc')



    # results_container = WebDriverWait(driver, timeout=3).until(
    #     EC.presence_of_element_located((By.ID, "rso"))

wait2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,"ItemPreview-content")))
wait = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME,"CatalogPage-items")))

# items = driver.find_elements(By.CLASS_NAME, "ItemPreview-content")
#driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
i = 0
# print(wait.children)
with open("test.txt", "w") as myfile:
    for items in wait.children():
        for item in items.children():
            #print(item.tag_name)

            # Write code to skip first it has no content
            for grandchild in item.children():
                 i+=1
                 myfile.write( f"{i} \n")
            #    print("\t\t", grandchild.tag_name, "\n\t\t\t", grandchild.text)
                 myfile.write(grandchild.text)



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
