#CREA UNA LISTA DE LOS ARCHIVOS DE UNA CARPETA

import os

carpeta_archivos=r'C:\Users\bug\OneDrive\PROYECTOS\proyecto_fotos_a_pdf\FOTOS'

lista_archivos = os.listdir(carpeta_archivos)

print(lista_archivos)

