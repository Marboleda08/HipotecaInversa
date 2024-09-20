import sys
sys.path.append("src")

from Logic.Logica import Mortgage

def main():
    print("Calculadora de Hipoteca Inversa")
    valor_inmueble = (input("Ingrese el valor del inmueble entre 650'000.000 y 800'000.000: "))
    edad_propietario = int(input("Ingrese la edad del propietario: "))
    estado_civil = input("Ingrese el estado civil del propietario (soltero/casado): ")
    edad_conyugue = int(input("Ingrese la edad del cónyuge (si aplica, de lo contrario ingrese 0): "))
    tasa_de_interes = float(input("Ingrese la tasa de interés: "))

    hipoteca = Mortgage(valor_inmueble, edad_propietario, estado_civil, edad_conyugue, tasa_de_interes)
    resultado = hipoteca.reverse_mortgage_calculator()

    if isinstance(resultado, str) and resultado.startswith("Error"):
        print(resultado)
    else:
        print(f"La cuota mensual de la hipoteca inversa es: {resultado:.2f} COP")

if __name__ == "__main__":
    main()