from idlelib.iomenu import encoding

import yaml
import xmltodict

file = open('../0MainTask/Data/MainTaskYaml.yaml', encoding="utf-8")
read_data = yaml.load_all(file, Loader=yaml.FullLoader)
for i in read_data:
    res = xmltodict.unparse(i, pretty=True)

open("Data/FirstTaskXml.xml", "w", encoding="utf-8").write(res)

print("Program finished")