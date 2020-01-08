from colorama import Style, init
init()
CARGOS = [0.05, 0.21]
NG = Style.BRIGHT


def Valor_con_env_incliedo2(monto_enviar):
    cargos = monto_enviar*CARGOS[0]
    cargos_iva = cargos * CARGOS[1]
    return cargos, cargos_iva


print(NG + "PROGRAMA PARA CALCULAR EL COSTO DE ENVIO ")
print(NG + "Costos de envio")
print(NG + "Por Favor Ingrese el monto que desea enviar...")
mont = float(input("$ "))
lista = []
lista.extend(Valor_con_env_incliedo2(mont))
print(NG + f"Usted desea enviar ${mont} y tiene un costo de ${lista[0]} + el iva de ${lista[1]}")
print(NG + f"en Total ${round(mont +lista[0]+lista[1],3)}")
