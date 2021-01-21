import json

# dict
dict_model = {
    'int': 1,
    'str': 'a',
    'bool': True,
}

# dict to json
json_return = json.dumps(dict_model, indent=True)

#print 
print(json_return)

# json
json_model = '{"int":2,"str":"b","bool":false}'

# json to dict
dict_return = json.loads(json_model)

#print 
print(dict_return)