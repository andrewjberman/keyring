# Maintained-source resolver: bounded independent source review

Reviewer: `3.0.0_SA_CVO~M`. Date: 2026-09-23 UTC.
Authority: completion CONTRACT reviewer assignment and CTO
IRPT-MAINTAINED-SOURCE-01/02 (`0429af3604`, `51b5d63a81`).
Trigger: exact COO~M notification `20260923T020511Z`.

## Verdict and exact scope

**BOUNDED SOURCE PASS** for candidate
`703e82ea015d840ce773d473a7b4909e275785c0`, parent
`8992447f8f677ac9706f5e74711361f171d46ee7`.
No defect was reproduced within the tested primitive's documented boundary.
This is not acceptance-service, retained-store, worker, runtime-reader, vendor,
renderer, deployment, three-firm E2E or full M1-M7 acceptance.

Reviewed from the clean detached reviewer checkout
`C:/Users/AndrewBerman/Desktop/ajb_irpt_cvo_m_review`; the producer's dirty
legacy-read patch was neither included nor exercised. Candidate changes exactly
six paths: new `_scope/maintained_sources.py`, its test and cross-owner probe,
and M's INTERFACES, MAINTAINED_SOURCE_INVENTORY and MAINTAINED_SOURCE_RESOLVER.
Read the complete new module, resolver contract, inventory, supplied tests/probe,
interface diff, existing prospect-owner primitive, relevant canonical getUser
implementation, complete getPartnerProfile, and pinned P integrity helper.

Exact compatibility peers:

- P schema/helper: `d91b2bdd10fe05a0e241ccbfb8f6d7f1b35a872c`.
- Y catalogue: `9daa67433e2d41b07c4b2221694bbaf71340a80d`.

## Independent findings

The canonical user lookup resolves email through the existing index, refuses a
second match, then reads the actual PROFILE key. Its projected name, email,
firmId, status and updatedAt match the adapter contract. The canonical partner
reader takes verified firm/email, returning advisorKey and raw data. The source
checks subject and advisor-key agreement. Canonical provisioning explicitly
assigns users-v2 to CloudOps. These are inspected source contracts, not live
record receipts or proof that the missing Python/TypeScript transport exists.

The profile primitive requires literal True from the supplied exact-input access
and retention authorizer before and after its reads. It compares current trusted
owner and input identity, rejects changed relevant projections, and deep-copies
reader/authorizer data. Advisors use the matching partner advisorName; operations
use their actual user.name without reading/borrowing an advisor identity. The
enabled client firm's registry display_name supplies organization. Credentials,
reset data and MFA contacts do not enter the allowlisted projections.

Descriptors preserve original updatedAt or explicit absence; unavailable upstream
versions and business dates stay unavailable. Projection hashes use the same
compact sorted unescaped UTF-8 encoding as P. No historical Git pin or process
timestamp is asserted as a runtime source revision. Double reads are not a
transaction, immutable upstream revision or freshness guarantee.

The exact user-entered prepared_for value retains its browser provenance and
verified principal/firm binding; it grants no identity, scope or entitlement.
Whitespace, Unicode and markup-looking text remain exact display text. Contacts
are explicitly absent. Required missing recipient or absent title with no trusted
recipe evidence refuses. Actual renderer escaping and vendor text limits remain
separate: 200 code points is only the application rule.

Empty comparison selection produces empty canonical fragments without catalogue
access and still rechecks authorization. Unknown/ambiguous keys and every selected
entry are unavailable. Edited VERIFIED flags, populated policy-looking fields and
historical live_proven cannot enable a comparison. This proves refusal behavior;
it does not deliver the full Comparison/Multi-Comp capability or validate IDs.

## Executed evidence

All commands ran at the exact detached source candidate, exit 0:

| Check | Result |
| --- | --- |
| `python -m pytest infra/aws/lambda/investor-reporting/_scope/tests -q` | 102 passed, 57 subtests passed, 2.37s |
| `python infra/aws/lambda/investor-reporting/_scope/tests/probe_maintained_composition.py` | Exact pinned P synthetic schema/helper and Unicode byte parity pass; all five tamper controls refuse; later profile change preserves frozen bytes; four actual Y entries plus unknown refuse; empty selection passes |
| Independent driver below via `python -m pytest <driver> -q` | 44 passed, 0.20s |

