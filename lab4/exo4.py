def function(dictionary, key):
    if key in dictionary.keys():
        return dictionary[key]
    return 'No such key'

print(function({'name': 'Audrey'},'name'))
