import json
import os

def get_filename_list(path):
    """ Returns a list of filenames for all txts in a directory. """
    return [os.path.join(path,f) for f in os.listdir(path)]

def get_dict_from_txt(filename):
    """  filename contains path """
    target = open(filename, 'r')
    string = target.read()
    return json.loads(string)