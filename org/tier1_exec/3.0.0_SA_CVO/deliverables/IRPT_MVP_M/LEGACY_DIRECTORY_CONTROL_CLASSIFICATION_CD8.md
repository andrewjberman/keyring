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
