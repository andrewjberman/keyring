# ADVI_FIRMBKTS task order -- `FB-e-7` -- THE COT PRICE BUILDER TOLERATES ABSENT TIER-2 INPUTS (row S11)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R2.md</decomp_doc>
<owned_cells>FB-e-7</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_FIRMBKTS~10</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, rule, schedule or cadence is added or changed; the optional S_00 SSM step of the original patch is NOT part of this cell.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change and no AWS act; the test stubs S3.
comp-adversary: RUN by the issuer (2.0.0_SA_COO~B1) on dell1 -- the issuer applied this cell in a scratch tree: the new test reads 3 passed, the two existing price tests 12 passed, and naming-gate.py --enforce on the diff reads PASS; the ORIGINAL patch's test (a literal key) reproduces the gate's NAMING REFUSE at :46 (the negative control). At base r2_s11.py reads NOT RUN (empty diff).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `FB-e-7` (round 2, enrichment item 6; row ADVI_FIRMBKTS-S11)

`data/cot/scripts/gold/build_canonical_prices_v2.py` builds the cot price table. It reads two Tier-2 inputs; if either
object is absent it raises, and the whole build dies. The fix, already written and tested by another seat, is a call-site
`_load_tier2()` that treats ONLY an S3 `NoSuchKey`/404 as "skip that tier" (a WARN line, an empty frame or the writer's
own override mapping) and lets every other error raise. It waited for this project because the naming gate refuses any
other project's diff to that file. The file's literal keys have since moved onto `legacy_addresses.json` rows, so the
tolerant load applies cleanly; the one thing that must change is its TEST, which may not type a key literal.

### 1a. The steps, in order

1. From the repository root: `git apply --include='data/cot/scripts/gold/build_canonical_prices_v2.py'
   org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/2.0.0_SA_COO~Q1/ADVI_FIRMBKTS_INPUT_S00_TOLERANT_LOAD.patch`. That
   applies the builder's hunks ONLY (`_is_missing_key`, `_load_tier2`, and the one call site). Do NOT apply the patch's
   test file or its `ssm.tf` hunk. If the builder hunks do not apply: a BLOCKING row with the error text.
2. Create `data/cot/scripts/gold/tests/test_s00_missing_tier2.py` with EXACTLY this content (LF endings):

```python
"""ADVI_FIRMBKTS FB-e-7: build_canonical_prices_v2 tolerates absent Tier-2 objects (S3 stubbed, no AWS).

Every S3 key is read from the writer's own INPUT_ADDRESSES (built from the registry's legacy_addresses rows), never typed.
"""
from __future__ import annotations

import importlib.util
import io
import json
import os
import shutil
import sys

import pandas as pd
import pytest

GOLD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(GOLD))))


def _load_writer(dest_dir):
    os.makedirs(dest_dir, exist_ok=True)
    shutil.copy(os.path.join(GOLD, "build_canonical_prices_v2.py"), os.path.join(dest_dir, "build_canonical_prices_v2.py"))
    for name in ("legacy_addresses.json", "scopes.json"):
        shutil.copy(os.path.join(REPO, "infra", "logic", "registry", name), os.path.join(dest_dir, name))
    shutil.copy(os.path.join(GOLD, "lib", "ticker_overrides.py"), os.path.join(dest_dir, "ticker_overrides.py"))
    if GOLD not in sys.path:
        sys.path.insert(0, GOLD)
    spec = importlib.util.spec_from_file_location("build_canonical_prices_v2_s00", os.path.join(dest_dir, "build_canonical_prices_v2.py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


@pytest.fixture()
def mod(tmp_path):
    return _load_writer(str(tmp_path / "writer_dir"))


class _ClientError(Exception):
    def __init__(self, code, status):
        self.response = {"Error": {"Code": code}, "ResponseMetadata": {"HTTPStatusCode": status}}


class _S3:
    def __init__(self, objects):
        self.objects = objects

    def get_object(self, Bucket, Key, **kw):
        if (Bucket, Key) not in self.objects:
            raise _ClientError("NoSuchKey", 404)
        return {"Body": io.BytesIO(self.objects[(Bucket, Key)])}


def _parquet():
    buf = io.BytesIO()
    pd.DataFrame({"ticker": ["AAA"], "date": ["2026-01-02"], "close": [10.5]}).to_parquet(buf)
    return buf.getvalue()


LOOKUP = json.dumps([{"asset_name": "Alpha", "ticker": "AAA"}]).encode()


def _addr(mod, name):
    a = mod.INPUT_ADDRESSES[name]
    return (a["bucket"], a["key"])


def test_missing_historical_prices_skips_tier2(mod, monkeypatch, capsys):
    monkeypatch.setattr(mod, "s3", _S3({_addr(mod, "ticker_lookup"): LOOKUP}))
    df, mp = mod._load_tier2()
    assert list(df.columns) == ["ticker", "date", "close"] and len(df) == 0
    assert "WARN:" in capsys.readouterr().out
    assert mp["Alpha"] == "AAA"


def test_missing_ticker_lookup_skips_tier2_lookup(mod, monkeypatch, capsys):
    monkeypatch.setattr(mod, "s3", _S3({_addr(mod, "historical_prices"): _parquet()}))
    df, mp = mod._load_tier2()
    assert "WARN:" in capsys.readouterr().out
    assert len(df) == 1 and isinstance(mp, dict) and "Alpha" not in mp


def test_present_inputs_are_joined_and_other_errors_raise(mod, monkeypatch, capsys):
    monkeypatch.setattr(mod, "s3", _S3({_addr(mod, "historical_prices"): _parquet(), _addr(mod, "ticker_lookup"): LOOKUP}))
    df, mp = mod._load_tier2()
    assert "WARN:" not in capsys.readouterr().out
    assert len(df) == 1 and df["close"].iloc[0] == 10.5 and mp["Alpha"] == "AAA"

    class Boom(_S3):
        def get_object(self, Bucket, Key, **kw):
            raise _ClientError("AccessDenied", 403)
    monkeypatch.setattr(mod, "s3", Boom({}))
    with pytest.raises(_ClientError):
        mod._load_tier2()
```

