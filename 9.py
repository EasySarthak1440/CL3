import random
from deap import base, creator, tools, algorithms
from multiprocessing import Pool

# Define the fitness function: Hamming distance between two binary strings
def hamming_distance(individual, target):
    return (sum(c1 != c2 for c1, c2 in zip(individual, target)),)

# Create a FitnessMin class inherited from base.Fitness with a weights attribute set to -1.0
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))

# Create an Individual class inherited from list and assign the fitness attribute to the FitnessMin class
creator.create("Individual", list, fitness=creator.FitnessMin)

# Define the toolbox
toolbox = base.Toolbox()

# Register the 'attr_bool' function to generate binary values (0 or 1) randomly
toolbox.register("attr_bool", random.randint, 0, 1)

# Register the individual generator to create individuals with 100 genes (binary values)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, n=100)

# Register the population generator to create a list of individuals
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# Register the evaluation function
toolbox.register("evaluate", hamming_distance, target="0101010101")

# Register the crossover operator: single-point crossover
toolbox.register("mate", tools.cxOnePoint)

# Register the mutation operator: flip each bit with probability 0.05
toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)

# Register the selection operator: tournament selection
toolbox.register("select", tools.selTournament, tournsize=3)

# Function to evaluate an individual using the evaluation function and assign the fitness
def evaluate_individual(individual):
    return (individual, toolbox.evaluate(individual))

# Parallel evaluation function using Pool.map
def eval_population_parallel(population):
    with Pool() as pool:
        return pool.map(evaluate_individual, population)

if __name__ == "__main__":
    # Generate an initial population of size 50
    pop = toolbox.population(n=50)

    # Evaluate the entire population
    fitnesses = eval_population_parallel(pop)

    # Assign fitness values to individuals
    for ind, fit in fitnesses:
        ind.fitness.values = fit

    # Evolution loop
    for g in range(10):
        print("-- Generation %i --" % g)

        # Select the next generation individuals
        offspring = toolbox.select(pop, len(pop))

        # Clone the selected individuals
        offspring = list(map(toolbox.clone, offspring))

        # Apply crossover and mutation on the offspring
        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if random.random() < 0.5:
                toolbox.mate(child1, child2)
                del child1.fitness.values
                del child2.fitness.values

        for mutant in offspring:
            if random.random() < 0.05:
                toolbox.mutate(mutant)
                del mutant.fitness.values

        # Evaluate the individuals with an invalid fitness
        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = eval_population_parallel(invalid_ind)
        for ind, fit in fitnesses:
            ind.fitness.values = fit

        # Replace the current population by the offspring
        pop[:] = offspring

    print("Best individual:", pop[0], "Fitness:", pop[0].fitness.values[0])
