import logging

from pathlib import Path

import os 

def setup_logger(name:str):
    # from config.config import cretate_logger_file
    """
     It will create a LOG dir under root project 
     make sure to add it in .gitignore
    
    This function will set up logger 
       
       ARGS:
       
        name -> logger name  


    """
    current_path = Path.cwd()
    log_path = current_path / "LOG"
    os.makedirs(log_path,exist_ok=True)
    logger = logging.getLogger(name)
    formatter = logging.Formatter(
         "| %(asctime)s | %(levelname)s | %(name)s | %(message)s |"
    )
    file_path = log_path
    file_handler = logging.FileHandler(file_path/"koushin.log")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger
