import uuid
import os
from bs4 import BeautifulSoup
from requests import get

try:
    import GT86WebScraping.Extensions.ExceptionsEx as exceptionsEx
    import GT86WebScraping.Extensions.SupportFunctionsEx as supportFuncs
except ModuleNotFoundError:
    os.getcwd()

def main():

# Global Variables
 
    user_agent_headers = {"User-Agent":"Mozilla/5.0"}
    clean_product_supplier = "TorqueGT"
    raw_html_directory = r'GT86WebScraping\\HTML\\RawHTML\\' + clean_product_supplier
    
# Check that files are being outputted to the correct directory

    try:
        supportFuncs.getCurrentPath()
        supportFuncs.createDirectoryIfNotExists(raw_html_directory)
        supportFuncs.switchToRawPath(raw_html_directory)
    except FileNotFoundError:
        raise exceptionsEx.FilePathNotCorrectException(raw_html_directory)

# Web Scrape
        
    page_header = 'https://www.torque-gt.co.uk/'
    page_stem = '/jdm-parts/select-car/toyota/gt86.html'

    page_url = page_header + page_stem

    response = get(page_url, headers = user_agent_headers)
        
    if response.status_code == 200:
        parent_url_soup = BeautifulSoup(response.text, 'html.parser')
            
        for child in parent_url_soup.find_all('a', href = True):
            if str(child).__contains__("https://www.torque-gt.co.uk/jdm-parts/select-car/toyota/gt86/"):
            
# Open new file and fill contents
                

                child_response = get(child['href'], headers = user_agent_headers)
                child_url_soup = BeautifulSoup(child_response.text, 'html.parser')
                
                
                items = str(child_url_soup.find_all("a", class_="product-item-link"))
                items_soup = BeautifulSoup(items, 'html.parser')
                for child_item in items_soup.find_all('a', href = True):
                    print(child_item['href'])
                    item_response = get(child_item['href'], headers = user_agent_headers)
                    item_url_soup = BeautifulSoup(item_response.text, 'html.parser')
                    
                    newGuid = str(uuid.uuid4())
                    file_name = "content_" + newGuid + ".html"      
                    print(file_name)
                    
                    f = open(
                    file_name, 
                    "w", 
                    encoding = "utf-8")

                    f.write(str(item_url_soup))
                    f.close()
                    
    else:
        raise exceptionsEx.HTTPFaultException(response.status_code)

    if 'Access Denied' in parent_url_soup:
        raise exceptionsEx.HTTPAccessDeniedException(response.status_code)
if __name__=="__main__":
	main()