import csv
import glob
import os
import xml.etree.cElementTree as ET
import array as arr


def sort_func(e):
    return e['id']


def create_xml(file_name):
    f = open("dataset/" + file_name + ".txt", "r")

    root = ET.Element("annotation")

    ET.SubElement(root, "filename").text = file_name + '.jpg'

    lines = f.readlines()

    for line in lines:
        numbers = []
        pomNumber = []
        for char in line:
            pomNumber.append(str(char))
            if char == ' ':
                numbers.append(''.join(pomNumber[:-1]))
                pomNumber = []
        numbers.append(''.join(pomNumber[:-1]))

        object = ET.SubElement(root, "object")
        name = ET.SubElement(object, "name").text = 'helmet' if numbers[0] == '0' else 'west'
        position1 = ET.SubElement(object, "position1").text = numbers[1]
        position2 = ET.SubElement(object, "position2").text = numbers[2]
        position3 = ET.SubElement(object, "position3").text = numbers[3]
        position4 = ET.SubElement(object, "position4").text = numbers[4]
    tree = ET.ElementTree(root)
    tree.write("dataset/" + file_name + ".xml")


def create_csv():
    row_list = [["ID", "Name"]]
    arr = os.listdir("dataset/")
    row_of_neg = []
    row_of_pos = []
    for file in arr:
        if file.endswith(".txt") and file.startswith("neg"):
            row_of_neg.append({'id': int(file.strip("neg_").strip(".txt")), 'name': file.strip(".txt")})

    row_of_neg.sort(key=sort_func)
    last_id = row_of_neg[-1]['id']
    print(last_id)

    for file in arr:
        if file.endswith(".txt") and file.startswith("pos"):
            row_of_pos.append({'id': last_id + int(file.strip("pos_").strip(".txt")), 'name': file.strip(".txt")})

    row_of_pos.sort(key=sort_func)

    for row in row_of_neg:
        row_list.append([row['id'], row['name']])
    for row in row_of_pos:
        row_list.append([row['id'], row['name']])

    for row in row_list[1:]:
        create_xml(row[1])

    with open('data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(row_list)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    create_csv()
