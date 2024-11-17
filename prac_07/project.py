def main():
    """Project management main program with menu options."""
    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")

    is_running = True
    while is_running:
        print("\n- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n"
              "- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit")
        choice = input(">>> ").lower()

        if choice == 'l':
            filename = input("Enter filename to load: ")
            projects = load_projects(filename)
        elif choice == 's':
            filename = input("Enter filename to save: ")
            save_projects(projects, filename)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            filter_projects_by_date(projects)
        elif choice == 'a':
            add_new_project(projects)
        elif choice == 'u':
            update_project(projects)
        elif choice == 'q':
            if input(f"Would you like to save to {FILENAME}? ").lower() == 'yes':
                save_projects(projects, FILENAME)
            print("Thank you for using custom-built project management software.")
            is_running = False
        else:
            print("Invalid choice")
