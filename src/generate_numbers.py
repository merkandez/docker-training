import numpy as np
import os

# Definir la ruta de salida
if os.getenv("DOCKER_ENV"):
    output_dir = "/app/output"  # Ruta en Docker
else:
    output_dir = "output"  # Ruta en local

# Crear la carpeta de salida si no existe
os.makedirs(output_dir, exist_ok=True)

def generate_random_numbers():
    numbers = np.random.randint(1, 100, size=10)
    return numbers

if __name__ == "__main__":
    numbers = generate_random_numbers()
    file_path = os.path.join(output_dir, "numbers.txt")

    with open(file_path, "w") as file:
        file.write("\n".join(map(str, numbers)))

    print(f"📁 Archivo guardado en: {os.path.abspath(file_path)}")
