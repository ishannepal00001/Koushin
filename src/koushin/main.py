import argparse

from config import config
from config import github
from koushin import logger_config

logger = logger_config.setup_logger(name=__name__)


def main():
    parser = argparse.ArgumentParser(prog="koushin")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("generate", help="Generate something")
    subparsers.add_parser("info", help="Show info")

    args = parser.parse_args()

    if args.command == "generate":
        github_url = github.get_remote_url()

        project_name = input("project name (it should be same as repo name ) :  ")

        if not github_url:
            github_url = input("github repo url for the project :  ")

        project_path = input(
            "project path where it will be installed at client side : "
        )

        try:
            config.create_config(
                project_name=project_name, project_path=project_path, github=github_url
            )
            print("Created config")
        except Exception as e:
            print(e)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
