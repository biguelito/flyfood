from runtest import RunTest 

def main():
    grafo = open('input10x10-11.txt', 'r')
    grafo11 = RunTest(grafo)
    grafo.close()

    grafo11.run()

    return

if __name__ == "__main__":
    main()