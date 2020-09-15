from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import os

def dowload_img(search_item):
    '''FUNCTION TO CONFIG THE DRIVER AND SAVE THE IMAGES LINKS.

    PARAMETER:
        search_item -- ITEM TO SEARCH

    RETURN:
        img -- LIST OF IMAGES LINKS
    '''

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")

    ## ATTENTION TO THIS LINE -> DRIVER USED FOR CHROME VERSION 85 ##
    ## EDIT THE DRIVE FOR THE BROWSER / VERSION OF YOUR PREFERENCE ##
    ## MAKE SURE THE DRIVER IS IN THE SAME FOLDER OF THE CODE ##
    driver = webdriver.Chrome(options=options)

    driver.get("https://www.google.com/imghp?hl=EN")

    time.sleep(2)

    search_tool = driver.find_element_by_name('q')

    search_tool.clear()
    search_tool.send_keys(f'{search_item}')
    search_tool.send_keys(Keys.ENTER)

    time.sleep(2)

    elements_img = driver.find_elements_by_tag_name('img')

    img = []

    elements = [itens for itens in elements_img if itens.get_attribute('class') == 'rg_i Q4LuWd']

    for elements_tag in range(len(elements)):
        try:
            elements[elements_tag].click()
            elements_img = driver.find_elements_by_tag_name('img')

            for image in elements_img:
                if image.get_attribute('class') == 'n3VNCb' and 'http' in image.get_attribute("src") and\
                    image.get_attribute("src") not in img and 'https://encrypted' not in image.get_attribute("src"):
                    img.append(image.get_attribute('src'))
        except:
            print('Error... Next Image')

    driver.quit()

    return img

def save_img(img_list, search_content):
    '''SAVE IMAGES IN A DIRECTORY WITH A .TXT WITH REFERENCE LINKS.

    PARAMETERS:
        img_list -- LIST OF IMAGES THE PROGRAM HAS SAVED
        search_content -- ITEM OF SEARCH
    '''

    count = 1
    link_text = ''
    os.mkdir(search_content)

    for img in img_list:
        try:
            urllib.request.urlretrieve(img, f'{search_content}/{count:03}.jpg')
            link_text += f'{count:03} --> {img}\n\n'
            count += 1
        except:
            print('Error... Next Image')

    document_save(link_text, search_content)

def document_save(text, dir_name):
    '''GENERATES .TXT WITH REFERENCE LINKS.

    PARAMETERS:
        text -- TEXT TO BE WRITTEN
        dir_name -- NAME OF DIRECTORY WHERE SHOULD BE SAVED
    '''

    with open(f'{dir_name}/{dir_name}.txt', 'w') as txt:
        txt.write(f'DOWNLOADED IMAGES:\n===========================\n\n{text}'
                  f'============END============')

def print_links(links):
    '''PRINT THE LINKS AT THE USER'S TERMINAL FOR YOUR CONVENIENCE.

    PARÂMETRO:
        links -- LINKS THAT HAVE BEEN SAVED
    '''

    print('THE SEARCH RESULTS:')
    print('=========================')

    for link in range(len(links)):
        print(f'{(link+1):03} - {links[link]}\n')

    print('==========END============\n')

search_item = input('SEARCH: ')

print('STARTING THE SEARCH')
print('~NOTE: SOMETIMES THE CODE DOESN`T FIND MANY IMAGES OR DOESN`T DOWLOAD ALL THE FOUND IMAGES~')

img_content = dowload_img(search_item)
print_links(img_content)
save_img(img_content, search_item)