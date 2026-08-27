# The signed in-kind field lands, and the acceptance instrument I wrote to judge it turned out to need judging too — 0.4.0_DS_ClientPlatform~U

**Seat:** `0.4.0_DS_ClientPlatform~U` (D2 re-seat S2) · **Window:** 2026-08-27T16:06Z – 17:55Z
**TO:** `ADVI_49F.c01-SIGNFIELD` · **GO:** `2.0.0_SA_COO` 76133 on Andrew's ~16:05Z release @fb79e6a4cd
**Work commit:** `0412a8d6d8` — on origin @0412a8d6d8 (ls-remote read; carried by another seat's push, not mine — I am not the integrator and my own push was correctly BLOCKED by LD-0367)

## Objective

Two acts on one plane, per the ruled design @69b2b7678c: give `flow_ledger` a NEW field carrying the
SIGNED in-kind value while `in_kind_value` keeps its unsigned contract untouched (CTO 74187 ruled
re-signing in place OUT), and fix defect 3 in `c01_nna_canonical` — which spent that unsigned
magnitude as a signed flow, so no in-kind OUTFLOW could ever reach `daily_outflow` and every
in-kind transfer, in or out, emitted POSITIVE into a client-facing NNA line.

## Compiler Tools

| Tool | Command | Result | Note |
|---|---|---|---|
| comp-pipescript io | `io c01_nna_canonical --pipeline advi` | WARN (expected) | The pre-declared KNOWN-THIN output: Group C / Order 200, READS/WRITES "(none detected)", manual-review WARN. Not an error, so the TO's STOP did not trigger. Body review done: reads `canonical/flow_ledger/date={date}/data.parquet`, writes `canonical/nna_canonical` via `rc.emit`. |
| comp-blast | `fact_trn` | **DID NOT ANSWER** | `NOT-FOUND` over 27,035 nodes, with the tool's own "this is a NOT-FOUND, not a nothing-breaks clear." Same run: `canonical rebuild failed (kuzu_nessie_load TIMED OUT after 1800s); serving existing`, `BEHIND Nessie HEAD`. Not recorded as a clear. |
| — (substitute instrument) | source enumeration of all 26 `flow_ledger` matches, every file opened | 4 readers outside the ruled set, all FIELD-DISJOINT | `d01:42 d02:28 d04:39 d11:30` read the ledger but only `final_class=='FEE-MANAGEMENT'` + fee-row `signed_amount`, which no fix touches. Backfill set UNCHANGED. Surfaced 76194/76195 before commit; CTO 76200 + COO 76211 verified at source, NO REVERT. |
| comp-validate | `c01_nna_canonical` / `nna_canonical` / `flow_ledger` | **UNVALIDATED** | No config exists for 49F Group C (`--list` covers BD + INF). Reported as UNVALIDATED, never SAFE. `nna_atomic` resolves but is a DIFFERENT artifact on the BD plane — a wrong-subject read, not quoted as validating this work. Trap: the not-found path returns **rc=0**, so rc does not discriminate. |
| comp-pipescript deployed | `c00_flow_ledger` / `c01_nna_canonical --pipeline advi` | MATCH, MATCH | Basis "raw bytes"; denominator 1 of 70 objects per file. Bare form REFUSED at rc=2 ("NO GUESS IS MADE") — correct, and not read as a result. The CRLF/LF false-STALE trap did not fire, and CRLF was independently measured absent from both sides. |
| comp-which | `"how do I validate a proof of spec instance"` | MISS, declared | "NO CURATED RULE MATCHED"; all 3 candidates below the vetted band. Did not take the top fuzzy guess (`comp-lease`, 0.63, unrelated). Resolved by direct listing. |
| proof-of-spec-check | `<instance> C01-1..C01-6` | rc=2 → rc=1 → **rc=0 VALID** | Three runs, and each failure was mine: `decomp_ref:null` (tool error, not a verdict — the tool says so explicitly), then 12 invented enum values, then VALID. |
| commit-gate / safe-commit / safe-deploy | per CLAUDE.md 14/14a/13 | PASS | risk-reflex clean, 6 files vs 1,891 danger nodes. |

## Work Completed

### 1. The producer — `c00_flow_ledger.py`, schema 1.1 → 1.2

Added `in_kind_signed_value` and `in_kind_direction_unresolved`. `in_kind_value` untouched.

The direction source is the feed's own `debit_credit`, read on the IC plane where it is
POSITION-SIDE — the same column THE IC TRAP forbids reading as CREDIT/DEBIT direction. I did not
assume the vocabulary, I censused it: IC rows carry `{LONG, SHORT}` **only** (141 of 141 on 08-24,
71 of 71 on 08-25); cash rows carry `{CREDIT, DEBIT}` **only** (1,006 of 1,006 and 963 of 963).
Disjoint at the prefix character, so `_IC_SIDE_SIGN` and `_DC_SIGN` cannot sign each other's rows —
kept as two maps with two call sites rather than one shared helper one edit away from conflating
them. LONG = IN, SHORT = OUT, corroborated on an **independent substrate** (valuation, not the
transaction label): `0016371483` is all-SHORT with bmv 110,063 → emv 0.00.

`in_kind_direction_unresolved` defaults TRUE on every IC row and clears only where a real LONG/SHORT
directs the leg — the same law as `in_kind_unvalued`, so `signed==0.0 AND unresolved==False` on a
valued leg is unreachable by construction. `quantity` is magnitude-only (141/141 and 71/71 positive),
so the sign is genuinely not recoverable from it; this column is the only in-partition carrier.

### 2. The consumer — `c01_nna_canonical.py`, schema 1.0 → 1.1

Reads `in_kind_signed_value`. A pre-1.2 partition is **REFUSED loudly** rather than falling back to
the unsigned column, because that fallback IS defect 3 and a silent version of it would reintroduce
the defect on every historical partition. Manifest gains `in_kind_direction_census` — the CONSUMING
half of the producer's claim, since an unenforced provenance field drifts to unpopulated.

### 3. Acceptance harness + four planted mutants

Builds both planes twice on identical inputs, PRE from a pinned vintage recovered by CONTENT, POST
from the working tree. Four mutants, because four criteria are supposed to discriminate
independently and a shared-fate control set cannot show that: `resign` fires C01-1 alone, `sign`
fires C01-2 alone, `drop` fires both, `c02` fires C01-4 — that last one planted **specifically
because C01-4 stayed green under the other three**, and a control never seen to fire is a promise.

## Decisions Made

| Decision | Rationale |
|---|---|
| New field, not a re-sign | CTO 74187. A TWR fix silently moving NNA output is how a change nobody scoped reaches a client figure. |
| Direction from `debit_credit` at the producer, not a join | My own design note said carry direction forward rather than re-derive by quantity; the column is already in `TRN_COLS`, and the quantity-join had a documented collision limit. |
| Refuse a pre-1.2 ledger; no silent fallback | The fallback is the defect. A loud refusal makes the pre-backfill gap non-silent at the code level. |
| Did **not** extend `row_quality`'s vocabulary | `c01_account_performance.py:121` BRANCHES on `row_quality=='clean'`. Adding a value is a Rule 24 taxonomy act owing a four-postulate record, and it is not in this TO. Consumed the claim via a manifest census instead. Surfaced, not built. |
| Substituted an instrument when comp-blast could not answer | Its zero came from a timed-out, stale snapshot. Surfaced the substitution and the finding BEFORE commit rather than quietly proceeding. |

## Files Modified

| File | Change | Committed |
|---|---|---|
| `data/assets/scripts/gold/runners_49f/c00_flow_ledger.py` | +2 fields, schema 1.2, direction census | Yes — `0412a8d6d8`, DEPLOYED-VERIFIED |
| `data/assets/scripts/gold/runners_49f/c01_nna_canonical.py` | defect-3 fix, refusal guard, direction census | Yes — `0412a8d6d8`, DEPLOYED-VERIFIED |
| `.../deliverables/ADVI_49F.c01-SIGNFIELD_ACCEPTANCE_HARNESS.py` | new; repinned baseline + baseline guard | Yes — `0412a8d6d8` + follow-up |
| `.../deliverables/ADVI_49F.c01-SIGNFIELD_ACCEPTANCE_RESULT.json` | new; ALL_PASS, byte-reproducible | Yes |
| `.../deliverables/ADVI_49F.c01-SIGNFIELD_PROOF_OF_SPEC.json` | new; VALID rc=0 | Yes — follow-up |
| `.../deliverables/ADVI_PERFRP_OUTLIER_ROOT_CAUSE_20260826T2355Z.md` | **corrected** — one wrong number, one wrong mechanism | Yes — `0412a8d6d8` |
| `.../task_orders/ADVI_49F.c01-SIGNFIELD...md` | status → pending | Yes — `0412a8d6d8` |

## Two things I got wrong, both caught by instruments rather than by review

**My own pre-registered acceptance table carried a bad row.** I registered `0033493115`'s pre-fix
`nna_unresolved_direction` as 64,841.33. It is **87,054.1359** — the live S3 partition says so and a
rebuild from `fact_trn` reproduces it to the cent. Both alternatives were measured out: the input did
not change (`fact_trn date=2026-08-24` LastModified 2026-08-25T09:46:15Z, before the table's own
stamp) and the method did not differ (the other three rows reproduce the live artifact exactly). One
mis-transcribed row, whose derived expectation inherited the error. My stated *mechanism* was wrong
too — I wrote these accounts hold MIXED-DIRECTION legs; **none do** (15/15, 30/30, 14/14 SHORT, 1/1
LONG). The asymmetry is the CASH component in the same bucket, signed before and after, so it does
not double while the in-kind part flips. *A pre-registered acceptance is only as good as the
substrate its "now" column was read from, and I never named that substrate when I wrote it.*

**The harness I committed had a moving baseline, invisible until the commit landed.** It read its PRE
arm from `git show HEAD:<path>`. Correct for exactly as long as the fix was uncommitted — then HEAD
*became* the post-fix code, both arms loaded the same module, and it reported C01-1 FAIL. A committed
acceptance artifact that could no longer reproduce its own committed result. Found by running the
determinism control **after** the commit; run only before, it would have missed this entirely. The
harness's own docstring cited Rule 22a about resolving pins by content while the code pinned to a
moving symbol. Now an explicit hash plus a guard that REFUSES a baseline already carrying the field —
exercised, rc=1.

## Blockers

**None.**

## Current State

`ADVI_49F.c01-SIGNFIELD` is **COMPLETE**: all six criteria PASS, proof instance VALID rc=0, both
scripts DEPLOYED-VERIFIED against the committed build input with a negative control. Historical
partitions still carry the old sign — the declared state, gated on `ADVI_49F.P14-VEHICLE`.

## Next Steps

1. Report field-landed / defect-3-fixed / both-negative-controls to `2.0.0_SA_COO`, cc `1.0.0_SA_CTO`; name the harness commit for `3.0.0_SA_CVO`'s cert P2 discharge (76206).
2. Begin `ADVI_49F.c02-CFINPUT` — gated on this TO, no new GO needed (76133 TO 2). Read BOTH the SEATING-EXECUTED and reconciliation blocks on the `~A` face before acting; the original Objective wording is superseded where they differ.
