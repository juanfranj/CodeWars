def domain_name(url):
    text = ''
    indice = buscar_indice(url)
    if indice >= 0:
        for i in url[indice::]:
            if '.' not in i:
                text += i
            else:
                break
    return text
def buscar_indice(url):
    indice = 0
    if '://' in url:
        indice = url.index('://')+3
    if  'www.' in url:
        indice = url.index('www.')+4
    return indice
if __name__ == '__main__':
    url = 'https://www.codewars.com/kata/514a024011ea4fb54200004b/solutions/python'
    text = domain_name(url)
    print(text)
    print(url.split('//')[-1].split("www.")[-1].split('.')[0])

'''
def domain_name(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]

import re
def domain_name(url):
    return re.search('(https?://)?(www\d?\.)?(?P<name>[\w-]+)\.', url).group('name')   
'''