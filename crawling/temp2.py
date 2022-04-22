from bs4 import BeautifulSoup
soup = BeautifulSoup(open("index2.html"), 'html.parser')

print(soup.title)
print("----------------")
print(soup.title.name)
print("----------------")
print(soup.title.string)
print("----------------")
print(soup.title.parent.name)
print("----------------")
print(soup.p)
print("----------------")
print(soup.p['class'])
print("----------------")
print(soup.a)
print("----------------")
print(soup.find_all('a'))
print("----------------")
print(soup.find(id="link3"))
