"""
A test parser is suppose to perform following operations:
1) Open the file provided by the user.
2) Read the file line-by-line.
3) Decide whether to skip the line (blank, comment or wrong type).
4) Extract useful pieces of information out.
5) Store this extract information into a variable for later use.l
"""
scorelist_names = []
scorelist_scores = []
with open('score.txt', 'r') as f: # opens the file, closes it automatically
    for line in f:                # one line at a time
        line = line.strip()       # removes the newline and spaces at the ends
        if not line:              # true for empty line
            continue              # jump to the next line
        if line.startswith("#"):  # True for comment line
            continue              # jump to next line
        parts = line.split()      # "alice 82" becomes ["alice", "82"]
        scorelist_names.append(parts[0])
        scorelist_scores.append(int(parts[1]))

print(scorelist_names, scorelist_scores)
deno = len(scorelist_scores)
numo = sum(scorelist_scores)

print("The average is ", numo/deno)
