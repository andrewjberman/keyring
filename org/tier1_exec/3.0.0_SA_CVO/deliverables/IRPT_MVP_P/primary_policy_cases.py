"""Reviewer controls after the pinned flat guarded-entry setup."""
import json

import entry
import enforce
import handler
import selection
import tenants
import transport

firm, opaque, a, b, headers, directory, ownership, save = (
    globals()[key] for key in ('firm', 'opaque', 'a', 'b', 'headers', 'directory', 'ownership', 'save'))
checks = []
calls = []


def forbidden(*args, **kwargs):
    calls.append('forbidden')
    raise AssertionError('provider/replay/transport must not run')


def scope_for(fid, requested, permitted=None):
    return {'verified_request_firm_id': fid, 'permitted_account_set': requested if permitted is None else permitted,
            'resolved_scope': {'scope_kind': 'ACCOUNT_SET', 'scope_ids': requested}}


original_replay = handler.replay_capture
handler.replay_capture = forbidden
handler.bd_adapter.adapt = forbidden
handler.orion_adapter.adapt = forbidden
transport.default_transport = forbidden
for short, provider in [('49F', 'SMARTX'), ('COT', 'BLACK_DIAMOND'), ('INF', 'ORION')]:
    fid = tenants._LEGACY_SHORT_ID[short]
    for mode in ('recorded', 'live'):
        result = handler.run(scope_for(fid, ['current-account-1', 'current-account-2']),
                             '2026-09-01', '2026-09-22', mode=mode, transport=object(),
                             per_use_token='non-authorizing-test-string', labels={'scope': 'orion_daily'})
        assert result['report'] is None and result['contract_validated'] is False
        assert result['lineage']['provider'] == provider and result['absences']
        assert not calls
        checks.append(short + '_' + mode + '_no_provider_or_transport')
    raw = handler.lambda_handler({'scope': scope_for(fid, ['900000001']),
                                  'requested_start': '2026-06-10', 'requested_end': '2026-09-09',
                                  'mode': 'recorded', 'labels': handler.STALE_SESSION_LABELS})
    assert json.loads(raw['body'])['report'] is None and not calls
    checks.append(short + '_legacy_lambda_cannot_serve_capture')

route = tenants.route_for(tenants._LEGACY_SHORT_ID['49F'])
assert route.provider == 'SMARTX' and route.host is None and route.session_secret_id is None
assert route.paths == {} and route.data_plane_bucket is None
assert tenants.verification_route_for(tenants._LEGACY_SHORT_ID['49F']).provider == 'BLACK_DIAMOND'
checks.append('49F_explicit_primary_and_separate_verifier')
for short in ('COT', 'INF'):
    try:
        tenants.verification_route_for(tenants._LEGACY_SHORT_ID[short])
    except tenants.UnknownTenant:
        pass
    else:
        raise AssertionError('foreign verifier')
checks.append('no_verifier_for_other_tenants')

old_provider = route.provider
try:
    route.provider = 'UNREGISTERED'
    result = handler.run(scope_for(tenants._LEGACY_SHORT_ID['49F'], ['a']), '2026-09-01', '2026-09-22')
    assert result['coverage']['outcome'] == 'UNSUPPORTED_PROVIDER' and not calls
finally:
    route.provider = old_provider
checks.append('unsupported_primary_no_adapter_fallback')

for requested, permitted in [([], []), (['a', 'a'], ['a']), (['a', 'foreign'], ['a'])]:
    try:
        handler.run(scope_for(opaque, requested, permitted), '2026-09-01', '2026-09-22')
    except handler.ScopeRefused:
        pass
    else:
        raise AssertionError('invalid selected set accepted')
assert not calls
checks.append('empty_duplicate_or_wider_selected_set_refused')

guard, ctx = entry.ENTRY.enforcer_for(firm)
resolved, refusal = guard.resolve_now(enforce.Request(headers, 'performance_report'))
assert refusal is None
selected = selection.create_selection(resolved, directory, [a],
    directory_revision=selection.directory_revision(directory), save_selection=save)
event = {'headers': headers, 'routeKey': next(iter(entry.ROUTES)),
         'pathParameters': {'accountSetId': selected['account_set_id']},
         'queryStringParameters': {'start': '2026-09-01', 'end': '2026-09-22'}}
outcome = entry.lambda_handler(event)
assert outcome.get('ok') is False and 'data' not in outcome and not calls
checks.append('actual_guarded_entry_no_capture_release')

original_run = handler.run
seen = []


def observe(scope, **kwargs):
    seen.append({'accounts': scope['resolved_scope']['scope_ids'], 'dates': kwargs})
    return original_run(scope, **kwargs)


handler.run = observe
entry.lambda_handler(event)
assert seen == [{'accounts': [a], 'dates': {'requested_start': '2026-09-01', 'requested_end': '2026-09-22'}}]
checks.append('actual_entry_passes_only_retained_selection_and_explicit_dates')
for bad in [
    {**event, 'pathParameters': {'accountSetId': 'sel_' + '0' * 64}},
    {**event, 'queryStringParameters': {**event['queryStringParameters'], 'mode': 'recorded'}},
]:
    seen.clear()
    outcome = entry.lambda_handler(bad)
    assert outcome.get('ok') is False and 'data' not in outcome and not seen
checks.append('missing_selection_and_query_transport_override_refused_before_provider')
ownership['advisors']['advisor']['accounts'] = [b]
seen.clear()
outcome = entry.lambda_handler(event)
assert outcome.get('ok') is False and 'data' not in outcome and not seen
checks.append('revoked_selection_refused_before_provider')

for short, accounts, start in [('49F', ['different'], '2026-06-10'),
                              ('INF', ['900000002'], '2026-06-10'),
                              ('49F', ['900000001'], '2026-09-01')]:
    try:
        original_replay(scope_for(tenants._LEGACY_SHORT_ID[short], accounts), start, '2026-09-09')
    except handler.ScopeRefused:
        pass
    else:
        raise AssertionError('capture reused for another set or period')
checks.append('capture_rejects_changed_set_subset_or_window')
assert not calls
print(json.dumps({'checks': checks, 'check_count': len(checks), 'forbidden_calls': calls,
                  'guarded_refusal': outcome, 'network': False}))
