# Paired candidate: classification of two legacy positive-control failures

Reviewer: `3.0.0_SA_CVO~M`, 2026-09-23 UTC.
Authority: completion CONTRACT and exact CTO request `20260923T045608Z`.
Candidate: `cd8d11825424e45fe82f1e78df0396904c0b9ae0`.
Reported integration receipt: COO~P `a75c822d71`,
IRPT_MVP_P/PAIRED_SMOKE_INTEGRATION_20260923.md.

## Classification

**Inherited route-dependent test-fixture defect; both reported tests remain FAIL
until their owner repairs and reruns them.** The two errors do not reproduce an
authorized directory-search rejection. The legacy fixture silently selects the
new selection-create operation but supplies no required body. Its refusal is
correct for that malformed request. No guard, scope, or production route was
changed to make a positive control pass.

Exact tests in
`infra/aws/lambda/investor-reporting/_authz/tests/test_guarded_entries.py`:

- `test_the_authorized_request_is_not_refused_for_an_authorization_reason[irpt-directory-search]`
- `test_the_same_admin_principal_still_reaches_an_advisor_inside_the_firm[irpt-directory-search]`

P reports **97 pass / 2 fail** for the guarded-entry file at the paired candidate.
That denominator is attributed to P; it was not recreated here. Existing M review
`b9bad0e9e7`, CURRENT_OWNER_READ_REVIEW_6AD.md, already records exactly these two
failures on both baseline `f7344d6e9a3833c7952b8f473a773634baea9dee` and candidate
`6ad86009fe5d42d57235095dcda2cffd7b952078`. Its broad-suite counts were respectively
154 pass/5 fail and 173 pass/5 fail; the other three were separate route-census
expectations. Do not merge these different denominators or describe a new
regression caused by the latest paired merge.

## Exact cause

1. `entries()` at test lines 84-95 iterates the real route table and keeps only
   the first route for each function name. This logic predates the selection
   route (blame `43560851223`, historical WK IRPT backend author).
2. `routes.json` lines 18-28 prepend
   `POST /api/scoped/investor-reporting/selections`, handler
   `irpt-directory-search`, operation `selection-create`. This addition is
   `63c6b39af65`, COO~P, 2026-09-22. Thus the test ID names a Lambda function,
   not the directory-search operation actually exercised by its title.
3. `base_event()` lines 129-151 supplies legacy top-level
   `selection: {account_ids: [...]}` but no body. The admin variant changes
   principal/object addressing and retains that same missing body.
4. `directory/entry.py:create_selected_set` reads the body, yielding query=None.
   `_scope/selection.py:create_requested_selection` lines 84-85 requires exactly
   scope_kind/scope_ids and raises SelectionRefused:
   `selection request must name only kind and nonempty ids`.
5. The directory Entry explicitly maps SelectionRefused to OBJECT_NOT_COVERED.
   The shared scope checks have been passed; the body rejection is then mistaken
   by these two positive-control assertions for an authorization failure.

The test-file diff between the earlier baseline and cd8 changes only a separate
public-status/correlation assertion. The failing functions, first-route selector
and base/admin events retain the same relevant code.

## Minimal independent diagnostic

Used the existing recorded fixtures and actual handler at a clean detached cd8
checkout. Five direct calls, no broad pytest rerun, no new source/test fixture
implementation, no network or cloud I/O. The diagnostic traces the actual
SelectionRefused throw site. For the positive counterfactual it changes only
routeKey and operation to explicit GET directory/search; principals and loaded
directory/ownership/policy remain identical.

| Call | Result |
| --- | --- |
| Existing advisor fixture, first route selection-create, no body | ok=false, UNAVAILABLE/OBJECT_NOT_COVERED; traced query=None malformed selection |
| Same advisor, explicit directory-search | Served one whole entry; PARTIAL/OBJECT_NOT_COVERED reports a withheld partially covered group, not ok=false refusal |
| Existing admin/in-firm-advisor fixture, first route selection-create, no body | ok=false, UNAVAILABLE/OBJECT_NOT_COVERED; same traced query=None |
| Same admin/in-firm advisor, explicit directory-search | Served three entries; no refusal |
| Same admin addressing foreign advisor, explicit directory-search | ok=false, UNAVAILABLE/OBJECT_NOT_COVERED; no selection exception |

