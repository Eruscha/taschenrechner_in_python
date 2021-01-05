while 1:
    # Eingabe der Zahlen
    a = input("Bitte geben Sie Ihre erste Zahl an:")
    b = input("Bitte geben Sie Ihre zweite Zahl an:")
    c = input("Möchten Sie Addieren(1), Subtrahieren(2), Multiplizieren(3) oder Dividieren(4)?")

    # Berechnung der Zahlen
    d = int(a) + int(b)
    e = int(a) - int(b)
    f = int(a) * int(b)
    g = int(a) / int(b)

    # Ausgabe des Ergebnisses
    if (int(c) == 1):
        print(d)

    elif (int(c) == 2):
        print(e)

    elif (int(c) == 3):
        print(f)

    elif (int(c) == 4):
        print(g)
    else:
        print("Ihre Eingabe ist ungültig.")
        
