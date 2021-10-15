listanum = []
insert = 0
reiniciar = 0
print("Incluir números na lista \nPara finalizar digite: stop \n")
while insert != 'stop':
    insert = input('Insira um valor númerico: ')
    if insert != 'stop':
        insert = int(insert)
    if insert != 'stop':
        for p, v in enumerate(listanum):
            if v == insert:
                reiniciar = 1
                print(f"Já existe o número {insert} na posição {p}")
        if reiniciar == 1:
            reiniciar = 0
        else:
            listanum.append(insert)

print('você finalizou')
print(f'foram inclusos {len(listanum)} número em sua lista')
listanum.sort()
print(f'aqui está sua lista em ordem crescente {listanum}')
listanum.sort(reverse=True)
print(f'aqui está sua lista em ordem decrescente {listanum}')

if 5 in listanum:
    print("O valor \"5\" faz parte da lista")
else:
    print('Não temos o valor \"5\" na lista')
