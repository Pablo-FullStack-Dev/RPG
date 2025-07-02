# alguns atributos que o personagem principal pode ter:
#   MAGIA DE: 
#               .DESTRUIÇÃO
#               .INVOCAÇÃO
#               .VIDA
#               .ALTERAÇÃO
#               .ILUSÃO

mana = 100


feiticos = {
    'fogo_simples' : 25,
    'raio_simples' : 25,
    'terra_simples' : 25,
    'bola_fogo' : 50,
    'tiro_raio' : 50,
    'pedra_terra' : 50,
    'fogo_puro' : 100,
    'raio' : 100,
    'terra' : 100,
    'teste' : 5.000,
    }


   
while True:
    print(f'1.ver feitiços\n 2.Usar feitiços\n')
    escolha = str(input('\n -> '))
    if mana == 0:
        print('\nvc está sem mana')
        break
    if escolha == 'ver feitiços':
        while True:
            print(feiticos)
            escolhas = str(input('\ndeseja encerrar?\n s/n-> '))
            if escolhas == 's'or'sim'or'Sim':
                break
    if escolha == 'usar feitiço':
        if escolha == 'fogo simples':
            resultado = mana - feiticos['fogo_simples']
            mana = resultado
            print(mana)

    

    





        



    

