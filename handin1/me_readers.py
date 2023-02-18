# 1 READ CSV FILE

#import yaml
import xml.etree.ElementTree as ET
import json
import csv
print("Reading CSV file...\n")

with open("me.csv") as file:
    reader = csv.reader(file)
    headers = next(reader)

    for row in reader:
        name, age, *hobbies = row
        print("Name:", name)
        print("Age:", age)
        print("Hobbies:", hobbies)
        print("\n\n")


# 2 READ JSON FILE

print("Reading JSON file...\n")

with open("me.json") as file:
    data = json.load(file)

person = data["person"]
name = person["name"]
age = person["age"]
hobbies = person["hobbies"]

print("Name:", name)
print("Age:", age)
print("Hobbies:", hobbies)
print("\n\n")


# 3 READ TXT FILE

print("Reading TXT file...\n")
with open("me.txt") as file:
    lines = file.readlines()

data = {}
for line in lines:
    key, value = line.strip().split(": ")
    data[key] = value

name = data["Name"]
age = int(data["Age"])
hobbies = data["Hobbies"].split(", ")

print("Name:", name)
print("Age:", age)
print("Hobbies:", hobbies)
print("\n\n")


# 4 READ XML FILE

print("Reading XML file...\n")

tree = ET.parse("me.xml")
root = tree.getroot()

name = root.find("name").text
age = int(root.find("age").text)
hobbies = [hobby.text for hobby in root.find("hobbies").findall("hobby")]

print("Name:", name)
print("Age:", age)
print("Hobbies:", hobbies)
print("\n\n")


# 5 READ YAML FILE

""" print("Reading YAML file...\n")

with open("me.yaml") as file:
    data = yaml.safe_load(file)

name = data["person"]["name"]
age = data["person"]["age"]
hobbies = data["person"]["hobbies"]

print("Name:", name)
print("Age:", age)
print("Hobbies:", hobbies) """
