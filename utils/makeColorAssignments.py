import json
import sys
import os

def getStringFromColorValues(vals):
    return '_'.join((str(int(val)) for val in vals.values()))


# Enum version:
def getEnumAssignments(colors):
    print('class Colors256(Enum):\n\t""" Enum for 256bit colors. Uses Each colorId has a name and aliases corresponding to the hex, rgb or hsl value"""')
    for entry in ['name','hexString', 'rgb', 'hsl']:
        uniqueName = set()
        for color in colors:
            colorid = color['colorId']
            value = color[entry]
            if entry == 'hexString':
                value = 'hex_' + value[1:]
            if isinstance(value, dict):
                value = entry + '_' + getStringFromColorValues(value)
            if value in uniqueName:
                continue
            uniqueName.add(value)
            print('\t{}{} = "{}"'.format(value, " " * (19 - len(value)), colorid))

# dict Version:
def getAssignments(colors):
    out = {'colorname' : {}, 'hex' : {}, 'rgb' : {}, 'hsl' : {}}
    for color in colors:
        hexString = color['hexString']
        rgbString = getStringFromColorValues(color['rgb'])
        hslString = getStringFromColorValues(color['hsl'])
        name = color['name']
        colorId = str(color['colorId'])
        for key, item in zip(out.keys(), (name, hexString, rgbString, hslString)):
                out[key][item] = colorId
    print(json.dumps(out, indent = 4))

if __name__ == '__main__':
    with open ('Resources/data.json', 'r') as jsonFile:
        data = jsonFile.read()
    
    getEnumAssignments(json.loads(data))
    
