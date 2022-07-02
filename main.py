import random
import os
from goober import Goober, number_list

##
# Genetic representation of a solution
# A function to generate new solutions
# Fitness function
# Selection function
# Crossover function
# Mutation fuction
##

# Global variables
generation_size = 10
initial_generation = []
list_of_totals = []
selected_goobers = []
new_generation = []
generation_number = 2
gen_1_total = 0
generation_totals = []
list_of_averages = []


# General functions
def create_initial_generation(size):
    for _ in range(size):
        new_goober = Goober()
        initial_generation.append(new_goober)

def check_fitness(generation):
    for goober in generation:
        list_of_totals.append(goober.total)
        list_of_totals.sort()

def select_goobers(generation):
    for goober in generation:
        if goober.total == list_of_totals[-1]:
            selected_goobers.append(goober)
        elif goober.total == list_of_totals[-2]:
            selected_goobers.append(goober)

def crossover_and_mutation(goober1, goober2, mutation_rate, mutation_occurrence, crossover_amount, desired_new_population_size):
    copy_of_goober1_genome = goober1.genome
    copy_of_goober2_genome = goober2.genome

    genome_starting_position1 = random.randint(0, len(number_list)-1)
    genome_starting_position2 = random.randint(0, len(number_list)-1)

    shift = 0
    for _ in range(desired_new_population_size//2):
        for _ in range(crossover_amount):
            goober1.genome[genome_starting_position1 + shift] = copy_of_goober2_genome[genome_starting_position1 + shift]
            shift += 1
            if genome_starting_position1 + shift > len(number_list)-1:
                genome_starting_position1 = 0
                shift = 0
        new_goober = Goober()
        new_goober.genome = goober1.genome
        mutation_chance = random.randint(1, mutation_rate)
        if mutation_chance == 1:
            for _ in range(mutation_occurrence): 
                position = random.randint(0, len(new_goober.genome)-1)
                new_goober.genome[position] = random.randint(0, 1)
        new_generation.append(new_goober)
    

    shift = 0
    for _ in range(desired_new_population_size//2):
        for _ in range(crossover_amount):
            goober2.genome[genome_starting_position2 + shift] = copy_of_goober1_genome[genome_starting_position2 + shift]
            shift += 1
            if genome_starting_position2 + shift > len(number_list)-1:
                genome_starting_position2 = 0
                shift = 0
        new_goober = Goober()
        new_goober.genome = goober2.genome
        mutation_chance = random.randint(1, mutation_rate)
        if mutation_chance == 1:
            for _ in range(mutation_occurrence):
                position = random.randint(0, len(new_goober.genome)-1)
                if new_goober.genome[position] == 0:
                    new_goober.genome[position] = 1
        new_generation.append(new_goober)

def update_goober_totals(generation):
    for goober in generation:
        goober.update_total()

def reset_values():
    global initial_generation, list_of_totals, generation_totals, new_generation, selected_goobers, gen_1_total
    initial_generation = []
    list_of_totals = []
    generation_totals = []
    new_generation = []
    selected_goobers = []
    gen_1_total = 0

def clear_console():
    os.system('cls')


# Main functions
def first_generation(population_size, mutation_rate, mutation_occurrence, crossover_amount):
    global gen_1_total
    for goober in initial_generation:
        gen_1_total += goober.total
    check_fitness(initial_generation)
    select_goobers(initial_generation)
    crossover_and_mutation(selected_goobers[0], selected_goobers[1], mutation_rate, mutation_occurrence, crossover_amount, population_size)
    update_goober_totals(new_generation)

def subsequent_generation(population_size, mutation_rate, mutation_occurrence, crossover_amount):
    gen_total = 0
    global new_generation
    for goober in new_generation:
        gen_total += goober.total
    global generation_totals
    generation_totals.append(gen_total)
    check_fitness(new_generation)
    select_goobers(new_generation)
    new_generation = []
    crossover_and_mutation(selected_goobers[0], selected_goobers[1], mutation_rate, mutation_occurrence, crossover_amount, population_size)
    update_goober_totals(new_generation)
 
def percentage_change(start_gen_total, end_gen_total):
    if end_gen_total > start_gen_total:
        increase = ((end_gen_total - start_gen_total) / start_gen_total) * 100
        return increase
    elif start_gen_total > end_gen_total:
        decrease = ((start_gen_total - end_gen_total) / start_gen_total) * 100
        return decrease

def run_simulation(number_of_simulations, number_of_populations_per_simulation, population_size, mutation_rate, mutation_occurrence,
                  crossover_amount, change_number_of_populations_per_simulation, change_population_size_per_simulation,
                  change_mutation_rate_per_simulation, change_mutation_occurrence_per_simulation, change_crossover_amount_per_simulation):

    clear_console()

    list_of_parameters_which_can_change = [change_number_of_populations_per_simulation, change_population_size_per_simulation,
                                           change_mutation_rate_per_simulation, change_mutation_occurrence_per_simulation,
                                           change_crossover_amount_per_simulation]
    list_of_parameters_which_can_change_names = ['the number of populations per simulation', 'the population size',
                                                 'the mutation rate', 'the mutation occurrence', 'the crossover amount']
    parameter_number = 0
    number_of_parameters_changed = 0
    for parameter in list_of_parameters_which_can_change:
        if parameter != 0:
            number_of_parameters_changed +=1
            changed_parameter = list_of_parameters_which_can_change_names[parameter_number]
            changed_parameter_amount = list_of_parameters_which_can_change[parameter_number]
            if parameter > 0:
                changed_parameter_direction = 'increased'
            else:
                changed_parameter_direction = 'decreased'
        parameter_number += 1

    if number_of_parameters_changed == 0 and number_of_simulations == 1:
        print(f"{number_of_simulations} simulation with no changing parameters.")   
    elif number_of_parameters_changed == 0:
        print(f"{number_of_simulations} simulations where no parameters change between simulations.")
    elif number_of_parameters_changed > 0:
        parameters_changed_text = (f"{changed_parameter} {changed_parameter_direction} by {changed_parameter_amount}")
        simulation_text = (f"{number_of_simulations} simulations where {parameters_changed_text}")
        for _ in range(number_of_parameters_changed-1):
            simulation_text += (f"{parameters_changed_text}")
        print(f"{simulation_text} per simulation.")
    elif number_of_parameters_changed > 0 and number_of_simulations ==1:
        print("1 simulation where no parameters change.")
        print("Parameters cannot be changed with only 1 simulation.")

    simulation_number = 1
    for _ in range(number_of_simulations):
        print()
        print(f"Simulation: {simulation_number}")
        print()
        print(f"{number_of_populations_per_simulation} simulations where:")
        print(f"Population size: {population_size}")
        print("Genome length: 25")
        print(f"{crossover_amount} gene recombinations in each crossover event")
        print(f"Mutation_rate = 1/{mutation_rate} and Mutation_occurrence = {mutation_occurrence}")
        print()
        generation_count_total = 0
        for _ in range(number_of_populations_per_simulation):
            create_initial_generation(population_size)
            first_generation(population_size, mutation_rate, mutation_occurrence, crossover_amount)
            subsequent_generation(population_size, mutation_rate, mutation_occurrence, crossover_amount)
            generation_count = 2
            while generation_totals[-1]/generation_size < 325:
                subsequent_generation(population_size, mutation_rate, mutation_occurrence, crossover_amount)
                generation_count += 1
            generation_count_total += generation_count
            reset_values()
            print(f"Generations needed to reach solution: {generation_count}")
        print(f"Average number of generations required across simulations = {generation_count_total/10}")
        print()
        print()
        simulation_number += 1
        list_of_averages.append(generation_count_total/10)
        if change_number_of_populations_per_simulation != 0:
            number_of_populations_per_simulation += change_number_of_populations_per_simulation

        if change_population_size_per_simulation != 0:
            population_size += change_population_size_per_simulation
        
        if change_mutation_rate_per_simulation != 0:
            mutation_rate += change_mutation_rate_per_simulation

        if change_mutation_occurrence_per_simulation != 0:
            mutation_occurrence += change_mutation_occurrence_per_simulation 

        if change_crossover_amount_per_simulation != 0:
            crossover_amount += change_crossover_amount_per_simulation
    print()

    list_of_averages_position = 1
    for average in list_of_averages:
        print(f"Simulation {list_of_averages_position} average: {average}")
        list_of_averages_position += 1
    if list_of_averages[0] < list_of_averages[-1]:
        change_type = 'increase'
    else:
        change_type = 'decrease'
    print(f"Percentage change between simulation 1 and {number_of_simulations}: {percentage_change(list_of_averages[0], list_of_averages[-1])}% {change_type}.")
    print()

def start_program():

    clear_console()

    print("This is an evolution simulation using a genetic algorithm.")
    print()
    print("Each 'Goober' has a randomly generated genome consisting of 1's and 0's, with a length of 25.")
    print("Where a 1 appears in the Goobers genome, the corresponding number in a list of numbers from 1-25 is picked.")
    print("Where a 0 appears in the Goobers genome, the corresponding number in a list of numbers from 1-25 is not picked.")
    print("A Goober wants to get the highest number possible from its genome, with the maximum being 325.")
    print()
    print("After each generation, the two Goobers with the highest totals are selected for breeding.")
    print("At a random point along the length of one Goobers genome a snippit of desired length will be swapped")
    print("with a snippit of the same length from a random point along the second Goobers genome.")
    print()
    print("After this recombination a mutation may occur in either of these parent Goobers genomes.")
    print("A random point on the genome is chosen and the gene is then randomly swapped to a 1 or 0.")
    print("The rate at which this may occur is the 'mutation rate'. Denonted by a 1/X chance.")
    print("The number of points chosen to have their genes swapped is the 'mutation occurrence'.")
    print()
    print("After the recombination and potential mutation of the parent Goobers they are both multiplied up to")
    print("account for half of the second generations total population.")
    print("This process is then repeated until a Goober reaches the maximum for their genome total.")
    print()
    print("Running multiple simulations back to back with multiple populations allows for the average")
    print("number of generations needed in each population to reach the maximum to be recored.")
    print("This allows us to see the percentage change in average time taken to reach the maximum.")
    print("Combined with changing various parameters such as mutation rate/occurrence between simulations, we can see what")
    print("changes to a Goobers genome allow it to reach the maximum value the fastest, or the slowest!")
    print()
    print()

    ready_to_begin = input("Are you ready to begin running your own simulations? Type 'y' for yes or 'n' for no.")
    if ready_to_begin == 'y':

        clear_console()

        desired_number_of_simulations = int(input("How many separate simulations would you like to run? "))
        desired_number_of_populations = int(input("How many populations would you like per simulation? "))

        desired_population_size = int(input("How large would you like each population to be in each simulation? "))
        while desired_population_size % 2 != 0:
            print("Population size must be divisible by 2. Please choose another number.")
            desired_population_size = int(input("How large would you like each population to be in each simulation? "))

        desired_mutation_rate = int(input("What would you like the mutation rate to be per simulation? "))
        desired_mutation_occurrence = int(input("What would you like the mutation occurrence to be per simulation? "))
        desired_cross_over_amount = int(input("What would you like the rate of crossover to be per simulation? "))

        change_number_of_populations = input("Would you like to change the number of populations per simulation? Type 'y' for yes or 'n' for no.")
        if change_number_of_populations == 'y':
            change_number_of_populations_amount = int(input("Change the number of populations per simulations by: "))
        else:
            change_number_of_populations_amount = 0

        change_population_size = input("Would you like to change the population size per simulation? Type 'y' for yes or 'n' for no.")
        if change_population_size == 'y':
            change_population_size_amount = int(input("Change the population size per simulation by: "))
        else:
            change_population_size_amount = 0

        change_muation_rate = input("Would you like to change the mutation rate per simulation? Type 'y' for yes or 'n' for no.")
        if change_muation_rate == 'y':
            change_muation_rate_amount = int(input("Change the muation rate per simulation by: "))
        else:
            change_muation_rate_amount = 0

        change_muation_occurrence = input("Would you like to change the muation occurrence per simulation? Type 'y' for yes or 'n' for no.")
        if change_muation_occurrence == 'y':
            change_muation_occurrence_amount = int(input("Change the mutation occurrence per simulation by: "))
        else:
            change_muation_occurrence_amount = 0

        change_crossover = input("Would you like to change the crossover amount per simulation? Type 'y' for yes or 'n' for no.")
        if change_crossover == 'y':
            change_crossover_amount = int(input("Change the crossover amount per simulation by: "))
        else:
            change_crossover_amount = 0

        run_simulation(desired_number_of_simulations, desired_number_of_populations, desired_population_size,
                    desired_mutation_rate, desired_mutation_occurrence, desired_cross_over_amount,
                    change_number_of_populations_amount, change_population_size_amount, change_muation_rate_amount,
                    change_muation_occurrence_amount, change_crossover_amount)
    
    else:
        ready_to_quit = input("Would you like to quit? Type 'y' for yes or 'n' for no.")
        if ready_to_quit == 'y':
            clear_console()
            print("Goodbye!")
        else:
            start_program()

start_program()        
