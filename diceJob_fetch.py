import requests
from bs4 import BeautifulSoup

def scrape_dice_job_links(url):
    
    # Fetching the number of pages to scrape
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
    try:
        response = requests.get(url,headers=header)
        soup = BeautifulSoup(response.content, 'html.parser')
        print(soup)
    except Exception as e:
        print("Error : ", str(e))
        
    # Extracting job details
    links_job = []

    job_id = soup.find_all('div', class_='overflow-hidden')

    print(job_id[:5])
    # for links in job_id:
    #     links_job.append('https://dice.com/job-details/' + links.get('id'))

    # return links_job



url = f'https://www.dice.com/jobs?q=machine%20learning%20engineer&location=Remote,%20OR%2097458,%20USA&latitude=43.00594549999999&longitude=-123.8925908&countryCode=US&locationPrecision=City&radius=30&radiusUnit=mi&page=1&pageSize=20&filters.postedDate=SEVEN&language=en&eid=0904'

scrape_dice_job_links(url)
