def soma(x, y, z): #def = definição de função
    # Definição
    print(f'{x=} y={y} {z=}', '|', 'x + y + z = ', x + y + z)

# 'soma' = nome da função. Dentro de parentese ()= execução de funções
soma(1, 2, 3) #argumento não nomeados ou argumentos posicionais
soma(x=3, y=1, z=2) #argumento nomeados
soma(1, y=2, z=5) #sempre que um argumentos está nomeado ex: y=2 o proximo tbem deve ser nomeado

print(1, 2, 3, sep='-')