Independent controls use newly constructed synthetic fixtures and the actual
candidate module; no producer test fixtures are imported. They cover both
advisor/operations projection provenance, detached results, every disallowed
control/surrogate recipient code point (65 + 2048), strict authorization results
at each boundary, claim/input/browser/user-date/partner/registry changes during
reads, source exceptions, deep-copy isolation, missing dates, no-comparison
revocation/mutation, unknown/duplicate/self-promoted comparisons and wrong
recipe scope/binding/digest/kind. The valid synthetic controls are 49financial;
this is not an actual three-firm record/transport exercise.

The P probe uses P's complete synthetic input/recipe fixture. It proves the
specified fragment/schema pairing, not a maintained recipe receipt, persisted
composition, actual protected acceptance or dispatch.

Source module on-disk SHA256:
`679022941e0068a33d0ca20248a0ea9639463c2ea9bc8e7616241e0c6f1d49f5`.
Independent driver SHA256:
`11fd79c2f3d9198e6edc0310b0912cbbd84fdac91d96f0ff518e9aafd47101ce`.
Driver runtime path:
`C:/Users/AndrewBerman/Desktop/ajb_workspace/.runtime/codex-seats/3.0.0_SA_CVO~M/test_maintained_703_review.py`.

## Required integration boundaries

Y must wire canonical reader adapters preserving ambiguity rejection and exact
current input/selection authorization and retention. P/Y must validate the closed
browser request, full canonical schema and P bindings, prevent source-ID
collisions, bind fragments to accepted owner/input/selection, and freeze exact
bytes. Retry/reopening/export must use retained composition and current access,
not rerun mutable profile resolution. The primitive returns preparation fragments
and does not itself persist an accepted request or establish those guarantees.

The browser closed validator and final full-schema validator remain caller
obligations. Source exceptions fail without fragments; public error normalization
belongs to actual service integration. Trusted injected readers/authorizers are
not client-controlled inputs. Recipe-title descriptors remain a trusted Y
interface with final P validation; no real default recipe evidence was supplied.

Independent P and Y integrated verdicts remain separate. Existing original
economic/reconciliation findings, final-index publication ambiguity, legacy-read,
retention/runtime and live/vendor/render/deployment holds are unchanged. No full
product grade or previously NOT_EVALUATED item is promoted by this review.

## Reproducible independent driver

The complete driver follows. Restore it as a UTF-8 Python file, update only ROOT
if the reviewer checkout location differs, and run the command above at the
pinned source. It performs no network or producer-worktree writes.

