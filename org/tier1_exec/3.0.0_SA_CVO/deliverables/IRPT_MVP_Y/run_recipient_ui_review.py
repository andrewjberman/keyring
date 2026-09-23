"""Archive exact recipient UI candidate and retain independent/supplied results."""
import hashlib
import io
import json
import os
from pathlib import Path
import shutil
import subprocess
import zipfile


def main():
    own = Path(__file__).resolve().parent
    root = own.parents[4]
    repo = Path('C:/Users/AndrewBerman/Desktop/irpt-mvp-p-portal-20260922')
    pin = subprocess.check_output(['git', 'rev-parse', '5c935bd6'], cwd=repo, text=True).strip()
    target = root / '.runtime/codex-seats/3.0.0_SA_CVO~Y/recipient-ui' / pin
    target.mkdir(parents=True, exist_ok=True)
    raw = subprocess.check_output(['git', 'archive', '--format=zip', pin, 'src', 'public', 'package.json',
        'bun.lock', 'tsconfig.json', 'tsconfig.app.json', 'tsconfig.node.json', 'vite.config.ts',
        'postcss.config.js', 'index.html'], cwd=repo)
    hashes = {}
    with zipfile.ZipFile(io.BytesIO(raw)) as archive:
        for member in archive.infolist():
            path = (target / member.filename).resolve()
            if not path.is_relative_to(target.resolve()):
                raise ValueError('snapshot escape')
            if member.is_dir():
                path.mkdir(parents=True, exist_ok=True)
            else:
                data = archive.read(member)
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(data)
                hashes[member.filename] = hashlib.sha256(data).hexdigest()
    (target / 'review-source-hashes.json').write_text(json.dumps(dict(pin=pin, hashes=hashes)), encoding='utf-8')
    modules = target / 'node_modules'
    if not modules.exists():
        subprocess.run(['powershell', '-NoProfile', '-Command',
            "New-Item -ItemType Junction -Path '" + str(modules) + "' -Target '" + str(repo / 'node_modules') + "' | Out-Null"], check=True)
    bun = shutil.which('bun')
    assert bun
    env = dict(os.environ, IRPT_PORTAL_REVIEW_ROOT=str(target),
               IRPT_RECIPIENT_UI_OUTPUT=str(own / 'RECIPIENT_UI_5c935bd6.json'))
    independent = subprocess.run([bun, 'test', str(own / 'probe_recipient_ui.test.ts')],
        cwd=target, env=env, capture_output=True, text=True, encoding='utf-8', errors='replace')
    prefix = 'src/pages/InvestorReporting/'
    tests = [prefix + 'tabs/analysis/tests', prefix + '__tests__/submission-request.test.ts']
    tests += [prefix + '__tests__/fe-s-15/' + name + '.test.ts' for name in ('composer', 'request-id', 'variant')]
    supplied = subprocess.run([bun, 'test'] + tests, cwd=target, capture_output=True, text=True,
                              encoding='utf-8', errors='replace')
    types = subprocess.run([bun, 'node_modules/typescript/bin/tsc', '-p', 'tsconfig.app.json', '--noEmit'],
                           cwd=target, capture_output=True, text=True, encoding='utf-8', errors='replace')
    def result(run):
        return dict(exit_code=run.returncode, stdout=run.stdout, stderr=run.stderr)
    receipt = dict(pin=pin, source_sha256=hashes, independent=result(independent), supplied=result(supplied),
                   app_typecheck=result(types), no_implementation_changes=True)
    (own / 'RECIPIENT_UI_5c935bd6_VALIDATION.json').write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in receipt.items() if k != 'source_sha256'}, indent=2))
    return int(any(run.returncode for run in (independent, supplied, types)))


if __name__ == '__main__':
    raise SystemExit(main())
