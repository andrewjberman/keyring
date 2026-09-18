"""RB10-AC2R -- the RENDERED ad-hoc state strings are gone. ISSUER artifact (2.0.0_SA_COO~D), READ-ONLY to the worker.

Usage (from the workspace worktree root):  python rb10-state-census.py [src-root]      default: portal/src
Prints:  VERDICT: MIGRATED | RAW-REMAIN | NO-TREE

Replaces RB10-AC2 (row DSGN_REBRND-W1-S32). AC2 counted four phrases in the WHOLE TEXT of every .tsx file, so
it counted developer log lines -- `console.error('Failed to load ...')` -- that no user ever sees. Its claim is
"every ad-hoc STATE string is gone; the four state components own them"; a string a user cannot see is not a
state string. So the domain is narrowed to the claim's population: any line carrying a console.* call is
EXCLUDED, and the exclusion is COUNTED AND PRINTED, never silent. Same four phrases, same file set, line-based
(AC2's `.{0,30}` never crossed a newline either). A tree with no .tsx files reads NO-TREE, never MIGRATED.
"""
import io
import pathlib
import re
import sys

ROOT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else 'portal/src')
PATS = [r'No .{0,30} available', r'No .{0,30} data', r'Unable to load', r'Failed to load']
CONSOLE = re.compile(r'\bconsole\.(log|warn|error|info|debug)\s*\(')

files = sorted(ROOT.rglob('*.tsx')) if ROOT.is_dir() else []
raw, excluded = [], []
for q in files:
    text = io.open(q, encoding='utf-8', errors='replace').read()
    for i, line in enumerate(text.splitlines(), 1):
        n = sum(len(re.findall(p, line)) for p in PATS)
        if not n:
            continue
        (excluded if CONSOLE.search(line) else raw).append((str(q), i, n, line.strip()[:110]))

nraw = sum(r[2] for r in raw)
nexc = sum(e[2] for e in excluded)
print('ROOT:', ROOT, '| TSX-FILES:', len(files))
print('RENDERED-STATE-STRINGS:', nraw, 'across', len({r[0] for r in raw}), 'file(s)')
print('EXCLUDED (console.* log lines, not rendered):', nexc)
for e in excluded[:10]:
    print('  EXCLUDED:', '%s:%d' % (e[0], e[1]), e[3])
for r in raw[:25]:
    print('  RAW:', '%s:%d' % (r[0], r[1]), r[3])
if not files:
    print('VERDICT: NO-TREE')
else:
    print('VERDICT:', 'MIGRATED' if nraw == 0 else 'RAW-REMAIN')
