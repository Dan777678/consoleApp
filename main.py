# stała przyspieszenia ziemskiego
g = 9.780318


# H - wysokosc w metrach
# m - masa w kg


def energia_kinetyczna(H: float, m: float):
    # Ek = mv^2
    # v = sqrt(2*gH)
    v = 2 * g * H
    # E = m * v / 2
    E = m * v
    E = E / 2
    return E

# Wyświetlanie wyników.


def wyswietl_wynik(E: float, m: float, H: float):
    print("Wynik")
    print("Masa: ", m, "kg")
    print("Wysokość: ", H, "m")
    print("Energia kinetyczna: ", E, "J")

# Funkcja kotrolująca pobranie danych, przypisanie danych do obliczeń i wyświetlanie wyników.


def main():
    try:
        m: float
        H: float
        print("Dane")
        m = float(input("Podaj mase: "))
        H = float(input("Podaj wyoskość: "))
        E = energia_kinetyczna(H, m)
        wyswietl_wynik(E, m, H)
        return True
    except ValueError:
        print("Wystąpił bład w danych wejściowych")
        return False


if __name__ == "__main__":
    t = main()
    while t == False:
        t = main()
