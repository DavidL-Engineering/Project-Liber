# encoding: utf-8
# Release 19.1
# Written by BOT Yokel
# ANSYS WORKBENCH AUTO-ARCHIVE
import os
SetScriptVersion(Version="19.1.103")

'''
INSTRUCTIONS:
1. Enter the project directories under proj_dir. Change all backslashes to forward slashes
e.g. "C:/Users/tom/Documents/DV2 Nose Study/Group 3"
2. Enter the project name under proj_name.
e.g. "Test"
3. Enter the cycle the project belongs to under cycle. The cycles you may choose from are: Gen X, Gen 11, Gen 12
e.g. "Gen 11"
3. Enter the design series of the project under series. The series you may choose from are: V1, V2, V3, V4, V5, V6, DV1, DV2, DV3, DV4, DV5, DV6, DV7. Do not include any spaces, and capitalize all letters.
e.g. "DV1"
4. Enter the desired name of the project's archive under archive_name.
e.g. "Test Archive"
'''

proj_dir = [
"INSERT_HERE",
"INSERT_HERE"
]

proj_name = [
"INSERT_HERE",
"INSERT_HERE"
]

cycle = [
"INSERT_HERE",
"INSERT_HERE"
]

series = [
"INSERT_HERE",
"INSERT_HERE"
]

archive_name = [
"INSERT_HERE",
"INSERT_HERE"
]

for i in range(len(proj_dir)):
    Open(FilePath="{}/{}.wbpj".format(proj_dir[i], proj_name[i]))
    Archive(
        FilePath="//172.16.1.12/hpc/sims/Archives/{}/{}/{}.wbpz".format(cycle[i], series[i], archive_name[i]),
        IncludeExternalImportedFiles=True)