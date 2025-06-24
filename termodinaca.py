import math

print("==SISTEMA DE FÍSICA - 2º BIMESTRE ===\n Escolha o tema:\n 1. 1ª Lei da termodinamica\n 2. Ciclos termodinamicos\n 3. Calores Específicos dos Gases Perfeitos\n 4. Máquinas Térmicas e 2ª Lei da termodinâmica\n 5. Ciclos de Carnot\n 6. Refrigeradores\n 7. Ondas\n 0. Sair") 

while True:
    tema=input("\nDigite o número do tema: ")
    if tema =='0':
        print("Encerrando o progama")
        break
    #1º Lei da Termodinâmica
    elif tema =='1':
        print("\n=== 1ª LEI DA TERMODINÂMICA ===")
        print("ΔU = Q - W")
        print("1. Calcular variação")
        print("2. Calcular calor trocado")
        print("3. Calcular trabalho realizado")
        
        opcao = input("Escolha o cálculo: ")
        if opcao == '1':
            Q = float(input("Calor trocado (J): "))
            W = float(input("Trabalho realizado (J): "))
            delta_U = Q - W   
            print(f"\nVariação de energia interna (ΔU)={delta_U} J")
        if delta_U > 0:
            print("A energia interna do sistema aumentou.")
        elif delta_U < 0:
            print("A energia interna diminuiu. ") 
        else:
            print("A energia interna do sistema permaneceu constante.")
    
    elif opcao == "2":
        delta_U = float(input("Variação de energia interna(J): "))
        W = float (input("Trabalho realizado (J): "))
        Q = delta_U + W
        print(f"\n Calor trocado (Q) = {Q} J")
        if Q > 0:
            print("O sistema absorveu calor.")
        elif Q < 0:
            print("O sistema liberou calor. ")
    elif opcao == '3':
        Q = float(input("Calor trocado (J):"))
        delta_U = float(input("Varição de energia interna (J): "))
        W = Q - delta_U
        print(f"\nTrabalho realizado (W) = {W} J")
        if W > 0:
            print("O sistema realizou trabalho sobre o ambiente. ")
        elif W < 0:
            print("O ambiente realizou trabalho sobre o sistema. ")
        #Ciclos Termodinâmicos
    elif tema == '2':
        print("\n=== CICLOS TERMODINÂMICOS ===")
        print("1. Trabalho no ciclo (Área do ciclo)")   
        print("2. Rendimento do ciclo")  

        opcao = input("Escolha o cálculo: ")

        if opcao=='1':
            print("\n Digite os valores do ciclo no diagrama P x V")
            P_max = float(input("Pressão máxima (Pa): "))
            P_min = float(input("Pressão mínimo (Pa): "))
            V_max = float(input("Volume máximo (m³): "))
            V_min = float(input("Volume mínimo (m³): "))
            W = (P_max - P_min) * (V_max - V_min)
            print(f"\nTrabalho no ciclo = {W} J")

        elif opcao  =='2':
            Q_abs = float(input("Calor absorvido (J): "))
            Q_libera = float(input("Calor liberado (J): "))
            rendimento = (Q_abs - Q_libera) / Q_abs
            print(f"\nRendimento do ciclo = {rendimento:.2%}")
    
    #Calores Específicos dos Gases Perfeitos
    elif tema =="3":
        print("\n=====CALORES ESPECÍFICOS DOS GASES PERFEITOS====")
        print("1. Calor específico a volume(Cv)")
        print("2. Calor específico a pressão constante (Cp)")
        print(" Relação entre Cp e Cv (γ = Cp/Cv")
        opcao=input("Escolha o cálculo: ")
        R = 8.314 #Constante dos gases

        if opcao == "1":
           graus_liberdade=int(input("Graus de liberdade do gás (1-3): "))
           Cv=(graus_liberdade / 2)*R
           print(f"\nCv = {Cv} J/(mol·K)")
        

        elif opcao == "3":
             graus_liberdade=int(input("Graus de liberdade do gás (1-3)"))
             gamma=((graus_liberdade / 2) + 1 ) / (graus_liberdade / 2)
             print(f"\nγ = Cp/Cv = {gamma:.4f}")
            
    #maquinas termicas e 2ª Lei
    elif tema == '4'
        print("\n=== MAQUINAS TERMICAS E 2ª LEI ===")
        print("1. Rendimento da máquina térmica")
        print("2. Calor rejeitado para fonte fria")
        
        opcao = input("Escolha o cálculo: ")

        if opcao == '1':
            
           