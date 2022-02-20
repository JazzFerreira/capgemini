# Palavras exemplo

a1 = 'ovo'
a2 = 'ifailuhkqq'

#Função

n = len(a1)
res = 0

for i in range(1,n):
    d={}
    for j in range(n-i+1):
        subs = ''.join(sorted(a1[j:j+i]))
        if subs not in d:
            d[subs]=1
        else:
            d[subs]+=1
        
        res +=d[subs]-1
        
print(res)