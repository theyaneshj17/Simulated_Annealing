# Simulated_Annealing

## Project Description

This project focuses on solving an optimization problem involving the assignment of students to project teams based on their preferences and constraints. The objective is to assign students to teams while minimizing the total cost, considering factors such as:

- **Base cost**: Each team incurs a fixed cost.
- **Penalties** for assigning students to teams that either do not meet their preferred teammates or include prohibited teammates.
- **Penalties** for incorrect team sizes, as teams can consist of 1-3 members.

The solution leverages the **Simulated Annealing** optimization algorithm to efficiently search for an optimal assignment. Simulated Annealing is a probabilistic technique that allows the exploration of a large solution space by gradually decreasing the probability of accepting worse solutions, helping the algorithm escape local optima and converge towards a globally optimal solution.

The project uses a custom script that:
- **Reads input data** about students' preferences and constraints.
- **Generates a random initial assignment** of students to teams.
- **Iterates** through potential assignments, modifying them by swapping students between teams to improve the overall cost.
- **Outputs the best assignment** found during the search process, with details about the total cost and the students' team assignments.

This project serves as an example of how advanced search heuristics can be applied to real-world problems in areas such as resource allocation, project management, and team formation, where constraints and preferences must be balanced.

## Abstraction of the Problem

1. **Valid States**: Groups of students where each group can contain up to 3 members, with each student belonging to exactly one group. Each student has preferences and prohibitions for teammates.

2. **Initial State**: A set of students with their:
   - Requested teammates
   - Prohibited teammates
   - Desired team size (1-3 members)

3. **Goal State**: An optimal assignment of students to teams that minimizes the total cost, considering:
   - Base grading cost per team (k)
   - Penalties for prohibited teammate assignments (m)
   - Penalties for unmet teammate requests (n)
   - Penalties for incorrect team sizes (+1)

4. **Cost Function**: Total cost is calculated as:
   - Base cost: k × number of teams
   - Plus penalties for:
     - Wrong team size (1 point per violation)
     - Unmet teammate requests (n points each)
     - Prohibited teammate assignments (m points each)

## Algorithm Followed

1. **Simulated Annealing Algorithm**:
   - Uses temperature-based probability for accepting worse solutions
   - Gradually decreases temperature to converge on optimal solution

    a) Starts with a random assignment of people to teams.  
    b) Iteratively modifies the assignment by swapping people between teams.  
    c) Accepts new assignments based on a probability that decreases over time (simulated annealing).  
    d) Keeps track of the best solution found so far.

## Implementation Approach

1. **parseInputTeamsFile(filename)**:
   - Reads the input file and parses the student preferences
   - Stores the preferred group size, preferred teammates, and not preferred teammates for each student

2. **calculate_cost(students_expectation, groups)**:
   - Calculates the total cost of the current assignment
   - Considers group size mismatch, assignment of preferred teammates, and assignment of non-preferred teammates

3. **FormRandomGroups(students_expectations)**:
   - Generates a random initial assignment of students to groups
   - Forms a limited number of groups by maximizing the number of students in each group to minimize cost value (k=30)

4. **getRandomNeighbors(original)**:
   - Generates a new assignment by randomly swapping two students between groups

5. **printoutput(groups, cost)**:
   - Formats the final assignment and cost into a dictionary

6. **solver(input_file)**:
   - The core function that orchestrates the algorithm, iterates through solutions, and applies simulated annealing to minimize the total cost

## Assumptions

1. **Parameters Considered**:
   - k=30
   - m=20
   - n=10

2. **Simulated Annealing Parameters**:
   - Initial temperature: 1.0
   - Cooling rate (Temperature Decreasing Rate): 0.995
   - Minimum Temperature: 0.0001

## Conclusion

This implementation provides an efficient solution to the team assignment problem using simulated annealing. It effectively balances multiple constraints and preferences while maintaining reasonable computational complexity. The program can handle various team sizes and student constraints while minimizing the total cost of assignments.

## How to Run

1. Download or clone the repository.
2. Ensure that Python 3 is installed on your system.
3. Prepare the input file with student preferences and constraints in the format specified in the assignment.
4. Run the script with the following command:

```bash
python assign.py <input_filename>
