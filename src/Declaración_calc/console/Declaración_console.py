from src.Declaración_calc.Logica import calcular_impuesto_renta

def obtener_numero_input(mensaje):
    """
    Solicita al usuario un valor numérico para un mensaje dado.
    """
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Por favor, ingrese un número válido.")

ingresos_laborales = obtener_numero_input("Ingrese los ingresos laborales en el año: ")
otros_ingresos = obtener_numero_input("Ingrese el valor de otros ingresos en el año: ")
retenciones_fuente = obtener_numero_input("Ingrese el valor de retenciones en la fuente en el año: ")
seguridad_social = obtener_numero_input("Ingrese los pagos de seguridad social en el año: ")
aportes_pension = obtener_numero_input("Ingrese los aportes a la pensión en el año: ")
gastos_creditos_hipotecarios = obtener_numero_input("Ingrese el valor de los pagos de créditos hipotecarios en el año: ")
donaciones = obtener_numero_input("Ingrese el valor de las donaciones en el año: ")
gastos_educacion = obtener_numero_input("Ingrese el valor de los gastos en educación en el año: ")

print("Procesando...")

result = calcular_impuesto_renta(ingresos_laborales, otros_ingresos, retenciones_fuente, seguridad_social, aportes_pension, gastos_creditos_hipotecarios, donaciones, gastos_educacion)
