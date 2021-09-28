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
    processes = 3
    mouse_population = 5
    mutation_rate = 0.5
    search_space = (0,1)
    goal = np.array([1,0,1,1,0,1,1, 0,1,1,0],int)
    chromosome_length = len(goal)

    # mouse_species = (
    # DarwinPy.DarwinPyCore(processes, "Genetics"))
    #
    # mouse_species.initializeGenetics(chromosome_length,
    # mouse_population,search_space,int)
    #
    # print(mouse_species)
    #
    # print(mouse_species.getChromosomeMatrixList())
    # chromosome_matrix_list = mouse_species.getChromosomeMatrixList()
    # fitness_matrix = np.array([[0]*mouse_population]*processes,float)
    #
    # for i in range(processes):
    #     # print("Oh!")
    #     # print(chromosome_matrix_list[i])
    #     fitness_matrix[i] = hammingDist(goal, chromosome_matrix_list[i])
    #
    # print(fitness_matrix)
    #
    # is_goal = False
    # gen = 1
    # while not is_goal:
    #     print("Generation #{}\n".format(gen))
    #     gen += 1
    #     mouse_species.evolve(fitness_matrix,
    #     mutation_rate, 0.5)
    #     print("get mouse matrix:\n {}".
    #     format(mouse_species.getChromosomeMatrixList()))
    #     for i in range(processes):
    #         fitness_matrix[i] = hammingDist(goal,
    #         chromosome_matrix_list[i])
    #     print("get fitness matrix: {}".format(fitness_matrix))
    #     i = 0
    #     # is_goal = True
    #     while (not is_goal) and (i < processes):
    #         if chromosome_length in fitness_matrix[i]:
    #             is_goal = True
    #         i += 1


    # mouse_species_async.populateInstancesGenetics()

    # print(mouse_species_async.getGenerationMatrices())

    # chromosome_length = 8
    # mouse_population = 5
    # mutation_rate = 0.05
    #
    mouse_species = DarwinPy.Genetics.Genetics(chromosome_length,
    mouse_population, (0,1), int)
    print("mouse species instantiated:\n {}".format(mouse_species))

    # goal = np.array([1,0,1,1,0,1,1, 0],int)

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


    # mouse_parent = 5
    # mouse_children = 3
    # mouse_species = DarwinPy.EvolutionaryStrategy.EvolutionaryStrategy(chromosome_length,
    # mouse_parent, mouse_children, (0,1), int)
    # print(mouse_species)
    # print("\n")
    # mouse_species.generateParent()
    # print("get (parent) mouse matrix(ES):\n {}".
    # format(mouse_species.getParentGeneration()))
    #
    # gen = 1
    # is_goal = False
    # while not is_goal:
    #     print("Generation #{}\n".format(gen))
    #     fitness_vector_1 = np.array(
    #     hammingDist(goal,mouse_species.getParentGeneration()),
    #     float)
    #
    #     print("get parent fitness(ES): {}".
    #     format(fitness_vector_1))
    #
    #     mouse_species.generateOffspring(mutation_rate, fitness_vector_1)
    #     print("get (children) mouse matrix(ES):\n {}".
    #     format(mouse_species.getChildrenGeneration()))
    #
    #     fitness_vector_2 = np.array(
    #     hammingDist(goal,mouse_species.getChildrenGeneration()),
    #     float)
    #
    #     print("get children fitness(ES): {}".
    #     format(fitness_vector_2))
    #
    #     mouse_species.selectNextGeneration(fitness_vector_1,fitness_vector_2)
    #     print("get (parent) mouse matrix(ES):\n {}".
    #     format(mouse_species.getParentGeneration()))
    #     gen += 1
    #     if chromosome_length in fitness_vector_1:
    #         is_goal = True
