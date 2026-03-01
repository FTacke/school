import os
import re
import argparse
from pathlib import Path

def process_match(match):
    summary_text = match.group(1).strip()
    content = match.group(2)

    # Convert <p>...</p> to markdown paragraphs
    content = re.sub(r'<p>', '', content)
    content = re.sub(r'</p>', '\n', content)

    # Normalize line endings and indentations
    lines = content.split('\n')
    
    indented_lines = []
    for line in lines:
        if line.strip():
            # Strip whatever previous indentation there was, and enforce exactly 4 spaces
            indented_lines.append('    ' + line.lstrip())
        else:
            indented_lines.append('')
    
    # Reassemble and strip leading/trailing whitespace
    indented_content = '\n'.join(indented_lines).strip('\n')

    return f'??? hoermal "{summary_text}"\n{indented_content}\n'

def migrate_file(filepath, dry_run=False):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    pattern = re.compile(
        r'<details\s+class="hoermal"\s*>\s*<summary>(.*?)</summary>\s*(.*?)\s*</details>',
        re.DOTALL
    )

    matches = list(pattern.finditer(content))
    if not matches:
        return False, 0
    
    new_content = pattern.sub(process_match, content)

    if not dry_run:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
            
    return True, len(matches)

def main():
    parser = argparse.ArgumentParser(description="Migrate hoermal details blocks to Admonitions.")
    parser.add_argument('--dir', type=str, default='docs', help='Directory to search for .md files')
    parser.add_argument('--dry-run', action='store_true', help='Print what would be done without modifying files')
    args = parser.parse_args()

    search_dir = Path(args.dir)
    if not search_dir.exists():
        print(f"Directory {search_dir} does not exist.")
        return

    total_files = 0
    total_blocks = 0

    for filepath in search_dir.rglob('*.md'):
        changed, count = migrate_file(filepath, dry_run=args.dry_run)
        if changed:
            total_files += 1
            total_blocks += count
            if args.dry_run:
                print(f"[Dry Run] Would update {filepath} ({count} blocks)")
            else:
                print(f"Updated {filepath} ({count} blocks)")

    action = "Would update" if args.dry_run else "Updated"
    print(f"\n{action} {total_blocks} blocks across {total_files} files.")

if __name__ == '__main__':
    main()
