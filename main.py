import json
import pandas as pd


def generateCSV(name):
    data = json.load(open(name + ".json"))
    classes = []
    details = []

    for key, value in data.items():
        print("class: ", key)
        classes.append(key)

    for class_ in classes:
        for key, value in data[class_].items():
            print("details_for: ", key)
            details.append(value)

    df = pd.json_normalize(details)
    df.to_csv(name + ".csv")
    print(f'\n \t CSV For json {name} Generated... \n')


generateCSV("sample-1")
generateCSV("sample-2")
