# stała przyspieszenia ziemskiego
g = 9.780318

# H - wysokosc w metrach
# m - masa w kg


def energia_kinetyczna(H: float, m: float):
    v = 2 * g * H
    E = m * v
    E = E / 2
    return E


def wyswietl_wynik(E: float, m: float, H: float):
    print("Masa: ", m, "kg")
    print("Wysokość: ", H, "m")
    print("Energia kinetyczna: ", E, "J")


def main():
    m = 2.97
    H = 1.97
    E = energia_kinetyczna(H, m)
    wyswietl_wynik(E, m, H)


if __name__ == "__main__":
    main()
