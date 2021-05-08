
class ValorCardinalPortugalConstantes(object):
    """description of class"""
    
    def __init__(self):
        pass

    #self.valorCardinal = ValorCardinalPortugal()

    # mylist = ["apple", "banana", "cherry"]
    # mytuple = ("apple", "banana", "cherry")
    # myset = {"apple", "banana", "cherry"}
    # mydict = { "brand": "Ford",  "model": "Mustang", "year": 1964 }

    CARDINAL_UNIDADES = ("", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove" )
    CARDINAL_DEZENAS = ("", "dez", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa" )
    CARDINAL_DEZENAS_DEZ = ("dez", "onze", "doze", "treze", "catorze", "quinze", "desasseis", "desassete", "dezoito", "dezanove" )
    CARDINAL_CENTENAS = ("", "cento", "duzentos", "trezentos", "quatrocentos", "quinhentos", "seiscentos", "setecentos", "oitocentos", "novecentos" )
    CARDINAL_ZERO = "zero" 
    CARDINAL_UM = "um"
    CARDINAL_UMA = "uma"
    CARDINAL_DOIS = "dois"
    CARDINAL_DUAS = "duas"
    CARDINAL_CEM = "cem"

    CARDINAL_GRUPOS_PLURAL = ("", "mil", "milhões", "milhares de milhão", "biliões", "dezenas de bilião", "centenas de bilião",
            "milhares de bilião", "dezenas de milhar de bilião", "centenas de milhar de bilião", "triliões")

    CARDINAL_GRUPOS_SINGULAR = ("", "mil", "milhão", "milhar de milhão", "bilião", "dezena de bilião", "centena de bilião",
            "milhar de bilião", "dezena de milhar de bilião", "centena de milhar de bilião", "trilião")

    CARDINAL_GRUPOS_MASCULINO = (True, True, True, True, True, False, False, True, False, False, True)

    FRASE_SUFIXO_AO = "ão"
    FRASE_SUFIXO_OES = "ões"
        
    FRASE_E = " e "
    FRASE_VIRGULA = ", "
    FRASE_DE = " de"
    FRASE_NOME_INTEIROS_PLURAL = "euros"
    FRASE_NOME_INTEIROS_SINGULAR = "euro"
    FRASE_NOME_DECIMAIS_PLURAL = "centimos"
    FRASE_NOME_DECIMAIS_SINGULAR = "centimo"
    FRASE_MENOS = "menos "
