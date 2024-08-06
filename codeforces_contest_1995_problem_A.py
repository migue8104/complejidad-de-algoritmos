def min_occupied_diagonals(t, test_cases):
    results = []

    for n, k in test_cases:
        if k == 0:
            results.append(0)
            continue

        diagonals_occupied = 0
        remaining_chips = k

        for length in range(n, 0, -1):
            if remaining_chips <= 0:
                break
            if length == n:   
                diagonals_occupied += 1
                remaining_chips -= n
            else:
                if remaining_chips > 0:
                    diagonals_occupied += 1
                    remaining_chips -= length
                if remaining_chips > 0:
                    diagonals_occupied += 1
                    remaining_chips -= length


        results.append(diagonals_occupied)

    return results

t  = int(input())
test_cases = []

for _ in range (t):
    n,k = map(int,input().split())
    test_cases.append((n,k))

resultado = min_occupied_diagonals(t,test_cases)
# Imprimir resultados
for resultado in resultado:
    print(resultado)

