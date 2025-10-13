FILENAME = "subject_data.txt"

def main():
    """Read data file and display subject details."""
    subject_details = load_subjects()
    display_subjects(subject_details)


def load_subjects():
    """Read file and return a list of subject details."""
    subjects = []
    with open(FILENAME, "r") as input_file:
        for line in input_file:
            parts = line.strip().split(',')
            parts[2] = int(parts[2])  # convert number of students to int
            subjects.append(parts)
    return subjects


def display_subjects(subjects):
    """Display each subject's details."""
    for subject in subjects:
        code, lecturer, students = subject
        print(f"{code} is taught by {lecturer} and has {students} students")


main()
