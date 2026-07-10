#!/usr/bin/env python3
"""Mutant-kill tests for comp-adapter-audit (adapter_audit_cli).

Bar (CTO, 2026-07-10): every guard test must be shown LOAD-BEARING -- break the guard on
purpose and confirm the assertion goes RED. A guard test that passes with the guard
removed is decoration. Each `*_mutant_*` test below is that negative control: it drives
the UNGUARDED comparison directly and asserts the bug reappears.

No test here touches S3 or the network. The S3 layer is injected.
"""
from __future__ import annotations

import argparse
import importlib.util
import io
import contextlib
import sys
from pathlib import Path

import pytest

_WS = Path(__file__).resolve().parents[4]
_CLI = _WS / 'org' / 'modules' / 'graph' / 'adapter_audit_cli.py'

spec = importlib.util.spec_from_file_location('adapter_audit_cli', _CLI)
A = importlib.util.module_from_spec(spec)
sys.modules['adapter_audit_cli'] = A
spec.loader.exec_module(A)


# --------------------------------------------------------------------------
# D1 -- the guard asymmetry. Empty typed side must NOT flag every S3 field.
# --------------------------------------------------------------------------

def test_d1_guard_holds_end_to_end(tmp_path, monkeypatch):
    """With an unresolvable raw type, cmd_audit must emit 0 findings, not print PASS,
    and return CANNOT-EVALUATE."""
    monkeypatch.setattr(A, '_find_adapter_source',
                        lambda n: (_WS / 'fake.ts', 'const x = await apiRequest<NopeType>(`/firm/d.json`)'))
    monkeypatch.setattr(A, '_import_corpus', lambda f: [])
    monkeypatch.setattr(A, '_fetch_s3_raw_fields',
                        lambda body, rt: ({'a': [], 'b': [], 'c': []}, A.OK, 's3://x/d.json', 'v1'))
    ns = argparse.Namespace(adapter_fn='fake', severity=None, manifest_dir=str(tmp_path))
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rc = A.cmd_audit(ns)
    out = buf.getvalue()
    assert rc == A.RC_CANNOT_EVALUATE
    assert 'TYPE_UNRESOLVED' in out
    assert '\nPASS:' not in out, 'an unaudited adapter must never print PASS'
    manifest = (tmp_path / 'fake.yaml').read_text()
    assert 'verified: false' in manifest
    assert 'total_findings: null' in manifest


def test_d1_MUTANT_unguarded_comparison_flags_every_s3_field():
    """NEGATIVE CONTROL. Drive the comparison with an empty typed side, exactly as the
    pre-fix code did. If this does NOT produce a finding per S3 field, the guard above
    is decoration and this test must fail loudly."""
    s3 = {'as_of_by_dim': [], 'firm_name': [], 'ytd': []}
    findings = A._audit_field_threading({}, s3, 'return raw', 'SomeType')
    drift = [f for f in findings if f['status'] == 'SCHEMA-DRIFT']
    assert len(drift) == len(s3), (
        'the unguarded comparison must flag EVERY S3 field -- if it does not, '
        'test_d1_guard_holds_end_to_end proves nothing'
    )


def test_d1_positive_control_real_drift_is_still_reported():
    """With BOTH sides populated, a genuinely drifted field MUST still be reported."""
    typed = {'kept': []}
    s3 = {'kept': [], 'drifted': []}
    findings = A._audit_field_threading(typed, s3, 'return raw', 'RealType')
    drift = [f['field'] for f in findings if f['status'] == 'SCHEMA-DRIFT']
    assert drift == ['drifted'], f'real drift must survive the guard, got {drift}'


# --------------------------------------------------------------------------
# guard (c) -- nested comparison against an UNRESOLVED named type
# --------------------------------------------------------------------------

# The body MUST actually thread `headline`, or the nested comparison is never reached
# and the guard test passes vacuously. (Caught by the mutant below on first run.)
_NESTED_BODY = ('const raw = await apiRequest<T>(`/firm/x.json`)\n'
                '  return { headline: raw.headline }')


def test_guard_c_unresolved_nested_type_emits_no_nested_drift():
    typed = {'headline': None}          # None == named type we could not resolve
    s3 = {'headline': ['aua', 'nna', 'ytd']}
    findings = A._audit_field_threading(typed, s3, _NESTED_BODY, 'T')
    assert not [f for f in findings if f['status'] == 'NOT-THREADED'], \
        'fixture must thread the field, else this test never reaches the nested branch'
    assert not [f for f in findings if f['status'] == 'NESTED-SCHEMA-DRIFT']


