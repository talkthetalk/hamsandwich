'''
Created on Jul 22, 2014

@author: Joseph.Higgins
'''
import re
import io
from bs4 import BeautifulSoup


outputHTML = '''
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/1999/REC-html401-19991224/strict.dtd">
    <html>
    <head>
    <META http-equiv=Content-Type content="text/html; charset=UTF-8">
    <title>Ham Sandwich direct creation</title>
    </head>
    <body>
        <div style="float: left; white-space: pre; line-height: 1; background: #999999; "></div>
        <p>\n
'''



html = io.open('clean emoji table.html','r',encoding='utf-8')
soup = BeautifulSoup(html)

unicode = soup.find_all('td','code',text=re.compile('U+'))
bytCode = soup.find_all('td','code',text=re.compile('x'))
descrip = soup.find_all('td','name')


for code,byte,name in zip(unicode, bytCode, descrip):
    #print(code.text +", "+byte.text+", "+ name.text+", "+"#x"+code.text.replace('U+','&#x'))
    outputHTML += "\t\t\t"+code.text.replace('U+','&#x')+"; "+name.text+"<br>\n"
    


outputHTML += '''
    </p>
    </p>
</body>
</html>
'''

Html_file= open("C:\\Users\\joseph.higgins\\Desktop\\gitRepos\\hamsandwich\\index.html","w")
Html_file.write(outputHTML)
Html_file.close()


    
print("did this make it into the repo?")
