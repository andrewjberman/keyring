# Crash recovery, scope resolution, and the custody inversion solved — 4.0.0_SA_CRO~A

**archetype:** MIXED (COORDINATE → DIAGNOSE → TRACE)
**Date:** 2026-08-11 (0245–0330Z)
**Task Order:** ad-hoc — Andrew-direct session scope @85e51be03a (MDPF + Cottonwood)
**Status:** IN PROGRESS (both scope deliverables landed; open items at Andrew)

---

## Objective

Recover the crashed `~A` seat, resolve the assignment ambiguity the crash left (launcher said
"two candidate assignments"; CTO's 0124Z brief said ADVI billing), then execute the resolved scope:
figure out the MDPF/Cottonwood scheduling jam and suggest implementation strategy, atom_decomp as
the suggested instrument.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-find | `comp-find "silver-precedes-bronze"` | PASS | 3 hits with bands+denominator — localized the residual's two records in one call |
| comp-find | `comp-find "forwardfill_v2"` | PASS | DEF band separated the 5 producers from 256 doc mentions; found `cot_bronze_ingest.py` + the bd-49f adjacency in one page |
| comp-find | `comp-find --name "*blackdiamond*"` | PARTIAL | converter is not named "blackdiamond" — the deploy-completion record (found via `--name "*silver*blackdiamond*"`) named `mirror_conversion.py`; filename search alone would have dead-ended |
| comp-which | A.3 exercise probe | PASS | forwarder ran (banner produced); PATH 96/97 |

**What worked:** comp-find's DENOMINATOR + band lines did exactly what the rail doctrine claims —
the DEF band turned a 632-hit query into a 19-line read. **What failed:** nothing crashed; the
`--name` miss above is a naming-convention gap, not a tool defect. **Gap found:** no comp-tool
answers "list all VERSIONS of this S3 key" — the decisive observation tonight
(`list-object-versions`) was raw-primitive only, and it is exactly the observation that dissolves
LastModified-based freshness misreads. Surfaced in the strategy doc's method note; a
`comp-freshness --versions` mode is a coverage candidate for the owning lane, not built by me.

---

## Work Completed

### 1. Crash recovery + scope resolution (0245–0300Z)
Re-registered (PID 4760), armed inbox Monitor `bqvcg4v12` (TaskOutput-confirmed), Step-1b mechanics
green. Surfaced the launcher-vs-CTO-brief scope discrepancy to MSTR rather than adjudicating;
MSTR located the durable Andrew-direct record @85e51be03a (predecessor's, 0139Z) — scope = MDPF +
Cottonwood, ADVI billing explicitly not mine ("CTO is confused…"). Read the record at the commit.
Opened the CTO channel; agreed split: I drive the scheduling-jam mechanism, CTO keeps the
custody-history adjudication, sync before fixes at the seam.

### 2. The custody inversion — mechanism solved (@562cbd444d)
The remediation plan's open residual ("real ~24h silver-precedes-bronze inversion, unexplained")
**dissolves**: multi-write bronze keys (post-retime `ce99054e44`) × first-write-wins silver
(`mirror_conversion.py:474`) read through two instruments that each see one write. Three real
defects underneath, all grounded: **C-1** silver frozen on least-settled versions since 08-05
(measured: 08-07 weekend case +$1,103,897.21 raw-grain MV between frozen Sat v1 and settled Mon v3;
08-05 weekday benign to the penny); **C-2** retry-net double-applies the as-of lag
(`cot_bronze_ingest.py:1135` + `:306-320`; marker "relanded 08-06" while the bytes were 08-05's —
live-proven both nights); **C-3** sweep-before-primary (`ssm.tf:143` vs `:165`) makes the newest
probe day structurally absent → deterministic nightly phantom heal.

### 3. The scheduling jam's general form + strategy (@1b43c23765)
Five-atom scheduling contract (write cardinality / date-label semantics / trigger predicate /
re-delivery policy / vendor settle window), Rule-24 self-checked; measured matrix placing every
known W1–W5b defect + tonight's findings at atom boundaries; three-move strategy (declare the
contract in existing registries · one Andrew ruling on restating-vendor conversion policy, jointly
with CTO · route C-2/C-3 mechanical fixes) + one gate candidate proposed-not-implemented. Honest
atom_decomp method assessment for the program record.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Surface the scope conflict, hold rather than act on the CTO relay | Predecessor's own summary (written AFTER ingesting the relay) showed the relay had not closed scope; launcher post-dated it |
| Diff bronze VERSIONS rather than trust LastModified tables | Both prior instruments (head-object, truth-JSON latency) read one write of a multi-write key; versions are the only view that sees all writes |
| Propose no C-1 fix | It is a point-in-time-vs-restate policy call — the neighbor of CTO's open call at Andrew; agreed split says sync first |
| Raw-grain sums labeled, AUA impact not computed | cot fact_holdings is Relationship×Account×Asset grain; naive sums double-count — the collapse is DS's computation |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/tier1_exec/4.0.0_SA_CRO/deliverables/MDPF_COTTONWOOD_CUSTODY_INVERSION_MECHANISM_20260811.md` | new — mechanism record | Yes — `562cbd444d` |
| `org/tier1_exec/4.0.0_SA_CRO/deliverables/MDPF_SCHEDULING_JAM_STRATEGY_20260811.md` | new — strategy record | Yes — `1b43c23765` |

Both local per lanes-commit-integrators-push; MSTR carrying them in the next integrator push.

---

## Blockers

None at me. At **Andrew** (via MSTR relay + the strategy doc §6): the Move-2 conversion-policy
ruling · Move-1 contract ratification · the gate candidate. At **1.0.0_SA_CTO** (not blocking):
edit/veto/co-sign of the Move-2 joint framing (my 032445Z message); C-1 stays parked behind his
custody-history call either way.

---

## Current State

The `~A` seat is live (Monitor `bqvcg4v12`), scope-bound by @85e51be03a to MDPF+Cottonwood. Both
scope halves are delivered and committed locally: the custody "inversion" is mechanism-solved
(@562cbd444d — no ordering anomaly; silver `blackdiamond/cottonwood/silver/fact_holdings` frozen on
first-write versions since 08-05, ~$1.1M raw-grain weekend divergence measured on
`HOLDINGS_DAILY_2026-08-07.xlsx` v1-vs-v3) and the strategy is on record (@1b43c23765 — five-atom
contract + three moves). C-2/C-3 suggested routing is with COO (MSTR pointed them); the 49F
same-code adjacency is flagged UNVERIFIED into CTO's consumer census. The live W1–W5b atomic-window
recovery (DS/COO/AE) was never gated or touched by any of this.

## Next Steps

1. **Sync the Move-2 joint framing with 1.0.0_SA_CTO** — his edit/veto/co-sign unblocks the one
   ruling C-1 waits on.
2. **Act on Andrew's word** on the §6 open list, whichever item he rules first.
3. **[2.0.0_SA_COO]** C-2/C-3 routing to DS/AE lanes if the direction gets his nod — suggested
   owners only, his call.
