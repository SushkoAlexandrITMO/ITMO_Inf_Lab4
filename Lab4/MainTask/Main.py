f = open("data/MainTaskYaml.yaml", encoding="utf-8").read()

f = f.replace("\n", " </>\n<").replace(": ", "> ")

i = 0

while "<  " in f:
    i += 1
    f = f.replace("<  ", "  <")
    if i > 6:
        break

f = "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<root>\n" + f

f = f.replace("t>\n", "t>\n<", 1)

m = f.split("\n")

metaSymbols = [["root", 0]]
idention = 0
res = ""

for i in range(len(m) - 1):

    line = m[i]

    if line == "<":
        continue

    lc = line.count("  ")
    metaSymbols.append([line[line.index("<") + 1:line.index(">")], lc])

    if "> <" in line and lc == 0:
        line = line.replace(" </>", "")

    elif lc > idention:
        idention = lc
        if lc == m[i + 1].count("  "):
            line = line.replace(" </>", f" </{metaSymbols[-1][0]}>")
            metaSymbols.pop(-1)
        else:
            line = line.replace(" </>", "")

    elif lc == idention:
        if lc >= m[i + 1].count("  "):
            line = line.replace(" </>", f" </{metaSymbols[-1][0]}>")
            metaSymbols.pop(-1)
        else:
            line = line.replace(" </>", "")

    else:
        if lc >= m[i + 1].count("  "):
            line = f"{"  "*metaSymbols[-2][1]}</{metaSymbols[-2][0]}>\n" + line
            line = line.replace(" </>", f" </{metaSymbols[-1][0]}>")
            metaSymbols.pop(-2)
            metaSymbols.pop(-1)
            idention -= 1
        else:
            line = f"{"  " * metaSymbols[-2][1]}</{metaSymbols[-2][0]}>\n" + line
            line = line.replace(" </>", "")
            metaSymbols.pop(-2)
            idention -= 1


    res += line
    res += "\n"


for i in metaSymbols[::-1]:
    res += f"{"  "*i[1]}</{i[0]}>\n"

ans = open("data/MainTaskXml.xml", "w", encoding="utf-8").write(res)

print("Program finished")