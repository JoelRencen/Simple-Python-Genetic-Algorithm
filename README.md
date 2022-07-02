# Simple-Python-Genetic-Algorithm
A simple genetic algorithm I created to see how a population of 'Goobers' will solve a simple maths problem through multiple generations with crossingover events and random mutation.

Each 'Goober' has a randomly generated genome consisting of 1's and 0's, with a length of 25.
Where a 1 appears in the Goobers genome, the corresponding number in a list of numbers from 1-25 is picked.
Where a 0 appears in the Goobers genome, the corresponding number in a list of numbers from 1-25 is not picked.
A Goober wants to get the highest number possible from its genome, with the maximum being 325.

After each generation, the two Goobers with the highest totals are selected for breeding.
At a random point along the length of one Goobers genome a snippit of desired length will be swapped with a snippit of the same length from a random point along the second Goobers genome.

After this recombination a mutation may occur in either of these parent Goobers genomes.
A random point on the genome is chosen and the gene is then randomly swapped to a 1 or 0.
The rate at which this may occur is the 'mutation rate'. Denonted by a 1/X chance.
The number of points chosen to have their genes swapped is the 'mutation occurrence'.

After the recombination and potential mutation of the parent Goobers they are both multiplied up to account for half of the second generations total population.
This process is then repeated until a Goober reaches the maximum for their genome total.

Running multiple simulations back to back with multiple populations allows for the average number of generations needed in each population to reach the maximum to be recored.
This allows us to see the percentage change in average time taken to reach the maximum.
Combined with changing various parameters such as mutation rate/occurrence between simulations, we can see what changes to a Goobers genome allow it to reach the maximum value the fastest, or the slowest!

'

Recommended starting values:

- A population size of 10. This value should always be divisible by 2.

- A mutation rate of 5, (denoting a 1/5 change to mutate).

- A mutation occurrence of 4.

- A crossover rate of 6.

When increasing or decreasing any parameters between simulations, only increase/decrease by a whole number. And check that if you are decreasing a parameter each simulation, you make sure no simulations will have a mutation rate lower than 1/1 chance or that mutation occurrence/crossover rate do no exceed 25.
