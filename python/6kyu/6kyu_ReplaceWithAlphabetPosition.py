def alphabet_position(text):
    return " ".join([str(ord(i)-96) for i in text.lower() if i.isalpha()])
    

if __name__ == '__main__':
    s = "The sunset sets at twelve o' clock."
    print(alphabet_position(s))
