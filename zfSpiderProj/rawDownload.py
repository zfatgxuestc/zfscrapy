import requests
url = 'https://arxiv.org/pdf/2006.14492'
r = requests.get(url)
with open('xxx.pdf','wb') as  f:
    f.write(r.content)