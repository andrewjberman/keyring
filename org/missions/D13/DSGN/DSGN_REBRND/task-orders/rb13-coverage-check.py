"""RB13-AC2R -- every render obligation in the inventory is covered by a render OF THIS CELL. ISSUER artifact
(2.0.0_SA_COO~D), READ-ONLY to the worker.

Usage (from the workspace worktree root):  python rb13-coverage-check.py
Reads:  design/brand/portal-surface-inventory.json                      (the obligations -- rows with render_obligation)
        org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~3/rb13-coverage.json
            {"<route>|<state>": "<png file name in that same folder>", ...}   (written by the RB-s-13 worker)
Prints: VERDICT: COVERED | SHORT | UNMEASURED

Replaces RB13-AC2. AC2 compared the count of EVERY .png under the whole deliverables tree with the number of
obligations, so other cells' captures counted toward this cell's coverage: at the cut, 54 of the 57 PNGs on
record were slot ~1's. Its claim is that every obligation has a render ON RECORD FROM THIS CELL; a count cannot
say WHICH obligation a render covers. So each obligation row must map, by route and state, to a PNG that EXISTS
IN THIS CELL'S OWN FOLDER. A mapping into another folder is refused, and a missing map reads UNMEASURED, never
COVERED. Every uncovered row prints.
"""
import io
import json
import os
import pathlib

INV = pathlib.Path('design/brand/portal-surface-inventory.json')
OWN = pathlib.Path('org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~3')
MAP = OWN / 'rb13-coverage.json'

rows = json.load(io.open(INV, encoding='utf-8')).get('rows', []) if INV.exists() else []
need = [r for r in rows if r.get('render_obligation')]
keys = ['%s|%s' % (r.get('route'), r.get('state')) for r in need]
print('INVENTORY:', INV, 'EXISTS:', INV.exists(), '| rows', len(rows), '| render obligations', len(need),
      '| distinct route|state keys', len(set(keys)))
if not MAP.exists():
    print('COVERAGE MAP:', MAP, 'ABSENT')
    print('VERDICT: UNMEASURED')
    raise SystemExit(0)
cmap = json.load(io.open(MAP, encoding='utf-8'))
covered, missing, foreign, absent = [], [], [], []
for k in keys:
    v = cmap.get(k)
    if not v:
        missing.append(k)
        continue
    if os.path.basename(v) != v:
        foreign.append((k, v))
        continue
    (covered if (OWN / v).is_file() else absent).append((k, v))
print('COVERAGE MAP:', MAP, '| entries', len(cmap))
print('COVERED:', len(covered), 'of', len(keys), '| distinct PNGs used', len({v for _, v in covered}))
for k in missing[:20]:
    print('  MISSING (no map entry):', k)
for k, v in foreign[:20]:
    print('  REFUSED (not a file in this cell\'s own folder):', k, '->', v)
for k, v in absent[:20]:
    print('  ABSENT (mapped PNG does not exist):', k, '->', v)
ok = bool(keys) and len(covered) == len(keys)
print('VERDICT:', 'COVERED' if ok else 'SHORT')
