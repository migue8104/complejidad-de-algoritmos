

def Capturados(cantidad):
    ListaPokemon=[]
    for i in range(cantidad):
        NombrePokemon = input()
        NombrePokemon=NombrePokemon.upper()
        ListaPokemon.append(NombrePokemon)
    return ListaPokemon

def CantidadPokemones(ListaPokemon):
    totalPokemones = 151
    PokemonesUnicos = set(ListaPokemon)
    ContarPokemonesCapturados=len(PokemonesUnicos)
    Faltante = totalPokemones - ContarPokemonesCapturados
    print(f"Falta(m) {Faltante} pomekon(s).")
    


N = int(input())
Pokemones =Capturados(N)
CantidadPokemones(Pokemones)
