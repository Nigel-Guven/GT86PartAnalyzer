import os
import sys
import uuid
from bs4 import BeautifulSoup
from requests import get
sys.path.insert(0, 'PythonScripts\\Extensions')

import ExceptionsEx as exceptionsEx
import SupportFunctionsEx as supportFuncs

def main():

# Check that files are being outputted to the correct directory

    try:
        supportFuncs.getCurrentPath()
        raw_html_directory = r'PythonScripts\\HTML\\RawHTML\\FenSport'
        supportFuncs.createDirectoryIfNotExists(raw_html_directory)
        supportFuncs.switchToRawPath(raw_html_directory)
    except FileNotFoundError:
        raise exceptionsEx.FilePathNotCorrectException(raw_html_directory)

# Global Variables
 
    user_agent_headers = {"User-Agent":"Mozilla/5.0"}
    index = 1

    while index < 35:

# Create File Name Parameters

        # Web Scrape
        page_header = 'https://www.fensport.co.uk'
        page_stem = '/collections/toyota-gt86-2012-to-2016?page=' + str(index)

        page_url = page_header + page_stem

        response = get(page_url, headers = user_agent_headers)
        
        if response.status_code == 200:
            parent_url_soup = BeautifulSoup(response.text, 'html.parser')

            for child in parent_url_soup.find_all('a', href = True):
                #print ("Found the URL:", child['href'])
                if str(child).__contains__("toyota-gt86-2012-to-2016/products"):
                    response = get(page_header + child['href'], headers = user_agent_headers)
          
# Open new file and fill contents
                    child_url_soup = BeautifulSoup(response.text, 'html.parser')
                    newGuid = str(uuid.uuid4())
                    file_name = "content_" + newGuid + ".html"      
                    print(str(index) + ": " + file_name)
                    
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

        index += 1

if __name__=="__main__":
	main()