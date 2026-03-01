"""
migrate_expand.py – Konvertiert <details>-Blöcke (ohne class="hoermal") in
??? expand "Titel"-Admonitions.

Usage:
    python migrate_expand.py --dir docs [--dry-run]
"""

import re
import argparse
import html
from pathlib import Path


# ---------------------------------------------------------------------------
# HTML → Markdown converter (subset, non-recursive via regex + substitutions)
# ---------------------------------------------------------------------------

def html_to_md(raw: str) -> str:
    """Converts a subset of HTML to Markdown."""
    text = raw

    # HTML entities first
    text = html.unescape(text)

    # Remove target/rel attrs from links to simplify (keep href + inner text)
    # <a href="…" target="…" rel="…">text</a>  →  [text](…)
    text = re.sub(
        r'<a\s+href="([^"]*)"[^>]*>(.*?)</a>',
        lambda m: f'[{_strip_inner_tags(m.group(2))}]({m.group(1)})',
        text, flags=re.DOTALL | re.IGNORECASE
    )

    # <strong> / <b>  →  **…**
    text = re.sub(r'<(?:strong|b)>(.*?)</(?:strong|b)>', r'**\1**',
                  text, flags=re.DOTALL | re.IGNORECASE)

    # <em> / <i>  →  *…*
    text = re.sub(r'<(?:em|i)>(.*?)</(?:em|i)>', r'*\1*',
                  text, flags=re.DOTALL | re.IGNORECASE)

    # <code>  →  `…`
    text = re.sub(r'<code>(.*?)</code>', r'`\1`',
                  text, flags=re.DOTALL | re.IGNORECASE)

    # <pre><code class="language-xyz">…</code></pre>  →  ```xyz\n…\n```
    text = re.sub(
        r'<pre><code(?:\s+class="language-([^"]*)")?>(.*?)</code></pre>',
        lambda m: f'\n```{m.group(1) or ""}\n{m.group(2).strip()}\n```\n',
        text, flags=re.DOTALL | re.IGNORECASE
    )

    # <br> / <br/>  →  two spaces + newline (Markdown line-break)
    text = re.sub(r'<br\s*/?>', '\n', text, flags=re.IGNORECASE)

    # <ul>…</ul>  →  collapse to plain list items
    text = re.sub(r'<ul[^>]*>', '', text, flags=re.IGNORECASE)
    text = re.sub(r'</ul>', '', text, flags=re.IGNORECASE)
    text = re.sub(r'<ol[^>]*>', '', text, flags=re.IGNORECASE)
    text = re.sub(r'</ol>', '', text, flags=re.IGNORECASE)

    # <li>…</li>  →  - …
    text = re.sub(r'<li[^>]*>(.*?)</li>',
                  lambda m: '- ' + m.group(1).strip(),
                  text, flags=re.DOTALL | re.IGNORECASE)

    # <blockquote>…</blockquote>  →  > …
    text = re.sub(
        r'<blockquote[^>]*>(.*?)</blockquote>',
        lambda m: '\n'.join('> ' + line for line in m.group(1).strip().split('\n')),
        text, flags=re.DOTALL | re.IGNORECASE
    )

    # <p>…</p>  →  paragraph (double newline)
    text = re.sub(r'<p[^>]*>(.*?)</p>',
                  lambda m: '\n\n' + m.group(1).strip() + '\n\n',
                  text, flags=re.DOTALL | re.IGNORECASE)

    # Strip remaining block-level wrappers: <div …> </div>
    text = re.sub(r'<div[^>]*>', '', text, flags=re.IGNORECASE)
    text = re.sub(r'</div>', '', text, flags=re.IGNORECASE)

    # Strip remaining <span …> </span>
    text = re.sub(r'<span[^>]*>', '', text, flags=re.IGNORECASE)
    text = re.sub(r'</span>', '', text, flags=re.IGNORECASE)

    # Strip any remaining HTML tags as fallback
    text = re.sub(r'<[^>]+>', '', text)

    # Collapse 3+ blank lines → 2
    text = re.sub(r'\n{3,}', '\n\n', text)

    return text.strip()


def _strip_inner_tags(s: str) -> str:
    """Remove HTML tags from a string (used for link text)."""
    return re.sub(r'<[^>]+>', '', html.unescape(s)).strip()


# ---------------------------------------------------------------------------
# Summary-Titel bereinigen
# ---------------------------------------------------------------------------

DEFAULT_TITLE = "Wer mehr wissen will"


def clean_title(summary_html: str) -> str:
    """Strip tags, decode entities, remove '(klickt hier)' variants."""
    title = _strip_inner_tags(summary_html)
    title = re.sub(r'\s*\(klickt hier\)\s*', '', title, flags=re.IGNORECASE).strip()
    if not title:
        return DEFAULT_TITLE
    return title


