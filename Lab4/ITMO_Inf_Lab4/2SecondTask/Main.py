import re

f = open("../0MainTask/Data/MainTaskYaml.yaml", encoding="utf-8").read()

f = f.replace("\n", " </>\n<").replace(": ", "> ")

i = 0

while "<  " in f:
    i += 1
    f = re.sub(r"<\s\s", "  <", f)
    if i > 6:
        break

f = "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<" + f

m = re.split("\n", f)

metaSymbols = []
idention = 0
res = ""

for i in range(len(m) - 1):

    line = m[i]
    if line == "<":
        continue

    lc = line.count("  ")
    metaSymbols.append([line[line.index("<") + 1:line.index(">")], lc])

    if "> <" in line and lc == 0:
        line = re.sub(r"\s\W/\W", "", line)

    elif lc > idention:
        idention = lc
        if lc == m[i + 1].count("  "):
            line = re.sub(r"\s\W/\W", f" </{metaSymbols[-1][0]}>", line)
            metaSymbols.pop(-1)
        else:
            line = re.sub(r"\s\W/\W", "", line)

    elif lc == idention:
        if lc >= m[i + 1].count("  "):
            line = re.sub(r"\s\W/\W", f" </{metaSymbols[-1][0]}>", line)
            metaSymbols.pop(-1)
        else:
            line = re.sub(r"\s\W/\W", "", line)

    else:
        if lc >= m[i + 1].count("  "):
            line = f"{"  "*metaSymbols[-2][1]}</{metaSymbols[-2][0]}>\n" + line
            line = re.sub(r"\s\W/\W", f" </{metaSymbols[-1][0]}>", line)
            metaSymbols.pop(-2)
            metaSymbols.pop(-1)
            idention -= 1
        else:
            line = f"{"  " * metaSymbols[-2][1]}</{metaSymbols[-2][0]}>\n" + line
            line = re.sub(r"\s\W/\W", "", line)
            metaSymbols.pop(-2)
            idention -= 1


    res += line
    res += "\n"


for i in metaSymbols[::-1]:
    res += f"{"  "*i[1]}</{i[0]}>\n"

ans = open("Data/SecondTaskXml.xml", "w", encoding="utf-8").write(res)

print("Program finished")