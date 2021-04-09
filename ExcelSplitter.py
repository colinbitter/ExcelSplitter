import pandas as pd
import glob
import numpy as np
from pathlib import Path

downloads_path = str(Path.home() / "Downloads")
path1 = downloads_path
allFiles = glob.glob(path1 + "/*.xlsx")
for file_ in allFiles:
    df = pd.read_excel(file_, engine='openpyxl')

print("Rows: " + str(df.shape[0]))
NumSplit1 = input('How many files? ')
NumSplit2 = int(NumSplit1)

i=1
for chunk in np.array_split(df, NumSplit2):
    chunk.to_excel(path1 + '/file_{:02d}.xlsx'.format(i), index=False)
    i += 1
