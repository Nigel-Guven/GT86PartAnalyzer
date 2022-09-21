# This program prints Hello, world!

import os
import sys
import re
import uuid
from xml.dom.minidom import Identified
from bs4 import BeautifulSoup
from requests import get
sys.path.insert(0, 'PythonScripts\\Extensions')

try:
    import Exceptions as exceptions 
    import ScriptFunctions as functions
except ModuleNotFoundError:
    current_working_directory = os.getcwd()
    print(current_working_directory)

def main():
    
    print('\n---------------------------------------------------------')

    try:
        current_working_directory = os.getcwd()
        print(current_working_directory)
        raw_html_directory = r'PythonScripts\\HTML\\RawHTML\\FenSport'
        processed_html_directory = r'PythonScripts\\HTML\\ProcessedHTML'

        if not os.path.exists(raw_html_directory):
            os.makedirs(raw_html_directory)

        if not os.path.exists(processed_html_directory):
            os.makedirs(processed_html_directory)

        os.chdir(raw_html_directory)
    except FileNotFoundError:
        raise exceptions.FilePathNotCorrectException(raw_html_directory)       
        
    # Parse Directory HTML Files

    for path in os.listdir(os.getcwd()):
        if(os.path.isfile(path)):
            tmpFile = open(
                path,
                "r",
                encoding="utf-8"
            )
            print(str(tmpFile))
            soup = BeautifulSoup(tmpFile, 'html.parser')

            # Full Product Description
            product_view = soup.find_all("a", class_="product-card")
            product_view = functions.remove_html_markup(str(product_view))

            # Product Description Link
            product_description_link = soup.find_all("a", class_="product-card")
            #product_description_link = functions.remove_html_markup(str(product_description_link))

            print(product_description_link)
            



        
        
            



    

    # Create File Name Parameters
    """
    newGuid = str(uuid.uuid4())
    file_name = "clean_fensport_content_" + newGuid + ".html"      
    print(str(file_name))


    
    
    # Open new file and fill contents
    
    f = open(
        file_name, 
        "w", 
        encoding = "utf-8")

    f.write(url_soup)
    f.close()
    """
    print('\n---------------------------------------------------------')
    
if __name__=="__main__":
	main()