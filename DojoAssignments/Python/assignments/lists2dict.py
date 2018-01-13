name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins"]

def list2dict(keys, values):
    new_dict = {}

    if len(keys) == len(values) or len(keys) > len(values):
        for each in range(0, len(values)):
            new_dict[keys[each]] = values[each]

    elif len(keys) < len(values):
        for each in range(0, len(keys)):
            new_dict[values[each]] = keys[each]

    print(new_dict)

list2dict(name, favorite_animal)
