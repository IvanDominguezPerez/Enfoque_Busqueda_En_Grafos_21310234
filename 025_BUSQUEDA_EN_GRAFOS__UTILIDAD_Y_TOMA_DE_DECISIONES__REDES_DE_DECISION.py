#Practica: 025_BUSQUEDA_EN_GRAFOS__UTILIDAD_Y_TOMA_DE_DECISIONES__REDES_DE_DECISION
#Alumno: IVAN_DOMINGUEZ
#Registro: 21310234
#Grupo: 7F1

import numpy as np  # Usamos numpy para cálculos matemáticos y manejo de arrays

# Definimos los estados del clima y las acciones posibles
estados_clima = ['soleado', 'lluvioso']
acciones = ['salir', 'no salir']

# Definimos la probabilidad de que ocurra cada tipo de clima
# Por ejemplo, asumimos un 70% de probabilidad de que el clima esté soleado y 30% de que esté lluvioso
probabilidades_clima = {
    'soleado': 0.7,
    'lluvioso': 0.3
}

# Definimos las utilidades asociadas a cada acción en cada estado del clima
# Las utilidades son valores numéricos que representan la satisfacción o beneficio esperado de cada acción.
# Por ejemplo, salir cuando está soleado tiene una utilidad de 10 (muy positivo),
# pero salir cuando está lluvioso tiene una utilidad de -5 (negativo, incomodidad).
utilidades = {
    'salir': {'soleado': 10, 'lluvioso': -5},
    'no salir': {'soleado': 5, 'lluvioso': 5}  # No salir tiene la misma utilidad independientemente del clima
}

# Función para calcular la utilidad esperada de cada acción
def calcular_utilidad_esperada(accion, probabilidades, utilidades):
    utilidad_esperada = 0
    # Iteramos sobre los posibles estados del clima (soleado o lluvioso)
    for estado in estados_clima:
        # Calculamos la utilidad esperada sumando la utilidad de la acción
        # en ese estado multiplicada por la probabilidad de que ocurra ese estado
        utilidad_esperada += probabilidades[estado] * utilidades[accion][estado]
    return utilidad_esperada

# Calculamos la utilidad esperada de cada acción (salir o no salir)
utilidad_salir = calcular_utilidad_esperada('salir', probabilidades_clima, utilidades)
utilidad_no_salir = calcular_utilidad_esperada('no salir', probabilidades_clima, utilidades)

# Imprimimos las utilidades esperadas de ambas acciones
print(f'Utilidad esperada de salir: {utilidad_salir}')
print(f'Utilidad esperada de no salir: {utilidad_no_salir}')

# Decidimos la acción óptima con base en la mayor utilidad esperada
if utilidad_salir > utilidad_no_salir:
    print('La mejor decisión es: Salir a caminar')
else:
    print('La mejor decisión es: No salir a caminar')

#Este programa simula una red de decisión simple que combina probabilidades y utilidades para
#tomar decisiones en un entorno incierto (en este caso, sobre si salir a caminar o no, basándose en
#clima). La red de decisión toma en cuenta las probabilidades del estado del clima (soleado o
#lluvioso) y las utilidades (beneficios o desventajas) de las posibles acciones.

#Utilidades: Representan el valor esperado de una acción dada un estado del mundo (el clima en este caso).
#Probabilidades: Representan la incertidumbre acerca del estado del mundo.
#Utilidad esperada: Se calcula combinando las utilidades de las acciones con las probabilidades
#de los diferentes estados. La acción con la mayor utilidad esperada será la que maximice la
#satisfacción o beneficio del usuario.

#Este enfoque es aplicable en muchos escenarios de la vida real, como la toma de decisiones
#financieras, la gestión de recursos en empresas, la planificación de viajes, o incluso la toma de
#decisiones médicas, donde existen múltiples resultados inciertos y se deben evaluar los riesgos y
#beneficios de diferentes acciones.
