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


def wyswietl_wynik(E: float, m: float, H: float):
    print("Masa: ", m, "kg")
    print("Wysokość: ", H, "m")
    print("Energia kinetyczna: ", E, "J")


def main():
    m = input("Podaj mase: ")
    H = input("Podaj wyoskość: ")
    E = energia_kinetyczna(H, m)
    wyswietl_wynik(E, m, H)


if __name__ == "__main__":
    main()
