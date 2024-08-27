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


count = {}


def get_testcase_count(item, call, result):
    parent_class = item.parent
    class_name = parent_class.name
    if class_name not in count:
        count[class_name] = {"passed": 0, "failed": 0, "skipped": 0}

    if result.when == "call":
        if result.failed:
            count[class_name]["failed"] += 1
        elif result.skipped:
            count[class_name]["skipped"] += 1
        else:
            count[class_name]["passed"] += 1
