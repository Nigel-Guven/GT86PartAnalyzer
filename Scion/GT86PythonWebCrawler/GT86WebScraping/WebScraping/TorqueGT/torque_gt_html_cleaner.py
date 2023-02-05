import os
import csv

from bs4 import BeautifulSoup
os.getcwd()

try:
    import GT86WebScraping.Extensions.ExceptionsEx as exceptions
    import GT86WebScraping.Extensions.SupportFunctionsEx as supportFuncs
    import GT86WebScraping.Extensions.WebScrapingEx as scrapeFuncs
except ModuleNotFoundError:
    os.getcwd()

def main():

    # global vars
    clean_product_supplier = "TorqueGT"
    rows = []
    raw_html_directory = r'GT86WebScraping\\HTML\\RawHTML\\' + clean_product_supplier
    processed_html_directory = r'GT86WebScraping\\HTML\\ProcessedHTML'
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
                dirty_product_title = str(soup.find_all("span", class_="base"))                          
                clean_product_title = cleanTitle(dirty_product_title)
                
                
                #price
                dirty_product_price = str(soup.find_all("span", class_="price"))
                clean_product_price = cleanPrice(dirty_product_price)
                
                
                #stock
                dirty_product_stock = str(soup.find_all("span", class_="shiplines"))
                clean_product_in_stock = checkStockLevels(dirty_product_stock)
                
                #notes
                dirty_product_notes = str(soup.find_all("div", class_="specific-desc desc-specification"))          
                clean_product_notes = cleanNotes(dirty_product_notes)
                print(clean_product_notes)
                
                #description
                dirty_product_description = str(soup.find_all("div", class_="specific-desc desc-description"))
                clean_product_description = cleanDescription(dirty_product_description)
                if clean_product_description.__contains__("[]"):
                    clean_product_description = clean_product_title

                
                # Add Item as it is parsed to list      
                rows.append([clean_product_title, clean_product_price, '', clean_product_description, clean_product_notes, clean_product_in_stock, clean_product_supplier])
                
                #tmpFile.close()
                #os.remove(path)
                
    except UnicodeDecodeError:
        pass 
    
    # Open new file and fill contents 
    supportFuncs.switchToProcessedPath(processed_html_directory)

    file_name = "torque_gt.csv" 
  
    file = open(file_name,'a+', encoding='latin1', errors='ignore', newline='')   
    csvwriter = csv.writer(file) 

    header = ['product_name', 'price', 'item_type', 'description', 'misc_notes', 'in_stock', 'supplier'] 
    csvwriter.writerow(header)
   
    for row in rows:
        csvwriter.writerow(row)
        
    file.close()  
    
def cleanTitle(text): 
    text = text.replace("[","").replace("]","").strip()  
    text = scrapeFuncs.remove_html_markup(text)
    text = text.replace("&amp;","&")
    return text

def cleanPrice(text): 
    text = text.replace("[","").replace("]","").strip()  
    text = scrapeFuncs.remove_html_markup(text)   
    text = text.replace("&amp;","&")
    return text

def cleanDescription(text): 
    text = text.replace("[","").replace("]","").strip()  
    text = scrapeFuncs.remove_html_markup(text) 
    if text.__contains__("jquery"):
        text = text[ 0 : text.index("require")]

    text = text.replace("See Less...","").strip()
    text = text.strip()
    return text

def cleanNotes(text):
    if text != "":
        text = text.replace("[","").replace("]","").strip()  
        text = scrapeFuncs.remove_html_markup(text)  
        text = text.strip()
        return text
    else:
        return "No notes available"

# helper functions
def checkStockLevels(text):
    if text.__contains__("Special order"):
        return "Preorder Only"        
    elif text.__contains__("In stock"):
        return "In Stock"
    else:
        return "Not In Stock"
 
if __name__=="__main__":
	main()