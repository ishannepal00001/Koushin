import aiofiles
import aiofiles.os as aos
import logging
import os


class StorageWriter:
    """Handles file system operations for repository storage."""

    def __init__(self):
        pass

    async def _async_walk(_self, top, follow_links=False):
        """Async generator that yields directory entries from a path.

        Args:
            top: Directory path to scan.

        Yields:
            Tuple of (dirs, non_dirs, top) containing directory names,
            file names, and the current path.
        """
        dirs, non_dirs = [], []
        try:
            entries = await aos.scandir(top)
        except OSError:
            return
        for entry in entries:
            try:
                is_dir = entry.is_dir()
            except OSError:
                is_dir = False
            (dirs if is_dir else non_dirs).append(entry.name)
        yield dirs, non_dirs, top
        for dir in dirs:
            full_path = os.path.join(top, dir)
            if follow_links or (not (await aos.path.islink(full_path))):
                async for result in _self._async_walk(full_path, follow_links):
                    yield result, dir, top, non_dirs

    async def make_dir(_self, name, path):
        """Create a new directory at the specified path.

        Args:
            name: Name identifier for the directory.
            path: Filesystem path where the directory should be created.
        """
        try:
            await aos.makedirs(name=path, exist_ok=False)

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
