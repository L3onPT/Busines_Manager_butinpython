from time import sleep
from money_graph import money
from estatistica import fabricas_de_automoveis
from estatistica import fabricas_de_alimentos
from estatistica import fabricas_de_materias_primas
from estatistica import fabricas_de_bebidas
from estatistica import loja_pequena
from estatistica import loja_media
from estatistica import loja_grande

def main(money, estatistica, fabricas_de_automoveis, fabricas_de_alimentos, fabricas_de_materias_primas, fabricas_de_bebidas, loja_pequena, loja_media, loja_grande):
    empresas = [] 
    print("[01] - Criar Empresas")
    print("[02] - As Minhas Empresas")
    print("[03] - Rankings")
    print("[04] - ")
    print("[99] - Salvar / Sair")

    decisao = input(">>> ")

    if decisao == 1:
        #Colocar comando de clear da tela
        print("Nome da empresa")
        nome_da_empresa = input("")

        #Colocar comando de clear da tela
        print("Que tipo de empresa vai ser?")
        print("[01] - Loja.")
        print("[02] - Shopping")
        print("[03] - Fábrica.")
        print("[04] - Empresa de tranportes.")
        print("[99] - Voltar")

        decidir_empresa = input(">>> ")

        if decidir_empresa == 1:
            #Colocar comando de clear da tela
            print("Tamanho da loja:")
            print("[01] - Pequena / 50.000$")
            print("[02] - Média / 175.000$")
            print("[03] - Grande / 370.000$")
        
        elif decidir_empresa == 2:
            #Colocar comando de clear da tela
            quit()

        elif decidir_empresa == 3:
            #Colocar comando de clear da tela

            print("Que tipo de Fábrica você quer criar?")
            print("[01] - Fábrica de Automóveis / 50M$")
            print("[02] - Fábrica de Alimentos / 112.5k$")
            print("[03] - Fábrica de Matérias Primas / 4M$")
            print("[04] - Fábrica de Bebidas / 5.388M$")
            print("[99] - Voltar")

            decidir_fabrica = input(">>> ")

            if decidir_fabrica == 1:
                if money >= 50000000:
                    #Colocar comando de dar clear da tela
                    empresas.append("Fábrica de Automóveis", estatistica.fabricas_de_automoveis + 1)
                    estatistica.fabrica_de_automoveis = fabricas_de_automoveis + 1
                    print("Fábrica:", nome_da_empresa, "foi criada com sucesso!")
                    print("Agora você pode gerir o seu novo negócio na aba: *As Minhas Empresas*!")
                    sleep(5)
                    #Colocar comando de dar clear da tela
                    main()
                else:
                    #Colocar comando de dar clear da tela
                    print("Você não tem dinheiro o suficiente para para poder inicializar esta fábrica!")
                    sleep(5)
                    #Colocar comando de dar clear da tela
                    main()

            elif decidir_fabrica == 2:
                if money >= 112500:
                    #Colocar comando de dar clear da tela
                    empresas.append("Fábrica de Alimentos", estatistica.fabricas_de_alimentos + 1)
                    estatistica.fabrica_de_alimentos = estatistica.fabrica_de_alimentos + 1
                    print("Fábrica", nome_da_empresa, "foi criada com sucesso!")
                    print("Agora você pode gerir o seu novo negócio na aba: *As Minhas Empresas*!")
                    sleep(5)
                    #Colocar comando de dar clear da tela
                    main()
                else: 
                    #Colocar comando de dar clear da tela
                    print("Você não tem dinheiro o suficiente para poder inicializar esta fábrica!")
                    sleep(5)
                    #Colocar comando de dar clear da tela
                    main()

            elif decidir_fabrica == 3:
                if money >= 4000000:
                    #Colocar comando de dar clear da tela
                    empresas.append("Fábrica de Matérias Primas", estatistica.fabricas_de_materias_primas + 1)
                    estatistica.fabricas_de_materias_primas = estatistica.fabrica_de_materias_primas + 1
                    print("Fábrica", nome_da_empresa, "foi criada com sucesso!")
                    print("Agora você pode gerir o seu novo negócio na aba: *As Minhas Empresas*!")
                    sleep(5)
                    #Colocar comando de dar clear da tela
                    main()
                else:
                    #Colocar comando de dar clear da tela
                    print("Você não tem dinheiro o suficiente para poder inicializar esta fábrica!")
                    sleep(5)
                    #Colocar comando de dar clear da tela
                    main()
                

            elif decidir_fabrica == 4:
                if money >= 5388000:
                    #Colocar comando de dar clear da tela
                    empresas.append("Fábrica de Bebidas", estatistica.fabricas_de_bebidas + 1)
                    estatistica.fabricas_de_bebidas = estatistica.fabricas_de_bebidas + 1
                    print("Fábrica", nome_da_empresa, "foi criada com sucesso!")
                    print("Agora você pode gerir o seu novo negócio na aba: *As Minhas Empresas*!")
                    sleep(5)
                    #Colocar comando de dar clear da tela
                    main()
                else:
                    #Colocar comando  de dar clear da tela
                    print("Você não tem dinheiro o suficiente para pode inicializar esta fábrica!")
                    sleep(5)
                    #Colocar comando de dar clear

                #Colocar comando de dar clear da tela
                quit()
        
        elif decidir_empresa == 4:
            #Colocar comando de clear da telas
            quit()

main()