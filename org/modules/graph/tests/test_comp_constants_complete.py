"""Bundle item 7 -- enumeration-completeness axis (NFRA_PSTMRT; design @d5ed44e2e).

Controls per the pinned design + ~Z s.2.5: synthetic firm N+1 (isolated positive
control), PHANTOM negative control, the SCOPE-FILTER lock (CTO's live mockadv
false-FAIL as a named case), exemption lifecycle, fail-closed registry, and the
polyglot key extraction with the item-2 comment-stripping control (a commented-out
firm is NOT present).
"""
from __future__ import annotations

import datetime as dt
import json
import sys
from pathlib import Path

WS = Path(__file__).resolve().parents[4]
if str(WS) not in sys.path:
    sys.path.insert(0, str(WS))

import pytest  # noqa: E402

from org.modules.graph.comp_constants_complete import (  # noqa: E402
    RegistryRefusal,
    check_completeness,
    expected_for_scope,
    load_registry,
    members_from_js_site,
    members_from_python_value,
    token_map,
)


class _Site:
    def __init__(self, file, line, value):
        self.file, self.line, self.value = file, line, value


def _registry(tmp_path, firms):
    p = tmp_path / "firm_registry.json"
    p.write_text(json.dumps({"firms": firms}), encoding="utf-8")
    return p


FIRMS = [
    {"firm_id": "49financial", "tree_token": "bd", "aliases": ["49f", "blackdiamond"],
     "enabled": True, "scopes": {"portal": True, "mdpf": True, "pipeline": True}},
    {"firm_id": "inflection", "tree_token": "inf", "aliases": [],
     "enabled": True, "scopes": {"portal": True, "mdpf": True, "pipeline": True}},
    {"firm_id": "cottonwood", "tree_token": "cot", "aliases": [],
     "enabled": True, "scopes": {"portal": True, "mdpf": True, "pipeline": True}},
    # the mockadv shape: PORTAL-ONLY. Asserting it into mdpf is the BL-1 death.
    {"firm_id": "mockadv", "tree_token": "mockadv", "aliases": [],
     "enabled": True, "scopes": {"portal": True, "mdpf": False, "pipeline": False}},
]


def _cfg(scope="mdpf", exemptions=None, sites=None):
    fk = {"complete_over": scope}
    if exemptions:
        fk["exemptions"] = exemptions
    if sites:
        fk["sites"] = sites
    return {"constants": [{"name": "FIRM_MAP", "lane": "multifirm", "firm_keyed": fk}]}


def _run(tmp_path, cfg, py_value=None, today=None):
    reg = load_registry(_registry(tmp_path, FIRMS))
    scanned = {}
    if py_value is not None:
        scanned[("FIRM_MAP", "multifirm")] = [_Site("x/y.py", 1, py_value)]
    return check_completeness(cfg, reg, scanned, tmp_path, today=today)


# ------------------------------------------------------------ the axis itself
def test_complete_set_passes_with_denominator():
    import tempfile
    with tempfile.TemporaryDirectory() as td:
        res = _run(Path(td), _cfg("mdpf"), py_value=repr({"bd": 1, "inf": 2, "cot": 3}))
    assert res["rc"] == 0
    assert any(f["verdict"] == "COMPLETE" for f in res["findings"])
    assert "registry vintage" in res["denominator"]


def test_uniformly_missing_firm_FAILS(tmp_path):
    # THE defect class: zero drift, one firm absent. Must fail, naming the firm.
    res = _run(tmp_path, _cfg("mdpf"), py_value=repr({"bd": 1, "inf": 2}))
    assert res["rc"] == 1
    inc = [f for f in res["findings"] if f["verdict"] == "INCOMPLETE"]
    assert inc and "cottonwood" in inc[0]["detail"]


def test_scope_filter_excludes_portal_only_firm_from_mdpf(tmp_path):
    # CTO's live mockadv false-FAIL, locked: mdpf-scope assertion must NOT expect
    # mockadv. Deleting the scope filter turns this red (the named mutant).
    assert "mockadv" not in expected_for_scope(FIRMS, "mdpf")
    res = _run(tmp_path, _cfg("mdpf"), py_value=repr({"bd": 1, "inf": 2, "cot": 3}))
    assert res["rc"] == 0, "portal-only firm false-fired an mdpf assertion"
    assert "mockadv" in expected_for_scope(FIRMS, "portal")


def test_phantom_unregistered_token_FAILS(tmp_path):
    res = _run(tmp_path, _cfg("mdpf"),
               py_value=repr({"bd": 1, "inf": 2, "cot": 3, "zzfirm": 4}))
    assert res["rc"] == 1
    ph = [f for f in res["findings"] if f["verdict"] == "PHANTOM"]
    assert ph and "zzfirm" in ph[0]["detail"]


def test_synthetic_firm_n_plus_1_control(tmp_path):
    # s.2.5 positive control, ISOLATED: registry grows a firm; every structure not
    # yet handling it must read INCOMPLETE naming it. Proves the gate CAN fire.
    firms = FIRMS + [{"firm_id": "synthfirm", "tree_token": "syn", "aliases": [],
                      "enabled": True,
                      "scopes": {"portal": True, "mdpf": True, "pipeline": True}}]
    reg = load_registry(_registry(tmp_path, firms))
    res = check_completeness(_cfg("mdpf"), reg,
                             {("FIRM_MAP", "multifirm"):
                              [_Site("x/y.py", 1, repr({"bd": 1, "inf": 2, "cot": 3}))]},
                             tmp_path)
    assert res["rc"] == 1
    assert any("synthfirm" in f["detail"] for f in res["findings"]
               if f["verdict"] == "INCOMPLETE")


