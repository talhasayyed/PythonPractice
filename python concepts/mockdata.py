import pickle
from collections import OrderedDict, defaultdict

# pickle .pkl
def save_data_to_pkl(filename, data):
    """take input filename as filename.pkl
    Args:
        filename (str):
        data (any):
    Return:
        None
    """
    with open(filename, "wb") as f:
        pickle.dump(data, f)

def load_data_from_pkl(filename):
    """take input filename as filename.pkl
    Args:
        filename (str):
        data (any):
    Return:
        None
    """
    with open(filename, "rb") as f:
        return pickle.load(f)

def save_data_to_txt(filename, data):
    """take input filename as filename.txt
    Args:
        filename (str):
        data (any):
    Return:
        None
    """
    with open(filename, "r") as f:
        f.write(data)

def load_data_from_txt(filename):
    """take input filename as filename.txt
    Args:
        filename (str):
        data (any):
    Return:
        None
    """
    with open(filename, "r") as f:
        return f.read()

# json
import json
def save_data_to_json(filename, data):
    """take input filename as filename.json
    Args:
        filename (str): _description_
        data (json): _description_
    """
    with open(filename, 'w') as f:
        json.dump(data, f)

def load_data_from_json(filename):
    """take input filename as filename.json
    Args:
        filename (str): _description_
        data (json): _description_
    """
    with open(filename, 'r') as f:
        dict_value = json.load(f)
    print(dict_value)
