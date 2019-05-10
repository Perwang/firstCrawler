from bs4 import BeautifulSoup
'''
soup 会把不合规的html解析成合规的html
'''
breken_html='<ul class=country><li> Area <li>Population</ul>'
#parse the HTML
soup = BeautifulSoup(breken_html,'html.parser')
fixed_html=soup.prettify()
#print(fixed_html)

ul=soup.find('ul',attrs={'class':'country'})
#print(ul.find('li')) # returns just the first match

print(ul.find_all('li')) # returns all matches

