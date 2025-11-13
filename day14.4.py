import csv

def enter_score():
    """Allows the user to enter quiz scores and saves them to scores.csv."""
    student_name = input("Enter student name: ")
    subject = input("Enter subject: ")
    while True:
        try:
            score = int(input("Enter score: "))
            if 0 <= score <= 100:
                break
            else:
                print("Score must be between 0 and 100.")
        except ValueError:
            print("Invalid score. Please enter a number.")

    with open('scores.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([student_name, subject, score])
    print("Score saved successfully!")

def view_scores():
    """Displays all stored quiz scores from scores.csv."""
    try:
        with open('scores.csv', 'r') as file:
            reader = csv.reader(file)
            header = next(reader)  # Read the header row
            print(f"{header[0]:<20} {header[1]:<15} {header[2]:<10}")
            print("-" * 45)
            for row in reader:
                print(f"{row[0]:<20} {row[1]:<15} {row[2]:<10}")
    except FileNotFoundError:
        print("No scores found. Please add some scores first.")

def search_score():
    """Searches for a student's score by name in scores.csv."""
    search_name = input("Enter the student name to search: ")
    found_scores = []
    try:
        with open('scores.csv', 'r') as file:
            reader = csv.reader(file)
            header = next(reader)  # Skip header
            for row in reader:
                if row[0].lower() == search_name.lower():
                    found_scores.append(row)
        
        if found_scores:
            print(f"\nScores for {search_name}:")
            print(f"{header[0]:<20} {header[1]:<15} {header[2]:<10}")
            print("-" * 45)
            for score in found_scores:
                print(f"{score[0]:<20} {score[1]:<15} {score[2]:<10}")
        else:
            print(f"No scores found for '{search_name}'.")
    except FileNotFoundError:
        print("No scores found. Please add some scores first.")

def main_menu():
    """Displays the main menu and handles user choices."""
    # Create the CSV file with headers if it doesn't exist
    try:
        with open('scores.csv', 'x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Student Name', 'Subject', 'Score'])
    except FileExistsError:
        pass # File already exists

    while True:
        print("\nQuiz Score Manager Menu:")
        print("1. Enter Quiz Score")
        print("2. View All Scores")
        print("3. Search Student Score")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            enter_score()
        elif choice == '2':
            view_scores()
        elif choice == '3':
            search_score()
        elif choice == '4':
            print("Exiting Quiz Score Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main_menu()