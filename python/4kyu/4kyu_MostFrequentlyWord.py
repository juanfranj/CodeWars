import re

def top_3_words(text):

    #text =[i.lower() for i in re.split(r"[^'a-zA-Z0-9]+|'{1,}\s", text) if len(i) != 0]
    text =[i.lower() for i in re.split(r"[^'a-zA-Z0-9]+|'{1,}\s", text) if len(i) != 0]
    print(text)
    dic = diccionario(text)
    sol = calcular_top(dic)
    print(dic)
    return sol
def diccionario(arr):
    dic = {}
    for key in arr:
        if key not in dic.keys():
            dic[key] = 1
        else:
            dic[key] += 1
    return dic
def tam_sol(top):
    if len(top) >= 3:
        sol = [None for i in range(3)]
    else:
        sol = [None for i in range(len(top))]
    return sol

def calcular_top(dic):
    top = sorted(dic.values(), reverse = True)
    sol = tam_sol(top)
    cont = 0
    print(top)
    while cont < len(sol):
        for key, value in dic.items():
            if cont == len(sol):
                continue
            if value == top[cont]:
                sol[cont] = key
                cont += 1
    return sol
if __name__ == '__main__':
    text = "Ksqnt;/,?BXWXfHPKnX  !FewD  'JsEU.?'JsEU,.!-,'JsEU:BXWXfHPKnX;-/ :FewD,?-JQWJGgDW'-_-;.nMB_. .-BXWXfHPKnX//../BXWXfHPKnX!?_?/ygDc?;;sCg Ksqnt? : 'JsEU;.FewD?;nMB..'JsEU--/sCg/;?/!ytyN_;-x'd?_JQWJGgDW';__JQWJGgDW'/:-:!BXWXfHPKnX/JQWJGgDW'!_ytyN-Ksqnt?/;!sCg/!!AqwAfVoCx!/??Ksqnt!_/x'd;:,--BXWXfHPKnX;_Ksqnt;.BXWXfHPKnX?nMB- ?ytyN:;?x'd:,.BXWXfHPKnX?//FewD!?,ygDc;x'd;??DYtJ'gp;. ;nMB?.:ygDc / ,.ytyN /?ygDc?,?ytyN;;,:-FewD:..sCg!'JsEU-,-JQWJGgDW';?:,ytyN!_!Ksqnt.!!_.FewD; ,JQWJGgDW'?.-ytyN !'JsEU!-:!?JQWJGgDW'-/__:sCg,:__:'JsEU/??ygDc:__/:ytyN_,sCg_x'd-/Ksqnt!/, !x'd;;:.nMB-:_BXWXfHPKnX,.ytyN/ytyN::Ksqnt :;_ygDc/!ygDc,!/!'JsEU_-/:'JsEU?;/ nMB-sCg?,? _x'd x'd-!,?.JQWJGgDW'/.nMB_;; ?nMB_JQWJGgDW'?'JsEU: _ygDc-/-;BXWXfHPKnX.!_,BXWXfHPKnX- JQWJGgDW'-_,?ygDc/!/ygDc!!!BXWXfHPKnX.,/-ygDc ,/!x'd  'JsEU?.x'd?/ygDc/-?x'd?_.sCg::?;ygDc/:-.FewD:FewD;:__nMB.;/ x'd-/ !'JsEU . /_ygDc! ;;;'JsEU_:ygDc-x'd/_?nMB-,-nMB.;,/ JQWJGgDW'-/?;?ytyN;?:!ygDc, ,FewD/sCg!!BXWXfHPKnX.-BXWXfHPKnX:;:.?sCg;/:: JQWJGgDW'-,-,ygDc!UPXF!/_.?ytyN.,/;sCg- / ygDc-/.x'd: ;FewD_ -.FewD/;?;sCg?/-BXWXfHPKnX?!.x'd;/;_!FewD!,::sCg,,sCg.nMB?//, ygDc_,sCg;?;UPXF,JQWJGgDW':!FewD;!?.?ygDc _,,nMB:?UPXF,_ygDc:;,nMB,.BXWXfHPKnX_,,;_sCg!.x'd:-x'd -/ytyN-_?/;sCg! ::;x'd._ ytyN ! ,.BXWXfHPKnX;_!/nMB;.,/ytyN-/!,?GzzbxSFZod Ksqnt-;,-x'd,-,/nMB.- ?BXWXfHPKnX:!,_,JQWJGgDW':?JQWJGgDW';!'JsEU-/JQWJGgDW'?-'JsEU!?JQWJGgDW',?!ygDc/-,FewD.._- FewD!?_,?sCg;_/BXWXfHPKnX ,-,-JQWJGgDW'_::;,'JsEU_.ygDc:?;Ksqnt!/,sCg ;Ksqnt,nMB.'JsEU?  /_BXWXfHPKnX_: x'd,?._JQWJGgDW'-_.'JsEU?./Ksqnt.!!: JQWJGgDW'/_FewD/_;:sCg.?:nMB??ytyN! .:;'JsEU/nMB-,ygDc .-JQWJGgDW'.;.--FewD?FewD-ytyN_/?!DYtJ'gp/ JQWJGgDW' _!;,x'd!.,//ygDc;?"
    sol = top_3_words(text)
    print(sol)

'''
import re
from collections import Counter

top_3_words=lambda t:[w for w,c in Counter(re.findall("'*[a-z][a-z']*",t.lower())).most_common(3)]
'''
