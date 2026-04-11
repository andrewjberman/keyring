"""comp-tooltip — Portal tooltip pattern detector and migration audit.

Scans portal/src/ for tooltip rendering patterns, classifies them against
the canonical spec (dark navy bg, white text, subtle border), and reports
migration status.

Canonical model: dark navy background (--bg-header or --bg-tooltip),
white text (full opacity values, /70 labels), subtle white/10 or white/20
border, rounded-lg, shadow, optional color swatches.

Usage:
    comp-tooltip scan          — full scan, all variants
    comp-tooltip canonical     — show only canonical (already correct) sites
    comp-tooltip drift         — show only non-conforming sites (migration targets)
    comp-tooltip migrated      — show only sites using <DataTooltip> (post-migration)
    comp-tooltip summary       — counts by variant
"""
import sys
import os
import re
from pathlib import Path
from collections import defaultdict

WORKSPACE = Path(__file__).resolve().parents[3]
PORTAL_SRC = WORKSPACE / "portal" / "src"


# --- Pattern definitions ---

# Background tokens used in tooltips
BG_HEADER = r'bg-\[hsl\(var\(--bg-header\)\)\]'
BG_TOOLTIP = r'bg-\[hsl\(var\(--bg-tooltip\)\)\]'
BG_CANONICAL = r'bg-\[hsl\(var\(--semantic-background-chartTooltipBg\)\)\]'
BG_SLATE = r'bg-slate-900'

# Border patterns
BORDER_WHITE_20 = r'border\s+border-white/20'
BORDER_WHITE_10 = r'border(?:-2)?\s+border-white/10'
BORDER_PRIMARY = r'border-2\s+border-\[hsl\(var\(--primary\)\)\]'
BORDER_ACCENT_INLINE = r'borderColor|border.*style\s*='

# Shadow patterns (key differentiator: tooltips have shadows, UI chrome doesn't)
SHADOW = r'shadow-(?:xl|2xl|lg)'

# Structural patterns
ROUNDED = r'rounded-(?:lg|md)'
PADDING_TOOLTIP = r'p[xy]?-[234]'

# Post-migration pattern
DATA_TOOLTIP_COMPONENT = r'<DataTooltip\b'

# Helper tooltip inline pattern
HELPER_INLINE = r'bg-\[hsl\(var\(--semantic-action-primary\)\)\].*whitespace-nowrap'

# Recharts tooltip content prop (identifies tooltip render function context)
RECHARTS_CONTENT = r'content=\{.*[Tt]ooltip|<(?:Recharts)?Tooltip\s+content='


def classify_line(line, file_content_around):
    """Classify a single line's tooltip variant."""
    # Post-migration: DataTooltip component
    if re.search(DATA_TOOLTIP_COMPONENT, line):
        return 'DATATOOLTIP'

    # Exclude non-tooltip UI elements:
    # - Dropdown panels (top-full = opens downward from a button)
    # - Fixed menus (fixed position popups like sidebar user menu)
    # - Option elements (select dropdown styling)
    if re.search(r'top-full\s+left-0\s+mt-', line):
        return None
    if re.search(r'\bfixed\b', line) and re.search(r'Z_INDEX', line):
        return None

    # Inline helper tooltips: pointer-events-none + absolute + bottom-full + HelpCircle context
    # These should use <Tooltip> component, not inline styles
    if re.search(r'pointer-events-none\s+absolute\s+bottom-full', line):
        if re.search(SHADOW, line):
            return 'HELPER_INLINE'
        return None

    # Check for shadow — the key differentiator between tooltip and UI chrome
    has_shadow = bool(re.search(SHADOW, line))

    # Old "canonical" silver bg — these are ALSO migration targets now.
    # The correct canonical is dark navy via DataTooltip component.
    if re.search(BG_CANONICAL, line):
        if re.search(BORDER_PRIMARY, line):
            return 'INLINE_SILVER'
        return 'VARIANT_E'

    # Only classify as tooltip if shadow is present
    if not has_shadow:
        return None

    # Variant A: bg-header + border-white/20 + shadow (most common drift)
    if re.search(BG_HEADER, line) and re.search(BORDER_WHITE_20, line):
        return 'INLINE_NAVY'

    # Variant A with border-white/10 + shadow (FactorTilts pattern)
    if re.search(BG_HEADER, line) and re.search(BORDER_WHITE_10, line) and re.search(ROUNDED, line):
        return 'INLINE_NAVY'

    # bg-tooltip variants (same dark navy family)
    if re.search(BG_TOOLTIP, line) and re.search(ROUNDED, line):
        return 'INLINE_NAVY'

    # Variant D: hardcoded slate-900 + shadow
    if re.search(BG_SLATE, line) and re.search(SHADOW, line):
        return 'INLINE_HARDCODED'

    return None


