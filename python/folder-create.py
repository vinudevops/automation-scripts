import os
import sys

def create_folder_structure(parent_directory, project_name):
    # Combine parent directory and project name to get full path
    project_directory = os.path.join(parent_directory, project_name)
    
    # Create main directory
    os.makedirs(project_directory)
    os.chdir(project_directory)

    # Create files
    open("main.tf", "a").close()
    open("variables.tf", "a").close()
    open("outputs.tf", "a").close()
    open("terraform.tfvars", "a").close()
    open("providers.tf", "a").close()

    # Create directories
    os.makedirs("modules")
    os.makedirs("environments")

    # Create module directories and files
    os.makedirs("modules/module1")
    os.makedirs("modules/module2")
    open("modules/module1/main.tf", "a").close()
    open("modules/module1/variables.tf", "a").close()
    open("modules/module1/outputs.tf", "a").close()
    open("modules/module2/main.tf", "a").close()
    open("modules/module2/variables.tf", "a").close()
    open("modules/module2/outputs.tf", "a").close()

    # Create environment directories and files
    os.makedirs("environments/dev")
    os.makedirs("environments/stage")
    os.makedirs("environments/prod")
    open("environments/dev/main.tf", "a").close()
    open("environments/dev/variables.tf", "a").close()
    open("environments/dev/outputs.tf", "a").close()
    open("environments/dev/terraform.tfvars", "a").close()
    open("environments/dev/providers.tf", "a").close()
    open("environments/stage/main.tf", "a").close()
    open("environments/stage/variables.tf", "a").close()
    open("environments/stage/outputs.tf", "a").close()
    open("environments/stage/terraform.tfvars", "a").close()
    open("environments/stage/providers.tf", "a").close()
    open("environments/prod/main.tf", "a").close()
    open("environments/prod/variables.tf", "a").close()
    open("environments/prod/outputs.tf", "a").close()
    open("environments/prod/terraform.tfvars", "a").close()
    open("environments/prod/providers.tf", "a").close()

    # Create .terraform directory
    os.makedirs(".terraform")

    # Create initial state file
    open(".terraform/terraform.tfstate", "a").close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <parent_directory> <project_name>")
        sys.exit(1)
    parent_directory = sys.argv[1]
    project_name = sys.argv[2]
    create_folder_structure(parent_directory, project_name)

