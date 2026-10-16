#!/opt/homebrew/bin/python3
import argparse
import os

"""
Next task is to write a program to extract ligand from a complex pdb.
Output the ligand file into another file.
save the file as XYZ.pdb
"""

parser = argparse.ArgumentParser(description="Extract HETATMS")
parser.add_argument("-i", "--inpdb", required=True, help="Enter the PDB file with path")
parser.add_argument("-o", "--outfile", required=True, help="Enter the output filename with path")
parser.add_argument("-r", "--resname", required=True, help="Enter the Resname in ALL CAPS")
args = parser.parse_args()
args.resname = args.resname.upper()

if not os.path.exists(args.inpdb):
    parser.error(f"input file not found: {args.inpdb}")
if os.path.abspath(args.inpdb) == os.path.abspath(args.outfile):
    parser.error("output file must be different from the input file")

with open(args.inpdb, 'r') as fin, open(args.outfile, 'w') as fout:
      for i in fin:
          if i.startswith("HETATM"):
            if i[17:20].strip() == args.resname: #need to as user for resname
              lines = i.strip()
              fout.write(lines + "\n")
fout.close()

