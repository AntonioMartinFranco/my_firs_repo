from colorama import Style, init
init()
COMICION = 0.05
IVA = 0.21
NG = Style.BRIGHT


def porcentaje(neto, porciento):
    return(neto*porciento)/100


def porcen(neto, porciento):
    return(neto * porciento)


def Valor_con_env_incliedo2(monto_enviar):
    cargos = porcen(monto_enviar, COMICION)
    cargos_iva = (float(porcen(cargos, IVA)))
    return monto_enviar, cargos, cargos_iva


print(NG + "|WESTERN UNION|")
print(NG + "Costos de envio")
print(NG + "Por Favor Ingrese el monto que desea enviar...")
mont = float(input("$ "))
lista = []
lista.extend(Valor_con_env_incliedo2(mont))
print(NG + f"Usted desea enviar ${lista[0]} y tiene un costo de ${lista[1]}+ el iva de ${lista[2]}")
print(NG + f"en Total ${round(lista[0]+lista[1]+lista[2],2)}")
