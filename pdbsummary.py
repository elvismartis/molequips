#!/usr/bin/env python3
import os
import sys
import argparse

parser = argparse.ArgumentParser(description="Extract HETATMS")
parser.add_argument("-i", "--inpdb", required=True, help="Enter the PDB file with path")
parser.add_argument("-c", "--chainID", help="Enter the chain ID [optional]")
args = parser.parse_args()

if not os.path.exists(args.inpdb):
    parser.error(f"input file not found: {args.inpdb}")

count = []
with open(args.inpdb, 'r') as fin:
      for i in fin:
          if i.startswith("ATOM"):
            if "CA" in i:
                lines = i[12:16].strip() == "CA"
                count.append(lines)
print("number of CA atoms in chain", args.chainID, "is ", len(count))