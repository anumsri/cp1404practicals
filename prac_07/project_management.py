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
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            date_str = input("Enter the date to filter: ")
            filter_by_date(projects, date_str)
        elif choice == "F":
            date_str = input("Enter the date to filter: ")
            filter_by_date(projects, date_str)
        elif choice == "A":
            add_project(projects)
        elif choice == "U":
            update_projects(projects)
        else:
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def update_projects(projects):
    """Update existing functions completion rate and priority"""
    for i, project in enumerate(projects):
        print(i, project)
    choice = int(input("Project choice: "))
    new_percentage = input("New Percentage: ")
    new_priority = input("New Priority: ")
    if new_percentage != "":
        projects[choice].completion_percentage = int(new_percentage)
    if new_priority != "":
        projects[choice].priority = int(new_priority)


def add_project(projects):
    """Add a new project to the list"""
    print("Lets add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: "))
    completion_rate = int(input("Percent complete: "))
    project = Project(name, start_date, cost_estimate, completion_rate, priority)
    projects.append(project)


def filter_by_date(projects, date_str):
    """Filter projects by given date"""
    print(f"Enter Date (dd/mm/yyyy): {date_str}")
    filtered_projects = []
    for project in projects:
        if project.start_date > date_str:
            filtered_projects.append(project)
    if filtered_projects:
        for project in filtered_projects:
            print(f"{project.name}, start: {project.start_date}, priority {project.priority}, "
                  f"estimate: ${project.cost_estimate:.2f}, completion: {project.completion_rate}%")
    else:
        print("No projects found!")


def display_projects(projects):
    """List incomplete and completed projects formatted"""
    projects.sort()
    print("Incomplete projects:")
    incomplete_projects = [project for project in projects if project.completion_rate < 100]
    for incomplete_project in incomplete_projects:
        print(incomplete_project)
    completed_projects = [project for project in projects if project.completion_rate >= 100]
    print("Completed projects:")
    for completed_project in completed_projects:
        print(completed_project)


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