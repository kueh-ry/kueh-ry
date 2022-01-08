import bs4
import requests
import os
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())

driver = webdriver.Chrome(service=service)

kuehs = ["kueh lapis transparent background", "curry puff transparent background", "kue dadar transparent background", "kueh bahulu transparent background", "kueh dodol transparent background",
"kueh lapis no background", "curry puff no background", "kue dadar no background", "kueh bahulu no background", "kueh dodol no background",
"kueh lapis white background", "curry puff white background", "kue dadar white background", "kueh bahulu white background", "kueh dodol white background"
]

for kueh in kuehs:
    query = kueh.replace(" ", "+")
    search_URL = "https://www.google.com/search?q={}&source=lnms&tbm=isch".format(query)
    driver.get(search_URL)

    driver.execute_script("window.scrollTo(0, 0);")

    page_html = driver.page_source
    pageSoup = bs4.BeautifulSoup(page_html, 'html.parser')
    containers = pageSoup.findAll('div', {'class':"isv-r PNCib MSM1fd BUooTd"} )

    len_containers = len(containers)

    folder_name = query
    if not os.path.isdir(folder_name):
        os.makedirs(folder_name)

    def download_image(url, folder_name, num):
        reponse = requests.get(url)
        if reponse.status_code == 200:
            with open(os.path.join(folder_name, str(num)+".jpg"), 'wb') as file:
                file.write(reponse.content)

    for i in range(1, len_containers + 1):
        if i % 25 == 0:
            continue
        xPath = """//*[@id="islrg"]/div[1]/div[{}]""".format(i)

        previewImageXPath = """//*[@id="islrg"]/div[1]/div[{}]/a[1]/div[1]/img""".format(i)
        previewImageElement = driver.find_element_by_xpath(previewImageXPath)
        previewImageURL = previewImageElement.get_attribute("src")

        driver.find_element_by_xpath(xPath).click()

        timeStarted = time.time()
        while True:

            imageElement = driver.find_element_by_xpath("""//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div[1]/a/img""")
            imageURL= imageElement.get_attribute('src')

            if imageURL != previewImageURL:
                break

            else:
                currentTime = time.time()

                if currentTime - timeStarted > 10:
                    print("Timeout! Download low res")
                    break

        try:
            download_image(imageURL, folder_name, i)
            print("Downloaded element {} out of {} total. URL: {}".format(i, len_containers + 1, imageURL))
        except:
            print("Couldn't download an image {}, continuing downloading the next one".format(i))