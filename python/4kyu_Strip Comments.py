"""
Complete the solution so that it strips all text that follows any of a set ofç
comment markers passed in. Any whitespace at the end of the line should also
be stripped out.

Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples
The output expected would be:

apples, pears
grapes
bananas
The code would be called like so:

result = solution("apples, pears # and bananas\ngrapes\nbananas !apples",
["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"
"""
# Best code
"""
def solution(string,markers):
    parts = string.split('\n')
    for s in markers:
        parts = [v.split(s)[0].rstrip() for v in parts]
    return '\n'.join(parts)
"""
# My code


def solution(string, markers):
    solucion = []
    if len(markers) == 0:
        return string
    for i in range(len(markers)):
        temporal = ""
        fin = False
        j = 0
        while not fin:
            if len(string) == 0:
                return ""
            if string[j] != markers[i]:
                temporal += string[j]
                j += 1
            else:
                if string[j-1] == " ":
                    temporal = temporal[0:-1]
                while string[j] != "\n":
                    j += 1
                    if j == len(string):
                        break
            if j == len(string):
                fin = True
        string = temporal
        solucion.append(temporal)
    solucionFinal = solucion[-1]
    if solucionFinal[-1] == " ":
        return solucionFinal[0:-2]
    else:
        return solucionFinal
