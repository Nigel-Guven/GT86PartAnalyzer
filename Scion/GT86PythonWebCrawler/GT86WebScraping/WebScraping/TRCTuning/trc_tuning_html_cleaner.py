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
    clean_product_supplier = "TRCTuning"
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
                dirty_product_title = str(soup.find_all("meta", property="og:title"))
                clean_product_title = cleanTitle(dirty_product_title)
                
                
                #price
                dirty_product_price = str(soup.find_all("div", class_="current-price-container"))
                clean_product_price = cleanPrice(dirty_product_price)
                
                #stock
                clean_product_in_stock = "In_Stock" 
                
                #notes
                clean_product_notes = "No notes available"
                
                #description
                dirty_product_description = str(soup.find_all("div", class_="tab-body active"))
                clean_product_description = cleanDescription(dirty_product_description)
                if dirty_product_description.__contains__("[]"):
                    clean_product_description = clean_product_title

                # Add Item as it is parsed to list      
                rows.append([clean_product_title, clean_product_price, '', clean_product_description, clean_product_notes, clean_product_in_stock, clean_product_supplier])
                tmpFile.close()
                os.remove(path)
                
    except UnicodeDecodeError:
        pass  
    
    # Open new file and fill contents 
    supportFuncs.switchToProcessedPath(processed_html_directory)
    
    file_name = "trc_tuning_content.csv" 
  
    file = open(file_name,'a+', encoding='latin1', errors='ignore', newline='')   
    csvwriter = csv.writer(file) 

    header = ['product_name', 'price', 'item_type', 'description', 'misc_notes', 'in_stock', 'supplier'] 
    csvwriter.writerow(header)
   
    for row in rows:
        csvwriter.writerow(row)
        
    file.close()  
    

def cleanTitle(text): 
    text = text.replace("&amp;","&")
    text = text.replace("EUR","")
    text = text.replace("[<meta content=\"","").replace("\" property=\"og:title\"/>]","").strip()  
    return text

def cleanPrice(text):
    text = scrapeFuncs.remove_html_markup(text)
    text = text.replace("[","").replace("]","")
    text = text.replace("Your price","").replace("Our standard price","").strip()
    text = text.replace("per set","").strip()
    text = text.replace("per piece(s)","").strip()
    text = text.replace("per pairs","").strip()
    text = text.replace("EUR","")
    text = text.strip()
    text = priceFormatter(text)
    if(text.count(".")>1):
        text = text.split[1]
        return text
    return text

def priceFormatter(text): 
    text = text.replace(",","d")   
    text = text.replace(".","c")
    text = text.replace("d",".")
    text = text.replace("c",",")
    return text
    
def cleanDescription(text): 
    text = text.replace("[","").replace("]","")
    text = scrapeFuncs.remove_html_markup(text).strip()   
    text = text.replace("&amp;","&")
    return text
    
if __name__=="__main__":
	main()