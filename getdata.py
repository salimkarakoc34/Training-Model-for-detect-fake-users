from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import csv
import time
import logging
import requests
import random

random_number = random.randint(3, 8)


logging.basicConfig(filename='test.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

# Tinder'ın ana sayfasını yükleyin
driver = webdriver.Chrome()
driver.get("https://tinder.com")
logging.info('Tinder ana sayfası yüklendi')

# Tinder'ın login 
# We have to sleep the driver bcs Tinder can stop your request when it realize you are a robot 

log_in = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Log in']")))
log_in.click()
time.sleep(random_number)
logging.info('Ana ekran giris')

log_in = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="o697594959"]/main/div/div/div[1]/div/div/div[3]/span/div[2]/button')))
log_in.click()
time.sleep(random_number) # We have to sleep the driver bcs Tinder can stop your request when it realize you are a robot 

# Oturum acma secenekleri 
#with facebook is easy 

logging.info('oturum acma baglantilari')#U can add logging info when the driver give error u can chech where is wrong

driver.get("https://www.facebook.com/login.php?skip_api_login=1&api_key=464891386855067&kid_directed_site=0&app_id=464891386855067&signed_next=1&next=https%3A%2F%2Fwww.facebook.com%2Fv2.8%2Fdialog%2Foauth%3Fapp_id%3D464891386855067%26cbt%3D1682322615334%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df210c84f8739374%2526domain%253Dtinder.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Ftinder.com%25252Ff2a97b2a1a43f38%2526relation%253Dopener%26client_id%3D464891386855067%26display%3Dpopup%26domain%3Dtinder.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Ftinder.com%252F%26locale%3Den_US%26logger_id%3Dfe4a3c2a28899c%26origin%3D1%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df5c039785558a4%2526domain%253Dtinder.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Ftinder.com%25252Ff2a97b2a1a43f38%2526relation%253Dopener%2526frame%253Df2cfec0b0c5dda%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Duser_birthday%252Cuser_photos%252Cemail%252Cuser_likes%26sdk%3Djoey%26version%3Dv2.8%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df5c039785558a4%26domain%3Dtinder.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Ftinder.com%252Ff2a97b2a1a43f38%26relation%3Dopener%26frame%3Df2cfec0b0c5dda%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=popup&locale=en_US&pl_dbl=0")
email_log_in= driver.find_element(By.XPATH, '//*[@id="email"]')
email_log_in.click()
email_log_in.send_keys('FACEBOOK EMAIL ')

time.sleep(random_number)

password_log_in =driver.find_element(By.XPATH, '//*[@id="pass"]')
password_log_in.click()
time.sleep(random_number)
password_log_in.send_keys('PASSWORD')
time.sleep(random_number)
logging.info('sifre girildi')

submit_log_in =driver.find_element(By.ID, 'loginbutton').click()
time.sleep(random_number)
logging.info('fb login is approved')

driver.get("https://tinder.com/app/recs")#When we login tinder direct us to main page and also we do :)

log_in = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Log in']")))
log_in.click()
time.sleep(random_number)

log_in = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="o697594959"]/main/div/div/div[1]/div/div/div[3]/span/div[2]/button')))
log_in.click()
time.sleep(random_number)




#Permission to location
loca_log_in = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="o697594959"]/main/div/div/div/div[3]/button[1]'))).click()
time.sleep(random_number)

#no need notification
notif_log_in = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="o697594959"]/main/div/div/div/div[3]/button[2]'))).click()
time.sleep(random_number)
#no cookies 
cook_log_in=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="o-1868991261"]/div/div[2]/div/div/div[1]/div[2]/button'))).click()
time.sleep(random_number)



logging.info('welcome to main page ')





driver.set_window_size(680, 1080) #for better picture we do that 
time.sleep(random_number)
bio =driver.find_element(By.ID, 'o-1868991261') #bios information
text1 = bio.text
text1=text1.split("Report")[0]
driver.save_screenshot(f"chicky001.png")
time.sleep(random_number)
like=driver.find_element(By.XPATH, '//*[@id="o-1868991261"]/div/div[1]/div/div/main/div/div/div[1]/div/div[3]/div/div[2]/button')
like.click()
text1=text1.split("Report")[0]



with open('bios.csv', 'w', newline='',encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['image name', 'bio','passions'])
    for i in range(500):

      time.sleep(2)
      driver.save_screenshot(f"chickies/chicky{i}.png") #bios information
      time.sleep(random_number)
      goddamnbutton=driver.find_element(By.XPATH, '//*[@id="o-1868991261"]/div/div[1]/div/div/main/div/div/div[1]/div/div[2]/div[3]/button')
      goddamnbutton.click()
      logging.info(f' {i}buton tamamlandi ')        
      time.sleep(random_number)
      driver.save_screenshot(f"chickies/chicky{i}.png")
      logging.info(f' chicky{i} kaydedildi ')
      try:
        information = driver.find_element(By.XPATH, '//*[@id="o-1868991261"]/div/div[1]/div/div/main/div/div[1]/div[1]/div/div[2]/div[2]/div')
        bio = information.text  #bios information
      except NoSuchElementException as e:
        print(f"Hata: {e}. Element bulunamadı.")
        bio = "  "  # sometimes there is no bio information we use try except for keeping the surf 


      
      logging.info(f'{i} we got  the bio  ')
      lifestyle=driver.find_element(By.XPATH, '//*[@id="o-1868991261"]/div/div[1]/div/div/main/div/div[1]/div[2]/div/div/div[2]/button')
      passion = lifestyle.text #passion information
      logging.info(f'{i} life style   ')
      like=driver.find_element(By.XPATH, '//*[@id="o-1868991261"]/div/div[1]/div/div/main/div/div[1]/div[2]/div/div/div[2]/button')      
      logging.info(f'{i} rejected ') 
      like.click()
      writer.writerow([f'girl{i}.png', bio])




driver.quit()
