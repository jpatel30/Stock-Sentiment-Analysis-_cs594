import urllib2

#with open("company.txt") as f:
#    content = f.read().splitlines()
#    print content

fileOpen = open('company.txt')
## Read the first line 
line = fileOpen.readline()


while line:
    print line.rstrip()
    target = open(line.rstrip()+'.json', 'a')
    companyName = 'https://api.stocktwits.com/api/2/streams/symbol/'+line.rstrip()+'.json'
    print companyName
    response = urllib2.urlopen(companyName)
    html = response.read()
    target.write('\n'+html)
    line = fileOpen.readline()
    target.close()

fileOpen.close()

