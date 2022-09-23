import os
from pickle import FALSE
import sys
import csv
import re

from bs4 import BeautifulSoup
sys.path.insert(0, 'PythonScripts\\Extensions')
cleaner = re.compile('<.*?>') 

try:
    import Exceptions as exceptions 
    import ScriptFunctions as functions
except ModuleNotFoundError:
    current_working_directory = os.getcwd()

def main():
    print('\n---------------------------------------------------------') 
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

            soup = BeautifulSoup(tmpFile, 'html.parser')

            
            dirty_product_title = str(soup.find_all("meta", property="og:title"))                       # All have names 
            dirty_product_price = str(soup.find_all("meta", property="og:price:amount"))                # All have prices
            dirty_product_description = str(soup.find_all("div", id="tab-1"))                           # All have description - needs to cleaned
            dirty_product_notes = str(soup.find_all("div", id="tab-3"))                                 # All have notes - needs to be cleaned
            dirty_product_in_stock = str(soup.find_all("span"))                                         # Needs Customisation
                                                   
            spanList = dirty_product_in_stock.split("span")   

            clean_product_in_stock = ""
            valueSet = False
            for i in spanList:
                if(valueSet == True):
                    clean_product_in_stock = clean_product_in_stock + i
                    break
                if "Stock status" in i:
                    clean_product_in_stock = i
                    valueSet = True   
                if "Not in Stock" in i:
                    clean_product_in_stock = "Not in Stock"
                    valueSet = True                                        

            clean_product_title = dirty_product_title.replace("[<meta content=\"", "").replace("&amp;", "&").replace("\" property=\"og:title\"/>]","").strip()
            clean_product_price = dirty_product_price.replace("[<meta content=\"", "").replace("\" property=\"og:price:amount\"/>]","").strip()

            clean_product_description = dirty_product_description
            clean_product_notes = dirty_product_notes.replace("[<div id=\"tab-3\">","").replace("]","").split()


            clean_product_supplier = str("FenSport")

            if str(dirty_product_title).__contains__("Crankshaft Main Bearing Set"):                
                print('\n---------------------------------------------------------')
                print(str(clean_product_title))
                print('\n---------------------------------------------------------')
                print(str(clean_product_price))
                print('\n---------------------------------------------------------')
                print(str(clean_product_description))
                print('\n---------------------------------------------------------')
                print(str(clean_product_notes))
                print('\n---------------------------------------------------------')
                print(str(clean_product_in_stock))
                print('\n---------------------------------------------------------')
                print(str(clean_product_supplier))
                print('\n---------------------------------------------------------')     
            
            # Create File Name Parameters
            
            """
            file_name = "fensport_content.html"      
            print(str(file_name))

            header = ['name', 'area', 'country_code2', 'country_code3']
            data = ['Afghanistan', 652090, 'AF', 'AFG']
    
            # Open new file and fill contents
            
            f = open(
                processed_html_directory + file_name, 
                "w", 
                encoding = "utf-8")

            f.write(url_soup)
            f.close()
            """
            
 
if __name__=="__main__":
	main()