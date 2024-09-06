import  unittest
from src.Logic.Logica import Mortgage
#Test Buenos
class HipotecaInversaTest(unittest.TestCase):
    def testHipoteca1(self):
        #valores de entrada
        valor_inmueble = 750000000
        edad = 65
        estado_civil = "single"
        edad_conyugue = 0
        tasa_de_interes = 10.75

        #valor esperado
        valor_esperado = 6998697.92
        #valor resultante
        valor_hipoteca = Mortgage(valor_inmueble, edad, estado_civil,edad_conyugue,tasa_de_interes).reverse_mortgage_calculator()
        #funcion para comparar
        self.assertEqual(valor_esperado, round(valor_hipoteca,2))
    
    def testHipoteca2(self):
        valor_inmueble = 700000000
        edad = 75 
        estado_civil = "married"
        edad_conyugue = 65
        tasa_de_interes = 10.75

        valor_esperado = 6532118.06

        valor_hipoteca = Mortgage(valor_inmueble, edad, estado_civil,edad_conyugue,tasa_de_interes).reverse_mortgage_calculator()
        self.assertEqual(valor_esperado, round(valor_hipoteca,2))

    def testHipoteca3(self):
        valor_inmueble = 725000000
        edad = 69
        estado_civil = "married"
        edad_conyugue = 66
        tasa_de_interes = 15.22

        valor_esperado = 10946924.60

        valor_hipoteca = Mortgage(valor_inmueble, edad, estado_civil,edad_conyugue,tasa_de_interes).reverse_mortgage_calculator()
        self.assertEqual(valor_esperado, round(valor_hipoteca,2))

    def testHipoteca4(self):
        valor_inmueble = 782000000
        edad = 67
        estado_civil = "single"
        edad_conyugue = 0
        tasa_de_interes = 12

        valor_esperado = 10861111.11

        valor_hipoteca = Mortgage(valor_inmueble, edad, estado_civil,edad_conyugue,tasa_de_interes).reverse_mortgage_calculator()
        self.assertEqual(valor_esperado, round(valor_hipoteca,2))

    def testHipoteca5(self):
        valor_inmueble = 690000000
        edad = 72
        estado_civil = "single"
        edad_conyugue = 0
        tasa_de_interes = 2

        valor_esperado = 9583333.33

        valor_hipoteca = Mortgage(valor_inmueble, edad, estado_civil,edad_conyugue,tasa_de_interes).reverse_mortgage_calculator()
        self.assertEqual(valor_esperado, round(valor_hipoteca,2))

    def testHipoteca6(self):
        valor_inmueble = 734000000
        edad = 78
        estado_civil = "married"
        edad_conyugue = 70
        tasa_de_interes = 22

        valor_esperado = 37379629.63

        valor_hipoteca = Mortgage(valor_inmueble, edad, estado_civil,edad_conyugue,tasa_de_interes).reverse_mortgage_calculator()
        self.assertEqual(valor_esperado, round(valor_hipoteca,2))

    def testHipoteca7(self):
        valor_inmueble = 650000000
        edad = 74
        estado_civil = "married"
        edad_conyugue = 73
        tasa_de_interes = 7

        valor_esperado = 31597222.22

        valor_hipoteca = Mortgage(valor_inmueble, edad, estado_civil,edad_conyugue,tasa_de_interes).reverse_mortgage_calculator()
        self.assertEqual(valor_esperado, round(valor_hipoteca,2))
