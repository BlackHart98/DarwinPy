# DarwinPy

## Introduction
DarwinPy is an evolutionary computation module built with python, to enable you to easily
implement evolutionary methods such as genetics algorithm and evolutionary strategies with
few lines of code.

## Classes in DarwinPy

### Genetics Classes (DarwinPy.Genetics.Genetics)

#### Methods
| Identifier | Type |
| ------------ | ---------- |
| setSearchSpace | None |
|setChromosomeLength| None |
|setPopulationSize| None |
|setChromosomeMatrix| None |
|getChromosomeMatrix| numpy.array |
|getSearchSpace| tuple |
|crossover| None |
|select| None |
|mutate| None |
|evolve| None |

#### Attributes
| Identifier | Type |
| ------------ | ---------- |
|chromosome_length | int |
|population_size | int |
|search_space | tuple |
|chromosome_matrix | numpy.array |
|pair_list | list |
|data_type | type |



## Sample DarwinPy implementation
```python

import DarwinPy
import numpy as np

def hammingDist(goal, matrix):
    result = []
    for i in range(len(matrix)):
        temp = 0.
        for j in range(len(goal)):
            if goal[j] == matrix[i][j]:
                temp += 1.
        result.append(temp)
    return result


if __name__ == "__main__":
    mouse_population = 5
    mutation_rate = 0.5
    search_space = (0,1)
    goal = np.array([1,0,1,1,0,1,1, 0,1,1,0],int)
    chromosome_length = len(goal)

    mouse_species = DarwinPy.Genetics.Genetics(chromosome_length,
    mouse_population, (0,1), int)
    print("mouse species instantiated:\n {}".format(mouse_species))

    print("the goal:\n {}".format(goal))

    mouse_species.populate()
    print("get mouse matrix(GA):\n {}".
    format(mouse_species.getChromosomeMatrix()))


    fitness_vector = np.array(
    hammingDist(goal,mouse_species.getChromosomeMatrix()),
    float)

    print("get fitness vector: {}".format(fitness_vector))

    is_goal = False
    gen = 1
    while is_goal == False:
        print("Generation #{}\n".format(gen))
        gen += 1
        mouse_species.evolve(fitness_vector,
        mutation_rate, 0.5)
        print("get mouse matrix(GA):\n {}".
        format(mouse_species.getChromosomeMatrix()))
        fitness_vector = np.array(
        hammingDist(goal,mouse_species.getChromosomeMatrix()),
        float)

        print("get fitness vector: {}".format(fitness_vector))
        if chromosome_length in fitness_vector:
            is_goal = True

```