```python
"""Independent offline CVO M review; no network or producer fixture imports."""
import copy
import hashlib
import json
import sys
from pathlib import Path

import pytest

ROOT = Path('C:/Users/AndrewBerman/Desktop/ajb_irpt_cvo_m_review')
sys.path.insert(0, str(ROOT / 'infra/aws/lambda/investor-reporting/_scope'))
import maintained_sources as m


@pytest.fixture
def env():
    headers = {'x-origin-verify': 'cloudfront', 'x-user-email': 'review@example.invalid',
               'x-firm-id': '49financial', 'x-advisor-id': 'review-advisor',
               'x-user-role': 'advisor', 'x-user-type': 'partner'}
    reference = {'input_id': 'synthetic-retained', 'revision': 'r1',
                 'artifact_ref': {'sha256': 'a' * 64, 'version': 'opaque-v1'}}
    user = {'email': headers['x-user-email'], 'firmId': headers['x-firm-id'],
            'status': 'active', 'name': 'Actual Operator', 'updatedAt': '2026-09-22T21:00:00-04:00',
            'password_hash': 'DO-NOT-RETAIN', 'phoneNumber': 'MFA-ONLY'}
    partner = {'advisorKey': 'review-advisor', 'firmRole': 'user', 'raw': {
        'email': user['email'], 'advisorKey': 'review-advisor', 'advisorName': 'Actual Advisor',
        'updatedAt': '2026-09-22T20:00:00Z', 'private': 'DO-NOT-RETAIN'}}
    browser = {'prepared_for': '  Recipient \U0001f9ed <b>Display</b>  ', 'report_title': 'Exact title'}
    calls = []
    def auth(owner, ref):
        calls.append((copy.deepcopy(owner), copy.deepcopy(ref)))
        return ref == reference and owner['principal_id'] == user['email']
    args = {'get_user': lambda email: user, 'get_partner_profile': lambda email, firm: partner,
            'authorize_input': auth}
    return headers, reference, user, partner, browser, args, calls


def fields(e, **overrides):
    h, ref, _, _, browser, args, _ = e
    return m.resolve_profile_fields(h, ref, browser, **(args | overrides))


def compare(e, keys, catalogue=None, **overrides):
    h, ref, _, _, _, args, _ = e
    return m.resolve_comparison_fields(h, ref, keys, **{
        'authorize_input': args['authorize_input'], 'get_catalogue': lambda: catalogue, **overrides})


@pytest.mark.parametrize('operations', [False, True])
def test_exact_projections_and_provenance(env, operations):
    if operations:
        env[0].update({'x-user-role': 'admin', 'x-advisor-id': ''})
        env[5]['get_partner_profile'] = lambda *_: pytest.fail('operations borrowed partner')
    out = fields(env)
    assert out['profile']['prepared_by'] == ('Actual Operator' if operations else 'Actual Advisor')
    assert out['profile']['prepared_for'] == env[4]['prepared_for']
    assert out['profile']['report_title'] == 'Exact title'
    for source in out['source_descriptors'].values():
        encoded = json.dumps(source['projection'], sort_keys=True, ensure_ascii=False,
                             separators=(',', ':'), allow_nan=False).encode('utf-8')
        assert source['projection_sha256'] == hashlib.sha256(encoded).hexdigest()
        assert source['binding']['principal_id'] == env[2]['email']
        assert source['binding']['firm_id'] == '49financial'
        assert source['upstream_revision']['state'] == 'UNAVAILABLE'
        assert all(source['upstream_revision'][key] is None for key in ('kind', 'value', 'commit'))
        assert source['source_dates']['business_date'] is None
        assert source['source_dates']['absence_reason']
    assert out['source_descriptors']['maintained-user']['source_dates']['updated_at'] == env[2]['updatedAt']
    for key in ('contact_email', 'contact_phone', 'contact_url', 'custom_field'):
        assert out['profile'][key] is None
        assert out['profile_provenance'][key]['state'] == 'ABSENT'
    blob = m.canonical_bytes(out)
    assert b'DO-NOT-RETAIN' not in blob and b'MFA-ONLY' not in blob
    assert len(env[6]) == 2 and all(ref == env[1] for _, ref in env[6])
    env[2]['name'] = 'Later'; env[3]['raw']['advisorName'] = 'Later'
    env[4]['prepared_for'] = 'Later'; env[1]['artifact_ref']['version'] = 'Later'
    assert m.canonical_bytes(out) == blob


@pytest.mark.parametrize('answer', [False, None, 0, 1, 'true', {}, []])
@pytest.mark.parametrize('phase', [1, 2])
def test_literal_true_at_both_authorization_boundaries(env, answer, phase):
    count = 0
    def authorize(*_):
        nonlocal count
        count += 1
        return answer if count == phase else True
    with pytest.raises(m.MaintainedSourceRefused):
        fields(env, authorize_input=authorize)
    assert count == phase


@pytest.mark.parametrize('field,value', [
    ('x-firm-id', 'cottonwood'), ('x-user-email', 'other@example.invalid'),
    ('x-advisor-id', 'other-advisor'), ('x-user-role', 'admin'), ('x-origin-verify', '')])
def test_claim_change_during_source_reads(env, field, value):
    count = 0
    def reader(_):
        nonlocal count
        count += 1
        if count == 2:
            env[0][field] = value
        return env[2]
    with pytest.raises(PermissionError):
        fields(env, get_user=reader)


@pytest.mark.parametrize('target', ['input', 'browser', 'user_date', 'partner_name', 'partner_date'])
def test_second_read_changes_refuse(env, target):
    count = 0
    def reader(_):
        nonlocal count
        count += 1
        if count == 2:
            if target == 'input': env[1]['artifact_ref']['version'] = 'v2'
            elif target == 'browser': env[4]['prepared_for'] = 'Changed'
            elif target == 'user_date': env[2]['updatedAt'] = '2026-09-23T02:00:00Z'
            elif target == 'partner_name': env[3]['raw']['advisorName'] = 'Changed'
            elif target == 'partner_date': env[3]['raw']['updatedAt'] = '2026-09-23T02:00:00Z'
        return env[2]
    with pytest.raises(m.MaintainedSourceRefused):
        fields(env, get_user=reader)


@pytest.mark.parametrize('which', ['user', 'partner', 'authorize'])
def test_reader_failure_never_returns_fragments(env, which):
    def fail(*_): raise RuntimeError('synthetic reader failure')
    key = {'user': 'get_user', 'partner': 'get_partner_profile', 'authorize': 'authorize_input'}[which]
    with pytest.raises(RuntimeError, match='synthetic reader failure'):
        fields(env, **{key: fail})


def test_callback_receives_deep_detached_owner_and_input(env):
    def authorize(owner, reference):
        owner.clear(); reference['artifact_ref']['sha256'] = 'b' * 64
        return True
    result = fields(env, authorize_input=authorize)
    assert env[1]['artifact_ref']['sha256'] == 'a' * 64
    assert result['source_descriptors']['maintained-user']['binding']['firm_id'] == '49financial'


def test_absent_original_dates_are_explicit(env):
    del env[2]['updatedAt']; del env[3]['raw']['updatedAt']
    result = fields(env)
    for key in ('maintained-user', 'maintained-partner'):
        assert result['source_descriptors'][key]['source_dates']['updated_at'] is None


def test_every_control_and_surrogate_recipient_refuses_before_io(env):
    def fail(*_): pytest.fail('invalid label reached a source reader')
    for point in list(range(32)) + list(range(127, 160)) + list(range(0xD800, 0xE000)):
        env[4]['prepared_for'] = 'a' + chr(point) + 'b'
        with pytest.raises(m.MaintainedSourceRefused):
            fields(env, get_user=fail, get_partner_profile=fail)


def test_empty_comparisons_do_not_read_catalogue_but_recheck_access(env):
    def fail(): pytest.fail('empty selection read catalogue')
    assert compare(env, [], get_catalogue=fail) == {'comparison_catalog': {}, 'source_descriptors': {}}
    assert len(env[6]) == 2
    values = iter([True, False])
    with pytest.raises(m.MaintainedSourceRefused):
        compare(env, [], get_catalogue=fail, authorize_input=lambda *_: next(values))


@pytest.mark.parametrize('change', ['input', 'selection', 'owner'])
def test_empty_comparison_mutations_refuse(env, change):
    keys = []
    def authorize(*_):
        if change == 'input': env[1]['revision'] = 'changed'
        if change == 'selection': keys.append('selected')
        if change == 'owner': env[0]['x-user-email'] = 'other@example.invalid'
        return True
    with pytest.raises(m.MaintainedSourceRefused):
        compare(env, keys, authorize_input=authorize)


@pytest.mark.parametrize('entries', [[], [{'key': 'x'}, {'key': 'x'}], [{'key': 'x',
    'security_id': 'P:1234', 'live_proven': True, 'candidate': {
        'identity_status': 'VERIFIED', 'entitlement_status': 'VERIFIED',
        'permitted_firm_ids': ['49financial'], 'permitted_principal_ids': ['review@example.invalid']}}]])
def test_unknown_ambiguous_and_self_promoted_comparisons_refuse(env, entries):
    catalogue = {'maintainer': '2.0.0_SA_COO~Y',
                 'candidate_version': 'irpt-ycharts-comparison-candidate.20260923.v1', 'entries': entries}
    with pytest.raises(m.MaintainedSourceRefused): compare(env, ['x'], catalogue)


@pytest.mark.parametrize('wrong', ['scope', 'binding', 'digest', 'kind'])
def test_recipe_title_wrong_scope_binding_digest_or_kind_refuses(env, wrong):
    source = copy.deepcopy(fields(env)['source_descriptors']['canonical-firm-display'])
    source['source_kind'] = 'RECIPE_CONFIGURATION'
    source['projection'] = {'report_title': 'Synthetic recipe title'}
    source['projection_sha256'] = m.projection_sha256(source['projection'])
    env[4]['report_title'] = None
    if wrong == 'scope': source['source_scope']['firm_id'] = 'cottonwood'
    elif wrong == 'binding': source['binding']['principal_id'] = 'other@example.invalid'
    elif wrong == 'digest': source['projection_sha256'] = '0' * 64
    elif wrong == 'kind': source['source_kind'] = 'BROWSER_REQUEST'
    with pytest.raises(m.MaintainedSourceRefused): fields(env, recipe_title_source=source)


def test_registry_changes_between_reads_refuse(env, tmp_path):
    registry = json.loads((ROOT / 'data/firm_registry.json').read_text(encoding='utf-8'))
    path = tmp_path / 'registry.json'; path.write_text(json.dumps(registry), encoding='utf-8')
    count = 0
    def reader(_):
        nonlocal count
        count += 1
        if count == 2:
            for row in registry['firms']:
                if row['firm_id'] == '49financial': row['display_name'] = 'Changed Firm'
            path.write_text(json.dumps(registry), encoding='utf-8')
        return env[2]
    with pytest.raises(m.MaintainedSourceRefused): fields(env, get_user=reader, registry_path=path)

```
