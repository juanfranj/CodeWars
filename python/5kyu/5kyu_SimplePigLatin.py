
def pig_it(text):
    text = text.split(" ")
    print(text)
    for i in range(len(text)):
        #if text[i] not in '/[¿!¡;,:\.\?#@()"]/':
        if text[i].isalpha():
            text[i] = text[i][1:len(text[i])]+text[i][0]+'ay'
    text = " ".join(text)
    return text

if __name__ == '__main__':
    text = "Hello world !"
    text = pig_it(text)
    print(text)