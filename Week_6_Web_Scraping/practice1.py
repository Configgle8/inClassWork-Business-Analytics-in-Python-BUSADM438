from bs4 import BeautifulSoup
names = []
html = []
with open('The Dormouses story.html', 'r') as f:
    html = f.read()
    soup = (BeautifulSoup(html, 'html.parser'))
    links = []
    for tag in soup.find_all('a', class_ = 'sister'):
        links.append(tag['href'])
        names.append(tag.text)
print(names)
print(links)