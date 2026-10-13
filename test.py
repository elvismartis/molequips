#!/opt/homebrew/bin/python3
"""
A test parser is suppose to perform following operations:
1) Open the file provided by the user.
2) Read the file line-by-line.
3) Decide whether to skip the line (blank, comment or wrong type).
4) Extract useful pieces of information out.
5) Store this extract information into a variable for later use.l
"""
#scorelist_names = []
#scorelist_scores = []
bfac = []
atmname = []
with open('./files/1EVE.pdb', 'r') as f: # opens the file, closes it automatically
    for line in f:                # one line at a time
        line = line.strip()       # removes the newline and spaces at the ends
        #print(line)
        if not line:              # true for empty line
            continue              # jump to the next line
        if line.startswith("ATOM"):  # Only extract files if line startswith this "ATOM" or "HETAM"
            if "ALA" in line:          # extract certain residues with "XXX"
                parts = line.split()      # splits lines as separate words
                bfac.append(parts[2])
                atmname.append(parts[9])


#print(scorelist_names, scorelist_scores)
#deno = len(scorelist_scores)
#numo = sum(scorelist_scores

#print("The average is ", numo/deno)
atm_bfac = list(zip(bfac, atmname))
#print(atm_bfac)
print("There are at least", int(len(atmname)/5), " ALA residues")

