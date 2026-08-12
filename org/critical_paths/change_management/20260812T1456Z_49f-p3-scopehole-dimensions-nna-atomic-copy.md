# 49F P3 SCOPE HOLE — dimensions/ + canonical/nna_atomic relocation copy

**Status:** CLOSED 2026-08-12T15:20Z (opened at act start 14:56Z; completed in-session)

**Owner:** 0.4.0_DS_ClientPlatform
**Authority:** 2.0.0_SA_COO 145428Z [DRIVE] ruling; gap found by 0.4.0_DS_ClientPlatform~B
**Class:** relocation completion (NOT a repair, NOT a producer run)
**Gates:** P4 LEG A served-key sign-off (3 keys, Andrew "proceed with the cutover" ~1425Z)

## WHAT THIS IS

P3 relocated the 49F gold product root from `s3://opal-data-assets/schwab/08335338/gold/`
to `s3://opal-data-assets/portal/gold/advi/49financial/`. The copy's scope covered the four
`canonical/` tables (4,206 objects, two-sided verified, ledger
`20260812T1403Z_49f-p3-gold-root-repoint.md`). It did **not** cover the `dimensions/` tier
or `canonical/nna_atomic`.

**This is a SCOPE hole, not an execution failure** — the 4,206/4,206 was complete for what it
covered. `d13:153` reads `dimensions/dim_relationship`, which is why the gap gates P4 LEG A.

## ⛔ RULED: COPY, NOT A PRODUCER RUN (COO 145428Z)

The producers ARE correctly re-pointed (`a01_dim_relationship.py:45` `TABLE=` via `rc.emit`
-> `runner_common.OUT_ROOT:31`; `a00_runner.py:43` `GOLD_ROOT`), so a run WOULD emit to the new
root. It is nonetheless the wrong act:

- The dims have not emitted since **2026-07-15 (28 days)**. A producer run computes a **NEW
  VINTAGE**, it does not relocate the existing one.
- That would make P4 LEG A's **DELTA=0 claim FALSE BY CONSTRUCTION** — different input, so the
  served bytes legitimately move, converting a cheap arithmetic sign-off into a real never-widen
  adjudication for no reason.
- A copy preserves DELTA=0. A producer run destroys it.

⚠ **28 days is NOT a staleness finding.** A relationship/account dimension legitimately changes
rarely; this is nowhere near the freshness bar, no trading-calendar claim is made or implied, and
DS~B correctly declined to call it stale. **The copy completes a relocation; it repairs nothing.**

## SCOPE — 10 objects, 3 tables (census materialised client-side, both roots)

| table | OLD objs | OLD bytes | NEW objs (pre-act) |
|---|---|---|---|
| `dimensions/dim_account` | 4 | 1,707,753 | 0 |
| `dimensions/dim_relationship` | 4 | 270,178 | 0 |
| `canonical/nna_atomic` | 2 | 11,686 | 0 |

**POSITIVE CONTROL on the absence:** the identical call shape against the P3-covered
`canonical/nna_canonical/` returns **1052 objects at BOTH roots**. The zeros above are a real
absence, not an empty result from a broken list.

