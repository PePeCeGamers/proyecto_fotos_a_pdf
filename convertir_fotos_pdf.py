from PIL import Image
import os

# Directorio donde se encuentran las imágenes
image_folder = r'C:\Users\bug\OneDrive\PROYECTOS\proyecto_fotos_a_pdf\FOTOS'  # Cambia esto a la ruta de tu carpeta

# Obtener una lista de todos los archivos en la carpeta
image_files = os.listdir(image_folder)

# Crear una lista de imágenes
images = []
for image_file in image_files:
    image_path = os.path.join(image_folder, image_file)
    # Abrir la imagen y convertirla a RGB
    img = Image.open(image_path)
    images.append(img.convert('RGB'))

# Verificar si hay imágenes para guardar
if images:
    pdf_path = 'output.pdf'  # Cambia esto al nombre que desees para el PDF
    images[0].save(pdf_path, save_all=True, append_images=images[1:])
    print(f'PDF creado exitosamente: {pdf_path}')
else:
    print('No se encontraron imágenes válidas en la carpeta.')
