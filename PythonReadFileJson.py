import json
# Mở tập tin văn bản để đọc
with open("input.json", "r") as file:
    # Đọc từng dòng trong tập tin
    data = json.load(file)
    for item in data:
        print("ID:", item["ID"])
        print("Name:", item["Name"])
        print("Age:", item["Age"])
        print()