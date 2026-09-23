# Independent bounded X10 integration review

Reviewer `3.0.0_SA_CVO~M`; 2026-09-23 UTC. Authority: completion CONTRACT and
CTO IRPT-X10-INTEGRATION-01 `f6a8721a59`.

## Disposition

**Bounded PASS** for source `ffbffcac503eb7f74de0b296e52f2088c02dfea8`, directly
parented by `3978b247b4ca5d114fb2f0981ab546d28d3def29`, with documentary proof
`40a1ced34e` separately read. This is option A's reviewed integration unit and
two owned generated stamp repairs. No policy activation, general feature drain,
source-cutoff repair, live/provisioning/deployment, full S7 or push authorization.
The five inherited broad-test failures are retained, not called an all-green suite.

Source commit changes exactly six implementation paths plus two M evidence
files; proof commit adds one M evidence file. Four implementation files match
reviewed `587e782bc6` after line-ending normalization: builder, destination tests,
scopes registry and reporting policies registry. The other two files change only
the generated comment stamp; all remaining normalized text and Python AST match
the actual CLOUD baseline. No other generated carrier, Terraform, harvest/fmt,
CLOUD_OPS_OR_ETL or governance file changes. Current RULINGS.md remains identical.

Five other registry files are byte-equivalent after line-ending normalization.
Removing only the new irpt scope row restores the exact baseline scope document.
There are **111 unchanged existing top-level functions**, two changed existing
functions (`load_registry`, `validate`) exactly matching the reviewed candidate,
and five reviewed additions. A separate qualified recursive function enumeration
counts **115 unchanged of 117 existing definitions** (including nested/class
methods), with the same two changed definitions and five additions. Producer
prose's 116 unchanged-functions count is not reproduced under either explicit
denominator; this is an evidence-count correction, not an extra source change.

## Fresh tests and staged gate proof

From the clean isolated reviewer checkout, ran the full existing naming test file
on the exact baseline: **88 PASS / 5 FAIL**, then restored the six exact candidate
implementation files into that checkout's worktree and index. The relevant full
candidate invocation ran existing naming plus destination tests: **148 PASS /
5 FAIL**, with exactly the same five failure IDs. The 60 added controls pass.
The failures concern inf-silver-chain Lambda, portal-data-proxy API, Inflection
DimConversionFailure alarm, wsb model-aua schedule and otp-relay secret worked-case
expectations. Fresh registry validation exits 0. No tests or candidate source
were altered to obtain the results.

Canonical generation to a private runtime output directory reproduced both
owned generated files exactly after newline normalization. The six-path staged
diff SHA-256 matches M's proof:
`f15e18a26cbc58f59df16cce7ab220d2060bad33c08727649323e0ae0941fefc`.

