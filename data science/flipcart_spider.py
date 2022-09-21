from dputils import scrape
import pandas as pd

#step1:get the data as soup object
#step2:create the setup dictionaries
#step3:pass the dictionaries into the extract_many() function
#step4:repeat step1 to step 3 until data keep coming
#step5:check and save data into file


#understanding the url
#url='https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
#after?- url parameter 
#print(url.split('?')[-1].split('&'))

def getdata(q):
    #STEP1
    #STEP2:
    #target dict,items dict,etc
    t={'tag':'div','attrs':{'class':'_1YokD2 _3Mn1Gg'}}
    rep_items={'tag':'div','attrs':{'class':'_1AtVbE col-12-12'}}
    title={'tag':'div','attrs':{'class':'_4rR01T'}}
    price={'tag':'div','attrs':{'class':'_30jeq3 _1_WHN1'}}
    link={'tag':'a','attrs':{'class':'_1fQZEK'},'output':'href'}
    pos=1
    all_data=[]
    while True:
        url=f'https://www.flipkart.com/search?q=(query)&page={pos}'
        print(url)
        soup=scrape.get_webpage_data(url) #we use get_webpage_data to fools the website
         #STEP3:
        data=scrape.extract_many(soup,target=t,items=rep_items,title=title,price=price,link=link) #extract_many will extract all the items in page
        if isinstance(data,list):
            if len(data)>0:
                pos+=1
                all_data.extend(data)
            else:
                break
        else:
            break
    return all_data            
#use
laptops=getdata('laptops')
#from pprint import pprint(laptops)
pd.DataFrame(laptops).to_csv('laptop_data.csv')
