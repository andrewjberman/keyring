# -*- coding: utf-8 -*-
"""RB4-AC4R -- THE CANONICAL DURATION LADDER IS INTACT AT EVERY SITE.

Andrew-direct 2026-09-11, VERBATIM: "all five are canonical, revert and add
FactorTilts as the sixth. These are the only colors that truly must stay locked
in."  The five duration colours are FIRM CONVENTION, not a style choice, and the
cell's original premise -- that an ordered quantity encoded as unordered hue is a
reading error to be removed -- DOES NOT REACH THEM.

Run from the workspace worktree root (the directory holding `portal/`):
    python org/missions/D13/DSGN/DSGN_REBRND/task-orders/rb4-canon-check.py

WHY FIVE ARMS. The ladder is written in five grammars, and an instrument that
reads one of them certifies the others clean while they are broken:
  ARM A  rung-LABELLED   `id: 'UST'` / `name: 'Ultra-Short Term'` -- self-describing.
                         AMENDMENT 2: when the label line carries NO colour, the
                         object's `primary:` line up to 4 lines below is read
                         (row DSGN_REBRND-W1-S17: MODEL_PORTFOLIO_COLORS puts the
                         name and the colour on separate lines, and the five
                         canonical primaries were invisible to arm A).
  ARM B  POSITIONAL      BOOK_COLOR_CYCLE, MODEL_COLORS -- five colours in rung
                         order with NO rung token anywhere on the line. Arm A is
                         structurally blind to these, and BOOK_COLOR_CYCLE is the
                         writer that actually renders the /positioning chips.
  ARM C  EARLIER NAMES   'Aggressive'/'Conservative'/... in aum.ts -- invisible to
                         both arms above. BOUNDED; see LEGACY_TELL below.
  ARM D  ORDER           duration order UST ST INT LT ULT along the reading axis.
  ARM E  RUNG-NAMED CONST (AMENDMENT 2, row DSGN_REBRND-W1-S15) --
                         `const ULT_COLOR = '#...'`. ReturnVolatilityScatter's
                         shared ULT/LT benchmark diamond is painted from two such
                         constants, and no other arm could see them.

FAIL-CLOSED: an absent tree, a missing writer or a rung never seen all read
CANON-BROKEN. An empty sweep must never score as a clean pass.
"""
import pathlib
import re
import sys

SRC = pathlib.Path('portal/src')
CANON = {'UST': '#F97316', 'ST': '#F59E0B', 'INT': '#10B981',
         'LT': '#3B82F6', 'ULT': '#EF4444'}
CANONSET = set(CANON.values())
POSITIONAL = ['BOOK_COLOR_CYCLE', 'MODEL_COLORS']
LONG = {'Ultra-Short Term': 'UST', 'Ultra Short-Term': 'UST',
        'Short Term': 'ST', 'Short-Term': 'ST',
        'Intermediate Term': 'INT', 'Intermediate': 'INT',
        'Long Term': 'LT', 'Long-Term': 'LT',
        'Ultra-Long Term': 'ULT', 'Ultra Long-Term': 'ULT'}
# ARM C -- the EARLIER model names. Andrew-direct 2026-09-11: "Those are earlier
# names, Aggressive is ULT, Conservative is LT, the rest are obvious." A writer
# keyed by a legacy name is invisible to arms A and B, and `aum.ts` is one.
LEGACY = {'Aggressive': 'ULT', 'Conservative': 'LT', 'Intermediate': 'INT',
          'Short-Term': 'ST', 'Ultra Short-Term': 'UST'}
LEGACY_KEY = re.compile(r"'(" + '|'.join(re.escape(k) for k in LEGACY) + r")'\s*:")
# ARM C IS BOUNDED, and the bound is load-bearing. 'Intermediate' and 'Short-Term'
# are AMBIGUOUS -- they also name maturity buckets in the sub-asset-class palettes,
# which are a deliberate green-by-duration ramp and are NOT the model ladder. Fired
# unbounded, arm C reported holdings-shared.tsx:82 and chartColors.ts:289 as
# off-canon when they are a different taxonomy entirely. 'Aggressive' and
# 'Conservative' are UNAMBIGUOUSLY model names, so they are the tell: arm C fires
# only inside a file that carries one of them as a key.
LEGACY_TELL = re.compile(r"'(Aggressive|Conservative)'\s*:")
# ARM E -- a constant NAMED for its rung.
RUNG_CONST = re.compile(r'\b(?:const|let|var)\s+(UST|ST|INT|LT|ULT)_COLOR\b[^=]*=(.*)')
HEX = re.compile(r'#([0-9a-fA-F]{6})\b')

if not SRC.is_dir():
    print('SRC-ABSENT:', SRC.resolve())
    print('VERDICT: CANON-BROKEN')
    sys.exit(0)

SYM = {}
for p in SRC.rglob('*.ts*'):
    for k, v in re.findall(r"(\w+)\s*:\s*'(#[0-9a-fA-F]{6})'",
                           p.read_text(encoding='utf-8', errors='replace')):
        SYM.setdefault(k, v.upper())


def colour_on(line):
    """Resolve a hex literal OR one level of PALETTE.<name> indirection.
    Grading only hex would score a correct named-constant encoding as broken."""
    m = HEX.search(line)
    if m:
        return '#' + m.group(1).upper()
    n = re.search(r'PALETTE\.(\w+)', line)
    return SYM.get(n.group(1)) if n and n.group(1) in SYM else None


