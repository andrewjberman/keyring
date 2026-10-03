# -*- coding: utf-8 -*-
"""RB4-AC6 -- the NON-CANONICAL ordered scales are on ONE hue.

The cell's original premise survives exactly where firm convention does not
reach. The duration ladder is canon and is graded by rb4-canon-check.py; the
sentiment scale is NOT canon -- it is a red-orange-yellow-green consumer-crypto
rainbow encoding a strictly ordered quantity -- and it is what this cell may
still fix.

THE /market EXCEPTION (round 3 E5; the round-2 grade's Q2). Andrew-direct 2026-09-14 ~19:0xZ ("it was changed to a Blue
Gradient, that is not necessary") put the sentiment scale back to its original gradient ON /market ONLY, as the
`[data-sentiment-original]` block in index.css (portal 45aaf58a); 1.0.0_SA_CTO RULINGS batch 215 extends that word to
the page's Global RSI bars. This checker therefore grades the PORTAL-WIDE sentiment tokens (every declaration outside
that block) and prints the block's tokens as EXCEPTED with the record, never as off-ramp. A sentiment token off the ramp
ANYWHERE ELSE still reads RAINBOW-REMAINS.

Run from the workspace worktree root (the directory holding `portal/`):
    python org/missions/D13/DSGN/DSGN_REBRND/task-orders/rb4-ramp-check.py [path-to-index.css]

FAIL-CLOSED: an absent stylesheet, a portal-wide sentiment token that does not
resolve to a ramp step, or a ramp whose steps disagree on hue, all read
RAINBOW-REMAINS.
"""
import pathlib
import re
import sys

CSS = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else 'portal/src/index.css')
if not CSS.is_file():
    print('CSS-ABSENT:', CSS.resolve())
    print('VERDICT: RAINBOW-REMAINS')
    sys.exit(0)

text = CSS.read_text(encoding='utf-8', errors='replace')

# The Andrew-direct /market exception: the one `[data-sentiment-original] { ... }` block, lifted out before grading.
EXCEPTION = re.compile(r'\[data-sentiment-original\]\s*\{[^}]*\}')
excepted_blocks = EXCEPTION.findall(text)
graded = EXCEPTION.sub('', text)

# every --ramp-N declaration, as `H S% L%`
ramps = re.findall(r'--ramp-([1-5])\s*:\s*([0-9.]+)\s+([0-9.]+)%\s+([0-9.]+)%', graded)
ramp_hues = sorted({r[1] for r in ramps})
# every portal-wide --sentiment-* declaration and what it points at
sent = re.findall(r'(--sentiment-[a-z-]+)\s*:\s*([^;]+);', graded)
unresolved = [(k, v.strip()) for k, v in sent if not re.match(r'var\(--ramp-[1-5]\)', v.strip())]
excepted = [k for block in excepted_blocks for k in re.findall(r'(--sentiment-[a-z-]+)\s*:', block)]

print('RAMP-DECLS:', len(ramps), 'across', len(ramp_hues), 'distinct hue(s):', ramp_hues)
print('SENTIMENT-TOKENS (portal-wide):', len(sent), 'of which', len(sent) - len(unresolved), 'resolve to a ramp step')
for k, v in unresolved:
    print('  OFF-RAMP:', k, '=', v[:60])
print('EXCEPTED (/market [data-sentiment-original], Andrew-direct 2026-09-14; CTO batch 215):', len(excepted_blocks),
      'block(s),', len(excepted), 'token(s)', excepted)

ok = (len(ramps) >= 5 and len(ramp_hues) == 1
      and len(sent) >= 5 and not unresolved)
print('VERDICT:', 'ONE-HUE-RAMPED' if ok else 'RAINBOW-REMAINS')
