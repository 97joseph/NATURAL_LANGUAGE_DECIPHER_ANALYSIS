#urllib will help crawl the webpage
import urllib.request
response =  urllib.request.urlopen('https://en.wikipedia.org/wiki/SpaceX')
html = response.read()
print(html)

#use beautiful soup for pulling data out of thr HTML and XML File
#Use beautiful soup to clean our webpage text of HTML tags
from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'html5lib')
text = soup.get_text(strip = True)
print(text)

#Token conversion
tokens = [t for t in text.split()]
print(tokens)

#Count word frequency
#Stopwords include (a,at,the ,for and etc)
from nltk.corpus import stopwords
sr= stopwords.words('english')
clean_tokens = tokens[:]
for token in tokens:
    if token in stopwords.words('english'):
        
        clean_tokens.remove(token)
freq = nltk.FreqDist(clean_tokens)
for key,val in freq.items():
    print(str(key) + ':' + str(val))
freq.plot(20, cumulative=False)