The actual enforcing command was rerun, with HEAD at the baseline and the exact
candidate worktree/index (not M's mutable checkout):

```text
python .tools/naming-gate.py --post-from-index --enforce --diff <review-runtime>/candidate.diff
```

It exits **0** with six paths seen, zero uncovered paths and `PASS 0 graded`.
That zero is the literal-verdict count, not proof that the generated-file branch
was unexercised. An independent negative control replaced only the reviewed
index's holdings_snapshot generated stamp with sixteen zeroes, leaving the
worktree unchanged; the same post-from-index command exits **1**, naming
`holdings_snapshot.py:145 <generated-file-edit>` and REFUSE. Restoring the exact
candidate index restored the original diff byte-for-byte. This proves the staged
post-image was consumed and stale generated stamp checking was active.

The reviewer then removed only its six reconstructed changes, verified a clean
checkout and selected the source candidate detached. No shared root index or
implementer's checkout was staged, reset or edited.

Independent enumeration of all three firms and twelve policy families produced
36 private nonwritable previews and **36 writer refusals**. Policy remains
PENDING_ENFORCEMENT, enforcement_ref null, and the added product scope remains
unprovisioned. The inherited address/key/default tier-home implementation is the
reviewed unchanged behavior. No consumer needs for absent generated IRPT maps
are asserted; integration at a different merged head requires fresh ordinary
checks by the integration owner.

## Exact evidence

```json
{
  "baseline": "3978b247b4ca5d114fb2f0981ab546d28d3def29",
  "candidate": "ffbffcac503eb7f74de0b296e52f2088c02dfea8",
  "baseline_tests": {
    "tests": 93,
    "passed": 88,
    "failures": [
      "lib.tests.test_opal_naming::test_grade_agrees_with_every_worked_case[inf-silver-chain|LAMBDA]",
      "lib.tests.test_opal_naming::test_grade_agrees_with_every_worked_case[opal-portal-data-proxy-api|API_GW]",
      "lib.tests.test_opal_naming::test_grade_agrees_with_every_worked_case[Inflection-SilverChain-DimConversionFailure|CW_ALARM]",
      "lib.tests.test_opal_naming::test_grade_agrees_with_every_worked_case[wsb-49f-model-aua-pull-daily|SCHEDULE]",
      "lib.tests.test_opal_naming::test_grade_agrees_with_every_worked_case[inf/otp-relay/token|SECRET]"
    ]
  },
  "candidate_tests": {
    "tests": 153,
    "passed": 148,
    "failures": [
      "lib.tests.test_opal_naming::test_grade_agrees_with_every_worked_case[inf-silver-chain|LAMBDA]",
      "lib.tests.test_opal_naming::test_grade_agrees_with_every_worked_case[opal-portal-data-proxy-api|API_GW]",
      "lib.tests.test_opal_naming::test_grade_agrees_with_every_worked_case[Inflection-SilverChain-DimConversionFailure|CW_ALARM]",
      "lib.tests.test_opal_naming::test_grade_agrees_with_every_worked_case[wsb-49f-model-aua-pull-daily|SCHEDULE]",
      "lib.tests.test_opal_naming::test_grade_agrees_with_every_worked_case[inf/otp-relay/token|SECRET]"
    ]
  },
  "reviewed_four_equal": {
    "lib/opal_naming.py": true,
    "lib/tests/test_irpt_destination.py": true,
    "infra/logic/registry/scopes.json": true,
    "infra/logic/registry/reporting_policies.json": true
  },
  "other_registry_equal": {
    "systems.json": true,
    "tiers.json": true,
    "exemptions.json": true,
    "remediations.json": true,
    "resources.json": true
  },
  "non_irpt_scope_equal": true,
  "unchanged_existing_functions": 111,
  "changed_existing_functions": [
    "load_registry",
    "validate"
  ],
  "added_functions": [
    "_reporting_destination",
    "_validate_reporting_policies",
    "preview_reporting_destination",
    "reporting_destination",
    "reporting_policy"
  ],
  "rulings_unchanged": true,
  "stamp_repairs": [
    {
      "path": "data/assets/scripts/gold/investor_reporting/holdings_snapshot.py",
      "before_sha256": "ce063c4188c52d1a1ed28d9be607ae548e5de0ba99e6d21b9dd57953480e9b29",
      "after_sha256": "61a60022b73b71e0c3ff78bfbf973478085a90d84bf029beb26e0f99059efa22",
      "stamp_only": true
    },
    {
      "path": "infra/aws/lambda/investor-reporting/_authz/loaders.py",
      "before_sha256": "0c086052e6e65d2cb411f15362862b1656bad0b2320f9756be6a32444b665765",
      "after_sha256": "37de7a7e171901f5344770b19abaf71b840b3a380a4f0af1fc28796c78c987e1",
      "stamp_only": true
    }
  ],
  "generated_bytes_equal": true,
  "candidate_gate_exit": 0,
  "candidate_gate_output": "DENOMINATOR: 6 path(s) in this diff; declaration-tree domain = 6 MINUS EXCLUDED(org/, docs/, run-artifact dirs ^workflows/[^/]+/[^/]+/[0-9]{8}T[0-9]{6}Z-[0-9a-f]{7,40}/) 0 = 6 path(s) [of the excluded, 0 are run artifacts and 0 are org//docs/]\nCOVERAGE: 0 path(s) in the declaration domain the gate could not see (extension outside its graded set and not .gitattributes); 6 seen\nNAMING-GATE: PASS 0 graded\n",
  "stale_stamp_gate_exit": 1,
  "stale_stamp_gate_output": "DENOMINATOR: 6 path(s) in this diff; declaration-tree domain = 6 MINUS EXCLUDED(org/, docs/, run-artifact dirs ^workflows/[^/]+/[^/]+/[0-9]{8}T[0-9]{6}Z-[0-9a-f]{7,40}/) 0 = 6 path(s) [of the excluded, 0 are run artifacts and 0 are org//docs/]\nCOVERAGE: 0 path(s) in the declaration domain the gate could not see (extension outside its graded set and not .gitattributes); 6 seen\nNAMING REFUSE data/assets/scripts/gold/investor_reporting/holdings_snapshot.py:145 <generated-file-edit> -> python lib/opal_naming.py generate --out <dir> --target data/assets/scripts/gold/investor_reporting/holdings_snapshot.py\n  why: a hand edit to a GENERATED file: its bytes differ from the generator's output from line 145\nNAMING-GATE: REFUSE 1 graded\n",
  "diff_sha256": "f15e18a26cbc58f59df16cce7ab220d2060bad33c08727649323e0ae0941fefc",
  "pending_writer_refusals": 36,
  "state": "PENDING_ENFORCEMENT",
  "enforcement_ref": null
}
```

## Reproduction script

SHA-256: `ba6ec7258fa2c680d14d8a9a2e40ad10cbb5e7a6227c07d520143627dc4929a7`.

The script requires a clean **private reviewer checkout** at its fixed ROOT. It reconstructs only the six named candidate paths, stages a controlled negative blob in that private index, restores its own changes, and leaves a clean detached candidate. Its full-suite expected exit 1 assertions preserve the five inherited failures.

```python
import ast,hashlib,importlib.util,json,re,subprocess,sys,xml.etree.ElementTree as ET
from pathlib import Path
ROOT=Path(r'C:/Users/AndrewBerman/Desktop/ajb_irpt_cvo_m_review')
OUT=Path(r'C:/Users/AndrewBerman/Desktop/ajb_workspace/.runtime/codex-seats/3.0.0_SA_CVO~M/x10_ffb_review')
OUT.mkdir(parents=True,exist_ok=True)
BASE='3978b247b4ca5d114fb2f0981ab546d28d3def29';CAND='ffbffcac503eb7f74de0b296e52f2088c02dfea8'
FOUR=['lib/opal_naming.py','lib/tests/test_irpt_destination.py','infra/logic/registry/scopes.json','infra/logic/registry/reporting_policies.json']
STAMPS=['data/assets/scripts/gold/investor_reporting/holdings_snapshot.py','infra/aws/lambda/investor-reporting/_authz/loaders.py']
PATHS=FOUR+STAMPS

def git(*args,input=None):
    return subprocess.check_output(['git',*args],cwd=ROOT,input=input)
def show(rev,path): return git('show',rev+':'+path).decode('utf-8').replace('\r\n','\n')
def run(label,args,expected):
    r=subprocess.run(args,cwd=ROOT,capture_output=True,text=True,encoding='utf-8',errors='replace')
    (OUT/(label+'.txt')).write_text(r.stdout+r.stderr,encoding='utf-8')
    assert r.returncode==expected,(label,r.returncode,r.stdout[-2000:],r.stderr[-2000:])
    print(label+': exit '+str(r.returncode),flush=True)
    return r.stdout+r.stderr
def xml_summary(name):
    tree=ET.parse(OUT/(name+'.xml'))
    cases=tree.findall('.//testcase')
    failures=[c.attrib['classname']+'::'+c.attrib['name'] for c in cases if c.find('failure') is not None]
    return {'tests':len(cases),'passed':len(cases)-len(failures),'failures':failures}
assert not git('status','--porcelain').strip()
assert git('rev-parse',CAND+'^').decode().strip()==BASE
matches={p:show(CAND,p)==show('587e782bc6',p) for p in FOUR};assert all(matches.values())
regs={p:show(BASE,'infra/logic/registry/'+p)==show(CAND,'infra/logic/registry/'+p) for p in ['systems.json','tiers.json','exemptions.json','remediations.json','resources.json']};assert all(regs.values())
scope=json.loads(show(CAND,'infra/logic/registry/scopes.json'));scope['scopes']=[x for x in scope['scopes'] if x['key']!='irpt'];assert scope==json.loads(show(BASE,'infra/logic/registry/scopes.json'))
rulings='org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/RULINGS.md'
assert show(BASE,rulings)==show(CAND,rulings)
funcs=lambda source:{n.name:ast.dump(n,include_attributes=False) for n in ast.parse(source).body if isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef))}
a,b=funcs(show(BASE,FOUR[0])),funcs(show(CAND,FOUR[0]))
changed=[k for k in a if a[k]!=b.get(k)]
assert set(changed)=={'load_registry','validate'}
assert all(b[k]==funcs(show('587e782bc6',FOUR[0]))[k] for k in changed)
stamps=[]
for path in STAMPS:
    before,after=show(BASE,path),show(CAND,path)
    strip=lambda s:'\n'.join(x for x in s.splitlines() if not x.startswith('# GENERATED by lib/opal_naming.py'))
    assert strip(before)==strip(after)
    assert ast.dump(ast.parse(before),include_attributes=False)==ast.dump(ast.parse(after),include_attributes=False)
    stamps.append({'path':path,'before_sha256':hashlib.sha256(before.encode()).hexdigest(),'after_sha256':hashlib.sha256(after.encode()).hexdigest(),'stamp_only':True})
git('switch','--detach',BASE)
run('baseline_tests',[sys.executable,'-m','pytest','lib/tests/test_opal_naming.py','-q','--tb=short','--junitxml='+str(OUT/'baseline.xml')],1)
git('restore','--source='+CAND,'--staged','--worktree','--',*PATHS)
assert set(git('diff','--cached','--name-only').decode().splitlines())==set(PATHS)
run('candidate_tests',[sys.executable,'-m','pytest',*FOUR[:2][1:],'lib/tests/test_opal_naming.py','-q','--tb=short','--junitxml='+str(OUT/'candidate.xml')],1)
base,candidate=xml_summary('baseline'),xml_summary('candidate')
assert base['failures']==candidate['failures'],(base,candidate)
run('registry_validate',[sys.executable,'lib/opal_naming.py','validate'],0)
run('canonical_generate',[sys.executable,'lib/opal_naming.py','generate','--out',str(OUT/'generated'),'--target',STAMPS[0],'--target',STAMPS[1]],0)
for path in STAMPS:
    assert (OUT/'generated'/path).read_text()==(ROOT/path).read_text()
diff=git('diff','--cached','--no-ext-diff','--',*PATHS)
(OUT/'candidate.diff').write_bytes(diff)
gatecmd=[sys.executable,'.tools/naming-gate.py','--post-from-index','--enforce','--diff',str(OUT/'candidate.diff')]
gate=run('candidate_gate',gatecmd,0)
# Negative control changes only this reviewer checkout's index blob. Restore it immediately.
path=STAMPS[0];original=git('show',':'+path);text=original.decode('utf-8')
bad=re.sub(r'(registry@)[0-9a-f]{16}',r'\g<1>0000000000000000',text,count=1).encode('utf-8')
assert bad!=original
blob=git('hash-object','-w','--stdin',input=bad).decode().strip()
mode=git('ls-files','-s','--',path).decode().split()[0]
try:
    git('update-index','--cacheinfo',mode,blob,path)
    negative=run('stale_stamp_gate',gatecmd,1)
    assert '<generated-file-edit>' in negative and 'REFUSE' in negative
finally:
    git('restore','--source='+CAND,'--staged','--',path)
assert git('diff','--cached','--no-ext-diff','--',*PATHS)==diff
spec=importlib.util.spec_from_file_location('independent_x10_subject',ROOT/FOUR[0]);n=importlib.util.module_from_spec(spec);spec.loader.exec_module(n)
policy=n.reporting_policy('irpt-x10-v1');assert policy['state']=='PENDING_ENFORCEMENT' and policy['enforcement_ref'] is None
refusals=0
for firm in policy['firms']:
    for family in policy['families']:
        preview=n.preview_reporting_destination(firm,family,'ART-'+'a'*64,'b'*64,policy_revision='irpt-x10-v1')
        assert not preview['writable'] and preview['key'].startswith('irpt/'+firm+'/')
        try:n.reporting_destination(firm,family,'ART-'+'a'*64,'b'*64,policy_revision='irpt-x10-v1')
        except ValueError:refusals+=1
        else:raise AssertionError('unexpected writable destination')
summary={'baseline':BASE,'candidate':CAND,'baseline_tests':base,'candidate_tests':candidate,'reviewed_four_equal':matches,'other_registry_equal':regs,'non_irpt_scope_equal':True,'unchanged_existing_functions':sum(a[k]==b.get(k) for k in a),'changed_existing_functions':changed,'added_functions':sorted(set(b)-set(a)),'rulings_unchanged':True,'stamp_repairs':stamps,'generated_bytes_equal':True,'candidate_gate_exit':0,'candidate_gate_output':gate,'stale_stamp_gate_exit':1,'stale_stamp_gate_output':negative,'diff_sha256':hashlib.sha256(diff).hexdigest(),'pending_writer_refusals':refusals,'state':policy['state'],'enforcement_ref':policy['enforcement_ref']}
(OUT/'evidence.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
print(json.dumps(summary,indent=2),flush=True)
# Remove only the six exact reconstruction paths from this private review index/tree, then select candidate.
git('restore','--source='+BASE,'--staged','--worktree','--',*PATHS)
assert not git('status','--porcelain').strip()
git('switch','--detach',CAND)

```
