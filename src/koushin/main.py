import argparse

from config.config import create_config


def main():
    parser = argparse.ArgumentParser(prog="koushin")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("generate", help="Generate something")
    subparsers.add_parser("info", help="Show info")

    args = parser.parse_args()

    if args.command == "generate":
        project_name = input("project name (it should be same as repo name ) :  ") 
        github_url = input("github repo url for the project :  ")
        project_path = input("project path where it will be installed at client side : ")
        try:
         create_config(project_name=project_name,project_path=project_path,github=github_url)
         print("Created config")
        except Exception as e:
            print(e)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
