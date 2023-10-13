import random
import itertools

cities = {
    'A': {'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30},
}

def calculate_total_distance(route):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += cities[route[i]][route[i+1]]
    total_distance += cities[route[-1]][route[0]]
    return total_distance

def genetic_algorithm(cities, population_size=100, generations=1000):
    cities_list = list(cities.keys())
    best_route = random.sample(cities_list, len(cities_list))
    best_distance = calculate_total_distance(best_route)

    for _ in range(generations):
        population = [random.sample(cities_list, len(cities_list)) for _ in range(population_size)]

        for route in population:
            distance = calculate_total_distance(route)
            if distance < best_distance:
                best_distance = distance
                best_route = route

    return best_route, best_distance

best_route, best_distance = genetic_algorithm(cities)
print("Best route:", best_route)
print("Shortest distance:", best_distance)
