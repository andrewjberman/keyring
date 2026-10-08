"""A deploy ships only the files its own ledger names (1.0.0_SA_CTO msg 107147, dell1 rows MDPF_SECCLASS-D1-S12/S13).

Reproduces the 2026-10-08 re-ship: a one-file BD gold deploy (C_06) used to upload every declared lib/_shared
shipped artifact at its CURRENT repo bytes, which released etf_classification_scheduled.py ahead of its own
ledger three times. Pure functions only -- nothing here touches git, S3 or the network.

Run: python -m pytest .tools/test_safe_deploy_named_only.py -q
"""
from __future__ import annotations

import sys
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
sys.path.insert(0, str(TOOLS))
import safe_deploy_core as sdc  # noqa: E402

C06 = "data/black_diamond/scripts/gold/C_06.client_mix_timeseries.py"
SCHED = "infra/aws/lambda/v2_portal/_shared/etf_classification_scheduled.py"
CLIENT = "infra/aws/lambda/v2_portal/_shared/etf_classifications_dynamodb.py"
ARTIFACTS = sdc.CODE_TREES["black_diamond"]["shipped_artifacts"]["gold"]["members"]
COT_A00 = "data/cot/scripts/gold/A_00.accounts_dimension.py"
_BD = sdc.CODE_TREES["black_diamond"]
# the other firm tree that declares the same shipped artifacts (found, never named: the naming gate)
_COT = next(t for t in sdc.CODE_TREES.values() if t is not _BD and t.get("shipped_artifacts"))
BD_BUCKET, COT_BUCKET = _BD["bucket"], _COT["bucket"]
# expected key derived from the registry, never typed: <layer prefix> + <dest_subdir> + <basename>
KEY = _BD["layers"]["gold"][1] + _BD["shipped_artifacts"]["gold"]["dest_subdir"] + SCHED.rsplit("/", 1)[-1]


def _paths(rows):
    return [r[0] for r in rows]


def test_one_file_gold_deploy_ships_no_unnamed_artifact():
    """THE REPRODUCTION. Old code: 3 artifacts rode along with C_06. Now: none."""
    assert sdc.file_to_s3_target(C06) is not None, "C_06 must be a deploy-scope bd gold file"
    assert sdc.shipped_artifacts_for([C06]) == []


def test_upload_plan_of_one_file_is_that_file_only():
    plan = sdc.upload_plan([C06])
    assert _paths(plan) == [C06]
    assert plan[0][1] == BD_BUCKET


def test_unnamed_artifacts_are_reported_not_shipped():
    assert sdc.unnamed_artifacts_for([C06], [C06]) == list(ARTIFACTS)


def test_an_artifact_named_alone_ships_to_every_declaring_layer():
    """The artifact's OWN deploy (no script named): ships to each layer that declares it, each target listed."""
    rows = sdc.shipped_artifacts_for([SCHED])
    assert rows == [(SCHED, BD_BUCKET, KEY), (SCHED, COT_BUCKET, KEY)]


def test_bd_deploy_naming_the_artifact_never_ships_it_to_cot():
    """Cross-firm: a BD gold script + the artifact ships the artifact to BD only."""
    rows = sdc.shipped_artifacts_for([C06, SCHED])
    assert rows == [(SCHED, BD_BUCKET, KEY)]


def test_cot_deploy_naming_the_artifact_ships_it_to_cot_only():
    assert sdc.file_to_s3_target(COT_A00) is not None
    assert sdc.shipped_artifacts_for([COT_A00, SCHED]) == [(SCHED, COT_BUCKET, KEY)]


def test_named_artifact_ships_alone_not_its_siblings():
    rows = sdc.shipped_artifacts_for([C06, SCHED])
    assert _paths(rows) == [SCHED]
    assert sdc.unnamed_artifacts_for([C06], [C06, SCHED]) == [m for m in ARTIFACTS if m != SCHED]


def test_windows_separators_are_named_too():
    assert _paths(sdc.shipped_artifacts_for([C06, CLIENT.replace("/", "\\")])) == [CLIENT]


def test_a_commit_range_that_changed_the_artifact_names_it():
    """Pre-push mode names what the range changed: an artifact changed in the range ships."""
    assert _paths(sdc.shipped_artifacts_for([C06, SCHED, "README.md"])) == [SCHED]
