import json
FILENAME = "input.json"
# TODO решите задачу
def task() -> float:
    with open(FILENAME, "r", encoding="utf-8") as file:
        data = json.load(file)  #  json в Python-объект
    total = sum(i["score"] * i["weight"] for i in data)
    return round(total, 3)
print(task())

