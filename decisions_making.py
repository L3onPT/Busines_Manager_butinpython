from money_graph import money

def main():
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
            quit()
        
        elif decidir_empresa == 2:
            #Colocar comando de clear da tela
            quit()

        elif decidir_empresa == 3:
            #Colocar comando de clear da tela

            print("Que tipo de Fábrica você quer criar?")
            print("[01] - Fábrica de Automóveis")
            print("[02] - Fábrica de Alimentos")
            print("[03] - Fábrica de Matérias Primas")
            print("[04] - Fábrica de Bebidas")
            print("[99] - Voltar")

            decidir_fabrica = input(">>> ")

            if decidir_fabrica == 1:
                #Colocar comando de dar clear da tela
                quit()

            elif decidir_fabrica == 2:
                #Colocar comando de dar clear da tela
                quit()

            elif decidir_fabrica == 3:
                #Colocar comando de dar clear da tela
                quit()

            elif decidir_fabrica == 4:
                #Colocar comando de dar clear da tela
                quit()
        
        elif decidir_empresa == 4:
            #Colocar comando de clear da telas
            quit()

main()