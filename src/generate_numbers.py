import numpy as np
import os

# Definir la ruta donde se guardará el archivo
output_dir = "/app/output"
os.makedirs(output_dir, exist_ok=True)  # Crear la carpeta si no existe

def generate_random_numbers():
    numbers = np.random.randint(1, 100, size=10)
    return numbers

if __name__ == "__main__":
    numbers = generate_random_numbers()
    file_path = os.path.join(output_dir, "numbers.txt")  # Guardar en /app/output/
    
    with open(file_path, "w") as file:
        file.write("\n".join(map(str, numbers)))
    
    print(f"Archivo guardado en: {file_path}")
