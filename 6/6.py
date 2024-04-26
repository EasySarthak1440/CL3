import numpy as np

# Objective function (example)
def objective_function(x):
    return np.sum(np.square(x))

# Initialization: Generate initial population of antibodies randomly
def initialize_population(population_size, dimensions, min_value, max_value):
    return np.random.uniform(min_value, max_value, size=(population_size, dimensions))

# Affinity Calculation: Calculate affinity (objective function value) for each antibody
def calculate_affinity(population):
    return np.apply_along_axis(objective_function, 1, population)

# Cloning: Clone antibodies based on their affinity
def clone_antibodies(population, affinity, clone_factor):
    num_clones = int(clone_factor * len(population))
    clones = np.repeat(population, num_clones, axis=0)
    return clones

# Hypermutation: Introduce random changes to cloned antibodies
def hypermutation(clones, mutation_rate, min_value, max_value):
    mutations = np.random.uniform(-mutation_rate, mutation_rate, size=clones.shape)
    mutated_clones = clones + mutations
    return np.clip(mutated_clones, min_value, max_value)

# Selection: Select antibodies with highest affinity from mutated antibodies
def select_antibodies(mutated_clones, mutated_affinity, population_size):
    sorted_indices = np.argsort(mutated_affinity)
    selected_indices = sorted_indices[:population_size]
    return mutated_clones[selected_indices]

# Replacement: Replace antibodies in original population with selected antibodies
def replace_antibodies(population, selected_antibodies):
    population[:len(selected_antibodies)] = selected_antibodies
    return population

# Clonal Selection Algorithm
def clonal_selection_algorithm(population_size, dimensions, min_value, max_value, clone_factor, mutation_rate, generations):
    # Initialization
    population = initialize_population(population_size, dimensions, min_value, max_value)
    
    for generation in range(generations):
        # Affinity Calculation
        affinity = calculate_affinity(population)
        
        # Cloning
        clones = clone_antibodies(population, affinity, clone_factor)
        
        # Hypermutation
        mutated_clones = hypermutation(clones, mutation_rate, min_value, max_value)
        mutated_affinity = calculate_affinity(mutated_clones)
        
        # Selection
        selected_antibodies = select_antibodies(mutated_clones, mutated_affinity, population_size)
        
        # Replacement
        population = replace_antibodies(population, selected_antibodies)
        
        # Optional: Print best solution in current generation
        best_solution = population[np.argmin(affinity)]
        print(f"Generation {generation+1}: Best solution - {best_solution}, Objective value - {np.min(affinity)}")
    
    # Return final population and its affinity
    return population, affinity

# Example usage
population_size = 50
dimensions = 10
min_value = -5
max_value = 5
clone_factor = 2
mutation_rate = 0.1
generations = 100

final_population, final_affinity = clonal_selection_algorithm(population_size, dimensions, min_value, max_value, clone_factor, mutation_rate, generations)
