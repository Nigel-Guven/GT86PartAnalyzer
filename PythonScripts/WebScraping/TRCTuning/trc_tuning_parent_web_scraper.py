from operator import contains
import os
import sys
import uuid
from bs4 import BeautifulSoup
from requests import get
sys.path.insert(0, 'PythonScripts\\Extensions')

import ExceptionsEx as exceptionsEx
import SupportFunctionsEx as supportFuncs

def main():

# Global Variables
 
    user_agent_headers = {"User-Agent":"Mozilla/5.0"}
    clean_product_supplier = "TRCTuning"
    raw_html_directory = r'PythonScripts\\HTML\\RawHTML\\' + clean_product_supplier
    
# Check that files are being outputted to the correct directory

    try:
        supportFuncs.getCurrentPath()
        supportFuncs.createDirectoryIfNotExists(raw_html_directory)
        supportFuncs.switchToRawPath(raw_html_directory)
    except FileNotFoundError:
        raise exceptionsEx.FilePathNotCorrectException(raw_html_directory)

# Web Scrape
    
    page_header = 'https://www.trc-tuning.com/'
    page_stem = '/TOYOTA-Tuning/GT86-FRS-BRZ-Tuning/GT86-FR-S-BRZ-Tuning/?view_mode=tiled&listing_sort=&listing_count=600'

    page_url = page_header + page_stem

    response = get(page_url, headers = user_agent_headers)
    
    if response.status_code == 200:
        parent_url_soup = BeautifulSoup(response.text, 'html.parser')

# Get Child Links that are product related

        for child in parent_url_soup.find_all('a', href = True):
            if isChildProductPage(str(child)):              
                response = get(page_header + child['href'], headers = user_agent_headers)    
                  
# Get the english version of the child page
                child_url_soup = BeautifulSoup(response.text, 'html.parser')

                english_link = str(child_url_soup.find_all("link", hreflang="en", rel="alternate"))
                english_page_url = cleanEnglishUrl(english_link)
                
                response_in_english = get(english_page_url, headers = user_agent_headers)   
                english_child_url_soup = BeautifulSoup(response_in_english.text, 'html.parser')
                print ("Found the URL:", english_page_url)  

# Save new HTML to file
                
                newGuid = str(uuid.uuid4())
                file_name = "content_" + newGuid + ".html"
                
                f = open(
                file_name, 
                "w", 
                encoding = "utf-8")

                f.write(str(english_child_url_soup))
                f.close()
                 
    else:
        raise exceptionsEx.HTTPFaultException(response.status_code)

    if 'Access Denied' in parent_url_soup:
        raise exceptionsEx.HTTPAccessDeniedException(response.status_code)

def isChildProductPage(text): 
    return text.__contains__("/GT86-FRS-BRZ-Tuning/GT86-FR-S-BRZ-Tuning/") and text.__contains__(".html")  

def cleanEnglishUrl(text): 
    text = text.replace("[<link href=\"","").replace("\" hreflang=\"en\" rel=\"alternate\"/>]","").strip()
    return text 

if __name__=="__main__":
	main()