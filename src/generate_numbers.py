import numpy as np

def generate_random_numbers():
    numbers = np.random.randint(1, 100, size=10)
    return numbers

if __name__ == "__main__":
    numbers = generate_random_numbers()
    with open("numbers.txt", "w") as file:
        file.write("\n".join(map(str, numbers)))
    print("Archivo 'numbers.txt' creado con éxito.")
