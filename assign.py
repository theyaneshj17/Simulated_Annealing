#!/usr/local/bin/python3
# assign.py : Assign people to teams
#
# Code by: name IU ID
#
# Based on skeleton code for CSCI-B551
#

import sys
import time

import random
import math


def parseInputTeamsFile(filename):

    student_expectation ={}

    with open(filename) as file:
        
        
        
        for line in file:

            
            sentence = line.strip().split()
            
            #print(sentence)

            userid = sentence[0]

            preferred_teammates  = sentence[1]

            not_preferred_teammates = sentence[2]

            pref =[]
            pref_count =1

            if '-' in preferred_teammates:

                indv_ids = preferred_teammates.split('-')

                pref_count = len(indv_ids)

                for indv_id in indv_ids:

                    if indv_id not in ('zzz') and indv_id != userid:        

                        pref.append(indv_id)

                #print(1, pref,pref_count)

            
            non_pref =[]
            
            if not_preferred_teammates != '_':

                indv_ids = not_preferred_teammates.split(',')

                for indv_id in indv_ids:

                        non_pref.append(indv_id)


            student_expectation[userid] ={
                'preferred_groupsize': pref_count,
                'preferred_teammates': pref,
                'not_preferred_teammates':non_pref
                }

    #print(students)

    return student_expectation

def calculate_cost(students_expectation, groups):
    
    k=30
    m=20
    n=10
      
    
    cost = len(groups) * k
    
    students_reality ={}
    for indv_group in groups:
        for indv_id in indv_group:
            students_reality[indv_id] = indv_group



    



    
    for indv_id, attributes in students_expectation.items():

        #Group Size mismatch +1 cost
        #print (indv_id)
        #print(attributes['preferred_groupsize'])
        #print(students_reality[indv_id])

        if len(students_reality[indv_id]) != attributes['preferred_groupsize']:


            #cost += abs(len(students_reality[indv_id]) - attributes['preferred_groupsize'] )

            cost +=1

            #print(indv_id, cost )

        #Cost for not assigning someone, who is requested (n =10)

        for preferred in attributes['preferred_teammates']:

            if preferred not in students_reality[indv_id]:



                cost+= n

                #print(indv_id, preferred, cost )

        #Cost for  assigning someone, who is not requested (n =10)

        for not_preferred in attributes['not_preferred_teammates']:

            if not_preferred in students_reality[indv_id]:



                cost+= m

                #print(indv_id, not_preferred, cost )

    return cost



def FormRandomGroups(students_expectations): 
   

    #random.seed(23)
   
    students = list(students_expectations.keys())
    
   
    random.shuffle(students)
    
   
    randomFinalGroup = []
    
    
    curr = []

    for indv in students:

        curr.append(indv)  
        

        #Form Limited number of groups by maximizing no of students in each group
        #to minimize cost value as k=30
        if len(curr) == 3:

            randomFinalGroup.append(curr) 
            
            
            curr = []  
    

    if len(curr) > 0: #Remaining students, if any
         
        randomFinalGroup.append(curr)
    

    return randomFinalGroup


def getRandomNeighbors(original):

    modified = []
    for group in original:
        modified.append(group[:])
        
    all_students = []

    
    for i, group in enumerate(modified):
       
        for student in group:
            
            all_students.append((i, student))
        

    student1, student2 = random.sample(all_students, 2)
    
    # Extract their indices
    group1_index, student1_name = student1
    group2_index, student2_name = student2
    
    # Swap the students
    modified[group1_index].remove(student1_name)
    modified[group2_index].remove(student2_name)
    modified[group1_index].append(student2_name)
    modified[group2_index].append(student1_name)
    
    return modified

def printoutput(groups, cost):
    
    result = {}

    final_group = []

   
    for group in groups:
       
        sorted_group = sorted(group)
        
        group_string = '-'.join(sorted_group)
        
        final_group.append(group_string)

    result["assigned-groups"] = final_group
    result["total-cost"] = cost


    return result



def solver(input_file):
    """
    1. This function should take the name of a .txt input file in the format indicated in the assignment.
    2. It should return a dictionary with the following keys:
        - "assigned-groups" : a list of groups assigned by the program, each consisting of usernames separated by hyphens
        - "total-cost" : total cost (time spent by instructors in minutes) in the group assignment
    3. Do not add any extra parameters to the solver() function, or it will break our grading and testing code.
    4. Please do not use any global variables, as it may cause the testing code to fail.
    5. To handle the fact that some problems may take longer than others, and you don't know ahead of time how
       much time it will take to find the best solution, you can compute a series of solutions and then
       call "yield" to return that preliminary solution. Your program can continue yielding multiple times;
       our test program will take the last answer you 'yielded' once time expired.
    """
    k, m, n = 30, 20, 10 


    students_expectations = parseInputTeamsFile(input_file)

    students_reality_groups = FormRandomGroups(students_expectations)

    current = students_reality_groups

    best_solution = students_reality_groups

    best_solution_cost = calculate_cost(students_expectations, students_reality_groups)


    yield printoutput(students_reality_groups, best_solution_cost)


        #Minimize cost using Simulated Annealing Algorithm

    temp = 1.0
    
    
    min_temp = 0.0001

    decreasingRate = 0.995
    
    while temp > min_temp:
        
        modified = getRandomNeighbors(current)



        current_cost = calculate_cost(students_expectations,current)

        new_cost = calculate_cost(students_expectations,modified)
        
        # Accept new solution if minimum cost or based on probability (e^-deltaE/T)
        
        if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / temp):
            
            current = modified
            
            current_cost = new_cost
            

            if current_cost < best_solution_cost:

                best = modified

                best_solution_cost = current_cost
                
                yield printoutput(best, best_solution_cost)
        
        temp = temp * decreasingRate



if __name__ == "__main__":
    if(len(sys.argv) != 2):
        raise(Exception("Error: expected an input filename"))

    for result in solver(sys.argv[1]):
        print("----- Latest solution:\n" + "\n".join(result["assigned-groups"]))
        print("\nAssignment cost: %d \n" % result["total-cost"])
    
