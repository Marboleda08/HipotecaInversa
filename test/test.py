import  unittest
from src.Logic.Logica import *
#Test melos
class HipotecaInversaTest(unittest.TestCase):
    def testHipoteca1(self):
        #valores de entrada
        valor_inmueble = 750000000
        edad = 65
        estado_civil = "Soltero"
        edad_conyugue = 0
        tasa_de_interes = 10.75

        #valor esperado
        valor_esperado = 6998697.92
        #valor resultante
        valor_hipoteca = Hipoteca(valor_inmueble, edad, estado_civil,edad_conyugue,tasa_de_interes).calculadora_hipoteca_inversa()
        #funcion para comparar
        self.assertEqual(valor_esperado, round(valor_hipoteca,2))
    
    def testHipoteca2(self):
        valor_inmueble = 700000000
        edad = 75 
        estado_civil = "casado"
        edad_conyugue = 65
        tasa_de_interes = 10.75

        valor_esperado = 6532118.06

        valor_hipoteca = Hipoteca(valor_inmueble, edad, estado_civil,edad_conyugue,tasa_de_interes).calculadora_hipoteca_inversa()
        self.assertEqual(valor_esperado, round(valor_hipoteca,2))


#Test Extremos
    def testHipoteca3(self):
        valor_inmueble = 800000000
        edad = 73 
        estado_civil = "Casado"
        edad_conyugue = 73
        tasa_de_interes = 10.75

        valor_esperado = 59722222.22

        valor_hipoteca = Hipoteca(valor_inmueble, edad, estado_civil,edad_conyugue,tasa_de_interes).calculadora_hipoteca_inversa()
        self.assertEqual(valor_esperado, round(valor_hipoteca,2))

    def testHipoteca4(self):
        valor_inmueble = 650000000
        edad = 75
        estado_civil = "Casado"
        edad_conyugue = 75
        tasa_de_interes = 10.75

        valor_esperado = 48524305.56

        valor_hipoteca = Hipoteca(valor_inmueble, edad, estado_civil,edad_conyugue,tasa_de_interes).calculadora_hipoteca_inversa()
        self.assertEqual(valor_esperado, round(valor_hipoteca, 2))

    def testHipoteca5(self):
        valor_inmueble = 650000000
        edad = 75
        estado_civil = "Casado"
        edad_conyugue = 75
        tasa_de_interes = 0

        valor_esperado = 54166666.67

        valor_hipoteca = Hipoteca(valor_inmueble, edad, estado_civil,edad_conyugue,tasa_de_interes).calculadora_hipoteca_inversa()
        self.assertEqual(valor_esperado, round(valor_hipoteca, 2))

#Test Erorr
    def testHipoteca6(self):
        valor_inmueble = -650000000
        edad = 75
        estado_civil = "Casado"
        edad_conyugue = 75
        tasa_de_interes = 15

        valor_esperado = 67708333.33

        valor_hipoteca = Hipoteca(valor_inmueble, edad, estado_civil,edad_conyugue,tasa_de_interes).calculadora_hipoteca_inversa()
        self.assertEqual(valor_esperado, round(valor_hipoteca, 2))

    def testHipoteca7(self):
        valor_inmueble = 800000000
        edad = -5
        estado_civil = "Soltero"
        edad_conyugue = 0
        tasa_de_interes = 0
        valor_esperado = 6998697.92

        valor_hipoteca = Hipoteca(valor_inmueble, edad, estado_civil, edad_conyugue,tasa_de_interes).calculadora_hipoteca_inversa()
        self.assertEqual(valor_esperado, round(valor_hipoteca, 2))



