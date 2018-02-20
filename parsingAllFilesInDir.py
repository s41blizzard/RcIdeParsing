import xml.etree.ElementTree as ET
import os

xml_dir = '/home/blizzard/Documents/edi_royal canin/'
for file in os.listdir(xml_dir):
    if file.endswith('.xml'):
        tree = ET.parse(xml_dir + file)
        root = tree.getroot()
        attribValues = dict()
        for child in root.iter():
            attribValues.update(child.attrib)
        file = open(xml_dir + file + '__Attribs', "w")
        for item in sorted(attribValues):
            file.write(str(item + ' ' + '"' + attribValues[item]) + '"' + '\n')
        file.close()
