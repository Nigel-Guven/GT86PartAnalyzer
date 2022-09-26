# This program prints Hello, world!

import os
import uuid
from bs4 import BeautifulSoup
from requests import get

try:
    import ExceptionsEx as exceptions 
except ModuleNotFoundError:
    current_working_directory = os.getcwd()
    print(current_working_directory)

def main():
    
    print('\n---------------------------------------------------------')
    # Check that files are being outputted to the correct directory

    try:
        current_working_directory = os.getcwd()
        print(current_working_directory)
        raw_html_directory = r'PythonScripts\\HTML\\RawHTML\\TRCTuning'

        if not os.path.exists(raw_html_directory):
            os.makedirs(raw_html_directory)

        os.chdir(raw_html_directory)
    except FileNotFoundError:
        raise exceptions.FilePathNotCorrectException(raw_html_directory)
        
        
    # Global Variables

    user_agent_headers = {"User-Agent":"Mozilla/5.0"}


    # Create File Name Parameters

    newGuid = str(uuid.uuid4())
    file_name = "content_" + newGuid + ".html"      
    print(str(file_name))

    # Web Scrape

    page_url = 'https://www.trc-tuning.com/TOYOTA-Tuning/GT86-FRS-BRZ-Tuning/GT86-FR-S-BRZ-Tuning/?view_mode=tiled&listing_sort=&listing_count=600'

    response = get(page_url, headers = user_agent_headers)
    
    if response.status_code == 200:
        url_soup = str(BeautifulSoup(response.text, 'html.parser'))
    else:
        raise exceptions.HTTPFaultException(response.status_code)

    if 'Access Denied' in url_soup:
        raise exceptions.HTTPAccessDeniedException(response.status_code)

    # Open new file and fill contents

    f = open(
        file_name, 
        "w", 
        encoding = "utf-8")

    f.write(url_soup)
    f.close()
    print('\n---------------------------------------------------------')
    
if __name__=="__main__":
	main()