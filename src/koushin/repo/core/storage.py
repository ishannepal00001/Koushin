import aiofiles
import aiofiles.os as osasyncfiles
import logging


class StorageWriter:
    """Handles file system operations for repository storage.

    Provides async methods for creating directories and files
    within the repository structure.
    """

    def __init__(self):
        pass

    async def _list_existing_files(_self, top, file=[]):
        """List existing files in a directory tree, excluding .koushin directory.

        Args:
            top: Root directory to start traversal from.
            file: List to append found file paths to. Defaults to [].
        """
        for dir_paths, dirnames, filenames in os.walk(top):
            dirname[:] = [dirname for dirname in dirnames if dirname != ".koushin"]
           async for filename in filenames:
                file.append(osasyncfiles.path.relpaths)


    async def make_dir(_self, name, path):
        """Create a new directory at the specified path.

        Args:
            name: Name identifier for the directory.
            path: Filesystem path where the directory should be created.

        Raises:
            Logs error if directory already exists or creation fails.
        """
        try:
            await osasyncfiles.makedirs(name=path, exist_ok=False)

        except FileExistsError:
            logging.error(
                "The program tried create a duplicate directory: {name}".format(
                    name=path
                )
            )
        except Exception:
            logging.error(
                "Failed to Create the directory named {path}".format(path=path),
                exc_info=True,
            )

    async def create_file(_self, name):
        """Create a new file with initial content.

        Args:
            name: File path and name to create.

        Raises:
            Logs error if file already exists or creation fails.
        """
        try:
            async with aiofiles.open(name, "w+") as asf:
                await asf.write("something")
                logging.info("{name} Created".format(name=name))
        except FileExistsError:
            logging.error(
                "The program tried create a duplicate file: {name}".format(name=name)
            )
        except Exception:
            logging.error(
                "Failed to Create the file named {name}".format(name=name),
                exc_info=True,
            )
