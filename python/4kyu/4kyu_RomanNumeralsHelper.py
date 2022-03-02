class RomanNumerals:
        
    def to_roman(val):
        desc = descomposicion(val)
        #print(desc)
        return traduccion(desc)

    def from_roman(roman_num):
        dic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        num = [dic[i] for i in roman_num]
        num.append(-1)
        cont = 0
        sol = 0
        while num[cont] > 0:
            if num[cont] >= num[cont+1]:
                sol += num[cont]
                cont += 1
            else:
                sol += num[cont+1] - num[cont]
                cont += 2
            
        #print(num)
        return sol
    
def descomposicion(val):
    millares = val // 1000
    centenas = val // 100 - millares * 10
    decenas = val // 10 - (val//100) * 10
    unidades = val % 10
    return [millares, centenas, decenas, unidades]

def traduccion(desc):
    trad = [
            ['M', 'MM', 'MMM'],
            ['C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
            ['X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
            ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
            ]
    text = ''
    for i in range(len(desc)):
        if desc[i] != 0:
            text += trad[i][desc[i]-1]            
    return text
   


if __name__ == '__main__':
    val = 3999
    rom = 'MDCLXVI'
    numRom = RomanNumerals.to_roman(val)
    numAra = RomanNumerals.from_roman(rom)
    print(numAra)

    '''
    import string
from collections import OrderedDict

class RomanNumerals:
  @classmethod
  def to_roman(self, num):
    conversions = OrderedDict([('M',1000), ('CM',900), ('D', 500), ('CD',400), ('C',100), ('XC',90), ('L',50), ('XL',40),
                               ('X',10), ('IX',9), ('V',5), ('IV',4), ('I',1)])
    out = ''
    for key, value in conversions.iteritems():
      while num >= value:
        out += key
        num -= value
    return out
  
  @classmethod
  def from_roman(self, roman):
    conversions = OrderedDict([('CM',900), ('CD',400), ('XC',90), ('XL',40), ('IX',9), ('IV',4), ('M',1000), ('D',500),
                               ('C',100), ('L',50), ('X',10), ('V',5), ('I',1)])
    out = 0
    for key, value in conversions.iteritems():
      out += value * roman.count(key)
      roman = string.replace(roman, key, "")
    return out
    '''