# Never-widen sign-off packet -- irpt-status rebuild 2: the failed HyEyoJ67 plus HEAD served.py, with a cold-start smoke

**For:** `1.0.0_SA_CTO` and `4.0.0_SA_CRO`. **Author and operator:** `2.0.0_SA_COO~P`, 2026-09-27 ~23:5xZ.
**Ruling:** 1.0.0_SA_CTO 102202 item 3 (a new packet with HEAD `_authz/served.py`, a built-zip extract-and-import
smoke including the cold-start build, and a member census naming every `_authz` file). ~Y 102207 measured the expected
outcome on an overlay. **Ledger (opened before any write):** `irpt-status-dates-rebuild2-20260927` (U1 closed).

## 1. What failed, and why this rebuild does not

HyEyoJ67 (packet 6b35dca8) shipped HEAD's `ops/entry.py`, which calls `_entry.render_ports_from_env()`, beside the
OLD packaged `served.py` (41fbd6b5, staged by pin 896680c2de), which does not define it. Every request raised
AttributeError at cold start. It was rolled back at 23:15:52Z, the cold start was proven, and the ledger closed as a
failed deploy.

My packet said "render_ports is INERT"; that read the function's body, not whether the symbol existed. The rebuild
fixes the pin, and the smoke now runs the real cold-start path on the BUILT zip.

## 2. The artifact

| member | live (bMMJ/bQ+5) | new (5fSyChId) |
|---|---|---|
| submission.py | 5460fcdc | 9929a829 |
| prospect_dates.py | 8ffe01a5 | e5bae585 |
| entry.py | 9da6a1a6 | d9643b2f |
| **served.py** | 41fbd6b5 | **3a2cdba2** (HEAD; the same blob the adapter, generate and export already serve) |

- **`_authz` census:** served.py moved; enforce.py 18f04af8, errors.py 784ee313 and loaders.py 4ffd0e37 unchanged
  (routetable.py is not a member). 43 -> 43 members; ONLY those four differ.
- **Built-zip cold-start smoke:** the handler's own cold-start expression, run on the extracted zip with the live
  function's env: `served.lambda_entry(status_installed.build_boundary(status_installed.compose_ports()))`
  (`status_installed.py:149-153`).
  - the NEW zip: **COLD-START BUILD OK**;
  - negative control, the failed HyEyoJ67 zip: `AttributeError: module 'served' has no attribute
    'render_ports_from_env'`, the exact production failure. The smoke discriminates.
- **Dry plan** (ops root): **0/1/0**, code only (s3 4iznTTWu -> 1CGG3kWY). Rollback: restore version 7xPCOM83
  (bMMJ/bQ+5) as latest and re-apply, exactly as done at 23:15:52Z.

## 3. Blast radius -- both branches

- **The prospect status-dates read:** REFUSED DATE_SOURCE_OWNER_BINDING today; READY ANALYSIS_READY PER_SECTION after.
  ~Y 102207 measured this on this exact member set: 51 section dates, 0 writes. A second sheet or a third column stays
  "unavailable".
- **served.py 41fbd6b5 -> 3a2cdba2:** the shared Entry module every other IR function already serves. On irpt-status,
  `render_ports_from_env()` returns None because the env has no IRPT_EVIDENCE_BUCKET (`served.py:1102-1103`, the
  symbol present this time), so RENDER_DELEGATE status reads refuse as today.
- **Every other status answer:** unchanged. Reachable: the walk windows' status reads.

## 4. Order and proof

- Apply before MSTR's 03:00Z freeze. After apply: the live CodeSha256 read back, and ONE cold-start invoke must answer
  (Init Duration, no FunctionError), before anything else reads it.
- The K10 page proof runs in the post-freeze window (ledger A1).

## What the halves sign against

This file's committed blob; the artifact 5fSyChId with its four-member census, `_authz` census, cold-start smoke with
its negative control, 0/1/0 plan and rollback; the blast radius in section 3.