Both served controls also assert contract version and directory-search operation.
Do not classify a PARTIAL served response solely by its reason string; the
existing positive test correctly distinguishes ok=false from served output.
The diagnostic exits 0. It confirms the fixture/operation mismatch and preserved
foreign-advisor refusal, not selection persistence or blanket runtime acceptance.

Driver:
`C:/Users/AndrewBerman/Desktop/ajb_workspace/.runtime/codex-seats/3.0.0_SA_CVO~M/classify_directory_cd8.py`.
SHA256: `238ad038265b05b54ecc9ae99144593e3299e3f912fbbc584aed03bf8ca5c488`.
Complete script below. Execute with Python from the pinned clean reviewer checkout.

## Owner and handoff

**COO~M owns the fixture correction**, under CONTRACT section 3's common non-render
`_authz/`, directory and selection ownership. Use explicit operation-aware route
and request fixtures so adding another route to one Lambda cannot silently change
the control's meaning. Preserve the valid in-firm and forbidden-advisor controls;
do not weaken authorization assertions or reorder production routes to appease
the test. Give selection-create its valid closed request and storage fixture if
it is included in this generic positive-control battery.

**COO~P owns paired integration and shared route/schema aggregation** and should
consume M's exact correction/evidence. CTO receives this classification; CVO~M
does not edit producer/test source. This classification is not a new Portal
visual-review gate and does not undo Andrew's direction for completed DEV and
canonical Portal PROD publication. It provides no new push/deploy action to this
seat. Existing backend render/key/runtime, full-product and live holds remain.

Initial P/M evidence requests were refused by the canonical sender because the
reviewer omitted the exact CONTRACT path required by section 6's direct-peer
exception. Nothing was written by those attempts. The final handoff uses that
documented citation through the same canonical sender; no alternate inbox write,
force option, guard change or broker workaround is involved.

CTO's exact acknowledgement `20260923T050228Z` accepted this classification and
specified that M's minimal fixture repair be consumed by P **after the current
frozen publication**, without silently mutating that candidate. That timing was
relayed to both owners. The first evidence safe-commit attempt staged nothing
because a shared merge was active; after MERGE_HEAD cleared, only this evidence
path was submitted again. No merge/index intervention occurred.

## Diagnostic script

