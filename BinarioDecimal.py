#Pasar de Decimal a Binario
def Decimal2Binario(decimal):
    binario = ''
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario
# Comentario : De Binario a Decimal
def Binario2Decimal(binario):
	n=len(binario)
	valor=0
	for bit in binario:
		if bit == "l"
			valor=valor+2**(n-1)
		n -=1
	return valor
