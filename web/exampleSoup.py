import bs4

exampleFile = open('C:/Users/Admin/Desktop/programs/web/example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read())
elems = exampleSoup.select('#author')
type(elems)
