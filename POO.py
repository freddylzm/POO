# -*- coding: utf-8 -*-
"""
Scrit name: POO
Brief Description: This script provides a simple example to explain object oriented programming concepts.
Author: Freddy Zambrano
Creation/Modification Date: March 1, 2024
Script Version: 1.0
Requirements/Dependencies: None
Usage instructions: None
Contact Information: freddyzm@gmail.com
Additional Notes: This script serves as an example and does not provide accurate calculations for IMC
"""

class Paciente():
    
    def __init__(self, nombre: str, ID: int, genero: str):
        self.nombre = nombre
        self.ID = ID
        self.genero = genero
        
class DatosPaciente(Paciente):
    
    def __init__(self, nombre: str, ID: int, genero: str, peso: float, altura: float):
        super().__init__(nombre, ID, genero)
        self.peso = peso
        self.altura = altura
        
class IMC(DatosPaciente):
    
    def IMC(self):
        IMC = self.peso / (self.altura) ** 2
        return round(IMC, 2)

    def condicionIMC(self):
        imc = self.IMC()
        
        if imc < 18.5:
            condicion = 'Bajo peso'
        elif 18.5 <= imc <= 24.9:
            condicion = 'Peso normal'
        elif 24.9 < imc <= 29.9:
            condicion = 'Sobrepeso'
        else:
            condicion = 'Obesidad'
        return condicion

    def dieta(self):
        if self.condicionIMC() in ['Bajo peso', 'Sobrepeso', 'Obesidad']:
            return "Se debe recomendar una dieta."
        else:
            return "No se recomienda una dieta."

class Diagnostico(IMC):

    def KgSobrepeso(self):
            maxPesoNormal = 24.9 * self.altura ** 2
            
            if self.condicionIMC() in ['Bajo peso', 'Peso normal']:
                return 0
            else:
                return round((self.peso - maxPesoNormal), 2)
        
    def dieta(self):
        
        if self.condicionIMC() == 'Bajo peso':
            return "Se recomienda una dieta rica en proteínas y calorías para aumentar de peso."
        elif self.condicionIMC() == 'Peso normal':
            return "Se recomienda una dieta equilibrada para mantener un peso saludable."
        elif self.condicionIMC() == 'Sobrepeso':
            return "Se recomienda una dieta baja en calorías y alta en fibras, junto con ejercicio regular."
        else:
            return "Se recomienda una dieta baja en calorías y grasas, junto con ejercicio regular para controlar la obesidad."        

""" Usando la clase Paciente """
# Pedro = Paciente('Pedro', 123, 'Masculino')
# Ana = Paciente('Maria', 456, 'Femenino')

# print(vars(Pedro))
# print(Pedro.ID)

""" Usando la clase DatosPaciente """
# Pedro = DatosPaciente('Pedro', 123, 'Masculino', 78, 1.72)
# Ana = DatosPaciente('Maria', 456, 'Femenino', 52, 1.54)

# print(vars(Pedro))

""" Usando la clase IMC """
# Pedro = IMC('Pedro', 123, 'Masculino', 78, 1.72)
# Ana = IMC('Maria', 456, 'Femenino', 52, 1.54)
# print(Pedro.IMC())
# print(f"{Pedro.nombre} tiene un IMC de {Pedro.IMC()} y su condición es {Pedro.condicionIMC()}. {Pedro.dieta()}")

""" Usando la clase Diagnostico """
# Pedro = Diagnostico('Pedro', 123, 'Masculino', 78, 1.72)
# Ana = Diagnostico('Maria', 456, 'Femenino', 52, 1.54)

# print(f"{Pedro.nombre} tiene {Pedro.KgSobrepeso()} Kg de sobrepeso. {Pedro.dieta()}")
# print(f"{Ana.nombre} tiene {Ana.KgSobrepeso()} Kg de sobrepeso. {Ana.dieta()}")

""" Polimorfismo """
Pedro = IMC('Pedro', 123, 'Masculino', 78, 1.72)
print(Pedro.dieta())
Pedro = Diagnostico('Pedro', 123, 'Masculino', 78, 1.72)
print(Pedro.dieta())