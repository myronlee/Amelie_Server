import json
def save_data(filename, key_list, value_list):
    dic = dict(zip(key_list, value_list))
    target = open(filename, 'w')
    target.write(json.dumps(dic))
    target.close()