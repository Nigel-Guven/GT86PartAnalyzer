import os
import sys
import csv

from bs4 import BeautifulSoup

sys.path.insert(0, 'PythonScripts\\Extensions')

try:
    import ExceptionsEx as exceptions 
    import WebScrapingEx as scrapeFuncs
    import SupportFunctionsEx as supportFuncs
except ModuleNotFoundError:
    os.getcwd()

def main():

    # global vars
    clean_product_supplier = "DriftShop"
    rows = []
    bundleTitleItems = []
    bundlePriceItems = []
    bundleStockItems = []
    bundleDescriptionItems = []
    bundleNotesItems = []

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
                
                # Check if bundle
                dirty_product_title_stock_price = str(soup.find_all("li", class_="bundleProductName"))

                #notes
                dirty_product_notes = str(soup.find_all("div", class_="shortdescription"))
                dirty_product_notes = cleanNotes(dirty_product_notes)
                bundleNotesItems.append(dirty_product_notes)

                #description
                dirty_product_description = str(soup.find_all("div", class_="longdescription"))
                dirty_product_description = cleanDescription(dirty_product_description)
                bundleDescriptionItems.append(dirty_product_description)  

                if dirty_product_title_stock_price == "[]":

                    #title
                    dirty_product_title = str(soup.find_all("h1", itemprop="name"))                           
                    clean_product_title = cleanTitle(dirty_product_title)
                    bundleTitleItems.append(clean_product_title)

                    #price
                    dirty_product_price = str(soup.find_all("meta", itemprop="price"))
                    
                    if dirty_product_price == "[]":
                        dirty_product_price = str(soup.find_all(attrs={"name":"bundlePrice[]"}))
                        dirty_product_price = dirty_product_price.split(" ")
                        for item in dirty_product_price:
                            item = item.replace("/>","")
                            item = item.replace(",","")
                            if item.__contains__("value") and not item.__contains__("0"):
                                item = item.replace("]","").replace("value=","").replace("\"","")
                                bundlePriceItems.append(item)
                    else:                   
                        clean_product_price = cleanPrice(dirty_product_price)
                        bundlePriceItems.append(clean_product_price)

                    #stock

                else:
                    #title
                    dirty_product_title_stock_price = cleanTitle(dirty_product_title_stock_price).replace("1 x ","").strip()
                    dirty_product_title_price = dirty_product_title_stock_price.splitlines()[0]
                    clean_product_title = dirty_product_title_price.split('+')[0]
                    print(clean_product_title)

                    #price
                    if(len(dirty_product_title_price) > 0):
                        print(clean_product_price)
                        clean_product_price = dirty_product_title_price.splitlines()[0].replace(",","")
                        print(clean_product_price)
                    else:
                        clean_product_price = "0.00"
                        print(clean_product_price)
                
            
                    #stock
                    if dirty_product_title_stock_price.__contains__("Dispatched"):
                        bundleStockItems.append("Preorder Only")
                    elif dirty_product_title_stock_price.__contains__("in stock"):
                        bundleStockItems.append("In Stock")
                    else :
                        bundleStockItems.append("Not In Stock")





                #tmpFile.close()
                #os.remove(path)
                    
    except UnicodeDecodeError:
        pass 

    '''
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
    '''

def cleanTitle(text): 
    text = scrapeFuncs.remove_html_markup(text)
    text = text.replace("[","").replace("]","").replace("&amp;","&")
    if text.__contains__('Oil Filter'):
        text = text.split('|', 1)[0]
        return text
    else:
        return text

def cleanNotes(text): 
    text = scrapeFuncs.remove_html_markup(text)
    text = text.replace("[","").replace("]","").replace("&amp;","&")
    return text

def cleanDescription(text): 
    text = scrapeFuncs.remove_html_markup(text)
    text = text.replace("[","").replace("]","").replace("&amp;","&")
    return text

def cleanPrice(text): 
    text = text.replace("[<meta content=\"","").replace("\" itemprop=\"price\"/>]","")
    return text

def checkForBadData(text): 
    if text.__contains__('#NAME'):
        return "No notes available"
    elif text.__contains__(''):
        return "No notes available"
    else:
        return text
 
if __name__=="__main__":
	main()