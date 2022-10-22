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
    clean_product_supplier = "DriftShop"

    bundleTitleItems = []
    bundlePriceItems = []
    bundleStockItems = []
    bundleDescriptionItems = []
    bundleNotesItems = []

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

                url_soup = BeautifulSoup(tmpFile, 'html.parser')

                #Handle Alloy pages
                document = str(url_soup.find_all("h3", class_="col-12"))
                if(document.__contains__("You might be interested in these rims")):
                    with open(tmpFile.name, "r", encoding='utf-8') as alloyFile:

                        clean_alloy_title = "Japan Racing JR-11 Wheel"
                        clean_alloy_price = ""
                        clean_alloy_stock = ""
                        clean_alloy_description = ""
                        clean_alloy_notes = clean_alloy_description

                        alloy_data = alloyFile.readlines()
                        for item in alloy_data:
                            if item.__contains__("div class=\"shortdescription\" itemprop=\"description"):
                                clean_alloy_description = cleanAlloyNotes(item)
                            if item.__contains__("\" itemprop=\"price\">"):                               
                                clean_alloy_price = item.replace("<meta content=\"","").replace("\" itemprop=\"price\">","").strip()    
                            if item.__contains__("in stock </strong>"):
                                clean_alloy_stock = "In Stock"
                            if item.__contains__("Expected in stock"):
                                clean_alloy_stock = "Preorder Only"
                        
                        bundleTitleItems.append(clean_alloy_title)
                        bundleNotesItems.append(clean_alloy_notes)
                        bundleDescriptionItems.append(clean_alloy_description)
                        bundlePriceItems.append(clean_alloy_price)
                        bundleStockItems.append(clean_alloy_stock)

                bundle_document = str(url_soup.find_all("input", id="bundleBase"))

                # Handle Black Friday Bunduru               
                if bundle_document != "[]":

                    

                    bundleInformation = str(url_soup.find_all("div", id="zoneBundle"))
                    if bundleInformation.__contains__("div class=\"row\" id=\"zoneBundle\""):

                        bundleItemTitle = []
                        bundleItemPrice = []
                        bundleItemStock = []

                        bundle_Data = bundleInformation.split("</li>")
                        for item in bundle_Data:
                            item = item.splitlines()

                            tmpStock = ""
                            tmpPrice = ""
                            tmpTitle = ""
                            
                            for subItem in item:      
                                tmpVal = True                        
                                if(subItem.__contains__("1 x ") or subItem.__contains__("3 x ")): 
                                    if subItem.__contains__("EDFC Motors Kit"):
                                        tmpTitlePriceStock = scrapeFuncs.remove_html_markup(subItem)
                                        tmpTitle = tmpTitlePriceStock.split("+€")[0].replace("1 x ","")

                                        tmpPriceStock = tmpTitlePriceStock.split("+€")[1]
                                        tmpPrice = tmpPriceStock.split(" ", 1)[0]
                                        tmpStock = checkStockLevels(tmpPriceStock)
                                        bundleItemTitle.append(tmpTitle)
                                        bundleItemPrice.append(tmpPrice)
                                        bundleItemStock.append(tmpStock)
                                        tmpVal = False

                                    elif subItem.__contains__("<option"):
                                        tmpTitlePriceStock = scrapeFuncs.remove_html_markup(subItem)
                                        tmpTitle = tmpTitlePriceStock.split("+€")[0].replace("1 x ","")

                                        tmpPriceStock = tmpTitlePriceStock.split("+€")[1]
                                        tmpPrice = tmpPriceStock.split(" ", 1)[0]
                                        tmpStock = checkStockLevels(tmpPriceStock)
                                        bundleItemTitle.append(tmpTitle)
                                        bundleItemPrice.append(tmpPrice)
                                        bundleItemStock.append(tmpStock)
                                        tmpVal = False                                    

                                    elif subItem.__contains__("+€"):
                                        tmpTitle = subItem.split("+€")[0].replace("1 x ","").replace("&amp;","&").replace("Your choice ","")
                                        tmpPrice = subItem.split("+€")[1]
                                        bundleItemTitle.append(tmpTitle)
                                        bundleItemPrice.append(tmpPrice)
                                    else:
                                        tmpTitle = subItem.replace("&amp;","&").replace("1 x ","").replace("Your choice ","")
                                        tmpPrice = "1.00"
                                        bundleItemTitle.append(tmpTitle)
                                        bundleItemPrice.append(tmpPrice)
                                
                                if subItem.__contains__("(<span class=\"") and "id=\"isRequiredError\"" not in subItem and "<option id=" not in subItem and tmpVal:
                                    tmpStock = checkStockLevels(subItem)
                                    bundleItemStock.append(tmpStock)
                    i = 0
                    while i < len(bundleItemTitle):
                        bundleTitleItems.append(bundleItemTitle[i])
                        bundlePriceItems.append(bundleItemPrice[i])
                        bundleStockItems.append(bundleItemStock[i])

                        bundleItemDescription = scrapeDescription(url_soup)
                        bundleItemNotes = scrapeNotes(url_soup)
                        bundleItemNotes = cleanBundleNotes(bundleItemNotes)

                        bundleDescriptionItems.append(bundleItemDescription)
                        bundleNotesItems.append(bundleItemNotes)
                        i+=1

                # Handle Singles
                if bundle_document == "[]":
                    
                    bundleTitleItems.append(scrapeTitle(url_soup))
                    bundleNotesItems.append(scrapeNotes(url_soup))
                    bundleDescriptionItems.append(scrapeDescription(url_soup))
                    bundlePriceItems.append(scrapePrice(url_soup))
                    bundleStockItems.append(scrapeStockLevels(url_soup))
               
    except UnicodeDecodeError:
        pass 
 
    print(str(len(bundleTitleItems)) + ": Title")
    print(str(len(bundlePriceItems)) + ": Price")
    print(str(len(bundleStockItems)) + ": Stock")
    print(str(len(bundleDescriptionItems)) + ": Description")
    print(str(len(bundleNotesItems)) + ": Notes")
  
    # Open new file and fill contents 
    supportFuncs.switchToProcessedPath(processed_html_directory)

    file_name = "driftshop_content.csv" 
  
    file = open(file_name, 'a+', encoding='utf-8', errors='ignore', newline='')   
    csvwriter = csv.writer(file) 

    header = ['product_name', 'price', 'item_type', 'description', 'misc_notes', 'in_stock', 'supplier'] 
    csvwriter.writerow(header)
    j = 0
    while( j < len(bundleTitleItems)):
        csvwriter.writerow([bundleTitleItems[j], bundlePriceItems[j], '', bundleDescriptionItems[j], bundleNotesItems[j], bundleStockItems[j], clean_product_supplier])
        j+=1
        
    file.close()  
    