def scan_file(filepath):
    """Scan a single file for tooltip patterns. Returns list of (line_num, variant, line_text)."""
    results = []
    try:
        content = filepath.read_text(encoding='utf-8', errors='replace')
    except Exception:
        return results

    lines = content.split('\n')
    for i, line in enumerate(lines, 1):
        variant = classify_line(line, lines[max(0, i-5):i+5])
        if variant:
            results.append((i, variant, line.strip()))

    # Also scan for DataTooltip component usage (multi-line)
    for i, line in enumerate(lines, 1):
        if re.search(DATA_TOOLTIP_COMPONENT, line) and not any(r[0] == i for r in results):
            results.append((i, 'DATATOOLTIP', line.strip()))

    return results


def scan_all():
    """Scan all .tsx files in portal/src/."""
    all_results = []
    for filepath in sorted(PORTAL_SRC.rglob('*.tsx')):
        file_results = scan_file(filepath)
        if file_results:
            rel = filepath.relative_to(WORKSPACE)
            for line_num, variant, line_text in file_results:
                all_results.append((str(rel).replace('\\', '/'), line_num, variant, line_text))
    return all_results


VARIANT_LABELS = {
    'DATATOOLTIP': 'DataTooltip component (correct)',
    'INLINE_NAVY': 'Inline navy tooltip -- migrate to <DataTooltip>',
    'INLINE_SILVER': 'Inline silver tooltip -- migrate to <DataTooltip>',
    'INLINE_HARDCODED': 'Inline hardcoded (slate-900) -- migrate to <DataTooltip>',
    'VARIANT_E': 'Inline silver + accent border -- migrate to <DataTooltip>',
    'HELPER_INLINE': 'Helper tooltip (inline, should use <Tooltip> component)',
}

VARIANT_ORDER = ['DATATOOLTIP', 'INLINE_NAVY', 'INLINE_SILVER', 'INLINE_HARDCODED', 'VARIANT_E', 'HELPER_INLINE']


def print_results(results, filter_fn=None):
    """Print results grouped by variant."""
    if filter_fn:
        results = [r for r in results if filter_fn(r[2])]

    if not results:
        print("No matches found.")
        return

    by_variant = defaultdict(list)
    for filepath, line_num, variant, line_text in results:
        by_variant[variant].append((filepath, line_num, line_text))

    for variant in VARIANT_ORDER:
        entries = by_variant.get(variant, [])
        if not entries:
            continue
        label = VARIANT_LABELS.get(variant, variant)
        print(f"\n## {label} ({len(entries)} sites)")
        print()
        for filepath, line_num, line_text in entries:
            # Truncate long lines
            display = line_text[:120] + ('...' if len(line_text) > 120 else '')
            print(f"  {filepath}:{line_num}")
            print(f"    {display}")
        print()


def print_summary(results):
    """Print summary counts."""
    counts = defaultdict(int)
    for _, _, variant, _ in results:
        counts[variant] += 1

    total = len(results)
    canonical = counts.get('DATATOOLTIP', 0)
    drift = total - canonical

    print("\n## Tooltip Audit Summary")
    print()
    print(f"  Total tooltip sites found: {total}")
    print(f"  Canonical / migrated:      {canonical}")
    print(f"  Non-conforming (drift):    {drift}")
    print()
    print("  Breakdown:")
    for variant in VARIANT_ORDER:
        count = counts.get(variant, 0)
        if count:
            label = VARIANT_LABELS.get(variant, variant)
            marker = ' (OK)' if variant == 'DATATOOLTIP' else ' ** MIGRATE **'
            print(f"    {label}: {count}{marker}")
    print()

    if drift > 0:
        print(f"  Migration progress: {canonical}/{total} ({100*canonical//total if total else 0}%)")
    else:
        print("  All tooltips are canonical or migrated.")


def main():
    if not PORTAL_SRC.exists():
        print(f"ERROR: portal/src/ not found at {PORTAL_SRC}", file=sys.stderr)
        sys.exit(1)

    cmd = sys.argv[1] if len(sys.argv) > 1 else 'scan'

    results = scan_all()

    if cmd == 'scan':
        print_results(results)
        print_summary(results)
    elif cmd == 'canonical':
        print_results(results, lambda v: v == 'DATATOOLTIP')
    elif cmd == 'drift':
        print_results(results, lambda v: v != 'DATATOOLTIP')
    elif cmd == 'migrated':
        print_results(results, lambda v: v == 'DATATOOLTIP')
    elif cmd == 'summary':
        print_summary(results)
    else:
        print(__doc__)
        sys.exit(1)


if __name__ == '__main__':
    main()
