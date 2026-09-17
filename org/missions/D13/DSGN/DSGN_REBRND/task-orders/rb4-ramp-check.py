# -*- coding: utf-8 -*-
"""RB4-AC6 -- the NON-CANONICAL ordered scales are on ONE hue.

The cell's original premise survives exactly where firm convention does not
reach. The duration ladder is canon and is graded by rb4-canon-check.py; the
sentiment scale is NOT canon -- it is a red-orange-yellow-green consumer-crypto
rainbow encoding a strictly ordered quantity -- and it is what this cell may
still fix.

Run from the workspace worktree root (the directory holding `portal/`):
    python org/missions/D13/DSGN/DSGN_REBRND/task-orders/rb4-ramp-check.py

FAIL-CLOSED: an absent stylesheet, a sentiment token that does not resolve to a
ramp step, or a ramp whose steps disagree on hue, all read RAINBOW-REMAINS.
"""
import pathlib
import re
import sys

CSS = pathlib.Path('portal/src/index.css')
if not CSS.is_file():
    print('CSS-ABSENT:', CSS.resolve())
    print('VERDICT: RAINBOW-REMAINS')
    sys.exit(0)

text = CSS.read_text(encoding='utf-8', errors='replace')

# every --ramp-N declaration, as `H S% L%`
ramps = re.findall(r'--ramp-([1-5])\s*:\s*([0-9.]+)\s+([0-9.]+)%\s+([0-9.]+)%', text)
ramp_hues = sorted({r[1] for r in ramps})
# every --sentiment-* declaration and what it points at
sent = re.findall(r'(--sentiment-[a-z-]+)\s*:\s*([^;]+);', text)
unresolved = [(k, v.strip()) for k, v in sent if not re.match(r'var\(--ramp-[1-5]\)', v.strip())]

print('RAMP-DECLS:', len(ramps), 'across', len(ramp_hues), 'distinct hue(s):', ramp_hues)
print('SENTIMENT-TOKENS:', len(sent), 'of which', len(sent) - len(unresolved), 'resolve to a ramp step')
for k, v in unresolved:
    print('  OFF-RAMP:', k, '=', v[:60])

ok = (len(ramps) >= 5 and len(ramp_hues) == 1
      and len(sent) >= 5 and not unresolved)
print('VERDICT:', 'ONE-HUE-RAMPED' if ok else 'RAINBOW-REMAINS')
