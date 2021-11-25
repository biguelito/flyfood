from runtest import RunTest 

def main():
    grafo_input = open('input.txt', 'r')
    grafo = RunTest(grafo_input)
    grafo_input.close()

    testes_totais = 6
    testes_por_valores = 300
    tamanho_populacao = 2
    geracoes = 4
    probabilidade_mutacao = 0.05
    cres_populacao = 2
    cres_geracao = 2

    grafo.run(testes_totais, testes_por_valores, tamanho_populacao, geracoes, probabilidade_mutacao, cres_populacao, cres_geracao)
    grafo.resume()
    
    return

if __name__ == "__main__":
    main()