`canonical/nna_atomic` gates nothing today (not in `d13`'s read set) — included per COO so a
second hole of the same class is not left for the next publisher. Two holes found one at a time
cost twice; the second is free now.

## METHOD (same discipline as the 4,206)

- per-key `copy_object` — every outcome OBSERVED, never inferred from a bulk rc=0
- two-sided counts per table on **objects AND bytes**, materialised client-side (no
  `--query length` on a paginated call)
- **ETag equality per key** — proves WHAT did not change while WHERE did
- **parquet PARSED** (not listed) from each table at the destination
- ⛔ **nothing deleted at the old root** — teardown is the P4 exit condition, not this act

## RESULT — COPY 10/10, PRODUCE 3/3, NOTHING DELETED

### COPY leg (COO 145428Z scope) — 10/10, zero failures
| table | objs src/dst | bytes src/dst | ETags identical | parquet PARSED |
|---|---|---|---|---|
| `dimensions/dim_account` | 4 / 4 MATCH | 1,707,753 / 1,707,753 MATCH | 4/4 | 7,146r x 35c `date=2026-07-15` |
| `dimensions/dim_relationship` | 4 / 4 MATCH | 270,178 / 270,178 MATCH | 4/4 | 7,142r x 6c `date=2026-07-15` |
| `canonical/nna_atomic` | 2 / 2 MATCH | 11,686 / 11,686 MATCH | 2/2 | 328r x 10c `date=2026-07-15` |

**ETag identity 10/10 is the load-bearing line: it proves WHERE changed and WHAT provably did not** —
which is what preserves P4 LEG A's DELTA=0.
**DISCRIMINATING CONTROL — old root re-enumerated AFTER the copy: all three tables STILL PRESENT**
at full object+byte count. The act is provably not a move.

### PRODUCE leg (COO 150527Z scope) — 3/3, verified at rest
`dim_security` 2,325r x 13c · `dim_boundary` 7,265r x 9c · `dim_calendar` 526r x 6c, all
`date=2026-08-11`, all parquet PARSED from S3 at the new root.
Dry-run preceded every upload (all rc=0): a03 2,325 securities / rate_bearing=112 · a02 7,265 rows,
classes disjoint=True, `boundary_version=13bc7edfcd48f6bc…` · a04 527 date keys, TRUE GAPS=0.

⚠ **`a03` and `a04` printed a bare `EMIT: rows=… cols=…` with NO destination while `a02` printed its
S3 path.** Verified at rest rather than trusting three inconsistent self-reports; all three had in
fact uploaded. **A producer that does not name where it wrote is a reporting defect** — the
inconsistency, not the outcome, is the finding.

### ⚠ HOLD/ACT CROSSING — stated, not smoothed
COO issued a HOLD on the produce half at **15:13:01Z**. The three uploads landed **15:09:43Z /
15:11:56Z / 15:11:59Z** — the act PRECEDED the counter-instruction. The deciding read (below) then
found the produce was correct as originally scoped, so nothing was unwound. **Recorded because a
crossing that resolves in the actor's favour is exactly the one that gets quietly dropped.**

### ✅ THE DECIDING READ — both dims CROSS THE RUN BOUNDARY (so they are gold, not intermediates)
CTO's criterion: does anything outside the producing run read it? **Yes — the S3 gold root is the
DEFAULT path; the `--*-local` flags are OVERRIDES:**
- `b00_canonical_valuation.py:99-103` — `else: rc.read_partition(f"{rc.OUT_ROOT}/{BOUNDARY_TABLE}", asof)`
- `b01_canonical_positions.py:105-108` — `dim_security`, `else:` branch reads `rc.OUT_ROOT`
- `b01:112-116` — `dim_boundary`, same
Exception: `c00_flow_ledger.py:314` reads `--boundary-local` with **no S3 fallback** — in-run-only,
a different calling convention; does not change the artifact class.

### ⛔ RETRACTION CARRIED INTO THE RECORD
An earlier claim of mine — *"`canonical_positions` is in S3, produced from a session-local input"* —
is **FALSE**. Bucket-wide scan: **0 keys**. The `canonical/` tier holds five tables at both roots
(`canonical_valuation`, `flow_ledger`, `nna_atomic`, `nna_canonical`, `twr_daily`). I read the
artifact from a session scratchpad mirror and asserted a production location without one S3 call
against the key. It is a genuine in-run intermediate consumed via a local root path (`d06:57-58`).
**No live provenance defect exists.** Retracted to CTO + COO same turn.

### ⛔ DEFECT FOUND, NOT FIXED (design call, routed)
`b01_canonical_positions.py:118-120` catches `FileNotFoundError` on `dim_boundary` and degrades to
`WARN: … boundary_version stamp EMPTY (stated)`. **`dim_boundary` did not exist in S3 until
15:11:56Z today — so every prior `b01` run took that branch and stamped an EMPTY provenance
version.** An absent gold dependency became a line of stdout nobody diffs. Whether an absent
boundary should be fatal is CTO/COO's call, not a unilateral fix.

### 📋 FLAGGED, NOT ACTED ON
`dim_identity_crosswalk` — **MEASURED ZERO READERS in tree**, never-launched vs superseded
indistinguishable from a zero-reader count. Successor-check owed before any disposition (COO
150527Z). Not produced: producing a dim nothing consumes is build-ladder rung 1.

### P4 EXIT CONDITION — UNCHANGED AND STILL LIVE
⛔ Nothing was deleted at the old root by this act. `schwab/08335338/gold/` must be decommissioned
at P4, and **P4 may not close while it exists**. Per CTO's four-part production criterion, a
session-local input anywhere in the chain fails clause (i) by construction — so these ad-hoc
artifacts are **NOT production evidence** and P4 must not close on them.
