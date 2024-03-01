# POO (Programación Orientada a Objetos)

## Descripción

Este script proporciona un ejemplo simple para explicar los conceptos de programación orientada a objetos. El artículo donde se explica el desarrollo del script se puede conseguir en: https://www.linkedin.com/in/freddyzambrano/

## Detalles

- **Autor:** Freddy Zambrano
- **Fecha de Creación/Modificación:** 1 de Marzo de 2024
- **Versión del Script:** 1.0
- **Requisitos/Dependencias:** Ninguno
- **Instrucciones de Uso:** Ninguno
- **Información de Contacto:** freddyzm@gmail.com
- **Notas Adicionales:** Este script sirve como ejemplo y no proporciona cálculos precisos para el IMC.

## Clases

- **Paciente:** Clase base que representa a un paciente con los atributos: Nombre, ID y género.
- **DatosPaciente:** Hereda de la clase Paciente y agrega los atributos peso y altura.
- **IMC:** Hereda de DatosPaciente y calcula el Índice de Masa Corporal (IMC), determina la condición del paciente en base al IMC y sugiere una dieta.
- **Diagnóstico:** Hereda de IMC y proporciona métodos adicionales para calcular el sobrepeso y recomendar una dieta específica.

## Ejemplo de Uso

```python
# Crear objeto IMC para Pedro
Pedro = IMC('Pedro', 123, 'Masculino', 78, 1.72)
print(Pedro.dieta())  # Imprimir dieta recomendada
