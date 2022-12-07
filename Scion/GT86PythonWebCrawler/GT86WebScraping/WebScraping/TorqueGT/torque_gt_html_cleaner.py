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
                dirty_product_title = str(soup.find_all("img", class="alt"))
                print(dirty_product_title)
                #clean_product_title = cleanTitle(dirty_product_title)
                '''
                #price
                dirty_product_price = str(soup.find_all("meta", property="og:price:amount"))
                clean_product_price = cleanPrice(dirty_product_price)

                #stock
                clean_product_in_stock = "Preorder Only" 

                #notes
                clean_product_notes = cleanNotes(clean_product_title)

                #description
                dirty_product_description = str(soup.find_all("meta", property="og:description"))
                clean_product_description = cleanDescription(dirty_product_description)
                if dirty_product_description.__contains__("[]"):
                    clean_product_description = clean_product_title

                # Add Item as it is parsed to list      
                rows.append([clean_product_title, clean_product_price, '', clean_product_description, clean_product_notes, clean_product_in_stock, clean_product_supplier])
                tmpFile.close()
                os.remove(path)
                  '''  
    except UnicodeDecodeError:
        pass  
    '''
    # Open new file and fill contents 
    supportFuncs.switchToProcessedPath(processed_html_directory)

    file_name = "groupd_content.csv" 
  
    file = open(file_name,'a+', encoding='latin1', errors='ignore', newline='')   
    csvwriter = csv.writer(file) 

    header = ['product_name', 'price', 'item_type', 'description', 'misc_notes', 'in_stock', 'supplier'] 
    csvwriter.writerow(header)
   
    for row in rows:
        csvwriter.writerow(row)
        
    file.close()  
    '''
def cleanTitle(text): 
    text = text.replace("[<meta content=\"","").replace("\" property=\"og:title\"/>]","").strip()  
    text = text.replace("&amp;","&")
    return text

def cleanPrice(text): 
    text = text.replace("[<meta content=\"","").replace("\" property=\"og:price:amount\"/>]","").strip()   
    text = text.replace("&amp;","&")
    return text

def cleanDescription(text): 
    text = text.replace("[<meta content=\"","").replace("\" property=\"og:description\"/>]","").strip()   
    text = text.replace("&amp;","&")
    return text

def cleanNotes(text): 
    if text.__contains__("ASNU Top Feed FA20"):
        return "Material: Acetal OR Stainless Steel --- Size In CC: 300-1000"
    elif text.__contains__("KAAZ 2 Way Super Q LSD GT86/BRZ"):
        return "Super Q: Yes OR No"
    elif text.__contains__("Toyota GT86 Zn6 (12+) RM Series"):
        return "Spring Rates: 6/4kg.mm OR 6/6kg.mm /OR 8/8kg.mm"
    elif text.__contains__("Toyota GT86 Zn6 (12+) BR Series"):
        return "Spring Rates: 6/4kg.mm OR 5/5kg.mm /OR 8/8kg.mm OR 8/8kg.mm Extra Low OR 18/20kg.mm OR 10/8kg.mm OR 20/20kg.mm OR 8/6kg.mm OR 20/20kg.mm Extra Low OR 16/16kg.mm Extra Low OR 5/6kg.mm OR 10/9kg.mm"
    elif text.__contains__("Toyota GT86 Zn6 (12+) ER Series"):
        return "Spring Rates: 6/4kg.mm OR 8/6kg.mm Race Damping /OR 8/6kg.mm OR 10/8kg.mm OR 5/6kg.mm OR 10/8kg.mm Race Damping OR 7/8kg.mm OR 8/8kg.mm OR 10/6kg.mm"
    elif text.__contains__("Toyota GT86 Zn6 (12+) ZR Series"):
        return "Spring Rates: 6/4kg.mm OR 10/10kg.mm /OR 8/8kg.mm OR 10/8kg.mm OR 10/8kg.mm OR 5/6kg.mm"
    else:
        return "No notes available"
 
if __name__=="__main__":
	main()