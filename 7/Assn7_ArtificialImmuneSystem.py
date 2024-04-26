import numpy as np

def create_antibody(size):
  return np.random.rand(size) 

# Affinity (closeness)
def affinity(antibody, datapoint):
  distance = np.linalg.norm(antibody - datapoint)     #calculating euclidean distance
  return 1 / (1 + distance)

def get_key(pair):
   return pair[1]

size = 3
healthy_data = np.array([[1.0, 2.0, 3.0], [1.1, 1.9, 3.2]])     # 2 x 3
num_antibodies = 10
antibody_population = []
for i in range(num_antibodies):
    antibody_population.append(create_antibody(size))

# Simulate sensor data with potential damage (replace with actual data)
damaged_data = np.array([[1.2, 1.7, 2.8], [1.4, 1.5, 3.5]])

for i in range(2):
    healthy_affinities = []
    for ab in antibody_population:
       for datapoint in healthy_data:
          healthy_affinities.append(affinity(ab, datapoint))

    # Select top 'n' antibodies based on affinity (healthy data)
    top_antibodies = []
    for i in range(len(antibody_population)):
        pair = [antibody_population[i], healthy_affinities[i]]
        top_antibodies.append(pair)
    top_antibodies.sort(key = get_key, reverse=True)
    top_antibodies = top_antibodies[0:5]

    # Clone and introduce random mutations (simplified)
    new_population = []
    for ab, i in top_antibodies:
        new_population.append(ab + create_antibody(size) * 0.1)  # Introduce small mutation
        antibody_population = new_population 

# Update antibody population
antibody_population.extend(new_population)

# Check affinity for damaged data
damaged_affinities = []
for datapoint in damaged_data:
  for ab in antibody_population:
      damaged_affinities.append(affinity(ab, datapoint))

# Identify potential damage based on high affinity for damaged data
potential_damage_index = damaged_affinities.index(max(damaged_affinities))

print(len(antibody_population))
print("Antibody that can heal damaged data: ", antibody_population[potential_damage_index])
