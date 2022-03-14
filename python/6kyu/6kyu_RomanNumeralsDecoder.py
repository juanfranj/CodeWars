def solution(roman):
    
    n_romano=['I','V','X','L','C','D','M']
    n_arabigo=[1,5,10,50,100,500,1000]
    dato=list(roman)
    conversion=[]
    for i in range(0, len(dato)):  
      for n in range(0,len(n_romano)):
        if n_romano[n]==dato[i]:  
          conversion.append(n_arabigo[n])  
    for i in range(0,len(conversion)):
      for j in range(1,len(conversion)):
        if j-i==1:    
          if conversion[j]>conversion[i]: 
            conversion[i]=conversion[i]*-1 
    suma=0     
    for i in conversion:
      suma=suma+i
      
    return suma