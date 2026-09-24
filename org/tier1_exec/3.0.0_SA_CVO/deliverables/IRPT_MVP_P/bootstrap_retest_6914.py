"""Replay committed R-P12 assertions unchanged on an exact replacement pair."""
import contextlib
import hashlib
import io
import json
from pathlib import Path
import subprocess

BASELINE = '008107ab97'
BACKEND = '69144433df8c4938cf95cb81e46ac04ae72cc61e'
PORTAL = 'cdc60da247597940b278dd43779b3953565093b7'


def main():
    here = Path(__file__).resolve()
    root = here.parents[5]
    home = here.parent.relative_to(root).as_posix()
    assertion_hashes = {}
    for name in ('bootstrap_cases_cd8.py', 'bootstrap_cases_cd8.test.ts'):
        committed = subprocess.check_output(['git', 'show', f'{BASELINE}:{home}/{name}'], cwd=root)
        local = here.with_name(name).read_bytes()
        assert local == committed, f'Original assertion bytes changed: {name}'
        assertion_hashes[name] = hashlib.sha256(committed).hexdigest()
    source = subprocess.check_output(
        ['git', 'show', f'{BASELINE}:{home}/bootstrap_probe_cd8.py'], cwd=root).decode('utf-8')
    # Adapt only pins, output names and the stated scope; keep capture and assertions intact.
    replacements = {
        "BACKEND = 'cd8d11825424e45fe82f1e78df0396904c0b9ae0'": f"BACKEND = '{BACKEND}'",
        "PORTAL = 'e83ebbfe4f83228f42925b24f77f43e6b6d2a037'": f"PORTAL = '{PORTAL}'",
        "prefix='cvo-p-bootstrap-cd8-'": "prefix='cvo-p-bootstrap-6914-'",
        "name.replace('.json', '_cd8.json')": "name.replace('.json', '_6914.json')",
        'Backend is prior exact source baseline, not a live deployed-hash assertion.':
            'Backend and Portal are exact replacement source commits, not deployed-hash assertions.',
    }
    for old, new in replacements.items():
        assert source.count(old) == 1, f'Driver adaptation no longer unique: {old}'
        source = source.replace(old, new)
    namespace = {'__file__': str(here), '__name__': 'unchanged_baseline_driver'}
    exec(compile(source, str(here), 'exec'), namespace)
    with contextlib.redirect_stdout(io.StringIO()):
        result = namespace['main']()
    evidence_path = here.with_suffix('.json')
    evidence = json.loads(evidence_path.read_text(encoding='utf-8'))
    evidence['baseline_commit'] = BASELINE
    evidence['assertions_identical_to_committed_baseline'] = assertion_hashes
    evidence_path.write_text(json.dumps(evidence, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({key: value for key, value in evidence.items() if key != 'source_sha256'}, indent=2))
    return result


if __name__ == '__main__':
    raise SystemExit(main())
