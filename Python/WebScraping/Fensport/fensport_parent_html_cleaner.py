# This program prints Hello, world!

import os
import re
import uuid
from xml.dom.minidom import Identified
from bs4 import BeautifulSoup
from requests import get


try:
    import PythonScripts.Extensions.Exceptions as exceptions 
    import PythonScripts.HTMLCleaning.scriptfunctions as functions
except ModuleNotFoundError:
    current_working_directory = os.getcwd()
    print(current_working_directory)

def main():
    
    print('\n---------------------------------------------------------')
    #Go to Raw HTML directory

    try:
        current_working_directory = os.getcwd()
        print(current_working_directory)
        raw_html_directory = r'Python\\HTML\\RawHTML\\FenSport'
        processed_html_directory = r'Python\\HTML\\ProcessedHTML'

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
            product_view = PythonScripts.HTMLCleaning.scriptfunctions.functions.remove_html_markup(product_view)

            # Product Description Link
            product_description_link = soup.find_all("a", class_="product-card")

            print(product_view)
            



        
        
            



    

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