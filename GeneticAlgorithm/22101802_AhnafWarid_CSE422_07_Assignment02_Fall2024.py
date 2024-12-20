import random

def calc_fitness(chromosome, nii, tii):
    penaltyOV = 0
    penaltyCS = 0

    for i in range(tii):
        segment = chromosome[i * nii:(i + 1) * nii]
        coursesSC = sum(segment)
        if coursesSC > 1:
            penaltyOV += (coursesSC - 1)

    for j in range(nii):
        countSCHE = sum(chromosome[j + i * nii] for i in range(tii))
        penaltyCS += abs(countSCHE - 1)

    # Total penalty = overlap + consistency
    penaltyTT = penaltyOV + penaltyCS
    return -penaltyTT

# Generate a valid chromosome
def generate_chromosome(n, t):
    chromosome = [0] * (n * t)
    for i in range(t):
        course = random.randint(0, n - 1)  # Ensure one course per timeslot
        chromosome[i * n + course] = 1
    return chromosome

# crossover
def crossover(parentOne, parentTwo):
    pnt = random.randint(1, len(parentOne) - 2)
    child1 = parentOne[:pnt] + parentTwo[pnt:]
    child2 = parentTwo[:pnt] + parentOne[pnt:]
    return child1, child2

# mutation for each chromosome A[i] = 1 - A[i], as mentioned by sir.
def mutate(chr, rateOfMutation=0.1):
    for i in range(len(chr)):
        if random.random() < rateOfMutation:
            chr[i] = 1 - chr[i]

# Genetic Algorithm
def genetic_algorithm(n, t, max_iterations=100, pop_size=10):
    population = [generate_chromosome(n, t) for _ in range(pop_size)]
    chromBest = None
    fitBest = float('-inf')

    for _ in range(max_iterations):
        valFit = [(chromosome, calc_fitness(chromosome, n, t)) for chromosome in population]
        valFit.sort(key=lambda x: x[1], reverse=True)

        # Update best chromosome
        if valFit[0][1] > fitBest:
            chromBest = valFit[0][0]
            fitBest = valFit[0][1]

        # Selection (Random parents for simplicity)
        parents = random.sample(population, 2)
        parentOne, parentTwo = parents[0], parents[1]

        # Crossover
        offspring1, offspring2 = crossover(parentOne, parentTwo)

        # Mutation
        mutate(offspring1)
        mutate(offspring2)

        # Replace worst chromosomes with new offspring
        population[-2:] = [offspring1, offspring2]

    return chromBest, fitBest

# Input handling
def main():
    n, t = map(int, input("Enter number of courses and timeslots (N T): ").split())
    courses = [input(f"Enter course code {i+1}: ") for i in range(n)]

    # Run genetic algorithm
    best_solution, fitBest = genetic_algorithm(n, t)

    # Output
    print("Best Chromosome:", ''.join(map(str, best_solution)))
    print("Fitness Value:", fitBest)

# Run the program
main()

import random

# Function to generate a random chromosome
def generate_chromosome(length):
    return [random.randint(0, 1) for _ in range(length)]

# Two-point crossover function
def two_point_crossover(parentOne, parentTwo):
    # Ensure the second point comes after the first point
    pointing1 = random.randint(0, len(parentOne) - 2)
    pointing2 = random.randint(pointing1 + 1, len(parentOne) - 1)

    # Generate offspring
    offspring1 = parentOne[:pointing1] + parentTwo[pointing1:pointing2] + parentOne[pointing2:]
    offspring2 = parentTwo[:pointing1] + parentOne[pointing1:pointing2] + parentTwo[pointing2:]

    return offspring1, offspring2

# Execution
def part2():
    parentOne = generate_chromosome(9)
    parentTwo = generate_chromosome(9)

    print("Parent 1:", ''.join(map(str, parentOne)))
    print("Parent 2:", ''.join(map(str, parentTwo)))

    childOne, childTwo = two_point_crossover(parentOne, parentTwo)

    print("Offspring 1:", ''.join(map(str, childOne)))
    print("Offspring 2:", ''.join(map(str, childTwo)))

# Run Part 2 (EZ)
part2()