import json

with open('Resources/data.json', 'r') as jsonFile:
    data = jsonFile.read()

colors = json.loads(data)

colorNames = set()

# iterate over all entries
for color in colors:
    # get color name
    colorName = color['name']
    
    # check if the color name has been seen before
    names = [colorName]
    once = False
    while (colorName in colorNames):
        once = True
        # increase the color name counter by one
        try:
            counter = int(colorName[-1]) + 1
            colorName = colorName[:-1] + str(counter)
        except ValueError:
            colorName = colorName + "0"
    color['name'] = colorName
    names.append(colorName) 
    if once: print("{} ==> {}".format(*list(names)))

    colorNames.add(colorName)

data = json.dumps(colors, indent = 4)

with open('Resources/data.json', 'w') as jsonFile:
    jsonFile.write(data)
