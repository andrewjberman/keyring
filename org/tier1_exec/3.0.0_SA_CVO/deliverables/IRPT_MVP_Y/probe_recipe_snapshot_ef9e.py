"""Independent recorded configuration capture and frozen-consumer review."""
import copy
import hashlib
import io
import json
import os
from pathlib import Path
import socket
import subprocess
import sys
from unittest.mock import Mock
import zipfile

from probe_recipe_decimal import deny_network, load


def main():
    own = Path(__file__).resolve().parent
    root = own.parents[4]
    pin = subprocess.check_output(['git', 'rev-parse', 'ef9e8f51c4'], cwd=root, text=True).strip()
    target = root / '.runtime/codex-seats/3.0.0_SA_CVO~Y/recipe-snapshot' / pin
    target.mkdir(parents=True, exist_ok=True)
    prefix = 'infra/aws/lambda/investor-reporting'
    raw = subprocess.check_output(['git', 'archive', '--format=zip', pin, prefix,
                                  'docs/contracts/investor-reporting', 'data/firm_registry.json'], cwd=root)
    hashes = {}
    with zipfile.ZipFile(io.BytesIO(raw)) as archive:
        for item in archive.infolist():
            path = (target / item.filename).resolve()
            if not path.is_relative_to(target.resolve()):
                raise ValueError('snapshot escape')
            if item.is_dir():
                path.mkdir(parents=True, exist_ok=True)
            else:
                data = archive.read(item)
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(data)
                hashes[item.filename] = hashlib.sha256(data).hexdigest()
    os.environ['IRPT_FIRM_REGISTRY'] = str(target / 'data/firm_registry.json')
    base = target / prefix
    tests = [base / x for x in (
        'ycharts/generate/tests/test_recipe_snapshot.py', 'ycharts/generate/tests/test_frozen_worker.py',
        'ycharts/generate/tests/test_composition_admission.py', 'ycharts/generate/tests/test_submission.py',
        'intake/tests/test_retained_uploads.py', 'intake/tests/test_uploads.py')]
    command = ('import socket,pytest; '
        'deny=lambda *a,**k: (_ for _ in ()).throw(AssertionError("NETWORK_FORBIDDEN")); '
        'socket.socket.connect=deny; socket.socket.connect_ex=deny; socket.create_connection=deny; '
        'raise SystemExit(pytest.main(' + repr(['-q'] + [str(p) for p in tests]) + '))')
    suite = subprocess.run([sys.executable, '-c', command], cwd=root, capture_output=True,
                           text=True, encoding='utf-8', errors='replace')
    socket.socket.connect = deny_network
    socket.socket.connect_ex = deny_network
    socket.create_connection = deny_network
    fixture = load('recipe_snapshot_review_fixture', tests[1])
    snapshot = load('recipe_snapshot', base / 'ycharts/generate/recipe_snapshot.py')
    recipe = sys.modules['recipe']
    canonical = fixture.canonical_bytes
    settings_bytes = Path(recipe.SETTINGS_PATH).read_bytes()
    template_bytes = Path(recipe.TEMPLATES_PATH).read_bytes()
    settings_doc = json.loads(settings_bytes)
    templates_doc = json.loads(template_bytes)
    results = []

    def world():
        return fixture.world.__wrapped__(fixture.retention_world.__wrapped__())

    def fresh(configuration=None):
        w = world()
        r = fixture.assembled(w, configuration=configuration or
            (lambda body, principal, owner: snapshot.capture_configuration(owner, body)))
        r.w = w
        r.inputs = lambda: r.worker.recipe_inputs(w.case.principal, r.store.request_id)
        return r

    def check(name, fn):
        try:
            results.append(dict(name=name, outcome='PASS', detail=fn()))
        except Exception as error:
            results.append(dict(name=name, outcome='FAIL', error=repr(error)))

    def refuse(fn):
        try:
            fn()
        except (ValueError, RuntimeError, PermissionError) as error:
            return dict(exception=type(error).__name__, reason=str(error))
        raise AssertionError('invalid configuration returned recipe inputs')

    def positive():
        scratch = target / 'independent-config'
        scratch.mkdir(exist_ok=True)
        tp, sp = scratch / 'templates.json', scratch / 'settings.json'
        tp.write_bytes(template_bytes)
        sp.write_bytes(settings_bytes)
        calls = []
        def configuration(body, principal, owner):
            calls.append(copy.deepcopy(body))
            return snapshot.capture_configuration(owner, body, templates_path=tp, settings_path=sp)
        r = fresh(configuration)
        first = r.inputs()
        before = (copy.deepcopy(r.client.rows), copy.deepcopy(r.w.table.rows), r.w.case.s3.put_count)
        sources = first['source_descriptors']
        for source_id, data in ((snapshot.RECIPE_SOURCE, template_bytes), (snapshot.SETTINGS_SOURCE, settings_bytes)):
            source = sources[source_id]
            assert source['projection']['configuration_sha256'] == hashlib.sha256(data).hexdigest()
            assert source['projection_sha256'] == fixture.digest(source['projection'])
            assert source['upstream_revision']['state'] == 'UNAVAILABLE'
            assert source['upstream_revision']['value'] is None and source['upstream_revision']['commit'] is None
            assert source['source_dates']['business_date'] is None
            assert source['source_dates']['absence_reason'] and source['retention_ref'] is None
        config = first['recipe']
        assert config['settings'] == settings_doc
        assert len(config['settings']['settings']) == 7
        portfolio = recipe.portfolio_body('synthetic', 7, config['settings'])
        expected = {'management_fee': 0.003, 'rebalance_frequency': 'quarterly', 'reinvest_dividends': False,
                    'start_of_series': 'oldest', 'level_as_of_type': 'prior_close',
                    'tax_status': 'non_qualified', 'benchmark_symbol': '^SPXTR'}
        assert {key: portfolio[key] for key in expected} == expected, repr({key: portfolio[key] for key in expected})
        generated = recipe.generation_body(config['template'], ['P:synthetic'], {},
            {**first['cover'], 'primary_name': 'Synthetic primary'})
        assert recipe.cover_fields_agree(generated)[0] is True
        assert generated['prepared_for'] == r.body['prepared_for']
        frozen = canonical(first)
        tp.write_text('corrupted after acceptance', encoding='utf-8')
        sp.write_text('corrupted after acceptance', encoding='utf-8')
        r.service.resolve_configuration = Mock(side_effect=AssertionError('REPLAY_CONFIGURATION_READ'))
        r.service.resolve_inputs = Mock(side_effect=AssertionError('REPLAY_SOURCE_READ'))
        r.accepted.lookup.return_value = r.record
        r.service.submit(r.body, None, {}, {}, None)
        assert canonical(r.inputs()) == frozen and len(calls) == 1
        first['recipe']['settings']['settings'].clear()
        first['source_descriptors'].clear()
        assert canonical(r.inputs()) == frozen
        assert before == (r.client.rows, r.w.table.rows, r.w.case.s3.put_count)
        r.client.update_item.assert_not_called()
        return dict(configuration_resolutions=1, seven_vendor_fields=expected,
                    template_id=config['template']['template_id'], frozen_sha256=hashlib.sha256(frozen).hexdigest(), writes=0)
    check('exact_capture_seven_body_settings_cover_and_no_reread_replay', positive)

    setting_faults = {
        'bool_fee': ('management_fee', True), 'negative_fee': ('management_fee', -0.01),
        'infinite_fee': ('management_fee', float('inf')), 'nan_fee': ('management_fee', float('nan')),
        'text_fee': ('management_fee', '0.003'), 'numeric_boolean': ('reinvest_dividends', 0),
        'text_boolean': ('reinvest_dividends', 'false'), 'empty_benchmark': ('benchmark', ' '),
        'cross_tax_mode': ('tax_status', 'QUARTERLY'), 'unknown_rebalance': ('rebalance_frequency', 'DAILY'),
        'unknown_start': ('start_of_series', 'TODAY'), 'unknown_level': ('level_as_of_type', 'OPEN'),
    }
    for name, (key, value) in setting_faults.items():
        def test_setting(key=key, value=value):
            doc = copy.deepcopy(settings_doc)
            doc['settings'][key]['value'] = value
            return refuse(lambda: snapshot.validate_settings(doc))
        check('setting_' + name, test_setting)
    def incomplete(kind):
        doc = copy.deepcopy(settings_doc)
        if kind == 'missing':
            del doc['settings']['benchmark']
        elif kind == 'extra':
            doc['settings']['unowned'] = {'value': True, 'source': 'synthetic'}
        else:
            doc['settings']['benchmark']['source'] = ' '
        return refuse(lambda: snapshot.validate_settings(doc))
    for kind in ('missing', 'extra', 'empty_source'):
        check('setting_' + kind, lambda kind=kind: incomplete(kind))

    def template_fault(kind):
        r = fresh()
        prepared = r.prepare()
        projection = prepared['source_descriptors'][snapshot.RECIPE_SOURCE]['projection']
        changes = {'zero_id': ('template_id', '0'), 'unicode_id': ('template_id', '\u0661'),
                   'numeric_id': ('template_id', 14141822), 'primary_bool': ('primary_securities', True),
                   'orientation': ('orientation', 'diagonal'), 'variant': ('variant', 'MULTI'),
                   'count_bool': ('comparison_min', False), 'count_outside': ('comparison_min', 1)}
        key, value = changes[kind]
        projection[key] = value
        prepared['source_descriptors'][snapshot.RECIPE_SOURCE]['projection_sha256'] = fixture.digest(projection)
        return refuse(lambda: snapshot.consume_configuration(prepared))
    for kind in ('zero_id', 'unicode_id', 'numeric_id', 'primary_bool', 'orientation', 'variant', 'count_bool', 'count_outside'):
        check('template_' + kind, lambda kind=kind: template_fault(kind))

    def changed_binding(kind):
        r = fresh()
        prepared = r.prepare()
        if kind == 'settings':
            prepared['settings']['settings']['management_fee']['value'] = 0.01
        elif kind == 'version':
            prepared['recipe_version'] = 'other'
        elif kind == 'source_kind':
            prepared['source_descriptors'][snapshot.RECIPE_SOURCE]['source_kind'] = 'BROWSER_REQUEST'
        else:
            prepared['source_descriptors'][snapshot.SETTINGS_SOURCE]['projection_sha256'] = '0' * 64
        return refuse(lambda: snapshot.consume_configuration(prepared))
    for kind in ('settings', 'version', 'source_kind', 'projection_digest'):
        check('binding_' + kind, lambda kind=kind: changed_binding(kind))

    def cardinalities():
        r = fresh()
        rows = []
        for count in range(6):
            body = {**r.body, 'variant': 'auto', 'comparison_keys': ['synthetic-' + str(i) for i in range(count)]}
            config = snapshot.capture_configuration(r.record['owner'], body)
            variant = config['source_descriptors'][snapshot.RECIPE_SOURCE]['projection']['variant']
            assert variant == ('OVERVIEW' if count == 0 else 'COMPARISON' if count == 1 else 'MULTI')
            rows.append(dict(count=count, variant=variant))
        return dict(pure_capture_only=rows, no_comparison_authority_or_admission=True)
    check('pure_capture_all_six_cardinalities_not_comparison_admission', cardinalities)

    def collision():
        w = world()
        def configuration(body, principal, owner):
            result = snapshot.capture_configuration(owner, body)
            result['source_descriptors']['recipe'] = copy.deepcopy(result['source_descriptors'][snapshot.RECIPE_SOURCE])
            return result
        detail = refuse(lambda: fixture.assembled(w, configuration=configuration))
        assert w.case.s3.put_count == 2
        return detail
    check('source_id_collision_refuses_before_composition_write', collision)

    def duplicate():
        w = world()
        doc = copy.deepcopy(templates_doc)
        doc['templates'].append(copy.deepcopy(next(x for x in doc['templates'] if x['variant'] == 'OVERVIEW')))
        path = target / 'duplicate-template.json'
        path.write_text(json.dumps(doc), encoding='utf-8')
        detail = refuse(lambda: fixture.assembled(w, configuration=lambda body, principal, owner:
            snapshot.capture_configuration(owner, body, templates_path=path)))
        assert w.case.s3.put_count == 2
        return detail
    check('duplicate_template_refuses_before_composition_write', duplicate)

    def old_minimal():
        w = world()
        r = fixture.assembled(w)
        assert r.prepare()['settings']['management_fee'] == 0.003
        return refuse(lambda: r.worker.recipe_inputs(w.case.principal, r.store.request_id))
    check('old_minimal_settings_inspectable_but_no_recipe_inputs', old_minimal)

    def guard(kind):
        r = fresh()
        if kind == 'access':
            r.w.case.headers['x-user-email'] = 'revoked@example.invalid'
        else:
            r.row['fence_token'] = {'N': '2'}
        return refuse(r.inputs)
    for kind in ('access', 'fence'):
        check('recipe_inputs_current_' + kind, lambda kind=kind: guard(kind))

    report = dict(pin=pin, results=results, source_sha256=hashes,
        supplied=dict(exit_code=suite.returncode, stdout=suite.stdout, stderr=suite.stderr),
        limits=['Actual capture/service/admission/retained worker/recipe code with synthetic source and storage effects',
                'Recorded file bytes are not current template/settings/vendor permission or source provenance',
                'No installed factory, atomicity, transport, selected comparison admission, vendor readback, render or READY grade'])
    (own / 'RECIPE_SNAPSHOT_ef9e8f51.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in report.items() if k != 'source_sha256'}, indent=2))
    return int(suite.returncode != 0 or any(row['outcome'] != 'PASS' for row in results))


if __name__ == '__main__':
    raise SystemExit(main())
