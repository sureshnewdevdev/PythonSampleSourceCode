# Read all lines into a list
with open('write_example.txt', 'r') as f:
    lines = f.readlines(5)
    print(lines)

# Iterate over lines
with open('write_example.txt', 'r') as f:
    for line in f:
        print(line.strip())