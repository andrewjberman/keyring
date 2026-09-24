"""Retest the committed original controls with only candidate/output bindings changed."""
import copy
import hashlib
import io
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import zipfile


def main():
    own = Path(__file__).resolve().parent
    root = own.parents[4]
    output = own / os.environ.get('IRPT_RETEST_DIRECTORY', 'OUTER_RETEST_960f')
    assert output.resolve().is_relative_to(own.resolve())
    output.mkdir(exist_ok=True)
    baseline = '64a2c522ef6144de657f6afccb5e7a3536b9aa49'
    backend_pin = subprocess.check_output(['git', 'rev-parse', os.environ.get('IRPT_RETEST_BACKEND', '960f5f2a45')], cwd=root, text=True).strip()
    portal_repo = Path('C:/Users/AndrewBerman/Desktop/irpt-mvp-p-portal-20260922')
    portal_pin = subprocess.check_output(['git', 'rev-parse', os.environ.get('IRPT_RETEST_PORTAL',
        'c09fea54e9f4613d44b874724e93b79c443f8cc8')], cwd=portal_repo, text=True).strip()
    original = own / 'probe_outer_pair.py'
    original_text = original.read_text(encoding='utf-8')
    committed = subprocess.check_output(['git', 'show', baseline + ':' + original.relative_to(root).as_posix()],
                                        cwd=root, text=True)
    assert original_text == committed, 'original Python controls changed'
    ts = own / 'probe_outer_pair.test.ts'
    ts_text = ts.read_text(encoding='utf-8')
    assert ts_text == subprocess.check_output(['git', 'show', baseline + ':' + ts.relative_to(root).as_posix()],
                                             cwd=root, text=True), 'original TypeScript controls changed'
    substitutions = [("'7915bc9b2c'", repr(backend_pin)),
                     ('own = Path(__file__).resolve().parent', 'own = Path(' + repr(str(output)) + ')')]
    bound = original_text
    for before, after in substitutions:
        assert bound.count(before) == 1
        bound = bound.replace(before, after)
    namespace = dict(__file__=str(original), __name__='unchanged_original_controls')
    exec(compile(bound, str(original), 'exec'), namespace)
    assert namespace['main']() == 0
    backend = json.loads((output / 'OUTER_PAIR_7915_REVIEW.json').read_text())
    assert backend['pin'] == backend_pin
    assert len(backend['controls']) == 24 and all(r['passed'] for r in backend['controls'])
    # The legacy artifact basename is kept solely for the unchanged TS reader.
    # Review and validation receipts record the full pin; baseline artifacts stay intact.
    for result in backend['public_refusal_contract_conflicts']:
        assert not result['exposed_server_only_fields'], result
        assert not result['raw_refusal_status_public_schema_errors'], result
        assert result['projected_refusal_status_valid'], result
    subject = sys.modules['outer_contract_source_tests']
    backend_root = root / '.runtime/codex-seats/3.0.0_SA_CVO~Y/outer-pair-backend' / backend_pin
    schemas = backend_root / 'docs/contracts/investor-reporting/v1'
    served = subject.producer.entry._entry
    extra_controls = []
    outer = json.loads((output / 'OUTER_PAIR_7915_OUTER.json').read_text())
    for kind, pair in outer['cases'].items():
        wire = copy.deepcopy(pair['refusal'])
        wire['status']['internal_correlation_id'] = 'review-server-only'
        assert list(subject.validator(schemas / 'BoundaryRefusal.schema.json').iter_errors(wire))
        extra_controls.append(dict(name=kind + '_public_schema_rejects_reinserted_cid', passed=True))
        operation = pair['refusal']['operation']
        internal = served.status_envelope(operation, 'CONTRACT_VERSION', 'review-server-only')
        assert internal['internal_correlation_id'] == 'review-server-only'
        subject.validator(schemas / 'StatusEnvelope.schema.json').validate(internal)
        public = served.refuse(operation, None, 'CONTRACT_VERSION', 'review-server-only')
        assert public['status'] == {k: v for k, v in internal.items() if k != 'internal_correlation_id'}
        assert internal['internal_correlation_id'] == 'review-server-only'
        extra_controls.append(dict(name=kind + '_internal_diagnostic_retained_exact_public_projection', passed=True))
    portal_root = root / '.runtime/codex-seats/3.0.0_SA_CVO~Y/outer-pair-portal' / portal_pin
    portal_root.mkdir(parents=True, exist_ok=True)
    raw = subprocess.check_output(['git', 'archive', '--format=zip', portal_pin,
        'src', 'public', 'package.json', 'bun.lock', 'tsconfig.json', 'tsconfig.app.json',
        'tsconfig.node.json', 'vite.config.ts', 'postcss.config.js', 'index.html'], cwd=portal_repo)
    hashes = {}
    with zipfile.ZipFile(io.BytesIO(raw)) as archive:
        for member in archive.infolist():
            path = (portal_root / member.filename).resolve()
            if not path.is_relative_to(portal_root.resolve()):
                raise ValueError('snapshot escape')
            if member.is_dir():
                path.mkdir(parents=True, exist_ok=True)
            else:
                data = archive.read(member)
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(data)
                hashes[member.filename] = hashlib.sha256(data).hexdigest()
    (portal_root / 'review-source-hashes.json').write_text(json.dumps(dict(pin=portal_pin, hashes=hashes)), encoding='utf-8')
    modules = portal_root / 'node_modules'
    if not modules.exists():
        subprocess.run(['powershell', '-NoProfile', '-Command',
            "New-Item -ItemType Junction -Path '" + str(modules) + "' -Target '" + str(portal_repo / 'node_modules') + "' | Out-Null"],
            check=True)
    bun = shutil.which('bun')
    assert bun
    environment = dict(os.environ, IRPT_PORTAL_REVIEW_ROOT=str(portal_root),
        IRPT_OUTER_EVIDENCE_ROOT=str(output), IRPT_PORTAL_REVIEW_OUTPUT=str(output / 'PORTAL_c09fea54.json'))
    independent = subprocess.run([bun, 'test', str(ts)], cwd=root, env=environment, capture_output=True, text=True)
    focus = 'src/pages/InvestorReporting/__tests__/mvp-selection/'
    supplied = subprocess.run([bun, 'test', focus + 'owned-outer.test.ts', focus + 'prospect-dates.test.tsx',
        focus + 'public-status.test.ts', focus + 'owned-history.test.ts'],
        cwd=portal_root, capture_output=True, text=True)
    types = subprocess.run([bun, 'node_modules/typescript/bin/tsc', '-p', 'tsconfig.app.json', '--noEmit'],
                           cwd=portal_root, capture_output=True, text=True)
    def result(run):
        return dict(exit_code=run.returncode, stdout=run.stdout, stderr=run.stderr)
    receipt = dict(backend_pin=backend_pin, portal_pin=portal_pin,
        original_review=baseline, original_python_sha256=hashlib.sha256(original_text.encode()).hexdigest(),
        original_ts_sha256=hashlib.sha256(ts_text.encode()).hexdigest(),
        bindings_only=substitutions, extra_controls=extra_controls,
        independent=result(independent), supplied=result(supplied), typecheck=result(types),
        original_controls_unchanged=True,
        scope='Offline actual Entry/source-schema/parser; no browser/runtime/package recertification or integrated grade')
    (output / 'RETEST_VALIDATION.json').write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in receipt.items() if k not in ('bindings_only',)}, indent=2))
    return int(any(run.returncode for run in (independent, supplied, types)))


if __name__ == '__main__':
    raise SystemExit(main())
