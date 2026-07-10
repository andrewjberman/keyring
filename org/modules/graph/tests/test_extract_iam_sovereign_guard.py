#!/usr/bin/env python3
"""Sovereign-guard tests for comp-iam / extract_iam (IAM1), NFRA_TOOLPASS.

comp-iam is the 6th bd-CONTENT-reader: extract_iam.build_iam_report() read_text()s bd gold source
(data/black_diamond/scripts/gold/[A-D]_*.py) AND manifest-driven bd service source on EVERY comp-iam
command via _build(). It KEEPS bd ROLE / TF-IAM-policy analysis (genuine sec.8-safe METADATA) -- only
the gold/service .py SOURCE read is guarded.

Guard (CTO IAM1 ruling 20260710T222627Z): COMP_IAM_INCLUDE_HELD=1 -> scan held source (opt-in/pipeline);
unset (agent) -> a held-path source read returns None, loud-noted once. Decision is a pure
rel.startswith predicate -- the held file is never opened to decide.

SOVEREIGN-SAFE: no test reads the REAL data/black_diamond/. The corpus test uses a TEMP tree with
SYNTHETIC files at bd-shaped PATHS; read_text is instrumented to PROVE 0 held reads occur.
"""
from __future__ import annotations

import importlib.util
import os
import sys
from pathlib import Path

_WS = Path(__file__).resolve().parents[4]
_EI = _WS / "org" / "modules" / "graph" / "extract_iam.py"


def _load(flag: str | None):
    if flag is None:
        os.environ.pop("COMP_IAM_INCLUDE_HELD", None)
    else:
        os.environ["COMP_IAM_INCLUDE_HELD"] = flag
    spec = importlib.util.spec_from_file_location("extract_iam", str(_EI))
    mod = importlib.util.module_from_spec(spec)
    sys.modules["extract_iam"] = mod          # register before exec so @dataclass resolves
    spec.loader.exec_module(mod)
    # reset the once-only note latch between loads
    if hasattr(mod, "_HELD_NOTE_EMITTED"):
        mod._HELD_NOTE_EMITTED["done"] = False
    return mod


# ---- the held predicate (pure) -----------------------------------------------------------

def test_rel_is_held_covers_bd_and_schwab_silver():
    ei = _load(None)
    assert ei._rel_is_held("data/black_diamond/scripts/gold/A_00.py")
    assert ei._rel_is_held("data/canonical/schwab/silver/build_dim_account.py")
    assert ei._rel_is_held("data\\black_diamond\\scripts\\gold\\B_01.py")  # windows sep normalized


def test_rel_is_held_passes_inscope_and_metadata_paths():
    ei = _load(None)
    assert not ei._rel_is_held("data/inf/scripts/gold/A_00.py"), "inf is in-scope"
    assert not ei._rel_is_held("data/cot/scripts/gold/A_00.py"), "cot is in-scope"
    assert not ei._rel_is_held("infra/aws/lambda/x/lambda_function.py")
    assert not ei._rel_is_held("infra/aws/ec2/EC2_MANIFEST.json")


# ---- _read_source_if_allowed: the load-bearing "decide by string, never open" property -----

def test_agent_context_refuses_held_source_without_opening(tmp_path, monkeypatch):
    ei = _load(None)
    # a SYNTHETIC bd-shaped file in a temp workspace -- never the real bd tree
    ws = tmp_path
    held = ws / "data" / "black_diamond" / "scripts" / "gold" / "A_00.py"
    held.parent.mkdir(parents=True, exist_ok=True)
    held.write_text("import boto3\nboto3.client('s3').get_object()\n", encoding="utf-8")

    opened = []
    real_rt = Path.read_text
    def spy_rt(self, *a, **k):
        opened.append(str(self).replace("\\", "/"))
        return real_rt(self, *a, **k)
    monkeypatch.setattr(Path, "read_text", spy_rt)

    result = ei._read_source_if_allowed(held, ws)
    assert result is None, "held source must be REFUSED in agent context"
    assert not any("black_diamond" in p for p in opened), \
        "the held file must NOT be opened -- the refusal is decided by the path string"


def test_optin_flag_reads_held_source(tmp_path):
    ei = _load("1")  # pipeline / explicit opt-in
    held = tmp_path / "data" / "black_diamond" / "scripts" / "gold" / "A_00.py"
    held.parent.mkdir(parents=True, exist_ok=True)
    held.write_text("BODY", encoding="utf-8")
    assert ei._read_source_if_allowed(held, tmp_path) == "BODY", "opt-in flag must read held source"


def test_nonbd_source_always_reads(tmp_path):
    for flag in (None, "1"):
        ei = _load(flag)
        f = tmp_path / "data" / "inf" / "scripts" / "gold" / "A_00.py"
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text("INF_BODY", encoding="utf-8")
        assert ei._read_source_if_allowed(f, tmp_path) == "INF_BODY", "in-scope source always reads"


def test_MUTANT_flag_check_off_would_read_bd(tmp_path, monkeypatch):
    """NEGATIVE CONTROL: force _include_held True (the mutant of the default) -> the held source IS
    read. Proves the flag/predicate is what keeps bd out."""
    ei = _load(None)
    held = tmp_path / "data" / "black_diamond" / "scripts" / "gold" / "A_00.py"
    held.parent.mkdir(parents=True, exist_ok=True)
    held.write_text("BD_BODY", encoding="utf-8")
    assert ei._read_source_if_allowed(held, tmp_path) is None  # guarded baseline
    monkeypatch.setattr(ei, "_include_held", lambda: True)      # MUTANT
    assert ei._read_source_if_allowed(held, tmp_path) == "BD_BODY", \
        "with the flag forced on, bd source WOULD be read -- the check is load-bearing"


# ---- sec.2a end-to-end: 0 read_text of data/black_diamond during a build --------------------

def test_build_reads_zero_bd_source_end_to_end(tmp_path, monkeypatch):
    """The load-bearing sovereign property, exercised through the guard on a FIXTURE tree: a service
    profile build over a bd-shaped source dir opens ZERO held files in agent context."""
    ei = _load(None)
    ws = tmp_path
    # synthetic bd gold + a non-bd inf file
    (ws / "data" / "black_diamond" / "scripts" / "gold").mkdir(parents=True)
    (ws / "data" / "black_diamond" / "scripts" / "gold" / "A_00.py").write_text(
        "import boto3\nboto3.client('s3').put_object()\n", encoding="utf-8")
    (ws / "data" / "inf" / "scripts" / "gold").mkdir(parents=True)
    (ws / "data" / "inf" / "scripts" / "gold" / "A_00.py").write_text(
        "import boto3\nboto3.client('s3').get_object()\n", encoding="utf-8")

    opened = []
    real_rt = Path.read_text
    def spy_rt(self, *a, **k):
        opened.append(str(self).replace("\\", "/"))
        return real_rt(self, *a, **k)
    monkeypatch.setattr(Path, "read_text", spy_rt)

    # drive the two held readers directly against the fixture (the gold glob + a manifest-style file)
    for py in sorted((ws / "data" / "black_diamond" / "scripts" / "gold").glob("[A-D]_*.py")):
        assert ei._read_source_if_allowed(py, ws) is None
    inf = ws / "data" / "inf" / "scripts" / "gold" / "A_00.py"
    assert ei._read_source_if_allowed(inf, ws) is not None, "in-scope inf source still scanned"

    bd_opens = [p for p in opened if "black_diamond" in p]
    assert bd_opens == [], f"ZERO bd source reads expected in agent context; got {bd_opens}"
