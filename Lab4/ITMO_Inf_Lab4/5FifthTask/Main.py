from idlelib.iomenu import encoding

import yaml
import lark

res = None

file = open('../0MainTask/Data/MainTaskYaml.yaml', encoding="utf-8")
read_data = yaml.load_all(file, Loader=yaml.FullLoader)
for i in read_data:
    res = dict_to_protobuf.dict_to_protobuf(i, res)

open("Data/FifthTaskProtobuf.proto", "w", encoding="utf-8").write(res)

print("Program finished")