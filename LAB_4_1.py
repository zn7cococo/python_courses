import json


def task() -> float:
    with open('input.json') as f:
        python_f = json.load(f)
    multiply = [ dict.get("score")*dict.get("weight") for dict in python_f]
    return round(sum(multiply),3)


print(task())
