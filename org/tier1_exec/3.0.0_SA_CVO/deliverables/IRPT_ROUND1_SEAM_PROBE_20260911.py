"""Offline CVO cross-project check. Never contacts cloud or a vendor."""
from pathlib import Path
import datetime
import hashlib
import json
import re
import subprocess
from jsonschema import Draft202012Validator
ROOT = Path(__file__).resolve().parents[4]
OUT = ROOT / '.runtime/codex-seats/3.0.0_SA_CVO/irpt-round1-review'
OUT.mkdir(parents=True, exist_ok=True)
def read(p): return (ROOT/p).read_text(encoding='utf-8-sig')
def git(*args): return subprocess.check_output(['git',*args],cwd=ROOT).decode().strip()
def provenance(p):
    pp=Path(p)
    sub=pp.parts[0]=='portal'
    repo=ROOT/'portal' if sub else ROOT
    rel=pp.relative_to('portal').as_posix() if sub else pp.as_posix()
    pin=subprocess.check_output(['git','log','-1','--format=%H','--',rel],cwd=repo).decode().strip()
    return {'path':pp.as_posix(),'repository':'portal' if sub else 'workspace','pin':pin,'sha256':hashlib.sha256((ROOT/pp).read_bytes()).hexdigest()}
client='portal/src/api/endpoints/investor-reporting.ts'
routefile='infra/aws/terraform/investor-reporting/api/routes.json'
source=read(client)
ops=re.findall(r"'([^']+)'",re.search(r'IR_OPERATIONS = \[(.*?)\] as const',source,re.S)[1])
verbs=dict(re.findall(r"'([^']+)': '(GET|POST)'",re.search(r'IR_METHOD_VERB.*?= \{(.*?)\n\}',source,re.S)[1]))
routes=json.loads(read(routefile))['routes']
declared=[r['route_key'] for r in routes if r['status']=='DECLARED']
comparisons=[]
for op in ops:
    key=verbs[op]+' /api/scoped/investor-reporting/'+op
    matches=[r for r in declared if re.fullmatch(re.sub(r'\{[^}]+\}',r'[^/]+',r),key)]
    comparisons.append({'operation':op,'frontend_route':key,'declared_backend_matches':matches})
schema_root='infra/aws/lambda/investor-reporting/_contracts'
pairs=[]
for schemafile in sorted((ROOT/schema_root).glob('*.schema.json')):
    name=schemafile.name.removesuffix('.schema.json')
    schema=json.loads(schemafile.read_text())
    validator=Draft202012Validator(schema)
    bk=f'{schema_root}/fixtures/{name}.valid.json'
    fe=f'portal/src/pages/InvestorReporting/fixtures/{name[0].lower()+name[1:]}.success.json'
    if name=='RenderPackage':
        # RenderPackage is a code/asset manifest, not an ExportBundle payload.
        pairs.append({'contract':name,'backend_positive_valid':validator.is_valid(json.loads(read(bk))['instance']),
                      'frontend_pair':'NO_SAME_NAMED_CONSUMER_JSON_FIXTURE','schema':provenance(schemafile.relative_to(ROOT)),
                      'backend_fixture':provenance(bk)})
        continue
    payload=json.loads(read(fe))
    errors=list(validator.iter_errors(payload))
    pairs.append({'contract':name,'backend_positive_valid':validator.is_valid(json.loads(read(bk))['instance']),
        'frontend_success_valid_against_backend_schema':not errors,'error_count':len(errors),
        'error_keywords':sorted(set(e.validator for e in errors)),
        'missing_required_top_level':[k for k in schema.get('required',[]) if k not in payload],
        'schema':provenance(schemafile.relative_to(ROOT)),'backend_fixture':provenance(bk),'frontend_fixture':provenance(fe)})
commands=[]
for args in (() if commands else (['bun','test','src/pages/InvestorReporting'],['node','node_modules/typescript/bin/tsc','-b','--noEmit'])):
    run=subprocess.run(args,cwd=ROOT/'portal',capture_output=True,text=True,encoding='utf-8',errors='replace',timeout=60)
    output=run.stdout+run.stderr
    label='bun-tests' if args[0]=='bun' else 'typescript'
    (OUT/f'{label}.txt').write_text(output,encoding='utf-8')
    selected=[s for s in output.splitlines() if (re.search(r'\d+ (pass|skip|fail)|expect\(\) calls|Ran \d+ tests',s) if label=='bun-tests' else 'error TS' in s)]
    commands.append({'cwd':'portal','argv':args,'exit_code':run.returncode,'output_sha256':hashlib.sha256(output.encode()).hexdigest(),'summary_lines':selected})
screens=[]
for p in sorted((ROOT/'org/missions/D9/IRPT/IRPT_FNTEND/deliverables').glob('*/*.png')):
    screens.append(provenance(p.relative_to(ROOT)))
data={'measured_at':datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
 'workspace_head':git('rev-parse','HEAD'),'portal_head':git('-C','portal','rev-parse','HEAD'),
 'limit':'Offline source/fixture comparison; no live authorization or deployment claim. Different fixture failures identify absent agreement or translation, not which vocabulary should win.',
 'routes':{'client':provenance(client),'backend':provenance(routefile),'frontend_count':len(ops),
           'backend_declared_count':len(declared),'backend_unimplemented_count':len(routes)-len(declared),'comparisons':comparisons},
 'contract_pairs':pairs,'commands':commands,'screenshots_visually_read':screens}
(OUT/'verifier_evidence.json').write_text(json.dumps(data,indent=2),encoding='utf-8')
print(json.dumps({'routes_matched':sum(bool(x['declared_backend_matches']) for x in comparisons),'frontend_operations':len(ops),
 'backend_positive_controls':sum(x['backend_positive_valid'] for x in pairs),'backend_schemas':len(pairs),
 'paired_consumer_fixtures':sum('frontend_success_valid_against_backend_schema' in x for x in pairs),
 'paired_consumer_valid':sum(x.get('frontend_success_valid_against_backend_schema',False) for x in pairs),
 'screenshots':len(screens),'commands':commands},indent=2))
