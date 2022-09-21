# This program prints Hello, world!

import os
import uuid
from bs4 import BeautifulSoup
from requests import get

from PythonScripts.Extensions.Exceptions import FilePathNotCorrectException, HTTPAccessDeniedException, HTTPFaultException

def main():

    # Check that files are being outputted to the correct directory

    try:
        current_working_directory = os.getcwd()
        print(current_working_directory)
        raw_html_directory = r'PythonScripts\\HTML\\RawHTML\\FenSport'

        if not os.path.exists(raw_html_directory):
            os.makedirs(raw_html_directory)

        os.chdir(raw_html_directory)
    except FileNotFoundError:
        raise FilePathNotCorrectException(raw_html_directory)
        
        
    # Global Variables

    user_agent_headers = {"User-Agent":"Mozilla/5.0"}
    index = 1

    while index < 35:

        # Create File Name Parameters

        newGuid = str(uuid.uuid4())
        file_name = "content_" + newGuid + ".html"      
        print(str(index) + ": " + file_name)

        # Web Scrape

        page_url = 'https://www.fensport.co.uk/collections/toyota-gt86-2012-to-2016?page='+ str(index)

        response = get(page_url, headers = user_agent_headers)
        
        if response.status_code == 200:
            url_soup = str(BeautifulSoup(response.text, 'html.parser'))
        else:
            raise HTTPFaultException(response.status_code)

        if 'Access Denied' in url_soup:
            raise HTTPAccessDeniedException(response.status_code)

        # Open new file and fill contents

        f = open(
            file_name, 
            "w", 
            encoding = "utf-8")

        f.write(url_soup)
        f.close()

        index += 1


if __name__=="__main__":
	main()