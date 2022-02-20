# Função

def verifica(n, senha):
    numeros = "0123456789"
    minusculas = "abcdefghijklmnopqrstuvwxyz"
    maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    especiais = "!@#$%^&*()-+"

    s = {'n','m','a','e'}
    c = set()

    for i in senha:
        if i in numeros:
            c.add('n')
        if i in minusculas:
            c.add('m')
        if i in maiusculas:
            c.add('a')
        if i in especiais:
            c.add('e')

    sf = len(s-c)

    if n < 6:
        sf += (6-n) - sf

    return sf

# Teste

s1 = 'Ya3'
s2 = 'Moon7!'

print(verifica(len(s1), s1))