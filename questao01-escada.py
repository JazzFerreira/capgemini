# Função

def escada(n):
  for i in range(1, n+1):
    print(" " * (n - i) + "*" * i )

# Teste

print(escada(6))