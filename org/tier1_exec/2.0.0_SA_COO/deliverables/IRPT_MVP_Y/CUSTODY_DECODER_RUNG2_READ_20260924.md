# Custody hop 4: the parquet decoder question (CTO 100649 item 1), measured

Author `2.0.0_SA_COO~Y`, 2026-09-24 ~20:2xZ. Read-only. It answers the CTO's rung-2 ask for 2.0.0_SA_COO~P's custody
composition: name the layer or image that already decodes these parquets and reuse it by ARN; a new pyarrow layer
only if that read comes back empty with its denominator.

## Measured

| Read | Result |
|---|---|
| The runtime that must decode | `irpt-ycharts-generate` (the custody branch of the analysis POST): python3.12, x86_64, **no layers**, 512 MB, Zip |
| `irpt-holdings` (M's served holdings) | python3.12, layer `irpt-common:5` (644,526 B; created 2026-09-11; "jsonschema, the IRPT contract schemas, BD request-body helpers"). Its zip holds 161 members; **pyarrow absent**. The served function reads M's published output, not the parquets. |
| Account Lambda layers (`list-layers`, one page, NextMarker none) | **18 layers**. Two carry pyarrow: `pandas-pyarrow-layer:1` and `pandas-pyarrow-requests-layer:1` (the Orion pull layer). Both declare **python3.11 only**. pyarrow wheels are CPython-ABI specific (cp311), so neither loads on the generate function's 3.12. |
| M's holdings BUILD | `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py:81` `import pandas as pd`; `:888-898` `_read_parquet` = `pd.read_parquet(io.BytesIO(...))`. **Its runtime is NOT located**: `comp-pipescript deployed` searched only the mdpf tree (0 of 26 gold scripts matched; `SUBJECT_ABSENT_FROM_CORPUS`, scoped to that tree). The bundle's runner is unread. |

## What that means for the decision (P brings it to the CTO)

- **Rung 2 returns EMPTY for python3.12.** The denominator is 18 account layers, 2 with pyarrow, 0 compatible, and the one IRPT layer holds none.
- **Rung 2 still OPEN:** the runtime behind M's build (the `investor_reporting` bundle's runner). If that is a Lambda or
  image on python3.12 with pandas/pyarrow, reuse it by ARN.
- **Rung 4 candidate [INFERRED, not read]:** the AWS-managed SDK-for-pandas layer for python3.12 carries pyarrow.
  It is a native platform artifact rather than a new build. Its exact ARN and version are unread here.
- **Y's port already allows the alternative without a layer:** `build_custody_ports(get_object, read_rows=...)`.
  The default decoder is pyarrow, imported lazily, so the generate zip does not change until a decoder is chosen.
