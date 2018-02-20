import xml.etree.ElementTree as ET
import os


def merge_dicts(dict_list):
    result = {}
    for d in dict_list:
        for k, v in d.items():
            if k in result:
                if not isinstance(result[k], list):
                    result[k], t = list(), result[k]
                    result[k].append(t)
                result[k].append(v)
            else:
                result[k] = v
    return result


xml_dir = 'C:/oxygen edi/edi3/'
dictss = []

for file in os.listdir(xml_dir):
    if file.endswith('.xml'):
        tree = ET.parse(xml_dir + file)
        root = tree.getroot()
        attribValues = dict()
        for child in root.iter():
            dictss.append(child)
result_dict = merge_dicts(dictss)

for key in result_dict:
    result_dict[key] = list(set(result_dict[key]))
file = open(xml_dir + ' ALLVALUES', "w")
for item in sorted(result_dict):
    file.write(item + '" ' + str(result_dict[item]) + '\n'+'"')

file.close()
