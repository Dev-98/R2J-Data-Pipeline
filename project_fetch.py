import requests
from bs4 import BeautifulSoup

def scrape_internshala_jobs(url):
    
    # Fetching the number of pages to scrape
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    num_pages = int(soup.find('span', id='total_pages').text) + 1
    
    # Extracting job details
    links_job = []

    for num in range(1,num_pages):
        print("page-",num)
        url_page = f'{url}/page-{num}/'
        response = requests.get(url_page)
        soup = BeautifulSoup(response.content, 'html.parser')
        job_cards = soup.find_all('div', class_='button_container_card')

        for links in job_cards:
            links_job.append('https://internshala.com' + links.find("a",class_ = 'btn btn-secondary view_detail_button_outline')['href'])

    return links_job

if __name__ == '__main__':
    url = f'https://internshala.com/internships/work-from-home-data-analysis,data-science,machine-learning,web-development-internship'
    links = scrape_internshala_jobs(url)
