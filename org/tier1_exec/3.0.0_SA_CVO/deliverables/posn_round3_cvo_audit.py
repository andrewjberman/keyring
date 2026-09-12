"""Bounded CVO controls: pinned source, local downloaded bytes, no live clients."""
import ast
import contextlib
import copy
import datetime
import hashlib
import io
import json
from pathlib import Path
import socket
import subprocess
import sys
import tempfile
import types
import zipfile

ROOT = Path(__file__).resolve().parents[4]
HOME = Path(__file__).parent
PROJECT = 'org/missions/D4/POSN/POSN_ASTTAX'
GEN = 'infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py'
SEED = 'infra/aws/lambda/v2_portal/yang_pipeline/seed-etf-classifications.py'
MODULE = 'infra/aws/lambda/v2_portal/_shared/etf_classification.py'
PIN = '3ce0c0e372'
PORTAL_PIN = 'e85f6eb84f'


def command(args):
    p = subprocess.run(args, cwd=ROOT, capture_output=True, text=True, encoding='utf-8', errors='replace')
    return {'rc': p.returncode, 'stdout': p.stdout, 'stderr': p.stderr}


def blob(path, pin=PIN):
    r = command(['git', 'show', pin + ':' + path])
    assert r['rc'] == 0, r
    return r['stdout']


def definitions(source, name):
    tree = ast.parse(source)
    # Deliberately omit top-level for/main: materialise() is never called.
    tree.body = [n for n in tree.body if isinstance(n, (ast.Import, ast.ImportFrom, ast.Assign, ast.FunctionDef, ast.ClassDef))]
    m = types.ModuleType(name)
    exec(compile(tree, name, 'exec'), m.__dict__)
    return m


def digest(data):
    return {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(), 'md5': hashlib.md5(data).hexdigest()}


