import random
import copy
import math
import numpy as np
import time

#this function calculates number of attacking pairs
def fitness(individual):
    conflicts = 0
    sideways = abs(len(individual) - len(np.unique(individual)))
    conflicts = conflicts + sideways    
    for i in range(len(individual)):
        x=1
        for j in range(i+1, len(individual)):
            
            if (individual[i]+x==individual[j] or individual[i]-x==individual[j]):
                conflicts+=1
            x+=1
    return conflicts
def crossover(individual1, individual2):
    if(random.random()<crossover_prob):
        n = len(individual1)
        c = random.randint(0, n - 1)
        return individual1[0:c] + individual2[c:n]
    else:
        return individual1


def mutation(individual):
    if(random.random()<mutation_prob):
        n = len(individual)
        c = random.randint(0, n - 1)
        m = random.randint(1, n)
        individual[c] = m
    return individual
    

def generate_individual(n):#this got input as no. of queens
    result = list(range(1, n + 1))#a list of 8 numbers is generated
    np.random.shuffle(result)#lets shuffle it for randomness
    return result#give it back

class Genetic(object):

    def __init__(self, n ,pop_size):#lets create population
        #initializing a random individuals with size of initial population entered by user
        self.queens = []#basically it will have lists of every individual constituting the whole population
        for i in range(pop_size):#whatever no. of individuals we wanted in our population
            self.queens.append(generate_individual(n))#so lets keep appending every individual
        print('queens:',self.queens)

    #generating individuals for a single iteration of algorithm
    def generate_population(self, random_selections=5):#here i've defined random selections
        candid_parents = []
        candid_fitness = []
        #getting individuals from queens randomly for an iteration
        for i in range(random_selections): #5
            candid_parents.append(self.queens[random.randint(0, len(self.queens) - 1)])#here i am selecting 1 individual from queens list randomly
            candid_fitness.append(fitness(candid_parents[i]))
        sorted_fitness = copy.deepcopy(candid_fitness)
        a_zip = zip(candid_parents, candid_fitness)
        zipped_list = list(a_zip)
        res = sorted(zipped_list, key = lambda x: x[1])
        aa = res[0][0]
        bb = res[1][0]
        x = crossover(aa,bb)
        x1 = mutation(x)
        #in code below check if each child is better than each one of queens individuals, set that individual the new child
        for i in range(len(self.queens)):
            if fitness(x1) < fitness(self.queens[i]):
                tvalue = 1
            else:
                tvalue = 0
                break
        if(tvalue == 1):
            self.queens.append(x1)

        #print('final : ',self.queens)
    def finished(self):
        d =[]
        for i in self.queens:
            if (fitness(i)==0):
                d=[1]
                d.append(i)
                return d
        if (len(d)==0):
            d = [0]
            return d
            #we check if for each queen there is no attacking(cause this algorithm should work for n queen,
            # it was easier to use attacking pairs for fitness instead of non-attacking)
            

    def start(self, random_selections=5):
        #generate new population and start algorithm until number of attacking pairs is zero
        while not self.finished()[0]:
            self.generate_population(random_selections)
        final_state = self.finished()
        print(('Solution : ' + str(final_state[1])))
        

#******************** N-Queen Problem With GA Algorithm ***********************
start_time = time.time()
n=(int)(input('Enter the value of N \n-'))
initial_population=(int)(input('Enter initial population size \n-'))
crossover_prob = (float)(input('Enter crossover probability \n-'))
mutation_prob = (float)(input('Enter mutation probability\n-'))
algorithm = Genetic(n=n,pop_size=initial_population)
algorithm.start()
print("--- %s seconds ---" % (time.time() - start_time))