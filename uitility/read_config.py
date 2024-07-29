import configparser
import json


def read_config(path: str):
    config = configparser.RawConfigParser()
    config.read(path)
    return config


# this method for read data from json file


def get_josn_data(json_file):
    with open(json_file, "r") as file:
        data = json.load(file)
        return data
