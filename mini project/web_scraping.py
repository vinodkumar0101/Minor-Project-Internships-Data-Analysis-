import random
from bs4 import BeautifulSoup
from lxml import etree
import requests
import re
import pandas as pd
import socket


socket.getaddrinfo('localhost', 8080)
# Defining list of browsers
user_agent_list = ['Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) \
                        Gecko/20100101 Firefox/61.0',
                       'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
                        (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36',
                       'Mozilla/5.0 (X11; Linux x86_64; rv:61.0) \
                        Gecko/20100101 Firefox/61.0',
                       'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
                        AppleWebKit/537.36 (KHTML, like Gecko) \
                        Chrome/60.0.3112.113 Safari/537.36',
                       'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
                        AppleWebKit/537.36 (KHTML, like Gecko) \
                        Chrome/63.0.3239.132 Safari/537.36',
                       'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
                        AppleWebKit/537.36 (KHTML, like Gecko) \
                        Chrome/66.0.3359.117 Safari/537.36',
                       'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) \
                        AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 \
                        Safari/603.3.8',
                       'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) \
                        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 \
                        Safari/537.36',
                       'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) \
                        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 \
                        Safari/537.36']
def page_url(url):
    user_agent = random.choice(user_agent_list)
    header = {'User-Agent': user_agent}
    page = requests.get(url, headers=header)
    try:
        
                soup = BeautifulSoup(page.content, 'lxml')        
                pages=soup.find(id="total_pages").text
                # pages="5"
                url_list=["https://internshala.com/internships/page-"+str(i) for i in range(0,int(pages)+1)]
                return url_list
    except Exception as e:
                print(e)

def ind_intern(apply_link):
    user_agent = random.choice(user_agent_list)
    header = {'User-Agent': user_agent}
    Hiring_since=[]
    opportunities_posted=[]
    candidates_hired=[]
    Skills_required=[]
    no_of_applications=[]
    perks=[]
    Number_of_openings=[]
    website_link=[]
    duration=[]
    start_date=[]
    for url in apply_link:
        page = requests.get(url, headers=header)
        soup = BeautifulSoup(page.content, 'lxml')
        dom = etree.HTML(str(soup))
        du=[" ".join(i.split()) for i in dom.xpath('//*[@class="item_body"]/text()')]
        temp2=[j for j in du if j!="" and j!="Part time allowed"]
        if len(temp2)==3:
                        temp2=temp2[1:]
        duration+=[temp2[i] for i in range(0,len(temp2),2)]
        start_date+=[temp2[i] for i in range(1,len(temp2),2)]
        activity=[]
        for a in soup.find_all(class_="activity_container"):
            for b in a.find_all(class_ = "text body-main" ):
                activity.append(b.text)
            # print(len(activity))
            if len(a.find_all(class_ = "text body-main" ))==0:
                activity.append([None])
        
        if len(activity)==3:
            Hiring_since.append(activity[0].replace("Hiring since ",""))
            opportunities_posted.append(int(re.findall('\d+',activity[1])[0]))
            candidates_hired.append(int(re.findall('\d+',activity[2])[0]))
        elif len(activity)==2:
            Hiring_since.append(activity[0].replace("Hiring since ",""))
            opportunities_posted.append(int(re.findall('\d+',activity[1])[0]))
            candidates_hired.append(0)
        else:
            Hiring_since.append(None)
            opportunities_posted.append(0)
            candidates_hired.append(0)
        no_of_applications+=[i for i in dom.xpath('//*[@class="applications_message"]/text()')]
        Sr=[",".join([b.text for b in a.find_all(class_ = "round_tabs" )]) for a in soup.find_all(class_ = "round_tabs_container")]
        if not Sr:
            Skills_required.append(None)
            perks.append(None)
        elif len(Sr)==1:
            Skills_required.append(None)
            perks.append(Sr[0])
        else:
            Skills_required.append(Sr[0])
            perks.append(Sr[1])   
        
        Number_of_openings.append(int(soup.find_all(class_ = "text-container")[-1].text))
        w=[]
        for i in dom.xpath('//*[@class="text-container website_link"]/a/@href'):
            w.append(i)
        if len(w)==0:
            website_link.append(None)
        else:
            website_link+=w
   
    return Hiring_since,opportunities_posted,candidates_hired,no_of_applications,Skills_required,perks,Number_of_openings,website_link,duration,start_date

    
def parse(urls):
    user_agent = random.choice(user_agent_list)
    header = {'User-Agent': user_agent}
    df=pd.DataFrame(columns=['jobrole', 'company', 'location', 'duration', 'start_date', 'stipend','apply_link',
                             'Hiring_since','opportunities_posted','candidates_hired','no_of_applications',
                             'Skills_required','perks','Number_of_openings','website_link'])
    
    pno=1
    for url in urls:
        try:
                    page = requests.get(url, headers=header)
                    soup = BeautifulSoup(page.content, 'lxml')
                    dom = etree.HTML(str(soup))
                    jobrole=[i.text for i in dom.xpath('//*[@class="heading_4_5 profile"]/a')]
                    company=[' '.join(i.text.split()) for i in dom.xpath('//*[@class="heading_6 company_name"]/a')]
                    location=[",".join([b.text for b in a.find_all(class_ = "location_link" )]) for a in soup.find_all(id="location_names")]
                    
                    stipend=[]
                    for i in dom.xpath('//*[@class="stipend"]/text()'):
                        a=re.findall('\d+',i)
                        if a:
                            stipend.append(int(a[0]))
                        else:
                            stipend.append(0)
                    apply_link=["https://internshala.com/"+i for i in dom.xpath('//*[@class="heading_4_5 profile"]/a/@href')]
                    Hiring_since,opportunities_posted,candidates_hired,no_of_applications,Skills_required,perks,Number_of_openings,website_link,duration,start_date=ind_intern(apply_link)
                    # print(len(jobrole),len(company),len(location),len(duration),len(start_date),len(stipend),len(apply_link),len(Hiring_since),
                    #       len(opportunities_posted),len(candidates_hired),len(no_of_applications),len(Skills_required),len(perks),len(Number_of_openings),len(website_link))
                    
                    df2=pd.DataFrame({"jobrole":jobrole,"company":company,"location":location,"duration":duration,"start_date":start_date,
                          "stipend":stipend,"apply_link":apply_link,"Hiring_since":Hiring_since,"opportunities_posted":opportunities_posted,
                          "candidates_hired":candidates_hired,"no_of_applications":no_of_applications,"Skills_required":Skills_required,"perks":perks,
                          "Number_of_openings":Number_of_openings,'website_link':website_link})
                    df=df.append(df2)
                    print("page-"+str(pno)+" completed")
                    pno+=1
        except :
            print("error")
        
    return df

# Change this url to your search result
url='https://internshala.com/internships/'
urls=page_url(url)
df=parse(urls)
df.to_excel("output5.xlsx",index=False)
print("Finished scraping")