import yaml
import xml.etree.ElementTree as xml
from lark import Lark, Transformer

f = open("../0MainTask/Data/MainTaskYaml.yaml", encoding="utf-8").read()

#f = "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<" + f

yamlGram = (r"""
  ?value: dict
 | list
 | string
 | SIGNED_NUMBER -> number
 | "true" -> true
 | "false" -> false
 | "null" -> null

 list : "["*"- "* [value ("," value)* ("- " value)*] "]"

 dict : value ":" "-" pair ("-" pair)*
 pair : ESCAPED_STRING ":" value
 
 string : ESCAPED_STRING

    %import common.ESCAPED_STRING
    %import common.SIGNED_NUMBER
    %import common.WS
    %ignore WS
""")

parser = Lark(yamlGram, start = "value", parser = "lalr")

class MyTransform(Transformer):

    def string(self, s):
        (s,) = s
        return s[1:-1]
    def number(self, n):
        (n,) = n
        return float(n)

    list = list
    pair = tuple
    dict = dict

    null = lambda self, _: None
    true = lambda self, _: True
    false = lambda self, _: False

#ans = open("Data/ThirdTaskXml.xml", "w", encoding="utf-8")

print(MyTransform().transform(parser().parse(f)))

'''
def yaml_to_xml(yaml_data):
    tree = parser.parse(json_data)
    transformer = JSONTransformer()
    data = transformer.transform(tree)

    with open("Data/ThirdTaskXml.xml", "w", encoding="utf-8") as xml_file:
        xml.dump(data, yaml_file, allow_unicode=True, sort_keys=False)

with open('json_file.json') as file:
    json_content = file.read()
    json_to_yaml(json_content, 'schedule_yaml_grammar.yaml')
'''
print("Program finished")