```python
"""Bounded diagnostic using the existing guarded-entry fixtures; no source edits."""
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path('C:/Users/AndrewBerman/Desktop/ajb_irpt_cvo_m_review')
PIN = 'cd8d11825424e45fe82f1e78df0396904c0b9ae0'
assert subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip() == PIN
sys.path.insert(0, str(ROOT / 'infra/aws/lambda/investor-reporting/_authz/tests'))
import test_guarded_entries as existing

route, handler = existing.entries()['irpt-directory-search']
operation = existing._routes()[route]['operation']
assert route == 'POST /api/scoped/investor-reporting/selections'
assert operation == 'selection-create'
entry = handler.__irpt_entry__
restore = existing._install_recorded_deps(entry)
results = []

def run(name, event):
    traces = []
    def trace(frame, kind, value):
        if frame.f_code.co_name == 'create_requested_selection' and kind == 'exception':
            cls, error, _ = value
            traces.append({'function': frame.f_code.co_name, 'exception': cls.__name__,
                           'message': str(error), 'query_is_none': frame.f_locals.get('query') is None})
        return trace
    sys.settrace(trace)
    try:
        answer = handler(event, None)
    finally:
        sys.settrace(None)
    result = {'name': name, 'route': event['routeKey'], 'operation': event['operation'],
              'body_present': 'body' in event, 'ok': answer.get('ok'),
              'reason': (answer.get('status') or {}).get('public_reason_code'),
              'status_state': (answer.get('status') or {}).get('state'),
              'data_count': len(answer['data']) if isinstance(answer.get('data'), list) else None,
              'selection_exception': traces}
    results.append(result)
    return answer

try:
    for mode in ['advisor', 'admin_inside_firm']:
        ev = (existing.base_event(route, operation) if mode == 'advisor' else
              existing._admin_event_addressing(route, operation, existing.fx.ADVISOR_B))
        answer = run('unchanged_fixture_' + mode, ev)
        assert answer.get('ok') is False
        assert answer['status']['public_reason_code'] == 'OBJECT_NOT_COVERED'
        assert results[-1]['selection_exception'][-1] == {
            'function': 'create_requested_selection', 'exception': 'SelectionRefused',
            'message': 'selection request must name only kind and nonempty ids', 'query_is_none': True}
        # Change route/operation only, preserving identical principal and loaders.
        ev['routeKey'] = 'GET /api/scoped/investor-reporting/directory/search'
        ev['operation'] = 'directory-search'
        corrected = run('explicit_search_' + mode, ev)
        assert corrected.get('ok') is not False, results[-1]
        assert isinstance(corrected.get('data'), list) and len(corrected['data']) > 0
        assert corrected['contract_version'] == existing.CONTRACT_VERSION
        assert corrected['operation'] == 'directory-search'
        assert not results[-1]['selection_exception']
    ev = existing._admin_event_addressing('GET /api/scoped/investor-reporting/directory/search',
                                         'directory-search', existing.FOREIGN_ADVISOR)
    refused = run('explicit_search_foreign_advisor', ev)
    assert refused.get('ok') is False and refused['status']['public_reason_code'] == 'OBJECT_NOT_COVERED'
finally:
    restore()

print(json.dumps({'candidate': PIN, 'calls': results, 'count': len(results),
                  'producer_or_test_source_modified': False, 'live_runtime_proven': False}, indent=2))

```

## Bounded fixture closure at f0aead3dcf, 2026-09-23 UTC

Trigger: exact COO~M `20260923T050514Z`. This addendum supersedes only the two
unresolved fixture-failure statuses above for the exact tested correction.
**CLOSED / bounded fixture PASS**, candidate
`f0aead3dcf90fa4f1049eee02c3ae30cb146f3c4`, parent
`8e2ba7830352b2a34c97ec96984d043654cab340`.

The sole changed path is `_authz/tests/test_guarded_entries.py`: 10 insertions,
1 deletion. `entries()` explicitly selects directory-search for this Lambda,
asserts that the published guarded operation exists, and documents the separate
selection-create tests. AST comparison proves every other test/module statement
is unchanged; production entry, reason mapping, scope, selection, and route
files are untouched. Missing search can no longer silently reduce the fixture
set. No existing positive/negative assertion was weakened.

Independent unchanged tests on clean detached f0a:

- `python -m pytest infra/aws/lambda/investor-reporting/_authz/tests/test_loader_freshness.py infra/aws/lambda/investor-reporting/_authz/tests/test_guarded_entries.py -q`: **99 PASS, 13.52s**, exit 0.
- `python -m pytest infra/aws/lambda/investor-reporting/directory/tests/test_selection_entry.py -q`: **6 PASS, 0.13s**, exit 0.

The actual reviewed diff also applies cleanly to the paired cd8 baseline. The
preimage of the only test file at cd8 is byte-identical to f0a's parent. In the
private reviewer checkout only, applied that exact diff and reran the same two
guard/loader files unchanged: **99 PASS, 10.70s**, exit 0. XML confirms both named
formerly failing directory positives and the foreign-advisor negative pass,
with no skip/error/failure substitution. The patched test file exactly matches
f0a's bytes. Restored only that known private edit, asserted clean, and returned
the reviewer checkout to f0a. No producer, shared, frozen publication or Portal
worktree/index was mutated.

