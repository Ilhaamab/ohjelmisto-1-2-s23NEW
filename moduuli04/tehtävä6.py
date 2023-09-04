import random

n = int(input("Syötä arvottavien pisteiden määrä: "))

if n <= 0:
    print("Pisteiden määrän tulee olla positiivinen kokonaisluku.")
else:
    points_inside_circle = 0

    for _ in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x**2 + y**2 < 1:
            points_inside_circle += 1

    pi_approximation = 4 * points_inside_circle / n
    print(f"Piin likiarvo arvottujen pisteiden perusteella on noin {pi_approximation:.5f}")