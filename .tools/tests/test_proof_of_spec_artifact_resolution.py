"""Controls for proof-of-spec-check's ARTIFACT ROW RESOLUTION arm (2026-08-30, 1.0.0_SA_CTO~X on
2.0.0_SA_COO~X 85753). Baseline FIRST on a real committed instance (a battery from a failing base
means nothing), then one mutant per branch the arm refuses, and one control per branch it must NOT
refuse (s3_object rows; a commit not in the local store is ANNOUNCED, not asserted).
"""
import copy
import importlib.util
import json
import pathlib

_SRC = pathlib.Path(__file__).resolve().parent.parent / "proof-of-spec-check.py"
_spec = importlib.util.spec_from_file_location("posc", _SRC)
posc = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(posc)

ROOT = _SRC.parent.parent
INSTANCE = ROOT / "org/tier2_senior/0.7.0_AE_CloudOps/deliverables/NFRA_C3MATERIALIZE.TO-L3W3-COX_PROOF_OF_SPEC.json"


def _inst():
    return json.loads(INSTANCE.read_text(encoding="utf-8"))


def _fires(inst):
    v, _ = posc.artifact_resolution_check(inst)
    return [x for x in v if x.startswith("artifact-resolution:")]


def test_real_instance_is_clean_baseline():
    inst = _inst()
    v, frames = posc.artifact_resolution_check(inst)
    assert v == [], v
    assert frames and "denominator" in frames[0]


def test_dead_path_at_a_real_pin_fires():
    inst = _inst()
    m = copy.deepcopy(inst)
    row = next(r for r in m["artifacts_produced"] if r["commit_or_etag"] != posc.PENDING_SENTINEL)
    row["path_or_key"] = "org/tier2_senior/0.7.0_AE_CloudOps/deliverables/DOES_NOT_EXIST_anywhere.json"
    assert any("does NOT exist at its declared pin" in x for x in _fires(m)), _fires(m)


def test_pending_row_with_dead_worktree_path_fires():
    inst = _inst()
    m = copy.deepcopy(inst)
    m["artifacts_produced"].append({"path_or_key": "org/tier2_senior/0.7.0_AE_CloudOps/deliverables/NOPE.py",
                                    "commit_or_etag": posc.PENDING_SENTINEL, "kind": "script",
                                    "deployed_state": "not-deployed", "deploy_evidence": "n/a"})
    assert any("PENDING-THIS-COMMIT but does NOT exist" in x for x in _fires(m)), _fires(m)


def test_s3_object_row_is_skipped_not_refused():
    inst = _inst()
    m = copy.deepcopy(inst)
    m["artifacts_produced"].append({"path_or_key": "s3://opal-data-bd/code/scripts/gold/x.py",
                                    "commit_or_etag": "3c2b659b5317e735c7e11d134c1e1f5d", "kind": "s3_object",
                                    "deployed_state": "deployed", "deploy_evidence": "head-object"})
    v, frames = posc.artifact_resolution_check(m)
    assert v == [], v
    assert "1 s3_object" in frames[0]


def test_commit_not_in_local_store_is_announced_not_asserted():
    inst = _inst()
    m = copy.deepcopy(inst)
    m["artifacts_produced"].append({"path_or_key": "org/whatever.py", "commit_or_etag": "0123456789abcdef0123",
                                    "kind": "script", "deployed_state": "not-deployed", "deploy_evidence": "n/a"})
    v, frames = posc.artifact_resolution_check(m)
    assert v == [], v
    assert "1 UNRESOLVED-HERE" in frames[0]