# scrape helpers
def scrapeTitle(soup):
    #title
    dirty_product_title = str(soup.find_all("h1", itemprop="name"))                    
    clean_product_title = cleanTitle(dirty_product_title)
    return clean_product_title

def scrapePrice(soup):
    #price
    dirty_product_price = str(soup.find_all("meta", itemprop="price"))                          
    clean_product_price = cleanPrice(dirty_product_price)
    return clean_product_price

def scrapeStockLevels(soup):
    #price
    dirty_product_stock = str(soup.find_all("div", itemprop="blockStock col-12 mt-2 pl-3 pr-3 text-left"))                          
    clean_product_stock = checkStockLevels(dirty_product_stock)
    return clean_product_stock

def scrapeNotes(soup):
    #notes
    dirty_product_notes = str(soup.find_all("div", class_="shortdescription"))
    clean_product_notes = cleanNotes(dirty_product_notes)
    return clean_product_notes

def scrapeDescription(soup):
    #description
    dirty_product_description = str(soup.find_all("div", class_="longdescription")).replace("Important Note","")
    clean_product_description = cleanDescription(dirty_product_description)
    return clean_product_description

# cleaner helpers
def cleanTitle(text): 
    text = scrapeFuncs.remove_html_markup(text)
    text = text.replace("[","").replace("]","").replace("&amp;","&").strip()
    if text.__contains__('Oil Filter'):
        text = text.split('|', 1)[0]
        return text
    else:
        return text

def cleanNotes(text): 
    text = scrapeFuncs.remove_html_markup(text)
    text = text.replace("[","").replace("]","").replace("&amp;","&").strip()
    return text

def cleanDescription(text): 
    text = scrapeFuncs.remove_html_markup(text)
    text = text.replace("[","").replace("]","").replace("&amp;","&").strip()
    return text

def cleanPrice(text): 
    text = text.replace("[<meta content=\"","").replace("\" itemprop=\"price\"/>]","").strip()
    return text

# bundle cleaner helpers
def cleanBundleTitle(text): 
    text = scrapeFuncs.remove_html_markup(text)
    text = text.replace("[","").replace("]","").replace("&amp;","&").replace("1 x ","").replace(",","").lstrip().rstrip()
    return text

# alloy files cleaner helpers
def cleanAlloyNotes(text): 
    text = scrapeFuncs.remove_html_markup(text)
    text = text.replace("Sold individually, select required amount in the cart","").replace("\"","")
    text = text.replace("Free shipping across Europe!","").replace("Japan Racing JR-11 ","").strip()   
    text = re.sub(r"(\w)([A-Z])", r"\1 \2", text)
    return text

def cleanBundleNotes(text): 
    text = text.replace("Japanese quality !","")  
    text = re.sub(r'([a-z](?=[A-Z])|[A-Z](?=[A-Z][a-z]))', r'\1 ', text)
    return text

# helper functions
def checkStockLevels(text):
    if text.__contains__("Dispatched"):
        return "Preorder Only"        
    elif text.__contains__("in stock"):
        return "In Stock"
    else:
        return "Not In Stock"

def checkForBadData(text): 
    if text.__contains__('#NAME'):
        return "No notes available"
    elif text.__contains__(''):
        return "No notes available"
    else:
        return text
 
if __name__=="__main__":
	main()