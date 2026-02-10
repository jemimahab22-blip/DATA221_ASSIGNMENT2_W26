def find_lines_containing(filename, keyword):
    results = []
    keyword = keyword.lower()

    with open(filename, "r") as f:
        for line_numbers, line in enumerate(f, start=1):
            if keyword in line.lower():
                results.append((line_numbers, line.strip()))

    return results
matches = find_lines_containing("sample-file.txt", "lorem")

# Print how many matching lines were found
print(f"Number of matching lines: {len(matches)}")

# Print the first 3 matching lines
for line_numbers, line_text in matches[:3]:
    print(f"Line {line_numbers}: {line_text}")
