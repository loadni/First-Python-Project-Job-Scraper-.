from bs4 import BeautifulSoup
import requests


def extract_remoteok_jobs(term):
  locations = []
  remoteok = []
  url = f"https://remoteok.com/remote-{term}-jobs"
  request = requests.get(url, headers={"User-Agent": "Kimchi"})
  if request.status_code == 200:
    soup = BeautifulSoup(request.text, "html.parser")
    jobs = soup.find_all('tr', 'job')
    for job in jobs:
      link = job['data-url']
      companyname = job.find_all('h3', itemprop="name")
      companyname = companyname[0].string
      title = job.find_all('h2', itemprop="title")
      title = title[0].string
      location = job.find_all('div', class_='location')
      #money = location[-1].string  #시간정보를 찾을 수 없어서 급여정보를 저장했습니다.
      location.pop(-1)
      for count in range(len(location)):
        locations.append(location[count].string)
      job_data = {
        'position': title,  #제목
        'company': companyname,  #회사 이름
        'location': locations,  #근무 지역
        #'money': money.replace(","," "),  #급여
        'link': link  #게시물 링크
      }
      remoteok.append(job_data)
      locations = []
    # write your ✨magical✨ code here
    return remoteok
  else:
    print("Can't get jobs.")
