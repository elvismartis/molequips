#!/opt/homebrew/bin/python3


"""
Next task is to write a program to extract ligand from a complex pdb.
Output the ligand file into another file.
save the file as XYZ.pdb
"""

with open('./files/1EVE.pdb', 'r') as fin, open('./files/LIG.pdb', 'w') as fout:
         for i in fin:
              if i.startswith("HETATM"):
                if i[17:20].strip() == "E20":
                    lines = i.strip()
                    #print(lines)
                    fout.write(lines + "\n")
fout.close()

