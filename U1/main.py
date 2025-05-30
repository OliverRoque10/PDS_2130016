from src.actividad_1 import actividad_1

def main():
    actividad = input("¿Qué actividad quieres correr? (ejemplo:'actividad_1'): ").strip().lower()

    if actividad == 'actividad_1':
        actividad_1()
    else:
        print("invalid")

if __name__ == "__main__":
    main()
