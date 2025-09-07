#capturar 5 calificaciones y guardarlas en una lista

def main():
    calificaciones = [] 

    for i in range(5):
        cal = int(input(f"Captura la calificación {i+1}: "))
        calificaciones.append(cal)

    print("Las calificaciones capturadas son:", calificaciones)


if __name__ == "__main__":
    main()


