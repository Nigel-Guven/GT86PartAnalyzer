#do cleaning here
import os
import sys
import csv

from bs4 import BeautifulSoup
os.getcwd()

try:
    import GT86WebScraping.Extensions.ExceptionsEx as exceptions
    import GT86WebScraping.Extensions.SupportFunctionsEx as supportFuncs
except ModuleNotFoundError:
    os.getcwd()

def main():

    # global vars
    clean_product_supplier = "TRCTuning"
    rows = []
    raw_html_directory = r'HTML\\RawHTML\\' + clean_product_supplier
    processed_html_directory = r'HTML\\ProcessedHTML'
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
                print(soup)
                '''
                #title
                dirty_product_title = str(soup.find_all("meta", property="og:title"))
                clean_product_title = cleanTitle(dirty_product_title)

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
    
if __name__=="__main__":
	main()