def main():
    def blocked(*args, **kwargs):
        raise AssertionError('CVO offline control blocked a network connection')
    socket.socket.connect = blocked
    socket.socket.connect_ex = blocked
    socket.create_connection = blocked
    sys.dont_write_bytecode = True
    result = {'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
              'head': command(['git', 'rev-parse', 'HEAD']), 'source_pin': PIN, 'portal_pin': PORTAL_PIN,
              'limits': 'No live AWS read/write, deploy, retag, portal build or DOM exercise. Synthetic generator inputs; downloaded zip provenance is worker-recorded, digest independently checked.'}
    t5path = PROJECT + '/deliverables/0.9.0_WK_POSN_ASTTAX~14/t5_ac3_bar_v2.py'
    t5 = definitions((ROOT / t5path).read_text(encoding='utf-8'), 'cvo_t5_defs')
    source = blob(GEN).encode()
    zip_path = Path('C:/tmp/wk-posn-t5/.scratch/yang-generate-positioning.DEPLOYED.zip')
    with zipfile.ZipFile(zip_path) as z:
        deployed = z.read('lambda_function.py')
    result['generator_bytes'] = {'source': digest(source), 'downloaded': digest(deployed), 'downloaded_path': str(zip_path)}
    assert digest(deployed)['md5'] == 'cc79aff7506f8c39e17453f386c69551'
    result['generator_arms'] = []
    with tempfile.TemporaryDirectory(prefix='cvo-posn-r3-') as td:
        for arm, data in [('pinned_source', source), ('worker_downloaded', deployed)]:
            p = Path(td) / (arm + '.py')
            p.write_bytes(data)
            for ticker, before, target, weight in t5.MEMBERS:
                readings = {}
                for phase, raw in [('before', before), ('after', target)]:
                    readings[phase] = t5.run_arm(str(p), arm + phase + ticker, ticker, raw, target, weight)
                result['generator_arms'].append({'arm': arm, 'ticker': ticker, 'candidate_target': target,
                                                 'input_weight': weight, 'readings': readings})
        t1 = definitions((ROOT / (PROJECT + '/deliverables/0.9.0_WK_POSN_ASTTAX~10/ac3_before_after_five_classes.py')).read_text(encoding='utf-8'), 'cvo_t1_defs')
        result['t1_classes'] = []
        p = Path(td) / 'pinned_source.py'
        for raw, label in [('equity','Equity'), ('fixed_income','Fixed Income'), ('cash','Cash'),
                           ('structured','Structured'), ('commodities','Commodities'), ('alternatives','Alternatives'),
                           ('ZZ_CVO_UNRATIFIED','Unknown')]:
            with contextlib.redirect_stdout(io.StringIO()):
                m = t1.load_generator('cvo_' + raw, str(p), t1.make_registry(raw))
                payload, log = t1.serve(m)
            r = t1.readings(payload, raw, label)
            r.update(raw=raw, target=label, warnings=[line for line in log.splitlines() if 'WARN' in line])
            result['t1_classes'].append(r)
        # Actual seed_table with real maps, wholly in-memory target. The race arm changes one
        # curated attribute AFTER scan and BEFORE put, exposing the snapshot boundary.
        source_seed = blob(SEED, '8adab5748d2b58091bb0a19ebf16e15e27846e47')
        maps = types.ModuleType('etf_classification')
        exec(compile(blob(MODULE, '8adab5748d2b58091bb0a19ebf16e15e27846e47'), MODULE, 'exec'), maps.__dict__)
        sys.modules['etf_classification'] = maps
        result['reseed_controls'] = []
        for scenario in ['normal', 'conflict', 'scan_denied', 'concurrent_curation']:
            class Table:
                def __init__(self):
                    self.rows = {'ACSG': {'ticker':'ACSG', 'asset_class': maps.ETF_CLASSIFICATIONS['ACSG'], 'curator_note':'A'}}
                    if scenario == 'conflict':
                        self.rows['ACSG']['asset_class'] = 'ZZ_CONFLICT'
                    self.writes = []
                def scan(self, **kwargs):
                    if scenario == 'scan_denied':
                        raise RuntimeError('CVO simulated missing Scan permission')
                    response = {'Items': copy.deepcopy(list(self.rows.values()))}
                    if scenario == 'concurrent_curation':
                        self.rows['ACSG']['curator_note'] = 'B'
                    return response
                def batch_writer(self):
                    return self
                def __enter__(self):
                    return self
                def __exit__(self, *args):
                    return False
                def put_item(self, Item):
                    self.writes.append(copy.deepcopy(Item))
                    self.rows[Item['ticker']] = copy.deepcopy(Item)
            table = Table()
            fake = types.ModuleType('boto3')
            fake.resource = lambda *a, **k: types.SimpleNamespace(Table=lambda name: table)
            fake.client = blocked
            sys.modules['boto3'] = fake
            seed = types.ModuleType('cvo_seed_' + scenario)
            seed.__file__ = str(ROOT / SEED)
            with contextlib.redirect_stdout(io.StringIO()) as captured:
                exec(compile(source_seed, SEED, 'exec'), seed.__dict__)
                rc = seed.seed_table()
            result['reseed_controls'].append({'scenario':scenario, 'rc':rc, 'writes':len(table.writes),
                                              'ACSG_after':table.rows['ACSG'], 'stdout':captured.getvalue()})
    second = 'data/black_diamond/scripts/classification/seed_canonical_securities.py'
    tree = ast.parse(blob(second))
    securities = next(ast.literal_eval(n.value) for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='CANONICAL_SECURITIES' for t in n.targets))
    candidates = {x[0] for x in t5.MEMBERS}
    result['second_writer'] = {'path': second, 'securities':len(securities),
                               'intersection':[x for x in securities if x['ticker'] in candidates],
                               'update_source':blob(second).splitlines()[252:274]}
    result['portal_category_consumers'] = command(['git','-C','portal','grep','-n','-e','getETFCategory','-e','ETF_CATEGORIZATION','-e','etf-categories',PORTAL_PIN,'--','src'])
    result['portal_snippets'] = {}
    for path, start, end in [('src/pages/Attribution/constants/holdings-shared.tsx',141,156),
                              ('src/pages/Positioning/tabs/HoldingsTab.tsx',276,295),
                              ('src/pages/Positioning/tabs/HoldingsTab.tsx',1380,1404)]:
        read = command(['git','-C','portal','show',PORTAL_PIN+':'+path])
        assert read['rc'] == 0
        result['portal_snippets'][path+':'+str(start)] = read['stdout'].splitlines()[start-1:end]
    result['summary'] = {'candidate_source_after_carried':sum('RAISED' not in x['readings']['after'] and x['readings']['after']['label']==x['candidate_target'] for x in result['generator_arms'] if x['arm']=='pinned_source'),
                         'candidate_downloaded_after_raises':sum('RAISED' in x['readings']['after'] for x in result['generator_arms'] if x['arm']=='worker_downloaded'),
                         'candidate_denominator':len(t5.MEMBERS)}
    (HOME / 'POSN_ASTTAX_ROUND3_CVO_EVIDENCE_20260912_Z.json').write_text(json.dumps(result,indent=2,ensure_ascii=True)+'\n',encoding='utf-8')
    print(json.dumps(result['summary']))
    print(json.dumps([{k:r[k] for k in ['scenario','rc','writes','ACSG_after']} for r in result['reseed_controls']]))
    print(result['portal_category_consumers']['stdout'])


if __name__ == '__main__':
    main()
