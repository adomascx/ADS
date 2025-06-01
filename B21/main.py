def ar_turi_cikla(V, edges):
    
    # Sukuriame kaimynystės sąrašą
    adj_list = [[] for _ in range(V)]
    for u, v in edges:
        adj_list[u].append(v)
    
    # Žymėsime aplankytas viršūnes
    visited = [False] * V       
    # Laikysime viršūnes, esančias DFS kelyje
    on_stack = [False] * V 

    # Vidinė DFS funkcija (rekursinė)
    def dfs(u):
        # Pažymime, kad viršūnė 'u' aplankyta ir įdedame ją į kStack
        visited[u] = True
        on_stack[u] = True
        
        # Iteruojame per visus kaimynus
        for v in adj_list[u]:
            if not visited[v]:
                if dfs(v):
                    return True
            elif on_stack[v]:
                return True
        # Išimame 'u' iš kStack, kai nukeliame iš jo
        on_stack[u] = False
        return False

    for u in range(V):
        if not visited[u] and dfs(u):
            return True
    return False

if __name__ == "__main__":
    
    V = int(input("Iveskite virsuniu kieki: "))
    E = int(input("Iveskite krastiniu kieki: "))
    
    edges = []
    print("Iveskite kiekviena krastine formatu 'u v'")
    for _ in range(E):
        # Nuskaitome kraštines
        u, v = map(int, input().split())
        
        # Konvertuojame į nulinį indeksą
        edges.append((u - 1, v - 1))
    
    print("Grafas turi cikla." if ar_turi_cikla(V, edges) else "Grafas neturi ciklo.")