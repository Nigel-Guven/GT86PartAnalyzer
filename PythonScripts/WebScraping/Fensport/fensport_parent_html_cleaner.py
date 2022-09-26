import os
import sys
import csv
import unicodedata

from bs4 import BeautifulSoup

sys.path.insert(0, 'PythonScripts\\Extensions')

try:
    import ExceptionsEx as exceptions 
    import WebScrapingEx as scrapeFuncs
    import SupportFunctionsEx as supportFuncs
except ModuleNotFoundError:
    current_working_directory = os.getcwd()

def main():

    # global vars
    clean_product_supplier = "FenSport"
    rows = []
    raw_html_directory = r'PythonScripts\\HTML\\RawHTML\\' + clean_product_supplier
    processed_html_directory = r'PythonScripts\\HTML\\ProcessedHTML'

    # Create Directories
    try:
        supportFuncs.getCurrentPath()
        supportFuncs.createDirectoryIfNotExists(raw_html_directory)
        supportFuncs.createDirectoryIfNotExists(processed_html_directory)
        supportFuncs.switchToRawPath(raw_html_directory)

    except FileNotFoundError:
        raise exceptions.FilePathNotCorrectException(raw_html_directory)  
    
# Parse Directory HTML Files
    try: 
        for path in os.listdir(os.getcwd()):
            if(os.path.isfile(path)):
                tmpFile = open(
                    path,
                    "r",
                    encoding="utf-8"
                )

                soup = BeautifulSoup(tmpFile, 'html.parser')

                #title
                dirty_product_title = str(soup.find_all("meta", property="og:title"))
                clean_product_title = dirty_product_title.replace("[<meta content=\"", "").replace("&amp;", "&").replace("\" property=\"og:title\"/>]","").strip()              
                clean_product_title = checkForRemnantHTML(clean_product_title)

                #price
                dirty_product_price = str(soup.find_all("meta", property="og:price:amount"))
                clean_product_price = dirty_product_price.replace("[<meta content=\"", "").replace("\" property=\"og:price:amount\"/>]","").strip()
                clean_product_price = supportFuncs.formatPrice(clean_product_price)

                #stock
                dirty_product_in_stock = str(soup.find_all("span"))

                clean_product_in_stock = ""
                if dirty_product_in_stock.__contains__("In stock"):
                    clean_product_in_stock = "In Stock"
                elif dirty_product_in_stock.__contains__("Discontinued"):
                    clean_product_in_stock = "Discontinued"    
                else:
                    clean_product_in_stock = "Not In Stock" 

                #notes
                dirty_product_notes = str(soup.find_all("div", id="tab-3"))
                clean_product_notes = scrapeFuncs.remove_html_markup(dirty_product_notes).replace("[","").replace("]","").lstrip("-").rstrip().lstrip()               
                try:
                # Remove all characters before the character '-' from string
                    clean_product_notes = clean_product_notes[clean_product_notes.index('-') + 1 : ]
                except ValueError:
                    pass
                clean_product_notes = clean_product_notes.lstrip()
                clean_product_notes = checkForBadData(clean_product_notes)

                #description
                dirty_product_description = str(soup.find_all("div", id="tab-1"))  
                clean_product_description = scrapeFuncs.remove_html_markup(dirty_product_description)
                clean_product_description = cleanDescription(clean_product_description)

                # Add Item as it is parsed to list      
                rows.append([clean_product_title, clean_product_price, '', clean_product_description, clean_product_notes, clean_product_in_stock, clean_product_supplier])

                tmpFile.close()
                os.remove(path)
                    
    except UnicodeDecodeError:
        pass  

    # Open new file and fill contents 

    supportFuncs.switchToProcessedPath(processed_html_directory)

    file_name = "fensport_content.csv" 
  
    file = open(file_name,'a+', encoding='latin1', errors='ignore', newline='')   
    csvwriter = csv.writer(file) 

    header = ['product_name', 'price', 'item_type', 'description', 'misc_notes', 'in_stock', 'supplier'] 
    csvwriter.writerow(header)
   
    for row in rows:
        csvwriter.writerow(row)
        
    file.close()  

def cleanDescription(text): 
    text = text.replace("[","").replace("]","").replace("&amp;", "&")
    text = text.replace(u'\x92', u'\'').replace(u'\xa0',u' ').replace(u'Φ','')
    text = text.replace(u'℃',u' Degrees Celsius ').replace(u'\u2033',u'"')
    text = text.replace(u'0.03 U/S -',u'').replace(u'0.05 U/S -',u'').replace(u'0.25 U/S -',u'')
    text = text.replace('\n', "")
    text = text.replace('.', '. ')    
    return text

def checkForRemnantHTML(text): 
    if text.__contains__('<meta'):
        text = text.replace("[<meta &=\"\" -=\"\" brz\"=\"\" content=\"", "")
        text = text.replace("\" gt86=\"", "")
        text = text.replace("[<meta aluminum=\"\" content=\"","")
        text = text.replace(" forged=\"\" property=\"og:title\" wheel\"=\"\"/>]","")
        return text
    else:
        return text

def checkForBadData(text): 
    if text.__contains__('#NAME'):
        return "No notes available"
    else:
        return text
 
if __name__=="__main__":
	main()