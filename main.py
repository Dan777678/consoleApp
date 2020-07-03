# stała przyspieszenia ziemskiego
g = 9.780318

# H - wysokosc w metrach
# m - masa w kg


def energia_kinetyczna(H: float, m: float):
    v = 2 * g * H
    E = m * v
    E = E / 2
    return E
