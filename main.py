from formas import Circulo, Quadrado, Cubo, Cilindro

def main():
    print("=" * 65)
    print("    Cálculo de Área, Perímetro e Volume de Formas Geométricas   ")
    print("=" * 65)
    print("Escolha uma das opções abaixo para calcular:\n")

    formas_map = {
        'circulo': Circulo,
        'quadrado': Quadrado,
        'cubo': Cubo,
        'cilindro': Cilindro
    }

    while True:
        print("\n(Para sair, digite 'sair'.)")
        forma = input("Digite a forma (circulo, quadrado, cubo, cilindro): ").strip().lower()

        if forma == 'sair':
            print("\nObrigado por usar o programa!")
            break

        if forma in formas_map:
            forma_classe = formas_map[forma]  # Obtém a classe correspondente dentro do mapa de formas
            parametros = forma_classe.obter_parametros()  # Obtém os parâmetros da classe anteriormente selecionada
            forma_obj = forma_classe(*parametros)  # Cria a instância com os parâmetros fornecidos da classe correspôndente
            print(forma_obj.coleta_dados_resultados_e_exibe())  # Chama o método
        else:
            print("Forma não reconhecida! Por favor, escolha uma forma válida: círculo, quadrado, cubo ou cilindro.")

if __name__ == '__main__':
    main()