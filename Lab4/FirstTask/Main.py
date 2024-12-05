f = open("data/MainTaskYaml.yaml", encoding="utf-8").read()



f = "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<root>\n" + f



ans = open("data/MainTaskXml.xml", "w", encoding="utf-8").write(res)

print("Program finished")