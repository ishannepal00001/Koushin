import aiofiles
import aiofiles.os as osasyncfiles
import logging


class StorageWriter:
    def __init__(self):
        pass

    async def _make_dir(_self, name, path):
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

    async def _create_files(_self, name):
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
