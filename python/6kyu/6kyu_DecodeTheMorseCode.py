def decodeMorse(morse_code):
    MORSE_CODE = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-','SOS':'...---...',
                    '!':'-.-.--'}
    codigoHumano=morse_code.split(" ")
    for i in range(10):
        if codigoHumano[-i]=="": codigoHumano.pop()
        else: break
    mensaje=""
    j=""
    for i in codigoHumano:
        if i!="":
            for letra, codigo in MORSE_CODE.items():
                if codigo==i: mensaje+=letra
                j=i
        else: 
            if j!="": 
                mensaje+=" "
                j=""
    return mensaje