# ---------------------------------------------------------------------------
# Block-Extraktor: findet <details>…</details> inkl. verschachtelter tags
# ---------------------------------------------------------------------------

def iter_details_blocks(text: str):
    """
    Yields (start_idx, end_idx, full_match_str) for every top-level
    <details …>…</details> block (supporting nested details).
    """
    pattern_open  = re.compile(r'<details(\s[^>]*)?>',  re.IGNORECASE)
    pattern_close = re.compile(r'</details>',            re.IGNORECASE)

    pos = 0
    while True:
        m_open = pattern_open.search(text, pos)
        if not m_open:
            break
        start = m_open.start()
        attrs = m_open.group(1) or ''

        # Walk forward counting open/close pairs
        depth = 1
        scan = m_open.end()
        while depth > 0 and scan < len(text):
            m_next_open  = pattern_open.search(text, scan)
            m_next_close = pattern_close.search(text, scan)

            if m_next_close is None:
                break  # malformed

            if m_next_open and m_next_open.start() < m_next_close.start():
                depth += 1
                scan = m_next_open.end()
            else:
                depth -= 1
                if depth == 0:
                    end = m_next_close.end()
                    yield start, end, text[start:end], attrs
                scan = m_next_close.end()

        pos = m_open.end()


# ---------------------------------------------------------------------------
# Einzelnen Block konvertieren
# ---------------------------------------------------------------------------

def convert_block(raw: str, attrs: str) -> tuple[str, bool, str]:
    """
    Returns (converted_markdown, was_converted, reason_if_not).
    """
    # Skip hoermal blocks – already migrated
    if 'hoermal' in attrs.lower():
        return raw, False, 'class=hoermal (skip)'

    # Extract <summary>…</summary>
    m_summary = re.search(r'<summary[^>]*>(.*?)</summary>', raw,
                           re.DOTALL | re.IGNORECASE)
    if not m_summary:
        return raw, False, 'no <summary> found'

    summary_raw = m_summary.group(1)
    title = clean_title(summary_raw)

    # Extract inner content (everything between </summary> and </details>)
    inner_start = m_summary.end()
    # Remove trailing </details>
    inner_raw = raw[inner_start:]
    inner_raw = re.sub(r'\s*</details>\s*$', '', inner_raw,
                        flags=re.IGNORECASE).strip()

    md_content = html_to_md(inner_raw)

    # Indent each content line by 4 spaces
    indented = '\n'.join(
        '    ' + line if line.strip() else ''
        for line in md_content.split('\n')
    ).rstrip()

    result = f'??? expand "{title}"\n{indented}\n'
    return result, True, ''


# ---------------------------------------------------------------------------
# Datei-Level Migration
# ---------------------------------------------------------------------------

def migrate_file(filepath: Path, dry_run: bool = False) -> dict:
    text = filepath.read_text(encoding='utf-8')
    result = {
        'path': filepath,
        'converted': 0,
        'skipped': [],
        'changed': False,
    }

    blocks = list(iter_details_blocks(text))
    if not blocks:
        return result

    # Replace from end → start so indices stay valid
    for start, end, raw, attrs in reversed(blocks):
        converted, ok, reason = convert_block(raw, attrs)
        if ok:
            text = text[:start] + converted + text[end:]
            result['converted'] += 1
        else:
            result['skipped'].append({
                'file': str(filepath),
                'summary': re.search(r'<summary[^>]*>(.*?)</summary>',
                                     raw, re.DOTALL | re.IGNORECASE),
                'reason': reason,
            })

    if result['converted'] > 0:
        result['changed'] = True
        if not dry_run:
            filepath.write_text(text, encoding='utf-8')

    return result


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description='Migrate <details> → ??? expand')
    parser.add_argument('--dir', default='docs', help='Root directory to search')
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()

    docs_dir = Path(args.dir)
    if not docs_dir.exists():
        print(f'Directory not found: {docs_dir}')
        return

    total_files = 0
    total_converted = 0
    all_skipped = []

    for md_file in sorted(docs_dir.rglob('*.md')):
        r = migrate_file(md_file, dry_run=args.dry_run)
        if r['converted'] > 0:
            total_files += 1
            total_converted += r['converted']
            verb = '[Dry Run] Would update' if args.dry_run else 'Updated'
            print(f'{verb}: {md_file} ({r["converted"]} blocks)')
        all_skipped.extend(r['skipped'])

    print(f'\n{"[Dry Run] " if args.dry_run else ""}Converted {total_converted} blocks across {total_files} files.')

    if all_skipped:
        print('\n=== Nicht migriert ===')
        for s in all_skipped:
            summary_text = s['summary'].group(1) if s['summary'] else '(no summary)'
            print(f'  {s["file"]}  summary={summary_text!r:.60}  reason={s["reason"]}')


if __name__ == '__main__':
    main()
