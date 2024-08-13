
def num_leds(N,casos):

    leds_digito={
        "1": 2,
        "2":5,
        "3":5,
        "4":4,
        "5":5,
        "6":6,
        "7":3,
        "8":7,
        "9":6,
        "0":6,

    }

    resultado = []
    for caso in casos:
        sumar = 0
        for digito in str(caso):
            V = str(digito) 
            sumar += leds_digito[digito]
        resultado.append(sumar)
    
    return resultado  


N = int(input())
casos = []

for _ in range (N):
    v = str(input().rstrip() )  
    casos.append(v)


resultado = (num_leds(N,casos))

for res in resultado:
    print(res,"leds")
