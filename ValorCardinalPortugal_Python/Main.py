

# from folder.file import class        
from ValorCardinalPortugal.F_ValorCardinalPortugal import ValorCardinalPortugal
from ValorCardinalPortugal.F_ValorCardinalPortugalTestes import ValorCardinalPortugalTestes


execute_testes = True

def main():

    print("ValorCardinalPortugal (Version: 1.0.1)");
    print("======================================");
    print("");

    valor = input("Introduza valor '#0.00':")

    print("");
    print("Processa :[" + valor + "]");
    print("");

    # executa
    conversor = ValorCardinalPortugal.valor_cardinal_portugal()
    conversor.Converte(valor)

    print("Resultado:[" + resultado + "]")
    print("")


def testes():
    print("ValorCardinalPortugal (Version: 1.0.2)");
    obj = ValorCardinalPortugalTestes()
    obj.executa_todos()


if __name__ == "__main__":
    if execute_testes:
        testes()
    else:
        main()
