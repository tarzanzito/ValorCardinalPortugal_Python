

# from folder.file import class        
from ValorCardinalPortugal.F_ValorCardinalPortugal import ValorCardinalPortugal
from ValorCardinalPortugal.F_ValorCardinalPortugalTestes import ValorCardinalPortugalTestes


execute_testes = False

def processa():

    print("ValorCardinalPortugal (Version: 1.0.1)");
    print("======================================");
    print("");

    valor = input("Introduza valor '#0.00':")

    print("");
    print("Processa :[" + valor + "]");
    print("");

	# instancia class
    conversor = ValorCardinalPortugal()
    
	# executa 
	# converte(valor, vazio_se_zero_parte_inteira, vazio_se_zero_parte_decimail)
    resultado = conversor.converte(valor, False, False)

    print("Resultado:[" + resultado + "]")
	
    print("")


def testes():
    print("ValorCardinalPortugal (Version: 1.0.2)");
    obj = ValorCardinalPortugalTestes()
    obj.executa_todos()


########
# main #
########
if __name__ == "__main__":
    if execute_testes:
        testes()
    else:
        processa()
