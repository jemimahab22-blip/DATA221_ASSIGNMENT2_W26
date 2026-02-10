import string

with open("sample-file.txt",'r') as f:
    lines=f.readlines()

near_duplicates = {}
for line_number, line in enumerate(lines,start=1):
       lower_file=line.lower().translate(str.maketrans("",'',string.punctuation)).replace(" ",'').strip()

       if lower_file not in near_duplicates:
           near_duplicates[lower_file]=[]

       near_duplicates[lower_file].append((line_number, line.strip()))

duplicate_sets=[]
for group in near_duplicates.values():
    if len(group)>1:
        duplicate_sets.append(group)
print(f"Number of near_duplicate sets is: {len(duplicate_sets)}")

for m, group in enumerate(duplicate_sets[:2],start=1):
    print(f"set{m}:")
    for line_number, original_lines in group:
        print(f"Line {line_number}: {original_lines}")
    print()
