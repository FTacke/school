import re
from pathlib import Path

def fix_indentation(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find blocks starting with ??? hoermal
    # We will match the entire block until we hit a line that is NOT indented with at least 4 spaces or empty.
    
    lines = content.split('\n')
    in_block = False
    new_lines = []
    
    for line in lines:
        if line.startswith('??? hoermal'):
            in_block = True
            new_lines.append(line)
        elif in_block:
            if line.strip() == '':
                new_lines.append(line)
            elif line.startswith('    '):  # Inside the block
                # Remove exactly 8 spaces if it has them, or strip all leading spaces and add 4
                stripped = line.lstrip()
                new_lines.append('    ' + stripped)
            else:
                # End of block
                in_block = False
                new_lines.append(line)
        else:
            new_lines.append(line)
            
    new_content = '\n'.join(new_lines)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed {filepath}")

for p in Path(r'c:\dev\school_dev\school-zensical\docs').rglob('*.md'):
    fix_indentation(p)
