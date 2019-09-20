import json

dictWork = {}
with open('fileutil.txt', 'r') as files:
    for line in files:
        key, value = line.strip().split(':')
        dictWork[key] = value

print(dictWork['a'])