def test_guard_c_MUTANT_resolved_empty_nested_flags_everything():
    """NEGATIVE CONTROL: [] (resolved, genuinely empty) must still flag -- proving the
    None sentinel, not the emptiness, is what suppresses."""
    typed = {'headline': []}
    s3 = {'headline': ['aua', 'nna', 'ytd']}
    findings = A._audit_field_threading(typed, s3, _NESTED_BODY, 'T')
    nested = [f for f in findings if f['status'] == 'NESTED-SCHEMA-DRIFT']
    assert len(nested) == 3


# --------------------------------------------------------------------------
# D11 -- NO_S3_SOURCE is not FETCH_FAILED
# --------------------------------------------------------------------------

def test_d11_lambda_backed_adapter_is_not_applicable_not_failed():
    body = 'return await apiRequest<PlatinumClientSummary>(`/api/scoped/partners/x/platinum-summary`)'
    fields, status, uri, vintage = A._fetch_s3_raw_fields(body, 'PlatinumClientSummary')
    assert status == A.NO_S3_SOURCE
    assert fields == {} and uri == ''


def test_d11_no_s3_source_never_prints_fetch_failed(tmp_path, monkeypatch):
    monkeypatch.setattr(A, '_find_adapter_source',
                        lambda n: (_WS / 'f.ts', 'return await apiRequest<T>(`/api/scoped/x`)'))
    monkeypatch.setattr(A, '_import_corpus', lambda f: [])
    ns = argparse.Namespace(adapter_fn='f', severity=None, manifest_dir=str(tmp_path))
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rc = A.cmd_audit(ns)
    out = buf.getvalue()
    assert rc == A.RC_CANNOT_EVALUATE
    assert 'NOT-APPLICABLE' in out
    assert 'S3 fetch failed' not in out, 'must not claim a fetch that never happened'


# --------------------------------------------------------------------------
# D3 -- the raw type must not be a nested sub-fetch's type
# --------------------------------------------------------------------------

# Faithful to portal/src/api/endpoints/advisor-intelligence.ts:448-502 @ working-tree.
# The `...(accessToken && ...)` spread is load-bearing: it is the `'...' in body` limb of
# the pre-fix has_spread predicate. Omitting it made the D7 mutant vacuous on first run.
_FIRM_BODY = '''export async function getPlatinumFirmDashboard(firmOverride?: string) {
  const response = await fetch(url, {
    headers: {
      'Content-Type': 'application/json',
      ...(accessToken && { 'Authorization': `Bearer ${accessToken}` }),
    },
  })
  const stub = JSON.parse(text.replace(/\\bNaN\\b/g, 'null'))
  if (!stub.split) return stub as PlatinumFirmDashboard
  const [a, feeEfficiency] = await Promise.all([
    apiRequest<FeeEfficiencyResponse>(`${PLATINUM_BASE}/firm/fee_efficiency.json`),
  ])
  return { generated_at: stub.generated_at, headline: stub.headline, split: true }
}'''


def test_d3_prefers_return_cast_over_nested_apirequest():
    name, how = A._extract_raw_type_name(_FIRM_BODY)
    assert name == 'PlatinumFirmDashboard', f'took the nested sub-fetch type: {name}'
    assert 'return-cast' in how


def test_d3_MUTANT_first_apirequest_would_pick_the_wrong_type():
    """NEGATIVE CONTROL: the pre-fix rule (first apiRequest<T> anywhere) picks the
    nested Promise.all sub-fetch type. If this stops being true, D3's fix is untested."""
    import re
    legacy = re.search(r'apiRequest<(\w+)>', _FIRM_BODY).group(1)
    assert legacy == 'FeeEfficiencyResponse'
    assert legacy != A._extract_raw_type_name(_FIRM_BODY)[0]


def test_d3_multi_fetch_adapter_audits_the_primary_and_declares_the_rest_unaudited():
    """A merge adapter (getPlatinumClientDetailStatic: 4 apiRequest calls) must still be
    audited against its PRIMARY envelope. Refusing outright regressed a working audit."""
    body = ('const detail = await apiRequest<InflecClientDetailRaw>(`/clients/1/detail.json`)\n'
            '  const comp = await apiRequest<InflecClientCompositionRaw>(`/clients/1/composition.json`)')
    name, how = A._extract_raw_type_name(body)
    assert name == 'InflecClientDetailRaw'
    assert '1 sub-fetch type(s) NOT audited' in how, f'must disclose the un-audited fetches: {how}'


def test_d3_nested_subfetch_never_wins_over_the_primary():
    """The Promise.all sub-fetch must not be chosen when the adapter has its own fetch."""
    name, _ = A._extract_raw_type_name(_FIRM_BODY)
    assert name != 'FeeEfficiencyResponse'


# --------------------------------------------------------------------------
# D2 -- the finding text must name the type actually consulted
# --------------------------------------------------------------------------

