"""
This file will be responsible for creating config.koushin 

"""
import configparser
import os
from pathlib import Path

import requests

from logger_config import setup_logger

logger = setup_logger(name=__name__)

def generate_raw_github_content(github:str):
   """  
        This fucntion will generate raw github content for config.koushin
   """
   koushin_path = f"{github.replace("github","raw.githubusercontent")}/refs/heads/main/config.koushin"
   logger.info("generating koushin_path")
   return koushin_path

def create_config(github:str,project_name:str,project_path:str):
    """ 
    This function will create config.koushin which will contain the following
    
    ARGS:
    
    github : github link forr the project 
     
    project_name : name of the project (should be same as repo nam ) 

    project_path : path where client will install the project add the project installation path it will genearte full path from home to the path specified during update on client side  
    
    Hint:

        when client runs the project for the first time it is suggested to add project_path 
        use add_install_path(path) function .
    """
    path = Path.cwd()
    repo = github or "https://github.com/Shishir-Kc/Koushin" 
    version_manager = generate_raw_github_content(github)
    install_path = project_path or "path/where/user/will/install/this/project"
    TEMPLATE = f""" 
[github]
repo = {repo}
[project]
name = {project_name}
[version]
version-manager = {version_manager}
version = 0.0.1 
[path]
install-path = {install_path}
"""
    logger.info("Creating config.koushin ")
    try:
     with open(f"{path}/config.koushin","w")as file:
        file.write(TEMPLATE)        
    except Exception as e:
        logger.error(e)
def read_config():
    """
    
    This function will read config.koushin (Local)  and will return the following:
    
    Returns:
    
    github : github repo for the project 

    version-manager : will return config.kosun raw github url  

    version : current version 
    
    project_name : name of the project 

    """

    config= configparser.ConfigParser()
    logger.info("reading config.koushin")
    try:
     config.read(f"{Path.cwd()}/config.koushin")
    except  Exception as e:
        logger.error(f"Could`nt find config.koushin{e}")
    return {
        "github":config["github"]["repo"],
        "version-manager":config["version"]["version-manager"],
        "version":config["version"]["version"],
        "install_path":config["path"]["install-path"],
        "project_name": config["project"]["name"]
    }

def add_install_path(path):
    """
        This function will add the installation_path in the config.koushin 
    """
    logger.info("adding install-path")
    config = configparser.ConfigParser()
    config.read(f"{Path.cwd()}/config.koushin")
    config.set('path','install-path',path)
    try:
     with open(f"{Path.cwd()}/config.koushin","w") as configfile:
        config.write(configfile)
    except Exception as e:
        logger.error(e)

def get_config():
    """ 
    This function will get the cloud (github) config.koushin

    Returns:
    
    github : github repo for the project 

    version-manager : will return config.kosun raw github url 

    version : cloud (github) version 

    project_name : name of the project 
    """
    config = configparser.ConfigParser()
    raw_config_url = str(read_config().get("version-manager"))
    try:
        logger.info("Getting config from github")
        response = requests.get(raw_config_url)
        if response.status_code == 200:
            logger.info("Got config from git ")
            config.read_string(response.text)
            return {
             "github":config["github"]["repo"],
             "version-manager":config["version"]["version-manager"],
             "version":config["version"]["version"],
             "install_path":config["path"]["install-path"],
             "project_name": config["project"]["name"]   
           }

    except Exception as e:
        logger.error(e)

def conversion(v):
    """ 
        This will convert str to int using map  
    """
    logger.info("Convering ....")
    return tuple(map(int,v.split(".")))

def generate_clean_path(path:str,project_name)->str:
    """
      This function will generate a clean path where the project lives
      suppose if a project is on path .config/os/koushin then this function 
      will return .config/os . 

    ARGS:

    path : full path where the project is installed on client side 

    project_name : project name (it should not be differ )


    """
    logger.info("generating clean path ")
    return str(path).replace(f"/{project_name}","")

