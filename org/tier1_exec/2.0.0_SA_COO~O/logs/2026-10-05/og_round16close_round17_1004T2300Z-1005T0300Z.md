# NFRA_OPLGTW round 16 closed, round 17 cut and driven: asset downloads under C3 are live in r17 -- 2.0.0_SA_COO~O

**archetype:** COORDINATE
**secondary_archetypes:** DEPLOY, VALIDATE
**Date:** 2026-10-04 23:00Z .. 2026-10-05 ~03:00Z
**Task Order:** NFRA_OPLGTW round 16 close (OG-rl-5) and round 17 (addendum R3-T.10): OG-q-7, OG-rl-6, OG-gr-4, OG-ti-1, OG-pm-1, OG-ar-2.
**Status:** IN PROGRESS. Round 17 is 5 of 6 complete. OG-pm-1 is pending on a dated window (2026-10-05 must close).

## Objective

Close round 16 (OG-rl-5 deploy and close). Push on Andrew's word. Cut round 17 from the CTO's analysis
@1f439fe6aa section 4 in ONE issuance, and drive it to the dated cell.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| comp-find | `'CLOSED_UNREMEDIATED' docs/doctrine org/ref` | PASS | 3 hits, 39 files. It found the four close reasons. |
| comp-find | `'CandidateRejected'` / `'class CandidateRejected'` | PASS | A measured 0 in app/, then 3 DEF hits repo-wide; the refusal lives in ops/. |
| proof-of-spec-check.py | OG-rl-5 instance | PASS | VALID; surprises 7 of 7 resolve. |
| to-pipeline-gate (via safe-commit) | round-17 issuance | REFUSED, then PASS | The risk floor refused LOCAL on two orders that touch the gateway tree. |
| safe-merge.sh | 9 drains | PASS | Tree checks dropped 0 everywhere. 3 channel conflicts were resolved by row-id union, 1 test-file conflict by hand. |

**What worked:** the to-pipeline-gate risk floor caught a class error before issuance. The safe-merge `--continue`
limb kept every conflicted drain inside the guards.
**What failed:** two issuer check scripts were wrong at first. q7.AC2 read pytest's Windows separators as new failures,
and the ti1 floor was not the measured count. Both were fixed before issuance and the fixes are named in the issuance
commit.
**Gap found:** a criterion's `<expect>` is not re-validated when its check script changes (row Z-W15-S38, the issuer's
defect). Amendment A6 fixed the instance; the class is open.

## Work Completed

### 1. Round 16 closed
- **OG-rl-5 Phase B:** live at 23:12:32Z (r16 `4b6b823fae`), verify 15 of 15, ledger CLOSED; drain b91a1a44cf.
- **A6:** the stale AC1 expect was fixed, and AC1 PASSed on the issuer's re-run. The order closed @1d2af57547.
- **Row Z-S52:** disarmed S33 and S34 on the post-act read.
- **Round-end message:** msg 29315. CVO slug v4, then the CTO analysis @1f439fe6aa.

### 2. Push
- Andrew-direct "1yes" was recorded @b641e1aeae, with its time corrected @7795a96d14.
- 0.0.0_AB_MSTR~Z pushed: origin CLOUD 5468d18362 -> 7cb2cf5ccc.

### 3. Round 17
- **Issuance @3ae49bc24b,** six cells. The analysis's "OG-q-6" collides with the completed 09-18 order and was cut as
  `OG-q-7`.
- **OG-ar-2** (drain ff0fde5f8b): the seven open rows all came back `moves_when`.
- **OG-gr-4** (drain 06e6db2995): `dim_balance` `(account_id,)` is unique on 28 of 28 served snapshots, and the page
  is OK. Row Z-S53 records W6-S2 as REMEDIATED on the owner's word; the CVO writes the clock.
- **OG-ti-1** (drain 985fd66ee0): the schwab set runs in one process with 0 errors (was 11).
- **OG-q-7** (drain fc70572578): the C3 restriction now applies on the download paths, and both guards are retired.
  The `test_schwab_rl5_asset_query.py` conflict with ti-1 was resolved by keeping both sides.
- **Issuer re-grades on merged CLOUD:** q7.AC1 4/4, q7.AC2 PASS, ti1.AC1 138 collected and 0 errors.
- **OG-rl-6:**
  - Phase A: drain 33be896a10.
  - Never-widen ask @1a21759226. CTO half @de3381d39f, CVO half @9c7fa957a3 (R1-R2).
  - Phase B: r17 `e91819e281` is LIVE, verify 12 of 12, ledger CLOSED; drain daa5f5ef70.
  - Issuer re-run on CLOUD: rl6.AC1 PASS, rl6.AC2 PASS.
- **R14:** `/yearinreview` is placed on this train. Its kit @0b6a5aff58 is not on origin, so it rides the next release.

## Decisions Made

| Decision | Rationale |
|---|---|
| OG-q-7, not "OG-q-6" | The id is held by a completed order; reusing it would corrupt the decomp index. |
| q-7 and ti-1 at WORLD | The gate's floor for gateway paths. |
| Keep conftest.py at live bytes in r17 | It is outside rl6.AC2's release set; tests are not executed by the service (row Z-W15-S40). |
| rl-6 does not carry /yearinreview | R14: never hold rl-6; the kit is not on origin. |

## Blockers

- **OG-pm-1:** handed only after 2026-10-06T00:00Z. That is an essential wait: the measured day must close (order
  record face). No cron is armed, because none is authorized for this seat.

## Current State

- **opal-gateway LIVE:** `e91819e281` (r17). `dim_asset` downloads are held-only under C3; an empty-holdings grant is
  refused.
- **Row Z-W15-S41:** the one live `dim_asset` grant lacks `download_filtered`. No real principal can download yet, so
  FWD-4's real-holder arm needs a grant change. That is Andrew's word per PRD v1.7. My ask's property (d) wording
  ("holders gain downloads") over-stated this; the served exposure to real users is unchanged.
- **Push state:** LOCAL beyond origin 3d5f1e2b7e (ls-remote read 01:5xZ).

## Next Steps

1. [2.0.0_SA_COO~O, after 2026-10-06T00:00Z] Hand OG-pm-1 (slot ~27); drain it; then send the round-17 terminal
   message to the CTO and CVO. It carries S40 (the one-process isolation is incomplete for some file subsets) and S41
   (the FWD-4 real-holder arm needs a grant op).
2. [3.0.0_SA_CVO~O] Write the W6-S2 clock on Z-S53, then the round-17 slug at terminal.
3. [laptop 1.0.0_SA_CTO / 0.0.0_AB_MSTR] Push `/yearinreview` @0b6a5aff58, so that it rides r18.