def test_d2_finding_names_the_type_actually_consulted():
    findings = A._audit_field_threading({'kept': []}, {'kept': [], 'drifted': []},
                                        'return raw', 'InflecAdvisorBookRaw')
    drift = next(f for f in findings if f['status'] == 'SCHEMA-DRIFT')
    assert 'InflecAdvisorBookRaw' in drift['detail']
    assert 'Raw;' not in drift['detail'].replace('InflecAdvisorBookRaw', '')


def test_d2_MUTANT_concatenated_name_would_not_exist():
    """The pre-fix text said f'{adapter_name}Raw'. That symbol has 0 occurrences in the
    portal -- the message named a comparand never consulted."""
    fabricated = 'getPlatinumFirmDashboard' + 'Raw'
    hits = list((_WS / 'portal' / 'src').rglob('*.ts'))
    found = sum(fabricated in p.read_text(encoding='utf-8', errors='ignore') for p in hits)
    assert found == 0, f'{fabricated} unexpectedly exists; D2 premise changed'
    assert len(hits) > 50, 'retrieval control: the corpus must be non-empty'


# --------------------------------------------------------------------------
# D4 -- resolve interfaces across imported files, incl. `type X = Y` aliases
# --------------------------------------------------------------------------

def test_d4_resolves_interface_in_imported_file(tmp_path):
    types = tmp_path / 'types.ts'
    types.write_text('export interface Foo {\n  a: string\n  b: Bar\n}\nexport interface Bar {\n  z: number\n}\n')
    ep = tmp_path / 'ep.ts'
    ep.write_text("import { Foo } from './types'\nexport async function f() {}\n")
    corpus = A._import_corpus(ep)
    fields, where = A._resolve_type_fields(corpus, 'Foo')
    assert set(fields) == {'a', 'b'}
    assert fields['b'] == ['z'], 'nested named type must resolve one hop'
    assert where == types


def test_d4_follows_type_alias():
    corpus = [(Path('t.ts'), 'export interface Base {\n  q: string\n}\nexport type Alias = Base\n')]
    fields, _ = A._resolve_type_fields(corpus, 'Alias')
    assert set(fields) == {'q'}, 'PlatinumAdvisorSummaryRaw is exactly this alias shape'


def test_d4_MUTANT_single_file_search_finds_nothing():
    """NEGATIVE CONTROL: searching only the endpoints file (pre-fix) yields {}."""
    corpus = [(Path('ep.ts'), "import { Foo } from './types'\n")]
    fields, _ = A._resolve_type_fields(corpus, 'Foo')
    assert fields == {}


# --------------------------------------------------------------------------
# D7 / U2 -- has_spread must not be decided by a variable NAME
# --------------------------------------------------------------------------

def test_d7_conditional_passthrough_does_not_suppress_mapped_path_drops():
    threaded, passthrough, cond = A._threaded_fields(_FIRM_BODY, 'stub')
    assert passthrough is False, 'a conditional `if (!stub.split) return stub` is not a passthrough'
    assert cond is True
    assert 'ytd' not in threaded and 'firm_name' not in threaded


def test_d7_MUTANT_renaming_the_variable_does_not_change_the_verdict():
    """The pre-fix predicate was `'...' in body and 'raw' in body`. Renaming stub->raw
    flipped it and SUPPRESSED three true findings. The new predicate must be invariant
    under the identifier."""
    renamed = _FIRM_BODY.replace('stub', 'raw')
    a = A._threaded_fields(_FIRM_BODY, 'stub')
    b = A._threaded_fields(renamed, 'raw')
    assert a == b, 'threading verdict must not depend on the raw variable name'

    legacy_stub = ('...' in _FIRM_BODY) and ('raw' in _FIRM_BODY)
    legacy_raw = ('...' in renamed) and ('raw' in renamed)
    assert legacy_stub != legacy_raw, 'pre-fix predicate was name-dependent (premise check)'


def test_d7_unconditional_passthrough_suppresses_not_threaded():
    body = 'const raw = await apiRequest<T>(`/firm/x.json`)\n  return raw\n'
    findings = A._audit_field_threading({'a': []}, {'a': [], 'b': []}, body, 'T')
    assert not [f for f in findings if f['status'] == 'NOT-THREADED']


# --------------------------------------------------------------------------
# D5 / D6 -- the manifest and the success token
# --------------------------------------------------------------------------

