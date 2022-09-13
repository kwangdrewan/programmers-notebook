from bs4 import BeautifulSoup as bs

with open('reddit.html', 'r') as html_file:
    content = html_file.read()

    soup = bs(content, 'lxml')
    tags = soup.find_all(class_="title may-blank")
    for title in tags:
        print(title.text)
