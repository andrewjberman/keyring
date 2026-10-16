"""NFRA_OPLGTW OG-ng-2 (round 37, XA-20261016T034740Z-28da, ruled (a)): the commit-time naming gate grades a name that has a
name_rulings.json row from that row, through naming-apply-gate.py's ruling_amend (imported, never copied).

IN PROCESS, READ-ONLY. The gate module is loaded from .tools/naming-gate.py by its own path. The rulings are injected into the
gate's _RULINGS cache for each case, so the registry file is never written; the unreadable-file case replaces the rootcheck reader.
"""
import importlib.machinery
import importlib.util
import os

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
GATE = os.path.join(ROOT, ".tools", "naming-gate.py")
NAME = "bd_account_id"  # a hand-kept carrier of 'bd' outside every permitted context: REFUSE with no row
PATH = "infra/aws/ec2/opal-gateway/app/selftest_planted_client.py"
CARRIER = "hand-kept carrier"


@pytest.fixture(scope="module")
def gate():
    loader = importlib.machinery.SourceFileLoader("naming_gate_rulings_under_test", GATE)
    spec = importlib.util.spec_from_loader(loader.name, loader)
    mod = importlib.util.module_from_spec(spec)
    loader.exec_module(mod)
    return mod


@pytest.fixture
def nm(gate):
    return gate.Naming(gate.load_opal())


@pytest.fixture(autouse=True)
def _clean_rulings(gate):
    gate._RULINGS.clear()
    gate._RULINGS["rows"] = {}
    yield
    gate._RULINGS.clear()
    gate._RULINGS["rows"] = {}


def _row(**kw):
    base = {"name": NAME, "type": CARRIER}
    base.update(kw)
    return base


def _judge(gate, nm, rows):
    gate._RULINGS.clear()
    gate._RULINGS["rows"] = rows
    return gate.judge(nm, PATH, gate.Lit(NAME, NAME, 1, None), None)


def test_none_owed_row_admits_the_planted_carrier(gate, nm):
    got = _judge(gate, nm, {(NAME, CARRIER): _row(none_owed="planted: no name is owed")})
    assert got[0] == "RULED" and got[3] == "PASS"
    assert "name_rulings.json" in got[2]


def test_no_row_keeps_the_refuse(gate, nm):
    got = _judge(gate, nm, {})
    assert got[0] == "REFUSE" and got[3] == "REFUSE"


def test_same_string_under_another_type_is_not_admitted(gate, nm):
    got = _judge(gate, nm, {(NAME, "INSTANCE_PROFILE"): _row(type="INSTANCE_PROFILE", none_owed="planted")})
    assert got[0] == "REFUSE" and got[3] == "REFUSE"


def test_canonical_equal_to_the_name_is_ruled(gate, nm):
    got = _judge(gate, nm, {(NAME, CARRIER): _row(canonical=NAME)})
    assert got[0] == "RULED" and got[3] == "PASS"


def test_canonical_different_keeps_the_refuse_and_names_the_canonical(gate, nm):
    got = _judge(gate, nm, {(NAME, CARRIER): _row(canonical="bd-other-name")})
    assert got[0] == "REFUSE" and got[3] == "REFUSE"
    assert got[1] == "bd-other-name"
    assert "NEW hand-kept carrier" in got[2] and "bd-other-name" in got[2]


def test_unreadable_registry_is_noticed_and_grades_as_today(gate, nm, monkeypatch):
    class _Broken(object):
        @staticmethod
        def load_name_rulings(path=None):
            raise ValueError("planted unreadable registry")

    monkeypatch.setattr(gate, "_rootcheck", lambda: _Broken)
    gate._RULINGS.clear()
    got = gate.judge(nm, PATH, gate.Lit(NAME, NAME, 1, None), None)
    assert got[0] == "REFUSE" and got[3] == "REFUSE"
    line = gate._rulings_notice_line()
    assert line is not None
    assert line.startswith("NAMING RULINGS-NOTICE name_rulings.json could not be read (")
    assert line.endswith("); no name is graded from a row")


# NFRA_OPLGTW OG-rr-2 (CTO ruling @8b9adcbd8d section 3 cell 2): the ruling_ref refusals, on planted dicts only. The registry file is
# never read or written here; the resolving ref is the registry file at HEAD, the unresolving ref a path HEAD does not hold.
RULING_KEY = (NAME, CARRIER)


def _head_commit(gate):
    import subprocess
    p = subprocess.run(["git", "rev-parse", "--verify", "-q", "HEAD^{commit}"], cwd=ROOT, capture_output=True)
    return p.stdout.decode("ascii", "replace").strip()


def test_ruling_ref_unresolved_is_refused(gate):
    bad = "infra/logic/registry/planted_absent_selftest.json@%s" % _head_commit(gate)
    got = gate.ruling_ref_refusals({RULING_KEY: _row(canonical=NAME, ruling_ref=bad)}, {})
    assert len(got) == 1 and got[0][1] == "(a)" and got[0][0] == RULING_KEY


def test_ruling_ref_resolved_is_admitted(gate):
    good = "%s@%s" % (gate.RULINGS_REL, _head_commit(gate))
    assert gate.ruling_ref_refusals({RULING_KEY: _row(canonical=NAME, ruling_ref=good)}, {}) == []


def test_new_row_without_ruling_ref_is_refused(gate):
    got = gate.ruling_ref_refusals({RULING_KEY: _row(canonical=NAME)}, {})
    assert len(got) == 1 and got[0][1] == "(b)"


def test_legacy_row_without_ruling_ref_is_not_refused(gate):
    row = _row(canonical=NAME)
    assert gate.ruling_ref_refusals({RULING_KEY: row}, {RULING_KEY: dict(row)}) == []