def primary_below(lines, i):
    """ARM A lookahead (Amendment 2): the object's `primary:` colour within 4 lines
    of a colourless label line, stopping at the object's close. Only `primary:` is
    read, so an unrelated object carrying a rung name and no primary yields nothing."""
    for k in range(i, min(i + 4, len(lines))):
        ln = lines[k]
        if re.match(r'\s*\}', ln):
            return None
        if re.search(r'\bprimary\s*:', ln):
            return colour_on(ln)
    return None


ORDER = ['UST', 'ST', 'INT', 'LT', 'ULT']          # duration order, left to right
CANON_SEQ = [CANON[r] for r in ORDER]
sites, bad, posn, idorder = [], [], {}, {}
arm_e, arm_a_look = [], []
for p in sorted(SRC.rglob('*.ts*')):
    text = p.read_text(encoding='utf-8', errors='replace')
    lines = text.splitlines()
    legacy_here = bool(LEGACY_TELL.search(text))
    seen = [m.group(1) for m in re.finditer(r"id:\s*'(UST|ST|INT|LT|ULT)'", text)]
    if sorted(seen) == sorted(ORDER):
        idorder[str(p)] = seen
    for i, line in enumerate(lines, 1):
        if line.strip().startswith('//'):
            continue
        rung, via = None, None
        m_id = re.search(r"id:\s*'(UST|ST|INT|LT|ULT)'", line)
        m_rc = RUNG_CONST.search(line)
        if m_id:
            rung = m_id.group(1)
        elif m_rc:
            rung, via = m_rc.group(1), 'E'
        else:
            m_nm = re.search(r"name:\s*'([^']+)'", line)
            if m_nm and m_nm.group(1) in LONG:
                rung = LONG[m_nm.group(1)]
            else:
                # ARM C -- a bare quoted key on an EARLIER model name. Anchored to
                # the whole key, so 'Long-Term Aggressive' does NOT match 'Aggressive'.
                m_lg = LEGACY_KEY.search(line) if legacy_here else None
                if m_lg:
                    rung = LEGACY[m_lg.group(1)]
        if not rung:
            continue
        got = colour_on(m_rc.group(2) if via == 'E' else line)
        if not got and via is None:
            got = primary_below(lines, i)
            if got:
                via = 'A-lookahead'
        if not got:
            continue
        sites.append((str(p), i, rung, got))
        if via == 'E':
            arm_e.append((str(p) + ':' + str(i), rung, got))
        elif via == 'A-lookahead':
            arm_a_look.append((str(p) + ':' + str(i), rung, got))
        if got != CANON[rung]:
            bad.append((str(p) + ':' + str(i), rung, got, CANON[rung]))
    for name in POSITIONAL:
        if name in posn:
            continue
        m = re.search(r'\b(?:const|let|var)\s+' + name + r'\b[^=]*=\s*\[', text)
        if not m:
            continue
        depth, j = 0, m.end() - 1
        start = j
        while j < len(text):
            if text[j] == '[':
                depth += 1
            elif text[j] == ']':
                depth -= 1
                if depth == 0:
                    break
            j += 1
        posn[name] = (str(p), [c for c in (colour_on(ln)
                                           for ln in text[start:j].splitlines()) if c])

files = sorted({s[0] for s in sites})
rungs = sorted({s[2] for s in sites})
print('ARM-A LADDER-SITES:', len(sites), 'across', len(files), 'file(s):', files)
print('ARM-A RUNGS-SEEN:', rungs, 'of', sorted(CANON))
print('ARM-A LOOKAHEAD SITES (label and primary on separate lines):', len(arm_a_look))
print('ARM-E RUNG-NAMED CONST SITES:', len(arm_e), [s[0] for s in arm_e])
for b in bad:
    print('  OFF-CANON:', b[0], b[1], 'is', b[2], 'canon', b[3])
missB = []
for name in POSITIONAL:
    if name not in posn:
        missB.append(name)
        print('  ARM-B', name, 'NOT FOUND -- a positional writer that vanished is not a pass')
        continue
    f, cs = posn[name]
    lack = sorted(CANONSET - set(cs))
    print('  ARM-B', name, 'in', f, '->', cs, ('OK' if not lack else 'MISSING ' + str(lack)))
    if lack:
        missB.append(name)

# ARM D -- ORDER IS CANON TOO. Andrew-direct 2026-09-11: "They must always be
# listed in the same order with same colors, it is duration order, UST ST INT LT
# ULT. Always this way, left to right" ... "or top to bottom if in a vertical
# context." Declaration sequence IS the reading axis on either orientation, so one
# check covers both. Applies to ARRAYS, which render in sequence; a keyed lookup
# Record is EXEMPT and the exemption is printed, never silent.
misorder = []
for f, seq in sorted(idorder.items()):
    good = seq[:5] == ORDER
    print('  ARM-D order', f, '->', seq[:5], 'OK' if good else 'NOT DURATION ORDER, want ' + str(ORDER))
    if not good:
        misorder.append(f)
for name in POSITIONAL:
    if name not in posn:
        continue
    f, cs = posn[name]
    tail = [c for c in cs if c in CANONSET]
    good = tail == CANON_SEQ
    print('  ARM-D order', name, '->', tail, 'OK' if good else 'NOT DURATION ORDER, want ' + str(CANON_SEQ))
    if not good:
        misorder.append(name)
print('  ARM-D EXEMPT (keyed lookup, declaration order does not render):'
      ' MODEL_PORTFOLIO_COLORS, getModelColor colorMap')

ok = (len(sites) >= 10 and len(files) >= 3 and len(rungs) == 5
      and not bad and not missB and not misorder and len(idorder) >= 2)
print('VERDICT:', 'CANON-INTACT' if ok else 'CANON-BROKEN')
