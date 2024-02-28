# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 06:51:43 2024

@author: FIZ
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

Pedro = Paciente('Pedro', 123, 'Masculino')
Ana = Paciente('Maria', 456, 'Femenino')

Pedro = DatosPaciente('Pedro', 123, 'Masculino', 72, 1.72)
Ana = DatosPaciente('Maria', 456, 'Femenino', 65, 1.52)

Pedro = IMC('Pedro', 123, 'Masculino', 72, 1.72)
Ana = IMC('Maria', 456, 'Femenino', 65, 1.54)

IMC_Pedro = Pedro.IMC()

print(f"{Pedro.nombre} tiene un IMC de {Pedro.IMC()} y su condición es {Pedro.condicionIMC()}. {Pedro.dieta()}")

Pedro = Diagnostico('Pedro', 123, 'Masculino', 72, 1.72)
Ana = Diagnostico('Maria', 456, 'Femenino', 65, 1.52)

print(f"{Pedro.nombre} tiene {Pedro.KgSobrepeso()} Kg de sobrepeso. {Pedro.dieta()}")
print(f"{Ana.nombre} tiene {Ana.KgSobrepeso()} Kg de sobrepeso. {Ana.dieta()}")

Pedro = IMC('Pedro', 123, 'Masculino', 72, 1.72)
print(Pedro.dieta())
Pedro = Diagnostico('Pedro', 123, 'Masculino', 72, 1.72)
print(Pedro.dieta())