def test_d6_warns_must_not_print_pass(tmp_path, monkeypatch):
    monkeypatch.setattr(A, '_find_adapter_source', lambda n: (_WS / 'f.ts', 'const raw = await apiRequest<T>(`/firm/x.json`)\n  return { a: raw.a }'))
    monkeypatch.setattr(A, '_import_corpus', lambda f: [(Path('t.ts'), 'interface T {\n  a: string\n}\n')])
    monkeypatch.setattr(A, '_fetch_s3_raw_fields', lambda b, rt: ({'a': [], 'zz': []}, A.OK, 's3://x', 'v'))
    ns = argparse.Namespace(adapter_fn='f', severity=None, manifest_dir=str(tmp_path))
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rc = A.cmd_audit(ns)
    out = buf.getvalue()
    assert '\nWARN: comp-adapter-audit complete' in out
    assert '\nPASS:' not in out
    assert rc == A.RC_OK, 'WARNs alone do not fail the run (gate contract)'


def test_d6_clean_adapter_still_passes_and_exits_zero(tmp_path, monkeypatch):
    monkeypatch.setattr(A, '_find_adapter_source', lambda n: (_WS / 'f.ts', 'const raw = await apiRequest<T>(`/firm/x.json`)\n  return raw'))
    monkeypatch.setattr(A, '_import_corpus', lambda f: [(Path('t.ts'), 'interface T {\n  a: string\n}\n')])
    monkeypatch.setattr(A, '_fetch_s3_raw_fields', lambda b, rt: ({'a': []}, A.OK, 's3://x', 'v'))
    ns = argparse.Namespace(adapter_fn='f', severity=None, manifest_dir=str(tmp_path))
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rc = A.cmd_audit(ns)
    assert rc == A.RC_OK
    assert '\nPASS: comp-adapter-audit complete -- 0 WARN(s)' in buf.getvalue()


def test_d5_unverified_manifest_cannot_be_mistaken_for_a_clean_audit(tmp_path):
    p = A._write_manifest(tmp_path, 'x', Path('a.ts'), '', None, A.NO_S3_SOURCE,
                          'no static artifact', '', '', {}, {}, [])
    text = p.read_text()
    assert 'verified: false' in text
    assert 'verification_status: NO_S3_SOURCE' in text
    assert 'total_findings: null' in text
    assert 'total_findings: 0' not in text, 'a zero-finding UNVERIFIED run must not read as clean'


def test_d12_manifest_records_the_artifact_vintage(tmp_path):
    p = A._write_manifest(tmp_path, 'x', Path('a.ts'), 'T', Path('t.ts'), A.OK, '',
                          's3://b/k.json', '2026-07-10T14:53:35Z', {'a': []}, {'a': []}, [])
    text = p.read_text()
    assert 's3_artifact_vintage: 2026-07-10T14:53:35Z' in text
    assert 's3_uri: s3://b/k.json' in text


# --------------------------------------------------------------------------
# The D-1 gate contract. The manifest is load-bearing; do not make it opt-in.
# --------------------------------------------------------------------------

def _gate():
    spec_g = importlib.util.spec_from_file_location(
        'd1gate', _WS / '.tools' / 'portal-hooks' / 'd1_adapter_threading_gate.py')
    g = importlib.util.module_from_spec(spec_g)
    spec_g.loader.exec_module(g)
    return g


def test_gate_still_parses_the_new_manifest_shape(tmp_path):
    """The new top-level keys must not leak into the gate's `status:` scan."""
    g = _gate()
    g._AUDIT_MANIFEST_DIR = tmp_path
    A._write_manifest(tmp_path, 'x', Path('a.ts'), 'T', Path('t.ts'), A.OK, '', 's3://b/k', 'v',
                      {'a': []}, {'a': [], 'b': []},
                      [{'field': 'b', 'status': 'SCHEMA-DRIFT', 'severity': 'WARN', 'detail': 'd'}])
    assert g._parse_manifest('x') == ['SCHEMA-DRIFT'], 'verification_status must not be read as a finding'


@pytest.mark.xfail(reason='FAIL-OPEN: the D-1 gate returns PASS for an unverified audit. '
                          'Blocking-behavior change is arch-gated to CTO (LD-0273 precedent).',
                   strict=True)
def test_gate_must_not_pass_an_unverified_audit(tmp_path):
    """EXERCISED 2026-07-10: an adapter that was never audited yields the same gate
    verdict as a clean one. The CLI alone cannot close this -- the gate's PASS means
    'no findings', and an unverified run has none. This xfail is the standing record."""
    g = _gate()
    g._AUDIT_MANIFEST_DIR = tmp_path
    A._write_manifest(tmp_path, 'x', Path('a.ts'), '', None, A.FETCH_FAILED, 'creds', '', '', {}, {}, [])
    verdict, _ = g._verdict_for_adapter(g._parse_manifest('x'), partner_facing=True)
    assert verdict != 'PASS', 'an unverified audit must never render a PASS gate verdict'
