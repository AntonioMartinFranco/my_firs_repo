from colorama import Style, init
init()
CARGOS = [0.05, 0.21]
NG = Style.BRIGHT


def porcen(neto, porciento):
    return(neto * porciento)


def Valor_con_env_incliedo2(monto_enviar):
    cargos = porcen(monto_enviar, CARGOS[0])
    cargos_iva = porcen(cargos, CARGOS[1])
    return monto_enviar, cargos, cargos_iva


print(NG + "PROGRAMA PARA CALCULAR EL COSTO DE ENVIO ")
print(NG + "Costos de envio")
print(NG + "Por Favor Ingrese el monto que desea enviar...")
mont = float(input("$ "))
lista = []
lista.extend(Valor_con_env_incliedo2(mont))
print(NG + f"Usted desea enviar ${lista[0]} y tiene un costo de ${lista[1]} + el iva de ${lista[2]}")
print(NG + f"en Total ${round(lista[0]+lista[1]+lista[2],2)}")
