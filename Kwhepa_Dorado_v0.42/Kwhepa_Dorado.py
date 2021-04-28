import os
from pathlib import Path

path = Path.home() / "Kwhepa_Dorado" / "PackageList"

with open(path, "r") as f:
    contains = f.read().splitlines()
for i in range(len(contains)):
    os.system("sudo apt-get install -y " + contains[i])