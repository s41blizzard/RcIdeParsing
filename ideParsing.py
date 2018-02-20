import xml.etree.ElementTree as ET

path = '/home/blizzard/Documents/edi_royal canin/10-download-2018-01-9-16-51-12-137006_LAS.xml'
tree = ET.parse(path)
root = tree.getroot()

attribValues = dict()

for child in root.iter():
    attribValues.update(child.attrib)

new_path = path + 'ATTRIBUTES'
file = open(new_path, "w")
for item in sorted(attribValues):
    file.write(str(item + ' ' + '"' + attribValues[item]) + '"' + '\n')
file.close()
