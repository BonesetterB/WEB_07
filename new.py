import configparser
import pathlib

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


file_config = pathlib.Path(__file__).parent.parent.joinpath('WEB_07\config.ini')
config = configparser.ConfigParser()
config.read(file_config)
username = config.get('DEV', 'USER')
print(username)