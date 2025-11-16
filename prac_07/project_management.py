"""
CP1404 Practical - Project Management Program
Estimated time: 3.5 hours
Actual time: 3 hours
"""

import datetime
from project import project

DEFAULT_FILENAME = "projects.txt"
MENU = """- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit
"""


def main():
    """Run the Project Management program."""
    print("Welcome to Pythonic Project Management")

    projects = load_projects(DEFAULT_FILENAME)
    print(f"Loaded {len(projects)} projects from {DEFAULT_FILENAME}")

    choice = ""
    while choice != "Q":
        print(MENU)
        choice = input(">>> ").strip().upper()

        if choice == "L":
            filename = input("Filename to load from: ")
            projects = load_projects(filename)
        elif choice == "S":
            filename = input("Filename to save to: ")
            save_projects(filename, projects)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects_by_date(projects)
        elif choice == "A":
            add_new_project(projects)
        elif choice == "U":
            update_project(projects)
        elif choice == "Q":
            save_choice = input(f"Would you like to save to {DEFAULT_FILENAME}? ").lower()
            if save_choice.startswith("y"):
                save_projects(DEFAULT_FILENAME, projects)
            print("Thank you for using custom-built project management software.")
        else:
            print("Invalid choice")


def load_projects(filename):
    """Load projects from a tab-delimited file into a list of Project objects."""
    projects = []
    try:
        with open(filename, "r", encoding="utf-8") as in_file:
            in_file.readline()  # Skip header line
            for line in in_file:
                line = line.strip()
                if not line:
                    continue
                # Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage
                name, date_string, priority_str, cost_str, completion_str = line.split('\t')
                start_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
                priority = int(priority_str)
                cost_estimate = float(cost_str)
                completion_percentage = int(completion_str)
                project = Project(name, start_date, priority, cost_estimate, completion_percentage)
                projects.append(project)
    except FileNotFoundError:
        print(f"File '{filename}' not found. Starting with no projects.")
    return projects


def save_projects(filename, projects):
    """Save projects to a tab-delimited file."""
    with open(filename, "w", encoding="utf-8") as out_file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
        for project in projects:
            date_string = project.start_date.strftime("%d/%m/%Y")
            print(f"{project.name}\t{date_string}\t{project.priority}\t"
                  f"{project.cost_estimate}\t{project.completion_percentage}", file=out_file)


def display_projects(projects):
    """Display incomplete and completed projects, each sorted by priority."""
    incomplete = [p for p in projects if not p.is_complete()]
    complete = [p for p in projects if p.is_complete()]

    incomplete.sort()
    complete.sort()

    print("Incomplete projects:")
    for project in incomplete:
        print(f"  {project}")

    print("Completed projects:")
    for project in complete:
        print(f"  {project}")


def filter_projects_by_date(projects):
    """Display projects that start after a given date, sorted by start date."""
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    try:
        filter_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    except ValueError:
        print("Invalid date format")
        return

    filtered = [p for p in projects if p.start_date > filter_date]
    filtered.sort(key=lambda p: p.start_date)

    for project in filtered:
        print(project)


def add_new_project(projects):
    """Prompt user for new project details and add to the list."""
    print("Let's add a new project")
    name = input("Name: ")
    date_string = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion_percentage = int(input("Percent complete: "))

    start_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(project)


def update_project(projects):
    """Update the completion percentage and/or priority of a chosen project."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")

    try:
        choice = int(input("Project choice: "))
        project = projects[choice]
    except (ValueError, IndexError):
        print("Invalid project choice")
        return

    print(project)
    new_completion = input("New Percentage: ")
    if new_completion != "":
        project.completion_percentage = int(new_completion)

    new_priority = input("New Priority: ")
    if new_priority != "":
        project.priority = int(new_priority)


if __name__ == "__main__":
    main()
