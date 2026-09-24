# Independent current-owner Entry review

Reviewer `3.0.0_SA_CVO~M`; 2026-09-23 UTC. Authority: completion CONTRACT S1/S4.

## Bounded disposition

**PASS for the opt-in shared Entry authorization interface** at
`6ad86009fe5d42d57235095dcda2cffd7b952078`, compared with its exact parent
`f7344d6e9a3833c7952b8f473a773634baea9dee`.
The clean detached reviewer checkout was switched between these exact commits;
no implementation or supplied test was edited. The change is limited to served.py,
owner_reads.py, 19 supplied Entry tests and OWNER_READ_INTERFACE.md. It does not
install a route or compose a deployed package.

OWNED_RECORD requires explicit constructor opt-in, an issued-reference parameter,
and both server-loaded retained-owner and current-authorization callbacks. Actual
Entry independently checks matching verified firm/principal, deep-copies retained
owner and principal inputs, rechecks the principal, reloads/reauthorizes the
record after compute and refuses a changed complete owner. Lookup IDs are not
bearer grants. Service authorization must return exactly True. No custody scope
is manufactured and no shared response cache is used by this owner-read path.

CURRENT_OWNER_HISTORY supplies a verified current principal only. This is not a
history-query or per-record authorization implementation. Y still owns bounded
querying, issued-ID grammar/accepted-state binding, exact-owner filtering,
current retained-custody permissions, retention and release checks. P/Y route
composition, flat packaging and independent actual consumer proof are still owed.
The callback ports must enforce those duties; an always-True test callback is
not production authorization evidence. Neither this review nor the new guard
relabels any existing custody operation as owner-only.

## Evidence

Fresh full `_authz/tests` baseline: **154 PASS, 5 FAIL**.
Fresh full candidate: **173 PASS, the same 5 FAIL** (15.86s), both pytest exit 1.
The candidate XML independently confirms **19 new owner Entry tests and 15
existing prospect Entry tests pass**. These do not constitute an all-green broad
suite. Two inherited directory-search positive controls receive OBJECT_NOT_COVERED;
three census tests assert 12 routes while the actual table has 13. The census
reports all 13 guarded and zero unguarded routes. None of these failures was
changed, suppressed or treated as passing.

Independent actual Entry driver: **24 PASS in 0.32s**, exit 0. Controls cover:

- Exact boolean authorization: numeric 1, text, collections and None refuse
  before compute rather than becoming permission through truthiness.
- Failure in second owner lookup, second authorization or compute releases no
  payload or internal exception text.
- Nested retained account-set change after compute refuses the whole response.
- Authorization callbacks and compute receive copies; their nested modifications
  cannot rewrite the retained before-read owner comparison or current principal.
- A reused warm Entry rechecks service permission and does not serve its previous
  response after revocation.
- Advisor identity changes during both OWNED_RECORD and CURRENT_OWNER_HISTORY
  compute refuse release.
- Overlong, non-ASCII, spaced, numeric and missing issued references refuse before
  storage callbacks or compute.
- History rejects browser owner/principal/firm/account-set/snapshot query fields.
  Permitted limit/cursor hints reach the service for its own validation without
  inventing a retained-record or custody grant.

The supplied 19 controls additionally exercise missing/foreign/revoked records,
GET/input restrictions, origin/renderer refusal, mandatory callback wiring and
before/after calls at the real Entry. This is local code execution with synthetic
service callbacks and trusted-claim fixtures, not live token verification, storage,
IAM, distributed atomic permission transactions, actual Y record filtering or
full product acceptance. Ordinary release-time race limits across separate
services remain; sequential rechecks are not an atomic multi-store guarantee.

## Full-suite results

