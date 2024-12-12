import requests
from bs4 import BeautifulSoup

def download_url_and_get_all_hrefs(url):
    """
    Funkce stahne url predanou v parametru url pomoci volani response = requests.get(),
    zkontroluje navratovy kod response.status_code, ktery musi byt 200,
    pokud ano, najdete ve stazenem obsahu stranky response.content vsechny vyskyty
    <a href="url">odkaz</a> a z nich nactete url, ktere vratite jako seznam pomoci return
    """
    hrefs = [] 
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'lxml')
            for ahref in soup.find_all('a', href=True):
                hrefs.append(ahref['href'])
    except Exception as e:
        print(f"Eror u URL: {e}")
    
    return hrefs

if __name__ == "__main__":
    try:
        # url = sys.argv[1]
        # hrefs = download_url_and_get_all_hrefs(url)
        
        hrefs = download_url_and_get_all_hrefs('https://www.jcu.cz')
        print(hrefs)
    except Exception as e:
        print(f"Error na konci: {e}")