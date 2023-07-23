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
        elif choice == "S":
            filename = input("Enter filename to save to: ")
            save_projects(filename, projects)
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
        file.readline()
        for line in file:
            name, start_date, priority, cost_estimate, completion_rate = line.strip().split('\t')
            cost_estimate = float(cost_estimate)
            completion_rate = int(completion_rate)
            priority = int(priority)
            project = Project(name, start_date, cost_estimate, completion_rate, priority)
            projects.append(project)
    print(f"Loaded {filename}")
    return projects


def save_projects(filename, projects):
    """Save projects to the given file"""
    with open(filename, 'w') as file:
        for project in projects:
            file.write(f"{project.name}\t{project.start_date}\t{project.priority}\t"
                       f"{project.cost_estimate}\t{project.completion_rate}\n")
    print(f"Saved to {filename}")


main()