```json
{
  "baseline": {
    "pin": "f7344d6e9a3833c7952b8f473a773634baea9dee",
    "exit": 1,
    "tests": 159,
    "passed": 154,
    "failures": [
      "infra.aws.lambda.investor-reporting._authz.tests.test_guarded_entries::test_the_authorized_request_is_not_refused_for_an_authorization_reason[irpt-directory-search]",
      "infra.aws.lambda.investor-reporting._authz.tests.test_guarded_entries::test_the_same_admin_principal_still_reaches_an_advisor_inside_the_firm[irpt-directory-search]",
      "infra.aws.lambda.investor-reporting._authz.tests.test_unguarded_census::test_every_published_route_resolves_to_a_real_entry_point",
      "infra.aws.lambda.investor-reporting._authz.tests.test_unguarded_census::test_zero_of_n_over_the_routes_this_order_may_open",
      "infra.aws.lambda.investor-reporting._authz.tests.test_unguarded_census::test_the_whole_file_census_is_zero"
    ],
    "errors": []
  },
  "candidate": {
    "pin": "6ad86009fe5d42d57235095dcda2cffd7b952078",
    "exit": 1,
    "tests": 178,
    "passed": 173,
    "failures": [
      "infra.aws.lambda.investor-reporting._authz.tests.test_guarded_entries::test_the_authorized_request_is_not_refused_for_an_authorization_reason[irpt-directory-search]",
      "infra.aws.lambda.investor-reporting._authz.tests.test_guarded_entries::test_the_same_admin_principal_still_reaches_an_advisor_inside_the_firm[irpt-directory-search]",
      "infra.aws.lambda.investor-reporting._authz.tests.test_unguarded_census::test_every_published_route_resolves_to_a_real_entry_point",
      "infra.aws.lambda.investor-reporting._authz.tests.test_unguarded_census::test_zero_of_n_over_the_routes_this_order_may_open",
      "infra.aws.lambda.investor-reporting._authz.tests.test_unguarded_census::test_the_whole_file_census_is_zero"
    ],
    "errors": []
  }
}
```

## Reproduction scripts

The suite runner requires the clean private reviewer checkout at ROOT and changes only its detached checkout selection. The independent driver imports the candidate test helpers for standard verified claims/Entry construction, then supplies separate mutations and assertions.

### run_owner_6ad_suites.py

SHA-256: `d58441e6a57b7c0c77d04b1f8c7c3cb06fd8766ae0af175f1f4a44655bf2dbdc`.

```python
import json,subprocess,sys,xml.etree.ElementTree as ET
from pathlib import Path
ROOT=Path(r'C:/Users/AndrewBerman/Desktop/ajb_irpt_cvo_m_review')
OUT=Path(r'C:/Users/AndrewBerman/Desktop/ajb_workspace/.runtime/codex-seats/3.0.0_SA_CVO~M/owner_6ad_review')
OUT.mkdir(parents=True,exist_ok=True)
CAND='6ad86009fe5d42d57235095dcda2cffd7b952078'
def git(*args):return subprocess.check_output(['git',*args],cwd=ROOT).decode().strip()
assert not git('status','--porcelain')
BASE=git('rev-parse',CAND+'^')
results={}
for label,pin in [('baseline',BASE),('candidate',CAND)]:
    git('switch','--detach',pin)
    result=subprocess.run([sys.executable,'-m','pytest','infra/aws/lambda/investor-reporting/_authz/tests','-q','--tb=short','--junitxml='+str(OUT/(label+'.xml'))],cwd=ROOT,capture_output=True,text=True,encoding='utf-8',errors='replace')
    (OUT/(label+'.txt')).write_text(result.stdout+result.stderr,encoding='utf-8')
    cases=ET.parse(OUT/(label+'.xml')).findall('.//testcase')
    failures=[c.attrib['classname']+'::'+c.attrib['name'] for c in cases if c.find('failure') is not None]
    errors=[c.attrib['classname']+'::'+c.attrib['name'] for c in cases if c.find('error') is not None]
    results[label]={'pin':pin,'exit':result.returncode,'tests':len(cases),'passed':len(cases)-len(failures)-len(errors),'failures':failures,'errors':errors}
    print(json.dumps(results[label]),flush=True)
assert results['baseline']['failures']==results['candidate']['failures']
assert results['baseline']['errors']==results['candidate']['errors']==[]
(OUT/'supplied.json').write_text(json.dumps(results,indent=2),encoding='utf-8')

```

### test_owner_6ad_review.py

SHA-256: `f97b9a104cb928d4b1fa92c464bd8d3c7ff1b108804ddb1e5dae2a09b162287e`.

