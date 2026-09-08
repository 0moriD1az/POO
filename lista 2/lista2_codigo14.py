frase=input('digite uma frase: ')
palavras=frase.split()

dic={}

for pal in palavras:
    
    if pal in dic:
        dic[pal]+=1

    else:
        dic[pal]=1

for i in dic.items():

    print(i)
