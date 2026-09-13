"""Validate the CVO's new rows and prospective original-item census."""
import importlib.util
import json
from pathlib import Path
import subprocess
from amgt_round6_cvo_write_review import rows

ROOT = Path(__file__).resolve().parents[4]
HOME = Path(__file__).parent
PREFIX = 'org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/'
NEW = [PREFIX + 'adjudications/ADJUDICATION_v6.md', PREFIX + 'remediations/REMEDIATION_v5.md', PREFIX + 'remediations/REMEDIATION_v6.md']
spec = importlib.util.spec_from_file_location('gate', ROOT / '.tools/surprise-row-gate.py')
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)
issues = {}
for path in NEW:
    kind = gate._kind(path)
    schema = gate._schema(str(ROOT), kind)
    issues[path] = [v for row in rows(ROOT / path) for v in gate._check_row(row, kind, schema)]
paths = set(NEW)
for pattern in gate.INVESTIGATION_PATTERNS + gate.ADJUDICATION_PATTERNS + gate.REMEDIATION_PATTERNS:
    result, note = gate._index_paths(str(ROOT), [pattern % 'AMGT_RESAPP'])
    assert result is not None, note
    paths.update(result)
files, rem_ids = [], []
for path in sorted(paths):
    records = rows(ROOT / path)
    if gate._kind(path) == 'REMEDIATION':
        rem_ids.extend(r['id'] for r in records)
    else:
        files.append((path, records))
latest, unknown = gate._resolve_latest(files, rem_ids)
duplicates = sorted({rid for rid in rem_ids if rem_ids.count(rid) > 1})
orders = gate._open_tos_for_project(str(ROOT), 'AMGT_RESAPP')
output = {'head': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip(),
          'new_rows': {p: len(rows(ROOT / p)) for p in NEW}, 'row_violations': issues,
          'originals': len(latest), 'open': [k for k, v in latest.items() if v == 'UNDER_INVESTIGATION'],
          'unknown_targets': unknown, 'duplicate_remediation_ids': duplicates, 'orders': orders,
          'limits': 'Prospective working-file census; safe-commit repeats enforcement against its actual index. No overrides.'}
(HOME / 'AMGT_RESAPP_ROUND6_CVO_VALIDATION_20260911_Z.json').write_text(json.dumps(output, indent=2) + '\n', encoding='utf-8')
print(json.dumps(output))
assert not any(issues.values()) and not output['open'] and not unknown and not duplicates
assert orders[0] == [] and orders[1] == 37