```python
"""Independent actual Entry controls for the opt-in owner read seam; no service/storage claims."""
import copy,sys
from pathlib import Path
import pytest
ROOT=Path(r'C:/Users/AndrewBerman/Desktop/ajb_irpt_cvo_m_review')
TESTS=ROOT/'infra/aws/lambda/investor-reporting/_authz/tests'
sys.path.insert(0,str(TESTS))
import test_owner_read_entry as E
from prospect import resolve_prospect_owner

def retained():
    return dict(resolve_prospect_owner(E.claims()),kind='CUSTODY',scope={'accounts':['account-a'],'revision':'one'})
def denied(result):
    assert result.get('ok') is False and 'data' not in result

@pytest.mark.parametrize('decision',[1,'true',{},[],None])
def test_truthy_or_non_boolean_service_authorization_is_not_true(decision):
    called=[]
    result=E.entry(lambda *a:called.append(True),lambda *a:retained(),lambda *a:decision).handle(E.event())
    denied(result);assert not called

@pytest.mark.parametrize('failure',['load','authorize','compute'])
def test_exception_at_post_compute_owner_ports_releases_no_result(failure):
    calls={'load':0,'authorize':0,'compute':0}
    def load(*args):
        calls['load']+=1
        if failure=='load' and calls['load']==2:raise RuntimeError('private owner store failure')
        return retained()
    def authorize(*args):
        calls['authorize']+=1
        if failure=='authorize' and calls['authorize']==2:raise RuntimeError('private grants failure')
        return True
    def compute(*args):
        calls['compute']+=1
        if failure=='compute':raise RuntimeError('private compute failure')
        return {'secret':'must not release'}
    result=E.entry(compute,load,authorize).handle(E.event())
    denied(result);assert calls['compute']==1
    assert 'private' not in str(result) and 'must not release' not in str(result)

def test_nested_retained_scope_change_after_compute_refuses():
    owner=retained()
    def compute(*args):owner['scope']['accounts'].append('account-b');return {'private':'value'}
    denied(E.entry(compute,lambda *a:owner,lambda *a:True).handle(E.event()))

def test_compute_and_authorize_receive_copies_of_complete_owner():
    owner=retained();before=copy.deepcopy(owner);checks=[]
    def authorize(principal,value):
        checks.append(copy.deepcopy(value));value['scope']['accounts'].append('callback-only');principal['principal_id']='callback-only';return True
    def compute(request,scope,event,ctx):
        assert ctx.directory is None and ctx.ownership is None
        assert 'permitted_account_set' not in scope
        scope['retained_record_owner']['scope']['accounts'].append('compute-only')
        scope['current_owner']['principal_id']='compute-only'
        return {'public':'okay'}
    result=E.entry(compute,lambda *a:owner,authorize).handle(E.event())
    assert result['data']=={'public':'okay'} and owner==before and checks==[before,before]

def test_warm_entry_rechecks_service_grant_without_reusing_previous_payload():
    state={'allow':True,'computes':0}
    def compute(*args):state['computes']+=1;return {'public':'one'}
    entry=E.entry(compute,lambda *a:retained(),lambda *a:state['allow'])
    assert entry.handle(E.event())['data']=={'public':'one'}
    state['allow']=False
    denied(entry.handle(E.event()));assert state['computes']==1

@pytest.mark.parametrize('mode',['OWNED_RECORD','CURRENT_OWNER_HISTORY'])
def test_current_advisor_or_role_change_before_release_refuses(mode):
    def compute(request,*args):request.headers['x-advisor-id']='different';return {'private':'value'}
    entry=E.entry(compute,lambda *a:retained(),lambda *a:True,mode=mode)
    denied(entry.handle(E.event()))

@pytest.mark.parametrize('reference',['a'*201,'nonascii-é','has space',123,None])
def test_issued_reference_boundary_before_owner_lookup(reference):
    calls=[]
    entry=E.entry(lambda *a:calls.append('compute'),lambda *a:calls.append('load'),lambda *a:True)
    denied(entry.handle(E.event(pathParameters={'requestId':reference})))
    assert not calls

@pytest.mark.parametrize('key',['owner','principal_id','firm_id','account_set_id','snapshot_id'])
def test_history_rejects_browser_authority_query_before_compute(key):
    calls=[]
    result=E.entry(lambda *a:calls.append(True),mode='CURRENT_OWNER_HISTORY').handle(E.event(pathParameters={},queryStringParameters={key:'supplied'}))
    denied(result);assert not calls

def test_history_page_parameters_remain_for_service_validation_without_owner_grant():
    def compute(request,scope,event,ctx):
        assert event['queryStringParameters']=={'limit':'5','cursor':'opaque-page-hint'}
        assert 'retained_record_owner' not in scope and 'permitted_account_set' not in scope
        return {'items':[],'next_cursor':None}
    def forbidden(*args):raise AssertionError('history Entry must not invent a retained record')
    result=E.entry(compute,forbidden,forbidden,mode='CURRENT_OWNER_HISTORY').handle(E.event(pathParameters={},queryStringParameters={'limit':'5','cursor':'opaque-page-hint'}))
    assert result['data']=={'items':[],'next_cursor':None}

```

