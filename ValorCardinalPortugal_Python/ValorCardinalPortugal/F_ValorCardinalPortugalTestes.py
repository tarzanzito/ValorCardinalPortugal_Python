        
from ValorCardinalPortugal.F_ValorCardinalPortugal import ValorCardinalPortugal

class ValorCardinalPortugalTestes(object):
    """classe de testes"""
    
    def __init__(self):
        self.valorCardinal = ValorCardinalPortugal()


    def executa_todos(self):

        print("Tests Begin...")

        self.test_valida_valor()
        self.test_formata_valor()
        self.test_valor_negativo()

        self.test_adiciona_sufixo_de_grupo_mil()
        self.test_obtem_qualificador_parte_decimal()
        self.test_obtem_qualificador_parte_inteira()
        self.test_obtem_centenas()
        self.test_obtem_dezenas()
        self.test_obtem_unidades()
        self.test_junta_centenas_dezenas_unidades()
        self.test_descodifica_cardinal()
        self.test_remove_ultimas_virgulas_em_excesso()
        self.test_junta_todos_grupos_de_mil() 
        self.test_divide_em_grupos_de_mil() 
        self.test_divide_em_partes_inteira_decimal()
    
        self.test_converte()

        print("Tests End...")
 
    ####################

    def test_valida_valor(self):

        print("testing function: valida_valor")

        ok = self.valorCardinal.valida_valor("123456.89")
        if not ok:
            print("ERROR testing function: valida_valor (0)")

        ok = self.valorCardinal.valida_valor("123.456.89")
        if ok:
            print("ERROR testing function: valida_valor (1)")


    def test_formata_valor(self):

        print("testing function: formata_valor")

        result = self.valorCardinal.formata_valor("123.89")
        if result != "123.89":
            print("ERROR testing function: formata_valor (0)")

        result1 = self.valorCardinal.formata_valor("123.8")
        if result1 != "123.80":
            print("ERROR testing function: formata_valor (1)")

        result2 = self.valorCardinal.formata_valor("123.")
        if result2 != "123.00":
            print("ERROR testing function: formata_valor (2)")

        result3 = self.valorCardinal.formata_valor(".")
        if result3 != "0.00":
            print("ERROR testing function: formata_valor (3)")

        result4 = self.valorCardinal.formata_valor("0.")
        if result4 != "0.00":
            print("ERROR testing function: formata_valor (4)")

        result5 = self.valorCardinal.formata_valor("")
        if result5 != "0.00":
            print("ERROR testing function: formata_valor (5)")

        result6 = self.valorCardinal.formata_valor("123")
        if result6 != "123.00":
            print("ERROR testing function: formata_valor (6)")


    def test_valor_negativo(self):

        print("testing function: ValorNegativo")

        negativo = self.valorCardinal.valor_negativo("-123456.89")
        if not negativo:
            print("ERROR testing function: ValorNegativo (1)")

        negativo = self.valorCardinal.valor_negativo("123456.89")
        if negativo:
            print("ERROR testing function: ValorNegativo (2)")

    #####################

    def test_adiciona_sufixo_de_grupo_mil(self):

        print("testing function: adiciona_sufixo_de_grupo_mil")
        input = "oito"
        result = self.valorCardinal.adiciona_sufixo_de_grupo_mil(input, 0) 
        if result != "oito":
            print("ERROR testing function: adiciona_sufixo_de_grupo_mil")

        result = self.valorCardinal.adiciona_sufixo_de_grupo_mil(input, 1)
        if result != "oito mil":
            print("ERROR testing function: adiciona_sufixo_de_grupo_mil")

        result = self.valorCardinal.adiciona_sufixo_de_grupo_mil(input, 2)
        if result != "oito milhões":
            print("ERROR testing function: adiciona_sufixo_de_grupo_mil")


    def test_obtem_qualificador_parte_decimal(self):
        
        print("testing function: obtem_qualificador_parte_decimal")
        input = "123"
        result = self.valorCardinal.obtem_qualificador_parte_decimal(input, False)
        if result != "centimos":
            print("ERROR testing function: obtem_qualificador_parte_decimal")


    def test_obtem_qualificador_parte_inteira(self):

        print("testing function: obtem_qualificador_parte_inteira")
        input = "123"
        result = self.valorCardinal.obtem_qualificador_parte_inteira(input, False)
        if result != "euros":
            print("ERROR testing function: obtem_qualificador_parte_inteira")


    def test_obtem_centenas(self):

        print("testing function: obtem_centenas")
        result = self.valorCardinal.obtem_centenas(2, 1, 3)
        if result != "duzentos":
            print("ERROR testing function: obtem_centenas (1)")

        result = self.valorCardinal.obtem_centenas(1, 0, 0)  #new
        if result != "cem": #new
            print("ERROR testing function: obtem_centenas (2)") #new


    def test_obtem_dezenas(self):

        print("testing function: obtem_dezenas")
        result = self.valorCardinal.obtem_dezenas(1, 2)
        if result != "doze":
            print("ERROR testing function: obtem_dezenas (1)")

        result = self.valorCardinal.obtem_dezenas(2, 1)
        if result != "vinte": #new
            print("ERROR testing function: obtem_dezenas (2)")


    def test_obtem_unidades(self):

        print("testing function: obtem_unidades")
        result = self.valorCardinal.obtem_unidades(8, 2)
        if result != "oito":
            print("ERROR testing function: obtem_unidades (1)")

        result = self.valorCardinal.obtem_unidades(8, 1)
        if result != "": 
            print("ERROR testing function: obtem_unidades (2)")


    def test_junta_centenas_dezenas_unidades(self):

        print("testing function: junta_centenas_dezenas_unidades")
        result = self.valorCardinal.junta_centenas_dezenas_unidades("oitocentos", "setenta", "seis")
        if result != "oitocentos e setenta e seis":
            print("ERROR testing function: junta_centenas_dezenas_unidades")


    def test_descodifica_cardinal(self):

        print("testing function: descodifica_cardinal")
        result = self.valorCardinal.descodifica_cardinal("123", 2)
        if result != "cento e vinte e três milhões":
            print("ERROR testing function: descodifica_cardinal")


    def test_remove_ultimas_virgulas_em_excesso(self):

        print("testing function: remove_ultimas_virgulas_em_excesso")
        result = self.valorCardinal.remove_ultimas_virgulas_em_excesso("123456789, , , ")
        if result != "123456789":
            print("ERROR testing function: remove_ultimas_virgulas_em_excesso")


    def test_junta_todos_grupos_de_mil(self):

        print("testing function: junta_todos_grupos_de_mil")

        phrases = ( "alfa", "beta", "zulu" )
        result = self.valorCardinal.junta_todos_grupos_de_mil(phrases, False)
        if result != "alfa, beta e zulu":
            print("ERROR testing function: junta_todos_grupos_de_mil (1)")

        phrases = ( "alfa", "beta", "" )
        result = self.valorCardinal.junta_todos_grupos_de_mil(phrases, False)
        if result != "alfa e beta":
            print("ERROR testing function: junta_todos_grupos_de_mil (2)")


    def test_divide_em_grupos_de_mil(self):

        print("testing function: divide_em_grupos_de_mil")

        result = self.valorCardinal.divide_em_grupos_de_mil("123456789012345")
        size_grp = len(result)

        if size_grp != 5:
            print("ERROR testing function: divide_em_grupos_de_mil (n1)")

        if result[0] != "123":
            print("ERROR testing function: divide_em_grupos_de_mil (0)")
        if result[1] != "456":
            print("ERROR testing function: divide_em_grupos_de_mil (1)")
        if result[2] != "789":
            print("ERROR testing function: divide_em_grupos_de_mil (2)")
        if result[3] != "012":
            print("ERROR testing function: divide_em_grupos_de_mil (3)")
        if result[4] != "345":
            print("ERROR testing function: divide_em_grupos_de_mil (4)")

        result = self.valorCardinal.divide_em_grupos_de_mil("1234567890123")
        size_grp = len(result)
        if size_grp != 5:
            print("ERROR testing function: divide_em_grupos_de_mil (n2)")

        if result[0] != "001":
            print("ERROR testing function: divide_em_grupos_de_mil (5)")


    def test_divide_em_partes_inteira_decimal(self):

        print("testing function: divide_em_partes_inteira_decimal")

        result = self.valorCardinal.divide_em_partes_inteira_decimal("1234567.89")
        if result[0] != "1234567":
            print("ERROR testing function: divide_em_partes_inteira_decimal (0)")
        if result[1] != "89":
            print("ERROR testing function: divide_em_partes_inteira_decimal (1)")


    def test_converte(self):

        print("testing function: Converte")

        result = self.valorCardinal.converte("123456789.87", False, False)
        if result != "cento e vinte e três milhões, quatrocentos e cinquenta e seis mil, setecentos e oitenta e nove euros e oitenta e sete centimos":
            print("ERROR testing function: Converte (0)")
