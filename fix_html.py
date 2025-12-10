
import os

file_path = r'c:\Users\Sergio Jacome\OneDrive\Escritorio\Emprendimientos\talentotechoriente\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# The duplicate starts at line 182 (index 181)
# Let's verify
start_index = 181
if "DOCTYPE html" not in lines[start_index]:
    # Fallback search
    for i, line in enumerate(lines):
        if "DOCTYPE html" in line and i > 10: # Skip the first one
            start_index = i
            break

new_content_lines = lines[start_index:]

# Dedent
# Find the indentation of the first line
first_line = new_content_lines[0]
indent = len(first_line) - len(first_line.lstrip())
dedented_lines = [line[indent:] if len(line) >= indent else line.lstrip() for line in new_content_lines]

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(dedented_lines)

print(f"Fixed {file_path}. Kept {len(dedented_lines)} lines starting from original line {start_index + 1}.")
