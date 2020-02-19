import requests
from bs4 import BeautifulSoup
import xlwt 
from xlwt import Workbook 
import urllib.parse

workbook = xlwt.Workbook()  
  
sheet = workbook.add_sheet("Sheet Name") 
  
# Specifying style 
style = xlwt.easyxf('font: bold 1') 
sheet.write(0, 0, 'Role', style)
sheet.write(0, 1, 'Company', style)
sheet.write(0, 2, 'Summary', style)
sheet.write(0, 3, 'Link', style)

findJobsByLocation(sys.argv[1],sys.argv[2])

def findJobsByLocation(location,count):

    location=urllib.parse.quote_plus(location)

    for i in range(0,count,10):
        URL = 'https://www.indeed.com/jobs?q=software+engineer+&l='+location+'&sort=date&start='+i
        page = requests.get(URL)

        soup = BeautifulSoup(page.content, 'html.parser') 
        results = soup.find(id='resultsCol')

        all_jobs = results.find_all('div', class_='jobsearch-SerpJobCard')
        i=1
        for each_job in all_jobs:
            title=each_job.find('div',class_='title')
            company=each_job.find('span',class_='company')
            summary=each_job.find('div',class_='summary')
            if None in (title,company,summary):continue
            sheet.write(i,0,title.text)
            sheet.write(i,1,company.text)
            sheet.write(i,2,summary.text)
            sheet.write(i,3,'https://www.indeed.com'+title.find('a')['href'])
            i+=1


    workbook.save('Jobs.xls')


    
   # urllib.parse.quote_plus
#print(all_jobs[0].text)
#print(each_job)