Exact test-only diff SHA256:
`31a4fe95769b0e8dddb81b9aeae004a640f46b104fa6c0447e4c6b05154c0a76`.
Paired verification driver SHA256:
`6b8d38b3894eaa640cc43b7dbc3dad6a3b7a605806c16a1d189d55e3f6b55ed0`.
Runtime evidence: `.runtime/codex-seats/3.0.0_SA_CVO~M/fixture_f0a_review/`
contains exact-test-only.patch, paired.xml, paired.txt and evidence.json.
Full driver follows. This is a test-fixture closure, not live/runtime/full-product
acceptance. Original unpatched cd8 retains its original result. P's consumption
remains after the current frozen publication, per CTO; this review introduces
no Portal publication/visual gate and changes no existing backend holds.

### Paired verification driver
```python
"""Apply only the reviewed test delta in the private cd8 checkout and restore it."""
import ast
import hashlib
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path('C:/Users/AndrewBerman/Desktop/ajb_irpt_cvo_m_review')
OUT = Path(__file__).resolve().parent / 'fixture_f0a_review'
OUT.mkdir(exist_ok=True)
CAND = 'f0aead3dcf90fa4f1049eee02c3ae30cb146f3c4'
PAIR = 'cd8d11825424e45fe82f1e78df0396904c0b9ae0'
PATH = 'infra/aws/lambda/investor-reporting/_authz/tests/test_guarded_entries.py'
def git(*args): return subprocess.check_output(['git', *args], cwd=ROOT)
assert not git('status', '--porcelain').strip()
parent = git('rev-parse', CAND + '^').decode().strip()
assert git('diff', '--name-only', parent, CAND).decode().splitlines() == [PATH]
before, after = git('show', parent + ':' + PATH), git('show', CAND + ':' + PATH)
def remaining_ast(body):
    tree = ast.parse(body)
    tree.body = [n for n in tree.body if not isinstance(n, ast.FunctionDef) or n.name != 'entries']
    return ast.dump(tree, include_attributes=False)
assert remaining_ast(before) == remaining_ast(after)
assert git('show', PAIR + ':' + PATH) == before
patch = git('diff', '--binary', parent, CAND, '--', PATH)
patch_path = OUT / 'exact-test-only.patch'; patch_path.write_bytes(patch)
git('switch', '--detach', PAIR)
applied = False
try:
    subprocess.run(['git', 'apply', '--check', str(patch_path)], cwd=ROOT, check=True)
    subprocess.run(['git', 'apply', str(patch_path)], cwd=ROOT, check=True)
    applied = True
    actual = (ROOT / PATH).read_text(encoding='utf-8').replace('\r\n', '\n').encode()
    assert actual == after.replace(b'\r\n', b'\n')
    result = subprocess.run([sys.executable, '-m', 'pytest',
        'infra/aws/lambda/investor-reporting/_authz/tests/test_loader_freshness.py', PATH,
        '-q', '--junitxml=' + str(OUT / 'paired.xml')], cwd=ROOT,
        capture_output=True, text=True, encoding='utf-8', errors='replace')
    (OUT / 'paired.txt').write_text(result.stdout + result.stderr, encoding='utf-8')
    print(result.stdout, end='')
    assert result.returncode == 0, result.stderr
finally:
    if applied:
        actual = (ROOT / PATH).read_text(encoding='utf-8').replace('\r\n', '\n').encode()
        assert actual == after.replace(b'\r\n', b'\n'), 'unexpected concurrent edit; refusing restore'
        git('restore', '--source=HEAD', '--worktree', '--', PATH)
    assert not git('status', '--porcelain').strip()
    git('switch', '--detach', CAND)
proof = {'candidate': CAND, 'parent': parent, 'paired_baseline': PAIR,
         'only_changed_path': PATH, 'all_other_AST_unchanged': True,
         'paired_test_preimage_identical': True, 'exact_patch_applies': True,
         'paired_returncode': result.returncode, 'review_checkout_restored_clean': True,
         'patch_sha256': hashlib.sha256(patch).hexdigest()}
(OUT / 'evidence.json').write_text(json.dumps(proof, indent=2), encoding='utf-8')
print(json.dumps(proof, indent=2))

```
