"""
CP1404/CP5632 Practical - Project Management Program
ESTIMATE: 1:30hr
ACTUAL:
"""
from project import Project
FILENAME = "projects.txt"


MENU = """
- (L)oad projects  
- (S)ave projects  
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit
"""


def main():
    projects = load_projects(FILENAME)
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            filename = input("Enter filename to load: ")
            projects = load_projects(filename)
        elif choice == "R":
            recommend_place(places)  # Recommends a random unvisited place
        elif choice == "A":
            add_new_place(places)  # Allow user to add new place
        elif choice == "M":
            mark_place(places)  # Mark place as visited
        else:
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>> ").upper()  # Overwrite and save places to csv file
    print("Thank you.")


def load_projects(filename):
    """Load project from given file"""
    projects = []
    with open(filename, 'r') as file:
        file.readlines()
        for line in file:
            name, start_date, priority, cost_estimate, completion_percentage = line.strip().split('\t')
            cost_estimate = float(cost_estimate)
            completion_percentage = int(completion_percentage)
            priority = int(priority)
            project = Project(name, start_date, cost_estimate, completion_percentage, priority)
            projects.append(project)
    return projects



main()