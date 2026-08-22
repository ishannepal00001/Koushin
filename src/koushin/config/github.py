import pathlib
import os
from koushin.logger_config import setup_logger
import time

start = time.perf_counter()

index_path = pathlib.Path(__file__).resolve().parent
print(index_path)
logger = setup_logger(name=__name__)


def get_all_dir() -> list:
    """
    function: Runs a list comprehension and returns a list of all the directories from the script where the code is being exectued from.
    returns: list
    keywords: os.fspaths : gives a string like path name for the PosixPath or PurePath
              iterdir() : loops through the parent directory
    """
    return [os.fspath(p) for p in index_path.iterdir() if p.is_dir()]


def get_full_path(path) -> pathlib.Path:
    """
    function: provides a full path for pathlib path
    """
    pathlib_path = pathlib.Path(path)
    return pathlib.Path(__file__).resolve().parent / pathlib_path


def check_config_file() -> list:
    """
    function: looks the config file inside the .git directory
    """
    config_files = []
    paths = get_all_dir()
    for path in paths:
        if path := ".git":
            print(path)
            files = [
                os.fspath(f)
                for f in get_full_path(path).iterdir()
                if os.fspath(f.name) == "config"
            ]
            config_files.append(files[0])

    return config_files


def get_remote_url():
    """
    function: provides a https friendly url
    keywords: https_url : full https url
    """
    config_path = check_config_file()
    try:
        with open(config_path[0], "r") as f:
            for line in f:
                if "url" in str(line):
                    sliceable = list(line)
                    url = "".join(sliceable[22:])
                    https_url = "https://github.com/" + url
                    return https_url
    except FileNotFoundError:
        logger.error("File doesn't exist")
    except PermissionError:
        logger.error("No permission to read this file")
    except UnicodeDecodeError:
        logger.error("File isn't valid text in this encoding")
    except OSError as e:
        logger.error(f"Some other OS-level error: {e}")


print(get_remote_url())
end = time.perf_counter()
elapsed = end - start
print(f"Elapsed: {elapsed:.6f} seconds")