#Test Extremos
    def testHipoteca8(self):
        valor_inmueble = 800000000
        edad = 73 
        estado_civil = "married"
        edad_conyugue = 73
        tasa_de_interes = 10.75

        valor_esperado = 59722222.22

        valor_hipoteca = Mortgage(valor_inmueble, edad, estado_civil,edad_conyugue,tasa_de_interes).reverse_mortgage_calculator()
        self.assertEqual(valor_esperado, round(valor_hipoteca,2))

    def testHipoteca9(self):
        valor_inmueble = 650000000
        edad = 75
        estado_civil = "Married"
        edad_conyugue = 75
        tasa_de_interes = 10.75

        valor_esperado = 48524305.56

        valor_hipoteca = Mortgage(valor_inmueble, edad, estado_civil,edad_conyugue,tasa_de_interes).reverse_mortgage_calculator()
        self.assertEqual(valor_esperado, round(valor_hipoteca, 2))

    def testHipoteca10(self):
        valor_inmueble = 650000000
        edad = 75
        estado_civil = "Married"
        edad_conyugue = 75
        tasa_de_interes = 0

        valor_esperado = 54166666.67

        valor_hipoteca = Mortgage(valor_inmueble, edad, estado_civil,edad_conyugue,tasa_de_interes).reverse_mortgage_calculator()
        self.assertEqual(valor_esperado, round(valor_hipoteca, 2))

    def testHipoteca11(self):
        valor_inmueble = 800000000
        edad = 75
        estado_civil = "Married"
        edad_conyugue = 75
        tasa_de_interes = 0

        valor_esperado = 66666666.67

        valor_hipoteca = Mortgage(valor_inmueble, edad, estado_civil,edad_conyugue,tasa_de_interes).reverse_mortgage_calculator()
        self.assertEqual(valor_esperado, round(valor_hipoteca, 2))

    def testHipoteca12(self):
        valor_inmueble = 750000000
        edad = 65
        estado_civil = "Married"
        edad_conyugue = 65
        tasa_de_interes = 0

        valor_esperado = 7812500.00

        valor_hipoteca = Mortgage(valor_inmueble, edad, estado_civil,edad_conyugue,tasa_de_interes).reverse_mortgage_calculator()
        self.assertEqual(valor_esperado, round(valor_hipoteca, 2))

    def testHipoteca13(self):
        valor_inmueble = 800000000
        edad = 65
        estado_civil = "Married"
        edad_conyugue = 65
        tasa_de_interes = 34

        valor_esperado = 23611111.11

        valor_hipoteca = Mortgage(valor_inmueble, edad, estado_civil,edad_conyugue,tasa_de_interes).reverse_mortgage_calculator()
        self.assertEqual(valor_esperado, round(valor_hipoteca, 2))

    def testHipoteca14(self):
        valor_inmueble = 650000000
        edad = 75
        estado_civil = "Married"
        edad_conyugue = 75
        tasa_de_interes = 15

        valor_esperado = 67708333.33

        valor_hipoteca = Mortgage(valor_inmueble, edad, estado_civil,edad_conyugue,tasa_de_interes).reverse_mortgage_calculator()
        self.assertEqual(valor_esperado, round(valor_hipoteca, 2))

#Test Erorr
    def testHipoteca15(self):
        valor_inmueble = -650000000
        edad = 75
        estado_civil = "Single"
        edad_conyugue = 75
        tasa_de_interes = 15

        valor_esperado = -67708333.33

        valor_hipoteca = Mortgage(valor_inmueble, edad, estado_civil,edad_conyugue,tasa_de_interes).reverse_mortgage_calculator()
        self.assertEqual(valor_esperado, round(valor_hipoteca, 2))

    def testHipoteca16(self):
        valor_inmueble = 800000000
        edad = -5
        estado_civil = "Single"
        edad_conyugue = 0
        tasa_de_interes = 0
        valor_esperado = 854700.85

        valor_hipoteca = Mortgage(valor_inmueble, edad, estado_civil, edad_conyugue,tasa_de_interes).reverse_mortgage_calculator()
        self.assertEqual(valor_esperado, round(valor_hipoteca, 2))

    def testHipoteca17(self):
        valor_inmueble = -800000000
        edad = 65
        estado_civil = "Single"
        edad_conyugue = 0
        tasa_de_interes = 15
        valor_esperado = -10416666.67

        valor_hipoteca = Mortgage(valor_inmueble, edad, estado_civil, edad_conyugue,tasa_de_interes).reverse_mortgage_calculator()
        self.assertEqual(valor_esperado, round(valor_hipoteca, 2))

    def testHipoteca18(self):
        valor_inmueble = 700000000
        edad = -65
        estado_civil = "Single"
        edad_conyugue = 0
        tasa_de_interes = 15
        valor_esperado = 528381.64

        valor_hipoteca = Mortgage(valor_inmueble, edad, estado_civil, edad_conyugue,tasa_de_interes).reverse_mortgage_calculator()
        self.assertEqual(valor_esperado, round(valor_hipoteca, 2))

    def testHipoteca19(self):
        valor_inmueble = -650000000
        edad = 73
        estado_civil = "Single"
        edad_conyugue = 0
        tasa_de_interes = 2
        valor_esperado = -9027777.78

        valor_hipoteca = Mortgage(valor_inmueble, edad, estado_civil, edad_conyugue,tasa_de_interes).reverse_mortgage_calculator()
        self.assertEqual(valor_esperado, round(valor_hipoteca, 2))

    def testHipoteca20(self):
        valor_inmueble = 800000000
        edad = 70
        estado_civil = "Single"
        edad_conyugue = 0
        tasa_de_interes = -23
        valor_esperado = -42592592.59

        valor_hipoteca = Mortgage(valor_inmueble, edad, estado_civil, edad_conyugue,tasa_de_interes).reverse_mortgage_calculator()
        self.assertEqual(valor_esperado, round(valor_hipoteca, 2))
