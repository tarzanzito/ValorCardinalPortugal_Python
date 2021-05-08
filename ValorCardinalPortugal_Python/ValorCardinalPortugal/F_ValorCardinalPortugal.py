
from decimal import Decimal
from ValorCardinalPortugal.F_ValorCardinalPortugalConstantes import ValorCardinalPortugalConstantes

class ValorCardinalPortugal(object):
    """Classe para descrever cardinal de um numero"""

    def __init__(self):

        self.CONSTANTES = ValorCardinalPortugalConstantes()


    def converte(self, valor, vazio_se_zero_parte_inteira = False, vazio_se_zero_parte_decimail = False):
        """ Metodo principal:
        parameters:
            valor = string no formato decimal para converter
            vazio_se_zero_parte_inteira = se o valor for zero aparece vazio se não aparece zero euros
            vazio_se_zero_parte_decimal = se o valor for zero aparece vazio se não aparece zero centimos
        """

        valorTrim = valor.strip()

        # validatição e formatação do impute
        valido = self.valida_valor(valorTrim)
        if not valido:
            return "ERRO: não é um valor valido: " + valor

        valorForm = self.formata_valor(valorTrim)

        #inicio
        valorInicial = ""
        negativo = self.valor_negativo(valorForm)
        if negativo:
            valorInicial = valorForm[1:]
        else:
            valorInicial = valorForm

        #processa

        #separa parte inteira pare decimal
        partes = self.divide_em_partes_inteira_decimal(valorInicial)

        #separa por grupos de mil "???"
        gruposInteiros = self.divide_em_grupos_de_mil(partes[0])
        gruposDecimais = self.divide_em_grupos_de_mil(partes[1])

        #descodifica os grupos inteiros
        comp = len(gruposInteiros)
        gruposCardinaisInteiros = [""] * comp
        for x in range(comp):
            gruposCardinaisInteiros[x] = self.descodifica_cardinal(gruposInteiros[x], (comp - x - 1))

        #descodifica os groupos decimais
        comp = len(gruposDecimais)
        gruposCardinaisDecimais = [""] * comp
        for x in range(comp):
            gruposCardinaisDecimais[x] = self.descodifica_cardinal(gruposDecimais[x], (comp - x - 1))

        #junta todos os grupos
        finalInteiros = self.junta_todos_grupos_de_mil(gruposCardinaisInteiros, vazio_se_zero_parte_inteira)
        finalDecimais = self.junta_todos_grupos_de_mil(gruposCardinaisDecimais, vazio_se_zero_parte_decimail)

        #caso: se valor = 0.0 mostra sempre "zero"
        if len(finalInteiros) == 0 and len(finalDecimais) == 0:
            finalInteiros = self.CONSTANTES.CARDINAL_ZERO + " " + self.CONSTANTES.FRASE_NOME_INTEIROS_PLURAL

        #caso: analiza se coloca "de" antes do qualificador
        comp = len(finalInteiros)
        if comp > 2:
            temp = finalInteiros[comp - 3: comp]
            if temp == self.CONSTANTES.FRASE_SUFIXO_OES:
                finalInteiros += self.CONSTANTES.FRASE_DE
            else:
                temp = finalInteiros[comp - 2: comp]
                if temp == self.CONSTANTES.FRASE_SUFIXO_AO:
                    finalInteiros += self.CONSTANTES.FRASE_DE

        #obtem qualificadores
        qualificadorInteiros = self.obtem_qualificador_parte_inteira(partes[0], vazio_se_zero_parte_inteira)
        qualificadoreDecimais = self.obtem_qualificador_parte_decimal(partes[1], vazio_se_zero_parte_decimail)

        #caso: adiciona qualificador inteiros
        if len(finalInteiros) > 0:
            finalInteiros += " " + qualificadorInteiros

        #caso: adiciona qualificador decimais
        if len(finalDecimais) > 0:
            finalDecimais += " " + qualificadoreDecimais

        #case: adiciona " e " entre a frase inteiros & frase decimais
        dual = ""
        if len(finalInteiros) > 0 and len(finalDecimais)> 0:
            dual = self.CONSTANTES.FRASE_E

        resultdofinal = finalInteiros + dual + finalDecimais
        if negativo:
            resultdofinal = self.CONSTANTES.FRASE_MENOS + resultdofinal

        return resultdofinal
        


    def divide_em_partes_inteira_decimal(self, valor):
            
            partes = valor.split('.')

            return partes
        

    def divide_em_grupos_de_mil(self, valor):
        
        temp = valor

        #extrai
        list = []
        while len(temp) > 3:
            
            str3 = temp[len(temp) - 3:] #3 ultimos
            list.append(str3)
            temp = temp[0: len(temp) - 3]
            
        list.append(temp.rjust(3, "0")) #garante comprimento = 3

        #reverte array
        count = len(list)
        groupos = [""] * count
        for x in range(count):
            groupos[count - 1 - x] = list[x]

        return groupos
        

    def junta_todos_grupos_de_mil(self, groupos_array, vazio_se_zero):

        resultado = ""
        comp = len(groupos_array)

        for x in range(comp):
            
            if len(groupos_array[x]) == 0:
                continue
            
            # no ultimo elemento analisa se coloca  " e " no fim
            if x == (comp - 1) and len(resultado) > 1:
                pos = groupos_array[x].find(self.CONSTANTES.FRASE_E)
                if pos == -1:
                    resultado = self.remove_ultimas_virgulas_em_excesso(resultado)
                    resultado += self.CONSTANTES.FRASE_E

            resultado += groupos_array[x]
            resultado += self.CONSTANTES.FRASE_VIRGULA

        if len(resultado) == 0 and not vazio_se_zero:
            resultado =  self.CONSTANTES.CARDINAL_ZERO

        resultado = self.remove_ultimas_virgulas_em_excesso(resultado)

        #caso: quantos " e " existem depois da ultima virgula? se zero substitui ultima ", " por " e " 
        pos = resultado.rfind(self.CONSTANTES.FRASE_VIRGULA)
        if pos > 0:
            temp1 = resultado[0: pos]
            temp2 = resultado[pos + len(self.CONSTANTES.FRASE_VIRGULA):]
            pos = temp2.find(self.CONSTANTES.FRASE_E)
            if (pos == -1):
                resultado = temp1 + self.CONSTANTES.FRASE_E + temp2;

        return resultado
        

    def remove_ultimas_virgulas_em_excesso(self, valor):

        if len(valor) < 2:
            return valor

        resultado = valor

        while resultado[len(resultado) - 2: len(resultado)] == self.CONSTANTES.FRASE_VIRGULA:
            resultado = resultado[0: len(resultado) - 2]

        return resultado
        

    def descodifica_cardinal(self, valor, nivel):

        if valor == "000":
            return ""

        cardinal_array = ["", "", ""]
        digit_array = [0, 0, 0]

        for x in range(3):
            digit_array[x] = int(valor[x: x + 1])

        cardinal_array[0] = self.obtem_centenas(digit_array[0], digit_array[1], digit_array[2])
        cardinal_array[1] = self.obtem_dezenas(digit_array[1], digit_array[2])
        cardinal_array[2] = self.obtem_unidades(digit_array[2], digit_array[1])

        temp = self.junta_centenas_dezenas_unidades(cardinal_array[0], cardinal_array[1], cardinal_array[2])
        resultado = self.adiciona_sufixo_de_grupo_mil(temp, nivel)

        return resultado
        

    def junta_centenas_dezenas_unidades(self, centena, dezena, unidade):

        resultado = centena

        if len(centena) > 0 and (len(dezena) > 0 or len(unidade) > 0):
            resultado += self.CONSTANTES.FRASE_E

        resultado += dezena
        
        if len(dezena) > 0 and len(unidade) > 0:
            resultado += self.CONSTANTES.FRASE_E

        resultado += unidade

        return resultado


    def obtem_unidades(self, digito, dezena):

        if dezena == 1:
            return ""

        return self.CONSTANTES.CARDINAL_UNIDADES[digito]


    def obtem_dezenas(self, digito, unidade):

        if digito == 1:
            return self.CONSTANTES.CARDINAL_DEZENAS_DEZ[unidade]

        return self.CONSTANTES.CARDINAL_DEZENAS[digito]


    def obtem_centenas(self, digito, dezena, unidade):
                
        if digito == 1 and  dezena == 0 and unidade == 0:
                return self.CONSTANTES.CARDINAL_CEM #Caso : Cem

        return self.CONSTANTES.CARDINAL_CENTENAS[digito]
        

    def obtem_qualificador_parte_decimal(self, valor, vazio_se_zero):
                    
        val_temp = Decimal(valor.replace(',','.'))

        if val_temp > 1:
            return  self.CONSTANTES.FRASE_NOME_DECIMAIS_PLURAL

        if val_temp == 1:
            return  self.CONSTANTES.FRASE_NOME_DECIMAIS_SINGULAR

        if val_temp == 0 and not vazio_se_zero:
            return self.CONSTANTES.FRASE_NOME_DECIMAIS_PLURAL

        return ""
        

    def obtem_qualificador_parte_inteira(self, valor, vazio_se_zero):

        val_temp = Decimal(valor.replace(',','.'))

        if val_temp > 1:
            return self.CONSTANTES.FRASE_NOME_INTEIROS_PLURAL

        if val_temp == 1:
            return self.CONSTANTES.FRASE_NOME_INTEIROS_SINGULAR

        if val_temp == 0 and not vazio_se_zero:
            return self.CONSTANTES.FRASE_NOME_INTEIROS_PLURAL

        return ""
        

    def adiciona_sufixo_de_grupo_mil(self, valor, nivel):

        resultado = ""

        if nivel == 0:
            resultado = valor

        elif nivel == 1:
            if valor == self.CONSTANTES.CARDINAL_UM:
                resultado = self.CONSTANTES.CARDINAL_GRUPOS_SINGULAR[nivel] #special : remove palavra "um" (um mil)
            else:
                resultado = valor + " " + self.CONSTANTES.CARDINAL_GRUPOS_PLURAL[nivel]
        
        else:
            if valor == self.CONSTANTES.CARDINAL_UM:
                if self.CONSTANTES.CARDINAL_GRUPOS_MASCULINO[nivel]:
                    resultado = self.CONSTANTES.CARDINAL_UM
                else:
                    resultado = self.CONSTANTES.CARDINAL_UMA
                resultado += " " + self.CONSTANTES.CARDINAL_GRUPOS_SINGULAR[nivel]

            elif valor == self.CONSTANTES.CARDINAL_DOIS:
                if CARDINAL_GRUPOS_MASCULINO[nivel]:
                    resultado = self.CONSTANTES.CARDINAL_DOIS;
                else:
                    resultado = self.CONSTANTES.CARDINAL_DUAS;

                resultado += " " + CARDINAL_GRUPOS_PLURAL[nivel];

            else:
                resultado = valor + " " + self.CONSTANTES.CARDINAL_GRUPOS_PLURAL[nivel]

        return resultado


    def valida_valor(self, valor):

        comp = len(valor)
        if comp == 0:
            return True

        pontos = 0
        for x in range(comp):
            chr = valor[x: x + 1]

            if chr == "-":
                if x > 0:
                    return False
                else:
                    continue

            if chr == ".":
                pontos += 1
                continue

            if chr < "0" or chr > "9":
                return False
            
        if pontos > 1:
            return False

        return True

        
    def formata_valor(self, valor):

        if len(valor) == 0:
            return "0.00"

        resultado = valor

        pos = valor.find(".")
        if pos == -1:
            resultado += ".00"
        elif pos == 0:
            resultado = "0" + resultado

        pos = resultado.find(".")
        rlen = len(resultado) - pos
        if rlen == 1:
            resultado += "00"
        elif rlen == 2:
            resultado += "0"
        else:
            resultado = resultado[0:pos + 3]

        return resultado.strip()
        

    def valor_negativo(self, valor):

        return (valor[0:1] == "-")
  
