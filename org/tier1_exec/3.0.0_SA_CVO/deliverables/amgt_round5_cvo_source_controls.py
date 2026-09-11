"""Pin source-only controls; no backend initialization, vendor call or portal write."""
import datetime
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[4]
OUT = Path(__file__).with_name('AMGT_RESAPP_ROUND5_CVO_SOURCE_CONTROLS_20260911_Z.json')


def git(*args, portal=False):
    result = subprocess.run(['git', *args], cwd=ROOT / 'portal' if portal else ROOT,
                            capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=60)
    if result.returncode:
        raise RuntimeError(result.stderr)
    return result.stdout


def main():
    head = git('rev-parse', 'HEAD').strip()
    paths = git('ls-tree', '-r', '--name-only', head, '--', 'infra/aws/terraform/amgt-resapp').splitlines()
    tf_paths = [p for p in paths if p.endswith('.tf') and '/' not in p.removeprefix('infra/aws/terraform/amgt-resapp/')]
    sources = {p: git('show', head + ':' + p) for p in tf_paths}
    definitions = [(p, name) for p, source in sources.items()
                   for name in re.findall(r'^\s*resource\s+"aws_dynamodb_table"\s+"([^"]+)"', source, re.M)]
    references = [(p, n, line.strip()) for p, source in sources.items()
                  for n, line in enumerate(source.splitlines(), 1)
                  if 'aws_dynamodb_table.' in line or 'table/opal-amgt-articles' in line]
    report = {'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'head': head,
              'scope': 'Committed source only. No AWS read/write, terraform init/apply, or deployed ZIP assertion.',
              'amgt_root_tf_files': tf_paths, 'dynamodb_definitions_in_root': definitions,
              'stale_scheduler_references': references,
              'source_sha256': {p: hashlib.sha256(s.encode()).hexdigest() for p, s in sources.items()}}
    harvest_path = 'infra/aws/terraform/harvest/dynamodb.tf'
    harvest = git('show', head + ':' + harvest_path)
    report['harvest_table_declarations'] = [(n, line.strip()) for n, line in enumerate(harvest.splitlines(), 1)
                                           if 'resource "aws_dynamodb_table"' in line or 'name ' in line]
    report['source_sha256'][harvest_path] = hashlib.sha256(harvest.encode()).hexdigest()
    pin = git('rev-parse', 'e6057f26^{commit}', portal=True).strip()
    report['portal_pin'] = pin
    report['portal_sources'] = {}
    for path in ['tsconfig.json', 'src/pages/SecurityAnalysis/components/LeadPanel.tsx',
                 'src/pages/SecurityAnalysis/components/StarredList.tsx',
                 'src/pages/SecurityAnalysis/components/RankedChart.tsx',
                 'src/pages/SecurityAnalysis/__rendercheck__/renderCheck.tsx']:
        source = git('show', pin + ':' + path, portal=True)
        report['portal_sources'][path] = {'sha256': hashlib.sha256(source.encode()).hexdigest(), 'source': source}
    spec = importlib.util.spec_from_file_location('cvo_row_gate', ROOT / '.tools/surprise-row-gate.py')
    gate = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(gate)
    report['open_tos'] = gate._open_tos_for_project(str(ROOT), 'AMGT_RESAPP')
    report['route_precondition'] = gate._route_precondition_violations(
        str(ROOT), 'org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/remediations/REMEDIATION_v5.md',
        {'id': 'AMGT_RESAPP-Z-CVO-PREFLIGHT', 'route': 'L6'}, 'AMGT_RESAPP')
    OUT.write_text(json.dumps(report, indent=2, ensure_ascii=True) + '\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in report.items() if k not in ['portal_sources', 'source_sha256']}, ensure_ascii=True))


if __name__ == '__main__':
    main()
