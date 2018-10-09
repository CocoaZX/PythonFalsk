import requests,bs4

exampleFile = open('example.html')#读取本地目录下这个html文件
exampleSoup = bs4.BeautifulSoup(exampleFile,features="html.parser")#读取此文件
# print(type(exampleSoup))
pElems = exampleSoup.select('p')#搜索所有p元素
print(pElems[0].getText)
print(pElems[1].getText)