3. Run AC1 and AC3 (section 4). Then commit the TWO source files first with
   `.tools/safe-commit.sh` (that commit's own naming gate must pass; a refusal there is your final report with its text).
4. Run AC2 (it reads `git diff fda1c4f0cc HEAD` over the two files, so it needs that commit).
5. Commit the proof instance and the status flip.

## 2. BOUNDS

1. The builder changes by the patch's builder hunks and nothing else; the test file is the text above and nothing else.
   Do not touch `ssm.tf`, `lib/`, the registry, or any other builder.
2. No AWS act (the test stubs S3). Never type an S3 key literal into the test or the builder.
3. No non-ASCII; LF line endings. If an item cannot be met within your paths, file a surprise row and stop on that criterion.

## 3. SURFACES

<paths>
data/cot/scripts/gold/build_canonical_prices_v2.py
data/cot/scripts/gold/tests/test_s00_missing_tier2.py
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~10/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the patch under `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/2.0.0_SA_COO~Q1/`, the two existing tests
`data/cot/scripts/gold/tests/test_canonical_prices_source_firm.py` and `test_canonical_prices_input_resolution.py`,
`infra/logic/registry/legacy_addresses.json` and `scopes.json`, the issuer's check under
`org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round2/checks/r2_s11.py` (never edit it).

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~10/ADVI_FIRMBKTS.TO-FB-e-7.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-e-7"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; timeout 110 python -m pytest -q -p no:cacheprovider data/cot/scripts/gold/tests/test_s00_missing_tier2.py; echo "exit=$?"</invocation><expect>3 passed</expect></criterion>
  <criterion id="AC2" cell_refs="FB-e-7"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; timeout 110 python "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round2/checks/r2_s11.py"; echo "exit=$?"</invocation><expect>S11 NAMING GATE: PASS</expect></criterion>
  <criterion id="AC3" cell_refs="FB-e-7"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; timeout 115 python -m pytest -q -p no:cacheprovider data/cot/scripts/gold/tests/test_canonical_prices_source_firm.py data/cot/scripts/gold/tests/test_canonical_prices_input_resolution.py; echo "exit=$?"</invocation><expect>12 passed</expect></criterion>
</proof_of_spec>

AC1 is the built behavior. AC3 is the difference control: the writer's two existing price tests still read 12 passed with
the tolerant load in place. AC2 is the seam to the naming gate that refused this file once (row MDPF_DEMQUE-D1-W7-S2).

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~10/ADVI_FIRMBKTS.TO-FB-e-7.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance**, only when AC1-AC3 pass. A row id on
this project carries the dell1 infix and your slot: `ADVI_FIRMBKTS-D1-W10-S<k>`, with `surfaced_at` from
`date -u +%FT%TZ`. Report once: the apply result, the output lines of AC1-AC3, the two commit hashes.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the CTO's item 6 named three criteria; the first (the naming gate on the diff) and the second (the
build runs with both Tier-2 objects absent, exits 0) are AC2 and AC1 here; the third (one SSM run with the S_00 step)
is dropped with the step, reason in L5_FACTS section 7 ruling 2 (MDPF_DEMQUE closed its S_00 SUPERSEDED, msg 1368; the
step would add an unconsumed production step to the cot daily chain). "The literal rename" was already done by
ADVI_COTBKF (CB-ap-1, CB-at-1, CB-ax-1 @19b3550e8a). Direct act: one cell, about 130 product lines, LOCAL.

# pipeline-override: the one refusal is LIMB PRD_HEADER.fabric='laptop' vs the register's 'dell1'. The register row is the authority since 1.0.0_SA_CTO's L3 re-placement @8afcb0f851; the PRD header repair is the CTO's. Every other limb passed in the issuer's dry run.
<status>complete</status>
<round>2</round>
<to_id>ADVI_FIRMBKTS.TO-FB-e-7</to_id>
<slot>~10</slot>
<fabric>dell1</fabric>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
