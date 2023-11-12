import csv
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME) as f:
        lines = [line for line in csv.DictReader(f)]
    with open(OUTPUT_FILENAME, 'w') as f:
        f.write(json.dumps(lines, indent=4))


if __name__ == '__main__':
    task()
    with open(OUTPUT_FILENAME) as output_f:
       for line in output_f:
           print(line, end="")