def test_alias_tokens_resolve(tmp_path):
    # blackdiamond + 49f are the SAME firm via aliases[] -- the one vocabulary.
    res = _run(tmp_path, _cfg("mdpf"),
               py_value=repr({"blackdiamond": 1, "inf": 2, "cot": 3}))
    assert res["rc"] == 0
    assert token_map(FIRMS)["49f"] == "49financial"


# ------------------------------------------------------------ exemption lifecycle
def test_valid_exemption_passes_and_says_so(tmp_path):
    ex = [{"firm": "cottonwood", "by": "0.8.0_AE_CloudComp", "date": "2026-07-22",
           "why": "test", "expires": "2027-01-01"}]
    res = _run(tmp_path, _cfg("mdpf", exemptions=ex),
               py_value=repr({"bd": 1, "inf": 2}), today=dt.date(2026, 7, 23))
    assert res["rc"] == 0
    assert any(f["verdict"] == "EXEMPT" for f in res["findings"])


def test_expired_exemption_FAILS(tmp_path):
    ex = [{"firm": "cottonwood", "by": "x", "date": "2026-01-01",
           "why": "old", "expires": "2026-06-01"}]
    res = _run(tmp_path, _cfg("mdpf", exemptions=ex),
               py_value=repr({"bd": 1, "inf": 2}), today=dt.date(2026, 7, 23))
    assert res["rc"] == 1
    assert any(f["verdict"] == "EXEMPT-EXPIRED" for f in res["findings"])


# ------------------------------------------------------------ fail-closed + honesty
def test_absent_registry_REFUSES(tmp_path):
    with pytest.raises(RegistryRefusal):
        load_registry(tmp_path / "nope.json")


def test_unparseable_registry_REFUSES(tmp_path):
    p = tmp_path / "firm_registry.json"
    p.write_text("{not json", encoding="utf-8")
    with pytest.raises(RegistryRefusal):
        load_registry(p)


def test_declared_but_no_site_is_UNPARSEABLE_not_clean(tmp_path):
    res = _run(tmp_path, _cfg("mdpf"), py_value=None)
    assert res["rc"] == 1
    assert any(f["verdict"] == "UNPARSEABLE-SITE" for f in res["findings"])


def test_scalar_python_value_is_unreadable_not_empty():
    assert members_from_python_value("'just-a-string'") is None
    assert members_from_python_value("{'a': 1}") == {"a"}
    assert members_from_python_value("['a', 'b']") == {"a", "b"}


# ------------------------------------------------------------ polyglot half (A)
def test_js_key_extraction_with_commented_firm_not_present(tmp_path):
    # The item-2 control applied on day one: a commented-out firm entry is NOT a
    # member. Nested objects do not leak depth-2 keys.
    mjs = tmp_path / "firm-config.mjs"
    mjs.write_text(
        "// header comment mentions phantomfirm: 1\n"
        "export const FIRM_MAP = {\n"
        "  bd: { bucket: 'opal-data-bd', nestedKey: 1 },\n"
        "  'inf': { bucket: 'opal-data-inf' },\n"
        "  // cot: { bucket: 'opal-data-cot' },\n"
        "  \"cot\": { bucket: 'opal-data-cot' },\n"
        "};\n"
        "const OTHER = { unrelated: true };\n",
        encoding="utf-8",
    )
    keys = members_from_js_site(mjs, "FIRM_MAP")
    assert keys == {"bd", "inf", "cot"}, keys
    assert "nestedKey" not in keys and "bucket" not in keys


def test_js_object_freeze_wrapper_is_transparent(tmp_path):
    # The LIVE idiom at the acceptance target (firm-config.mjs:29).
    mjs = tmp_path / "f.mjs"
    mjs.write_text(
        "export const FIRM_MAP = Object.freeze({\n"
        "  '49financial': { bucket: 'opal-data-bd' },\n"
        "  inflection: { bucket: 'opal-data-inf' },\n"
        "});\n",
        encoding="utf-8",
    )
    assert members_from_js_site(mjs, "FIRM_MAP") == {"49financial", "inflection"}


def test_js_site_missing_const_is_None_not_empty(tmp_path):
    mjs = tmp_path / "x.mjs"
    mjs.write_text("export const OTHER = { a: 1 };\n", encoding="utf-8")
    assert members_from_js_site(mjs, "FIRM_MAP") is None


def test_js_site_wired_through_check(tmp_path):
    mjs = tmp_path / "firm-config.mjs"
    mjs.write_text("export const FIRM_MAP = { bd: 1, inf: 1 };\n", encoding="utf-8")
    res = check_completeness(_cfg("mdpf", sites=["firm-config.mjs"]),
                             load_registry(_registry(tmp_path, FIRMS)),
                             {}, tmp_path)
    assert res["rc"] == 1
    assert any(f["verdict"] == "INCOMPLETE" and "cottonwood" in f["detail"]
               for f in res["findings"])
