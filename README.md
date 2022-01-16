# DarwinPy

## Introduction
DarwinPy is an evolutionary computation module built with python, to enable you to easily
implement evolutionary methods such as genetics algorithm and evolutionary strategies with
few lines of code.

## Installing DarwinPy
DarwinPy can be installed with the command below
 ` pip install DarwinPy
 `

## Classes in DarwinPy

### Genetics Classes (DarwinPy.Genetics.Genetics)

#### Methods

DarwinPy.Genetics.Genetics.**setSearchSpace**(search_space)
Sets the search_space attribute of the DarwinPy object.

DarwinPy.Genetics.Genetics.**setChromosomeLength**(chromosome_length)
Sets the chromosome_length attribute of the DarwinPy object.

DarwinPy.Genetics.Genetics.**setPopulationSize**(population_size)
Sets the population_size attribute of the DarwinPy object.

DarwinPy.Genetics.Genetics.**setChromosomeMatrix**(search_space)
Sets the chromosome_matrix attribute of the DarwinPy object.

DarwinPy.Genetics.Genetics.**getChromosomeMatrix**()
Returns the chromosome_matrix which is a numpy array.

DarwinPy.Genetics.Genetics.**getSearchSpace**()
Returns the search_space which is tuple (more specifically a pair).

DarwinPy.Genetics.Genetics.**populate**()
Sets the initial values in the chromosome_matrix attribute or more specifically initialize the gene population.

DarwinPy.Genetics.Genetics.**select**(fitness_vector)
Selects mating pairs with respect the fitness.

DarwinPy.Genetics.Genetics.**crossover**(crossover_rate)
Performs mating between two selected mating pairs, which in turn updates the chromosome_matrix attribute

DarwinPy.Genetics.Genetics.**mutate**(mutation_rate)
Mutates the chromosome_matrix attribute of the DarwinPy object.


DarwinPy.Genetics.Genetics.**evolve**(fitness_vector, mutation_rate, crossover_rate)
Performs the a complete genetic algorithm cycle, which includes selection, crossover and mutation.




| Identifier | Type |
| ------------ | ---------- |
| setSearchSpace | None |
|setChromosomeLength| None |
|setPopulationSize| None |
|setChromosomeMatrix| None |
|getChromosomeMatrix| numpy.array |
|getSearchSpace| tuple |
|populate | None|
|select| None |
|crossover| None |
|mutate| None |
|evolve| None |
Table 1. Methods and their respective return type


#### Attributes

DarwinPy.Genetics.Genetics.**chromosome_length**
The length of each chromosome in the DarwinPy object.

DarwinPy.Genetics.Genetics.**population_size**
The size of the population in the DarwinPy object.

DarwinPy.Genetics.Genetics.**search_space**
The search space for the genetic algorithm which is a tuple with a upper and lower bound.

DarwinPy.Genetics.Genetics.**chromosome_matrix**
The array of chromosome in the DarwinPy object.

DarwinPy.Genetics.Genetics.**pair_list**
The list of mating pairs.

DarwinPy.Genetics.Genetics.**data_type**
The data type in which the genetic algorithm is bounded within.




| Identifier | Type |
| ------------ | ---------- |
|chromosome_length | int |
|population_size | int |
|search_space | tuple |
|chromosome_matrix | numpy.array |
|pair_list | list |
|data_type | type |
Table 2. Attributes and their respective data type


## A Sample DarwinPy implementation
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
