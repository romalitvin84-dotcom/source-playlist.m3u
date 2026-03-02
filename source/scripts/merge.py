files = [
    "source/playlist1.m3u"
]

result = []

for file in files:
    with open(file, encoding="utf-8") as f:
        for line in f:
            if line.startswith("#EXTINF") or line.startswith("http"):
                result.append(line)

with open("output/final.m3u", "w", encoding="utf-8") as out:
    out.write("#EXTM3U\n")
    for line in result:
        out.write(line)
