import copy
import json
from pathlib import Path

SOURCE = Path("source-full.json")
PART1 = Path("source.json")
PART2 = Path("source-part2.json")

CHUNK_SIZE = 50

with SOURCE.open("r", encoding="utf-8") as f:
    full = json.load(f)

apps = full.get("apps", [])

part1 = copy.deepcopy(full)
part1["name"] = "Carmine Personal Source"
part1["identifier"] = "com.carmolab.source.part1"
part1["subtitle"] = "Personal AltStore / LiveContainer source - Part 1"
part1["apps"] = apps[:CHUNK_SIZE]

part2 = copy.deepcopy(full)
part2["name"] = "Carmine Personal Source 2"
part2["identifier"] = "com.carmolab.source.part2"
part2["subtitle"] = "Personal AltStore / LiveContainer source - Part 2"
part2["apps"] = apps[CHUNK_SIZE:]

with PART1.open("w", encoding="utf-8") as f:
    json.dump(part1, f, indent=4, ensure_ascii=False)

with PART2.open("w", encoding="utf-8") as f:
    json.dump(part2, f, indent=4, ensure_ascii=False)

print(f"Full apps: {len(apps)}")
print(f"Part 1 apps: {len(part1['apps'])}")
print(f"Part 2 apps: {len(part2['apps'])}")
