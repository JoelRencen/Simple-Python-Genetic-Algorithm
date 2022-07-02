import random

number_list = []
for _ in range(26):
    number_list.append(_)

# Maximum value possible if all genes are '1' = 325

class Goober():

    def __init__(self):
        self.genome = []
        self.generate_genome()
        self.total = self.determine_total_number()

    def generate_genome(self):
        for _ in range(len(number_list)):
           self.genome.append(random.randint(0, 1))

    def determine_total_number(self):
        position = 0
        total = 0
        for number in number_list:
            if self.genome[position] == 1:
                total += number
            position += 1
        return total
    
    def update_total(self):
