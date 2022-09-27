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
    page_header = "https://www.driftshop.com"
    clean_product_supplier = "DriftShop"
    raw_html_directory = r'PythonScripts\\HTML\\RawHTML\\' + clean_product_supplier

# Check that files are being outputted to the correct directory

    try:
        supportFuncs.getCurrentPath()
        supportFuncs.createDirectoryIfNotExists(raw_html_directory)
        supportFuncs.switchToRawPath(raw_html_directory)
    except FileNotFoundError:
        raise exceptionsEx.FilePathNotCorrectException(raw_html_directory)

    # Web Scrape

    page_url = 'https://www.driftshop.com/my-car/gt86-toyota-subaru-brz.html'
    response = get(page_url, headers = user_agent_headers)

    if response.status_code == 200:
        parent_url_soup = BeautifulSoup(response.text, 'html.parser')

        for child in parent_url_soup.find_all('a', class_="productImage", href = True):
            child_header = child['href']

            child_page_url = page_header + child_header
            response = get(child_page_url, headers = user_agent_headers)
            child_url_soup = BeautifulSoup(response.content, 'html.parser')

            newGuid = str(uuid.uuid4())
            file_name = "content_" + newGuid + ".html"

            # Open new file and fill contents
            
            f = open(
                file_name, 
                "w", 
                encoding = "utf-8")

            f.write(str(child_url_soup))
            f.close()
    else:
        raise exceptionsEx.HTTPFaultException(response.status_code)

    if 'Access Denied' in parent_url_soup:
        raise exceptionsEx.HTTPAccessDeniedException(response.status_code)
if __name__=="__main__":
	main()